<!--
Shared protocol referenced by the unified screening skill:
- skills/04-screen/SKILL.md (dispatches on --stage {title|abstract|full-text})

The screen skill opens with:
"Follow the shared screening protocol in `agents/_screening-protocol.md`.
 Stage-specific rules below override it when in conflict."

This file centralizes mechanics that would otherwise be triplicated across the three
screening stages: the two-pass architecture (deterministic regex classifier first,
single LLM reviewer second), the spreadsheet round-trip, the conservative doctrine,
the per-stage evidence sources, and the lock discipline.
-->

# Screening Protocol (shared)

This file is the authoritative specification of the common mechanics used by the three screening stages (04 title, 05 abstract, 06 full-text). A stage-specific agent may add rules (e.g., which evidence source is allowed, how the full-text excerpt is built) but MUST NOT contradict the rules below unless explicitly stated.

The architecture is **two passes in series**, not adversarial sub-agents in parallel. Pass 1 is a deterministic regex classifier elicited from the user via Q&A. Pass 2 is a single LLM reviewer that reads the pass-1 record + the stage-allowed body and writes the consultative `My Final Decision` and `My Justification`. The user has the final say in the spreadsheet; the markdown is the source-of-truth, the xlsx is a projection.

## 1. Conservative doctrine

When in doubt, keep `Include` at the title and abstract stages. A false positive costs one extra read at the next stage; a false negative loses a relevant paper forever. The doctrine is operationalized at three levels:

- **Pattern elicitation (`_screening-classifier-runner` Q&A):** the user is invited to write categories that are _clearly_ off-topic or _clearly_ in-scope; everything else falls through to the default decision (typically `Exclude` at title, but with the understanding that the LLM reviewer of pass 2 may override).
- **Override resolution (`scripts/deterministic_classifier.py`):** when both a positive trigger and an override fire on the same paper, the category is suppressed and control passes to the next priority slot — no automatic promotion to Include, but the override is recorded in `overrides_applied` so the LLM reviewer can reason about it.
- **LLM reviewer tiebreak (`_screening-llm-reviewer`):** when the regex is silent (`winning_category == "default"`) and evidence is genuinely ambiguous, prefer `Include` at title and abstract. Full-text has no recall-preserving rule; ambiguity is resolved by reading deeper.

The doctrine is also anchored in `CLAUDE.md §2`. Any conflict between this file and the review's `CLAUDE.md` is resolved in favor of `CLAUDE.md`.

## 2. Two-pass architecture with accretive audit trail

```
paper sem My Final Decision
        │
        ▼
[pass 1] _screening-classifier-runner
   ├─ Q&A → protocols/classifier-config.json (first run only; reuse/refine after)
   └─ scripts/deterministic_classifier.py
        ├─ proposed_decision        → frontmatter (mirror) + iter-K body block (regex_decision)
        ├─ proposed_justification   → frontmatter + iter-K body block (regex_justification)
        ├─ evidence_trail           → iter-K body block
        ├─ winning_category         → frontmatter + iter-K body block
        └─ overrides_applied        → frontmatter + iter-K body block
        │
        ▼
[pass 2] _screening-llm-reviewer (modelo de CLAUDE.md §6.models.<stage>)
        ├─ my_final_decision        → frontmatter (mirror) + iter-K body block (llm_decision)
        ├─ my_justification         → frontmatter + iter-K body block (llm_justification)
        ├─ agrees_with_regex        → frontmatter + iter-K body block
        └─ divergence_reason        → frontmatter + iter-K body block
        │
        ▼
human review → on lock, parent skill writes `### final` block with the user's verdict
              and `locked_at_iteration: iter-K` pointing at the iteration kept; mirrors
              `my_final_decision` + `my_justification` to the frontmatter
```

The body record is **accretive**: the first run writes `### iter-0 (initial classification)` combining the pass-1 and pass-2 outputs in a single block. Refinements via `04-screen --refine` append `### iter-(K+1) (after refine: <summary>)` blocks; prior iter-K blocks are immutable. The frontmatter mirrors the **latest** iter-K's verdict plus the human-edited fields; `last_iteration` points at K.

Pass 1 is a pure function: same papers + same config = byte-identical output. Pass 2 is consultative; it never overwrites an `### final` block or a `My Final Decision` cell already filled by the user (the parent skill excludes such papers from the batch via `--skip-paper-ids`).

## 3. Stage execution loop (six steps)

Each `04-screen --stage <stage>` invocation runs the following sequence. The shared sub-agents (`_screening-classifier-runner`, `_screening-llm-reviewer`) implement the per-paper machinery; this loop wires them to the screening stage and to the review repo.

1. **Choose the LLM reviewer model.** Read `CLAUDE.md §6.models.<stage>`. If absent, ask the user, suggest 2–3 alternatives (Haiku for speed, Sonnet for balance, Opus for hard cases), record the choice via commit `[NN] claude-md: model selected (<id>)`, then proceed.
2. **Elicit or reuse criteria.** Spawn `_screening-classifier-runner` with `stage`, `papers` (eligible batch — papers with no `### final` block for this stage), `config_path` (read from `CLAUDE.md §6.classifier_configs.<stage>`, default `protocols/classifier-config.json`), `existing_my_final_decision_ids` (empty on first run), `review_root`, and `previous_classifier_config_signature` (or null). On first run, the runner conducts a Q&A and writes the config; on subsequent runs, the runner offers reuse-as-is or refine.
3. **Generate the config.** The runner persists `<config_path>` according to `templates/classifier-config-schema.md` and commits `[NN] config: classifier-config initialized` (or `[NN] iteration: criteria refined` when refining via `04-screen --refine`).
4. **Pass 1 — deterministic classifier.** The runner invokes `scripts/deterministic_classifier.py` and materializes the pass-1 fields of the `### iter-K (initial classification | after refine: <summary>)` block in every `papers/paper-NNNN.md` for the eligible batch (creating the iter-K block when first run; appending a new iter-(K+1) block during refinement, never overwriting prior iter-K). Mirror the same fields to the frontmatter (`proposed_decision`, `proposed_justification`, `winning_category`, `overrides_applied`, `last_iteration: K`). Commit `[NN] run: <count> papers classified by regex` with a footer reporting the distribution by `winning_category`.
5. **Pass 2 — LLM reviewer.** Spawn `_screening-llm-reviewer` with the model chosen in step 1, the `criteria_summary` prose synthesized by the runner, and the batch with the pass-1 record attached. The reviewer returns a JSON array; the parent persists it to `screening/<stage_dir>/reviewed.json` and appends the pass-2 fields (`llm_decision`, `llm_justification`, `agrees_with_regex`, `divergence_reason`, `model`, `timestamp`) to the **same** `### iter-K` block written by pass 1 in each paper's markdown. Mirror to the frontmatter as the _initial_ `my_final_decision` / `my_justification` (the user may flip them in the spreadsheet). Commit `[NN] run: <count> papers reviewed by LLM` with a footer reporting the number of divergences (`agrees_with_regex == false`).
6. **Human review and lock.** The post-commit hook regenerates `spreadsheet.xlsx`. Tell the user explicitly: "Abra `spreadsheet.xlsx`, aba `<NN> — <Stage>`. Coluna L (`My Final Decision`) está pré-preenchida pelo LLM revisor; revise — comece pelas linhas em vermelho (`Exclude`) e edite as que discordar para `Include`. Coluna M (`My Justification`) é livre. Salve. Diga `pronto`, `done` ou `confirmo`." Wait for the textual confirmation. Then re-read the xlsx (preserving rich-text), validate every row has a non-empty `My Final Decision`, append a `### final` block to every paper's body section with `my_final_decision`, `my_justification`, `locked_at_iteration: iter-K` (= the latest iter-K), `locked_at: <ISO>`, mirror the same to the frontmatter (plus `status.<stage>`), and commit `[NN] lock`.

## 4. Per-stage evidence sources

The pass-1 classifier and pass-2 reviewer agree on what fields of each paper they may consume:

|     stage      | fields available to pass 1 / pass 2                                                                                                                        |
| :------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   04 (title)   | `title`                                                                                                                                                    |
| 05 (abstract)  | `title`, `abstract`, `keywords` (when present)                                                                                                             |
| 06 (full_text) | `title`, `abstract`, `keywords`, `full_text_sections` (Introduction, System/Model/Method, Setup, Evaluation, Conclusion + sections referenced by criteria) |

Pattern `applicable_stages` in `protocols/classifier-config.json` lets a regex be active in some stages and idle in others (useful for subtitle-only patterns, more reliable on title than on abstract). The stage 06 agent may use either the same `<config_path>` as stage 05 or a separate `protocols/classifier-config-fulltext.json` (configured via `CLAUDE.md §6.classifier_configs.full-text-screening`).

## 5. Spreadsheet contract

`spreadsheet.xlsx` is regenerated from the markdown source-of-truth + the per-stage `proposed.json` + `reviewed.json` files by `scripts/regenerate_spreadsheet.py` after every commit. Filter tabs (one per screening stage) carry these columns in order:

| col | header                 | source                                                                                                                                        | editable |
| :-: | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | :------: |
|  A  | Paper ID               | frontmatter `id`                                                                                                                              |    no    |
|  B  | Title                  | frontmatter `title` (rich-text bold spans from `protocols/bolding-keywords.yaml`, with legacy `evidence_trail` fallback)                      |    no    |
|  C  | Authors                | frontmatter `authors`                                                                                                                         |    no    |
|  D  | Year                   | frontmatter `year`                                                                                                                            |    no    |
|  E  | Venue                  | frontmatter `venue`                                                                                                                           |    no    |
|  F  | Abstract               | body Metadata section (rich-text bold spans from `protocols/bolding-keywords.yaml`, with legacy `evidence_trail` fallback; stages 05/06 only) |    no    |
|  G  | Proposed Decision      | `### Proposed (regex)` `proposed_decision`                                                                                                    |    no    |
|  H  | Proposed Justification | `### Proposed (regex)` `proposed_justification`                                                                                               |    no    |
|  I  | Evidence Trail         | `### Proposed (regex)` `evidence_trail` (JSON serialized)                                                                                     |    no    |
|  J  | Winning Category       | `### Proposed (regex)` `winning_category`                                                                                                     |    no    |
|  K  | Overrides Applied      | `### Proposed (regex)` `overrides_applied` (JSON list)                                                                                        |    no    |
|  L  | My Final Decision      | `### Reviewed (LLM)` `my_final_decision`; user may edit                                                                                       | **yes**  |
|  M  | My Justification       | `### Reviewed (LLM)` `my_justification`; user may edit                                                                                        | **yes**  |
|  N  | Agrees with Regex      | `### Reviewed (LLM)` `agrees_with_regex`                                                                                                      |    no    |
|  O  | Divergence Reason      | `### Reviewed (LLM)` `divergence_reason`                                                                                                      |    no    |

Mandatory formatting (filter tabs only):

1. **PatternFill on A and B** keyed by `My Final Decision`:
   - `Include` → green fill `FFE7FFEE`.
   - `Exclude` → red fill `FFFFEFF0`.
   - empty → no fill.
2. **Sort within the tab:** `Exclude` first, then `Include`, then empty. Tie-break by `Paper ID` ascending. Zero-padded ids preserve natural order up to `paper-9999`.
3. **Bold via `CellRichText`** in B (Title) and F (Abstract). Default source: the curated keyword list at `protocols/bolding-keywords.yaml` (seeded from `templates/bolding-keywords.yaml.template` at scaffold time). The pipeline runs `strip_patterns` to remove editorial noise (copyright lines, publisher boilerplate), then a spaCy `PhraseMatcher` (LOWER, longest-match-first), then merges adjacent spans separated by whitespace or hyphens, absorbs trailing plural `s`, trims `stopword_trim` tokens at span edges, and drops the shortest spans first when total bolded length would exceed 50% of the cell. When the YAML file is absent or spaCy / `en_core_web_sm` is unavailable, falls back to the legacy behavior — bolding every `matched_substring` from any `evidence_trail` entry of the paper (with overlapping spans merged into a single run).
4. **Hyperlinks (Phase 3 of the migration):** A → `papers/paper-NNNN.md` relative; I at stage 06 → `papers/paper-NNNN.fulltext.md#§<seção>:para-<n>` when available. Phase 1 may ship without hyperlinks.

Read rules at lock time:

- `openpyxl.load_workbook(path, rich_text=True)` to preserve `CellRichText`.
- Read L and M only; never re-read read-only columns from the xlsx.
- Preserve fills, table definitions, and frozen panes across regenerations.
- Atomically update on edit: cell L value, cell M value, fills on A and B of the same row.

## 5b. Few-shot cross-review cache + Anthropic prompt caching (Phase 5)

The pass-2 LLM reviewer's prompt has two layers (PLUGIN-SPEC §20.5–§20.6):

- **Cacheable prefix** — verbatim categories from `protocols/classifier-config.json`, the prose `criteria_summary`, the top-K (default 15) cross-review few-shot examples, the locked taxonomy excerpt (when present), and the JSON output schema. Identical bytes across every paper in a batch.
- **Variable suffix** — the batch's per-paper content (title, abstract, full-text excerpt, pass-1 record).

The parent skill (`skills/04-screen/SKILL.md`) computes the current review's `criteria_signature` (sha256 of the criteria text) and queries `scripts/few_shot_cache.py --query` before spawning the reviewer. The query selects examples by:

1. **Same review + same signature** (best — direct prior decisions): score = similarity + 1.0.
2. **Same review, signature drifted** (criteria moved since the example was captured): score = similarity + 0.3.
3. **Cross-review, same signature** (rare consensus signal): score = similarity + 0.5; capped at 5 examples per query.
4. **Cross-review, drifted signature** (only the most relevant survive ranking): score = similarity × 0.5; same cap.

Similarity is TF-IDF cosine over tokenized `criteria_summary` strings — pure Python, no ML dependencies in Phase 5. Future revisions can swap to MiniLM cosine via a shared embedding cache without changing the schema or CLI.

After the user locks a screening stage, the parent skill walks the flips (papers where `My Final Decision` differs from the LLM reviewer's pre-fill) and appends one example per flip to `~/.rapid-review/few-shot-cache/index.jsonl` plus the per-review mirror at `reviews/<slug>.jsonl`. TTL is 18 months; expired entries are dropped from the global index by `scripts/few_shot_cache.py --purge-expired`.

## 6. Idempotency and reruns

The classifier is a pure function; the runner skips papers in `existing_my_final_decision_ids`. The reviewer is non-deterministic (LLM) but skips the same set. Two consecutive runs yield byte-identical `proposed.json` and a `reviewed.json` whose `my_final_decision` field is stable in 95+% of cases under modern Anthropic models; the parent skill commits both runs and the materialized `### iter-K` block reflects the latest run. Prior runs are preserved in git history.

Reopen-by-checkpoint (per `_agent-contract.md §6` and `PLUGIN-SPEC §18`): a stage that has been locked may be reopened by `[NN] checkpoint: <reason>` (e.g., `criteria revised`, `model changed`). The reopen flips `locks.<stage>` from `locked` to `iterating` and re-enters the loop at step 2 (criteria reuse/refine). Papers whose `My Final Decision` was filled in the previous run are bypassed by default; the user may explicitly clear specific cells in the xlsx to force re-review.

## 7. Per-stage frontmatter (paper markdown)

Each `papers/paper-NNNN.md` carries per-stage records under the `screening` key:

```yaml
status:
  04-title-screening:      pending | include | exclude
  05-abstract-screening:   …
  06-full-text-screening:  …  (or "unavailable" when no PDF)

screening:
  04-title-screening:
    last_iteration:          0   # integer K — points at the latest iter-K body block
    proposed_decision:       Include | Exclude | null
    proposed_justification:  "<verbatim PT-BR>" | null
    winning_category:        "<category_id | default>" | null
    overrides_applied:       ["<override_id>", …]
    my_final_decision:       Include | Exclude | null
    my_justification:        "<1–3 frases PT-BR>" | null
    agrees_with_regex:       true | false | null
    divergence_reason:       "<…>" | null
    locked_at_iteration:     "iter-K" | null
    locked_at:               "<ISO timestamp>" | null
  05-abstract-screening: { … same shape … }
  06-full-text-screening: { … same shape … }
```

The frontmatter mirrors the **latest** iter-K block. `last_iteration` is set by the runner whenever it appends a new iter-K body block; the spreadsheet's `Last Iteration` column reads it directly. `locked_at_iteration` is set at lock time and points at the iteration whose verdict the user kept (typically the latest, but the user may roll back via `04-screen --revert`).

`status.<stage>` mirrors `my_final_decision` (lower-cased) when present; otherwise it equals `proposed_decision` (lower-cased). `pending` is the initial state before any pass.

## 8. Commit batching

Within a single stage execution:

- `[NN] claude-md: model selected (<id>)` — emitted once at step 1 if the model was missing.
- `[NN] config: classifier-config initialized` — emitted once at step 3 on first run.
- `[NN] iteration: criteria refined (<summary>)` — emitted by `04-screen --refine`; replaces `[NN] config: classifier-config initialized` on subsequent reruns.
- `[NN] run: <count> papers classified by regex` — emitted at step 4. Footer: distribution by `winning_category`.
- `[NN] run: <count> papers reviewed by LLM` — emitted at step 5. Footer: number of divergences.
- `[NN] checkpoint: <reason>` — reserved for reopens (criteria, model, threshold). Flips lock to `iterating`.
- `[NN] lock` — final commit, after the human edits are reconciled and the user confirms textually. Sets `locks.<stage>: locked` in `CLAUDE.md §1` and updates `Current stage` in §0.

The pre-v3 commit families (`[NN] consolidate: <count> papers`, `[NN] claude-md: threshold <value>`, etc.) are gone. Threshold and criteria changes go through `04-screen --refine` and the stage-01 reopen-by-checkpoint flow respectively.

## 9. What v2 had and v3 does not

The adversarial sub-agent architecture (two postures + halo-randomized criterion order + deterministic consolidator + per-stage Cohen's kappa) is gone. Reasons:

- **Cost and latency.** Two LLM calls per paper × hundreds of papers × three stages was the dominant runtime cost.
- **Reproducibility.** The pass-1 classifier is a pure function; pass-2 is a single non-deterministic call (cached prefix amortizes the cost). The result is more auditable and cheaper to rerun.
- **Better signal at the spreadsheet.** Disagreement-sorted tabs surfaced framing-robustness, not relevance. The xlsx now sorts by `My Final Decision`, putting the user-controllable verdict at the front.

Reviews started under v2 are not migrated automatically; v2 is preserved at tag `v2-final`. New reviews use this protocol from `/01-bootstrap` onward.
