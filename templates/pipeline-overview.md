# Rapid Review — Pipeline Overview

The plugin drives a rapid-review pipeline as a sequence of macro skills. Each skill owns a stage, a branch in the review repo, an explicit lock in `CLAUDE.md §1`, and the artifacts it produces. Markdown is the single source of truth; the post-commit hook regenerates `spreadsheet.xlsx` from the markdown on every commit.

You invoke a skill by typing `/<skill-name>` (e.g. `/04-screen --stage title`). When in doubt about which skill to run next, type `/_router` (or simply ask "qual a próxima skill?") and the conversational router will read the lock state plus the filesystem and propose the next step. The router never auto-invokes — you have the final say.

## 01-bootstrap (`/01-bootstrap`)

You are running this skill right now. It scaffolds the review repository, initializes git, installs the post-commit hook, pairs the local repo with an empty GitHub remote, pushes the initial scaffold, presents this overview, and routes you to the next skill based on what you already have in mind. Locks `00-new-review`.

## 02-define-protocol (`/02-define-protocol`)

Fuses what the v2 plugin called stages 01 (research questions) and 02 (search string) into one extended dialog. Half A produces 3–5 numbered RQs, sub-RQs, typed inclusion criteria (`thematic_rq` / `thematic_sub_rq` / `qa`), and per-criterion weights, validates them with `scripts/validate_protocol.py`, and locks `01-research-questions`. Half B derives the Boolean search string with concept extraction from the locked RQs/sub-RQs/criteria, captures per-database adaptations, and locks `02-search-string`.

Produces: CLAUDE.md §0/§2/§3/§4/§5; `protocols/screening.yaml`. Locks `01-research-questions` and `02-search-string`.

After this skill: run the search manually in each target database and drop the exports into `raw/exports/` (one file per database, named `<db>-YYYY-MM-DD.bib|ris|csv`).

## 03-import-results (`/03-import-results`)

Reads every file in `raw/exports/`, normalizes fields, deduplicates records (by DOI > title+year+first-author > title+year with confirmation), and materializes one `papers/paper-NNNN.md` per unique record from the per-paper template. Paper IDs are 4-digit zero-padded and stable for the entire review.

Produces: `papers/paper-NNNN.md` per record; `stages/03-parse-references-metadata.md` import + dedup log. Locks `03-parse-references-metadata`.

## 04-screen (`/04-screen --stage {title|abstract|full-text}`)

The unified screening skill. Replaces what the v2 plugin called stages 04/05/06 with one skill that dispatches on `--stage`. Each stage runs in two passes:

- **Pass 1** — a deterministic regex classifier configured by Q&A on first run of `--stage title` and persisted in `protocols/classifier-config.json`. Stages `abstract` and `full-text` reuse the same config or refine it; stage `full-text` may split to `protocols/classifier-config-fulltext.json` for stage-specific patterns.
- **Pass 2** — a single LLM reviewer (model from `CLAUDE.md §6.models.<stage>`) reads the pass-1 record + the stage-allowed body and pre-fills `My Final Decision` (col L) and `My Justification` (col M) in the spreadsheet.

The user reviews the spreadsheet, flips disagreements directly in col L, and confirms with `pronto`. The skill reconciles edits into the markdown source-of-truth and locks `<stage>`.

Produces per stage: `protocols/classifier-config.json` (created at first `--stage title`); `screening/<stage_dir>/proposed.json` and `reviewed.json`; `### Proposed (regex)` + `### Reviewed (LLM)` sub-sections per paper; the corresponding `## NN — <Stage>` body section.

After `--stage abstract` lock: download PDFs for every included paper into `raw/pdfs/paper-NNNN.pdf`. Optionally invoke `prepare-pdf` to extract structured fulltexts (Phase 3 feature; Phase 1/2 builds the excerpt at runtime).

## 05-code-taxonomy (`/05-code-taxonomy`)

Builds the review's taxonomy. Three possible origins (chosen in the opening ritual): `from-sub-rqs` (every sub-RQ becomes a seed axis), `inductive` (pure open coding → clustering loop), or `hybrid` (subset of sub-RQs as seeds + inductive over the remainder). Phase 07a is open coding per paper; phase 07b is per-axis classification after the taxonomy structure locks.

Produces: CLAUDE.md §8; `## 07a` and `## 07b` sections per paper; `stages/07-taxonomy-development.md`. Locks `07-taxonomy-development`.

## 06-analyze (`/06-analyze`)

Maps each RQ to one or more analysis views over the taxonomy (pivot, temporal, venue, distribution). Every view declares an explicit `rq_anchor` field naming the RQ or sub-RQ it answers — empty views are diagnosed against the protocol hierarchy and routed back to `05-code-taxonomy` or `02-define-protocol` checkpoints.

Produces: `## 08` section per paper with the views it contributes to; `stages/08-analysis.md`; `spreadsheet.xlsx` analysis tabs (one per view). Locks `08-analysis`.

## 07-report (`/07-report`)

Generates `report/index.md`, the navigable final summary. Per RQ: views anchored on the RQ, taxonomy axes the views touch, contributing papers, and 2–4 verbatim quotes per view. Plus a corpus summary (counts), a protocol summary (RQs + search string + screening pipeline), and a reproducibility section. The report is the entry point for the manuscript-writing phase that happens outside the plugin.

Produces: `report/index.md`. Locks `09-report`.

---

## Auxiliary skills and screen modes

- **`/04-screen --refine '<patch-or-prose>'`** — refines `protocols/classifier-config.json` mid-screening with a pre-flight diff that shows the projected impact on unreviewed papers before applying the change.
- **`/04-screen --revert [--dry-run]`** — rolls back the most recent `[NN] iteration: criteria refined` commit on the current branch via `git revert --no-edit`.
- **`/prepare-pdf`** — extracts section-anchored text from `raw/pdfs/paper-NNNN.pdf` into `papers/paper-NNNN.fulltext.md` with quality flags and a sha256 cache.
- **`/refine-bolding`** — refines `protocols/bolding-keywords.yaml` against the actual corpus once `03-import-results` has run.
- **`/sheets-sync --mode {push|pull}`** — opt-in Google Sheets integration. First call is `--mode push` to create the document; later sync alternates push and pull explicitly.

## How skills relate

- Each macro skill runs on its own branch (`01-research-questions`, `02-search-string`, …, `08-analysis`, `09-report`).
- A skill cannot run until every upstream lock is set. The locks live in `CLAUDE.md §1`.
- Reopening a stage requires an explicit `[NN] checkpoint: <reason>` commit on its branch. Later locks are preserved in their commits and remain accessible.
- The xlsx is regenerated on every commit and is gitignored. It is a projection of the markdown — never edit it by hand expecting changes to persist (except during `04-screen`, where `My Final Decision` cells are read back into paper markdowns at lock time).

## What you do between skills

The plugin does not access databases, fetch PDFs, or edit external systems. Manual steps:

- Between `02-define-protocol` and `03-import-results`: run the search in each database, place exports in `raw/exports/`.
- Between `04-screen --stage abstract` and `04-screen --stage full-text`: download PDFs for included papers into `raw/pdfs/paper-NNNN.pdf`.
- During `04-screen`: review and edit `My Final Decision` (column L) in the corresponding `spreadsheet.xlsx` tab. The cell is pre-filled by the LLM reviewer; you flip the verdicts you disagree with. The skill waits for your `pronto` confirmation before re-importing decisions.

## Reference reviews

If you have placed exemplar reviews under `reference-reviews/` (in the plugin directory) and registered them in `reference-reviews/index.yaml`, the skills at the early stages (`02-define-protocol`, `04-screen`, `05-code-taxonomy`) may consult them to inform their suggestions. They never replicate a reference verbatim and always cite the influencing entry by `citation_key`. Use `/add-reference-review <pdf-or-md>` to extract a new entry from a manuscript.
