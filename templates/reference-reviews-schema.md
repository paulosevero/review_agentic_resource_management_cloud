# Reference Reviews — Schema

This document is the authoritative description of `reference-reviews/index.yaml`. Both `/add-reference-review` and the consuming agents (stages 01/02/04/05/06/07) rely on this schema; keep it in sync if the YAML structure changes.

## File location

- `reference-reviews/index.yaml` — the index itself, lives in the plugin repository (not in any individual review repo).
- `reference-reviews/pdfs/<file>.pdf` — optional. PDFs are *not* read by agents during normal operation; agents consult the YAML index only. PDFs are read on explicit user request.

## Top-level structure

```yaml
entries:
  - <entry 1>
  - <entry 2>
  - ...
```

`entries` is a list. The order is purely cosmetic (sort by `citation_key` alphabetically as a convention). An empty list (`entries: []`) is valid and means "no exemplars registered yet".

## Per-entry fields

Each entry is a YAML mapping with the following keys.

### Required

- **`citation_key`** *(string)* — short stable identifier. Convention: `<first-author-surname><year><short-slug>`, e.g., `kitchenham2007guidelines`, `petersen2015mapping`. Lowercase, no spaces. Must be unique across `entries`.
- **`doi_or_url`** *(string)* — DOI in canonical form (`https://doi.org/10.xxxx/yyyy`) or a stable URL when no DOI exists. One value, no list.
- **`domain`** *(string)* — one short noun phrase, e.g., `software engineering`, `edge computing`, `agentic AI for cloud orchestration`. Used by agents as a coarse relevance filter.
- **`research_questions`** *(list of strings)* — verbatim RQs from the reference review. Numbered prefix (`RQ1: …`) optional but recommended.
- **`inclusion_criteria`** *(list of mappings)* — each mapping has `text` (the criterion verbatim) and `type` ∈ `{thematic_rq, thematic_sub_rq, qa}`. Entries that predate the v2 hierarchical typing (Phase D) may use `type: legacy` until reclassified.
- **`what_this_does_well`** *(list of strings)* — 1–3 bullets, in the curator's voice. The reason this entry was added as an exemplar. Subjective; only the user fills this — the agent must ask, never infer.

### Optional

- **`local_pdf`** *(string, relative path)* — e.g., `reference-reviews/pdfs/kitchenham2007guidelines.pdf`. Omit if no local copy.
- **`sub_research_questions`** *(list of strings or list of mappings)* — sub-RQs verbatim. Mappings may carry `parent: RQ1` to record the parent linkage when known.
- **`search_string`** *(string)* — the Boolean search string verbatim, on a single line if possible. Use a literal block (`|`) if multi-line in the source.
- **`taxonomy_axes`** *(list of mappings)* — each mapping has `name` and `values` (list of strings). Captures the taxonomy structure the reference review used.
- **`metrics_reported`** *(list of strings)* — short labels of evaluation metrics the reference review reported (e.g., `included papers count`, `inter-rater agreement (kappa)`).
- **`caveats`** *(list of strings)* — 1–2 bullets noting things the reader should *not* replicate from this entry. Subjective; the agent must ask the user, never infer.

## Validation rules

A YAML file is valid when:

1. The top level has exactly one key, `entries`, mapping to a list.
2. Every entry is a mapping with all the **Required** fields listed above and no extra unknown keys.
3. `citation_key` values are unique across the file.
4. `inclusion_criteria[*].type` ∈ `{thematic_rq, thematic_sub_rq, qa, legacy}`.
5. If `local_pdf` is present, the path is resolvable (file exists at that path relative to the plugin root). Agents must warn but not refuse when the file is missing.

## Example entry

```yaml
entries:
  - citation_key: kitchenham2007guidelines
    doi_or_url: https://www.elsevier.com/__data/assets/pdf_file/0006/55382/EBSE-2007-01.pdf
    domain: software engineering systematic reviews
    research_questions:
      - "RQ1: What guidelines exist for performing systematic literature reviews in software engineering?"
    sub_research_questions:
      - text: "What protocol elements should be defined before a review starts?"
        parent: RQ1
      - text: "What quality assessment criteria apply to primary studies?"
        parent: RQ1
    inclusion_criteria:
      - text: "The study addresses methodology for systematic reviews."
        type: thematic_rq
      - text: "The study reports an empirical evaluation of the methodology."
        type: qa
    search_string: |
      ("systematic literature review" OR "systematic review")
      AND ("software engineering" OR "software development")
    taxonomy_axes:
      - name: review_type
        values: ["systematic", "mapping", "rapid", "tertiary"]
      - name: domain
        values: ["software engineering", "empirical software engineering"]
    metrics_reported:
      - "included primary studies count"
      - "quality assessment scores"
    what_this_does_well:
      - "Establishes the canonical SLR protocol used in software engineering."
      - "Defines a quality assessment rubric that downstream reviews adopt verbatim."
    caveats:
      - "The reporting framework predates AI-assisted screening; do not import its threading rules wholesale."
```

## How the schema evolves

Schema changes happen via a single PR that updates this document, the example, and any agent or script that consumes the YAML. Backwards-compatible additions (new optional fields) require no migration. Backwards-incompatible changes (renaming or removing required fields) require a migration script under `scripts/` and a `[ref] migrate: schema-vX` commit on the plugin repo.
