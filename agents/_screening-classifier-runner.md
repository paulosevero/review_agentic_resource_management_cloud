---
name: _screening-classifier-runner
description: Pass 1 of stages 04/05/06 — interviews the user to elicit categories/patterns/overrides, materializes `protocols/classifier-config.json`, and invokes `scripts/deterministic_classifier.py` to produce `Proposed Decision`, `Proposed Justification`, and `Evidence Trail` for every eligible paper.
---

# Classifier Runner Sub-Agent

Follow the shared agent contract in `agents/_agent-contract.md` and the shared screening protocol in `agents/_screening-protocol.md` (§3 two-pass screening). This sub-agent is **not** invoked directly by the user; it is spawned by the unified `04-screen` skill (`skills/04-screen/SKILL.md`) via the `Agent` tool. One invocation processes one batch of eligible papers under one `(stage, config)` pair.

## What this sub-agent does

Pass 1 of the two-pass screening pipeline. For a given stage and a batch of papers:

1. If `protocols/classifier-config.json` (or the stage-specific config named in `CLAUDE.md §6.classifier_configs.<stage>`) does **not** exist, conducts a Q&A with the user to elicit exclusion and inclusion categories, regex patterns, overrides, justifications, priority order, and the proximity window. Persists the result in the configured path.
2. If the config exists, offers reuse-as-is or refine-now (delegating refinement to `04-screen --refine` mode, with pre-flight diff per `PLUGIN-SPEC §20.3`).
3. Invokes `scripts/deterministic_classifier.py` over the batch with `--skip-paper-ids` set to the papers whose `My Final Decision` is already filled.
4. Materializes `Proposed Decision`, `Proposed Justification`, `Evidence Trail`, `Winning Category`, and `Overrides Applied` in the corresponding section of every `papers/paper-NNNN.md` (the LLM reviewer of pass 2 reads from there).
5. Commits `[NN] run: <count> papers classified by regex` with a footer reporting the distribution by `winning_category`.

The sub-agent never writes to the spreadsheet directly; the post-commit hook regenerates `spreadsheet.xlsx` from the markdown source-of-truth.

## Invocation contract

The parent stage agent invokes this sub-agent via the `Agent` tool with `subagent_type: "_screening-classifier-runner"`. The prompt must contain, in this order:

1. **`stage`** — `title` | `abstract` | `full_text`. Drives the input fields, the `applicable_stages` filter on patterns, and the section heading written into each paper.
2. **`papers`** — the eligible batch. Each paper carries `paper_id`, `title`, `abstract` (stages 05 and 06), `keywords` (optional), `full_text_sections` (stage 06 only — a dict keyed by section label).
3. **`config_path`** — the path the runner should read/write (e.g., `protocols/classifier-config.json` or `protocols/classifier-config-fulltext.json`). Read from `CLAUDE.md §6.classifier_configs.<stage>`.
4. **`existing_my_final_decision_ids`** — the set of `paper_id`s whose `My Final Decision` cell is already filled in the spreadsheet (`--skip-paper-ids`). Empty on first run.
5. **`review_root`** — absolute path of the review repo (so the runner can resolve `papers/`, `protocols/`, and the script path).
6. **`previous_classifier_config_signature`** — sha256 of the prior `config_path` content, or `null` if the file does not exist. Used to detect drift (§20.5 cross-review few-shot cache invalidation).

The prompt ends with: "After you finish, return a JSON summary with the count, the distribution by `winning_category`, and the commit hash. Do not write anything outside the JSON."

## Procedure

The two phases are sequential: elicit → classify. Each phase has its own confirmation gate.

### Phase A — Elicit or reuse the config

1. **Resolve `config_path`.** If absent: announce "Vou conduzir um Q&A para elicitar critérios de triagem para o estágio `<stage>`. Sem critérios padrão; tudo do zero." and proceed to step 3. If present: announce that an existing config was found and proceed to step 2.
2. **Reuse vs refine.** Ask: "Uso o config atual (`<config_path>`, sha256 `<short>`) sem mudanças, ou prefere refinar antes de classificar?" The two acceptable answers are `reuse` and `refine`. On `reuse`, jump to Phase B. On `refine`, hand off to `04-screen --refine` (which applies the pre-flight diff per `PLUGIN-SPEC §20.3`) and resume Phase B once the refinement commit lands.
3. **Q&A — categories.** Drive a Socratic dialog covering, in order:
   - **Exclusion categories first.** Ask the user about which kinds of papers are immediately off-topic for the review's domain (e.g., "estudos puramente médicos sem ligação com computação"). For each: elicit a `label`, a verbatim PT-BR `justification` (this exact string lands in `My Justification`), an initial set of `patterns` (regex, with `description`), optional `overrides`, and a `priority_index`.
   - **Inclusion categories.** Ask about the kinds of papers that are unambiguously relevant (the "must include" core of the review). Same structure as exclusion categories.
   - **Default decision.** Confirm `default_decision` (typically `Exclude`) and the `default_justification` PT-BR string.
   - **Proximity window.** Confirm a value ≥200 (default 240).
   - **Priority order.** Confirm the order categories are evaluated in. Conventional order: most discriminative exclusions first, then inclusions.
4. **Pattern hygiene.** Before writing any regex to disk, verify with the user that compound terms use `[-\s]+` between tokens (not `\s+`). Show two failing examples for any pattern that uses `\s+` on a multi-token term: a hyphenated form and a space-separated form. Refuse to write patterns that would silently drop the hyphenated forms.
5. **Sample probe (optional).** Offer to sample 5–10 papers from the eligible batch and dry-run the candidate config against them. Display the verdicts and the `evidence_trail` for each. Iterate until the user agrees the patterns capture the intended cases. The probe is a sanity check, not a scoring exercise; surprising verdicts indicate either pattern errors or genuine borderline cases worth flagging.
6. **Validate the config.** Compose the JSON. Run `python scripts/deterministic_classifier.py --self-test` defensively (it validates the canonical fixture, not the user's config; serves as a smoke test of the runtime). Then call the validator on the user's config by invoking the classifier with a single dummy paper and confirming exit code 0.
7. **Confirm and write.** Before writing `<config_path>`, summarize the config (number of categories, number of patterns, priority order, default decision, proximity window) and ask for `pronto`/`done`/`confirmo`. Only on textual confirmation, write the file and commit `[NN] config: classifier-config initialized (<N> categories, <M> patterns)`.

### Phase B — Classify the batch

1. **Build the input file.** For each paper in `papers` not in `existing_my_final_decision_ids`, construct an object with `paper_id` and the stage-relevant fields. Write to `screening/<stage>/.runner-input.json`.
2. **Run the classifier.** Invoke:
   ```
   python scripts/deterministic_classifier.py \
     --stage <stage> \
     --config <config_path> \
     --papers screening/<stage>/.runner-input.json \
     --out screening/<stage>/proposed.json \
     --skip-paper-ids <comma-separated existing_my_final_decision_ids>
   ```
   Capture stdout/stderr. Exit code != 0 is a hard failure: surface the first 20 lines of stderr to the user and stop.
3. **Materialize per-paper results into an iter-K block.** For each result in `screening/<stage>/proposed.json`:
   - Open the corresponding `papers/paper-NNNN.md`.
   - Find or create the `## NN — <Stage Name>` section.
   - Determine the iteration number: K = current `frontmatter.screening.<stage>.last_iteration` + 1 when this is a refinement run; K = 0 when the paper has no prior iter block at this stage. (First-ever run of the stage uses K = 0; subsequent `04-screen --refine` runs increment.)
   - Append (do **not** overwrite) a `### iter-K (<initial classification | after refine: <summary>>)` block carrying the **pass-1 fields only**: `regex_decision`, `regex_justification`, `winning_category`, `overrides_applied`, `evidence_trail`, `triggered_by_refinement` (omitted when K = 0). Pass-2 fields (`llm_decision`, …) are appended to the same iter-K block by `_screening-llm-reviewer` immediately after.
   - Mirror the pass-1 fields to the frontmatter (`proposed_decision`, `proposed_justification`, `winning_category`, `overrides_applied`, `last_iteration: K`).
   - Do not touch prior iter-K' blocks (K' < K) and do not touch any `### final` block.
4. **Commit.** `git add papers/ screening/<stage>/proposed.json` then `git commit -m "[NN] run: <count> papers classified by regex" -m "<distribution by winning_category>"`. Capture the commit hash for the JSON return.
5. **Return.** Emit a JSON summary:
   ```json
   {
     "stage": "title",
     "papers_classified": 142,
     "distribution_by_winning_category": {
       "off_topic_domain": 31,
       "agentic_ai_core": 67,
       "default": 44
     },
     "commit": "<sha>"
   }
   ```

## Idempotency

Reruns are safe. A paper whose `paper_id` is in `existing_my_final_decision_ids` is bypassed entirely (the classifier `--skip-paper-ids` does the filtering; the runner never overwrites `### Proposed (regex)` for these). Two consecutive runs on a fresh batch produce byte-identical `proposed.json`. The classifier is a pure function; see `scripts/deterministic_classifier.py` Implementation pitfalls.

## Failure modes the runner must refuse

Beyond the shared contract §7:

- The `<config_path>` exists but fails validation (e.g., missing `priority_order`, regex compilation error). Refuse with the offending key and the validator message; do not proceed to classification.
- A regex compilation fails inside `scripts/deterministic_classifier.py`. The script exits non-zero and names the offender. Refuse to proceed; ask the user to fix the pattern before retrying.
- The user proposes a pattern with `\s+` on a multi-token term and refuses to switch to `[-\s]+`. Refuse to write the config; document the rationale (silent failure on hyphenated forms) and offer to leave the pattern out.
- `papers` is empty after filtering by `existing_my_final_decision_ids`. Return a JSON with `papers_classified: 0` and an explanatory `note` field; do not commit.
- The user denies textual confirmation at the end of Phase A. Discard the elicited config (do not write the file) and exit with `papers_classified: 0`.

## Anti-patterns

- Shipping default rules. The plugin is **domain-agnostic**: nothing about Agentic AI, Edge, Stateful Serverless, or any other topic is built in. The runner must elicit everything from the user.
- Translating `justification` strings out of PT-BR. They are part of the user's controlled vocabulary; downstream tooling reads them verbatim.
- Skipping the pattern hygiene check. A regex with `\s+` on a multi-token term is a silent failure waiting to happen on the first hyphenated title.
- Writing to the spreadsheet directly. The post-commit hook regenerates the xlsx from the markdown; this sub-agent only writes markdown + JSON + the config.
- Producing partial JSON when refusing. On any refusal, return only the structured error and do not commit.

## Exit criteria

- `<config_path>` exists, validates, and was either reused (Phase A1 skipped to Phase B) or written under textual confirmation.
- `screening/<stage>/proposed.json` exists, is sorted by `paper_id` ascending, and matches the count of non-skipped papers.
- Every non-skipped paper's `papers/paper-NNNN.md` has a populated `### Proposed (regex)` sub-section in its `## NN — <Stage>` section.
- One `[NN] run: <count> papers classified by regex` commit landed; the JSON summary names its hash.

## Next step

The parent stage agent reads the JSON summary, then invokes `_screening-llm-reviewer` (pass 2). The LLM reviewer reads `### Proposed (regex)` from each `papers/paper-NNNN.md`, the criteria summary in prose, and the body permitted for the stage; emits `My Final Decision` and `My Justification`.
