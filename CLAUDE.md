<!--
Template for the per-review CLAUDE.md.
Instantiated by `/00-new-review <topic>`. Placeholders in <angle brackets> are filled by the user
(directly or through the /01-research-questions, /02-search-string, /03-parse-references-metadata agents).

IMPORTANT: At runtime, this file is the protocol for the review. Agents READ it at the start of
every command and NEVER modify it autonomously. Any protocol change goes through a checkpoint
conversation and is committed as `[NN] claude-md: <change>` before the agent resumes work.
-->

# Rapid Review — Protocol

This file is the authoritative protocol for this review. It declares the theme, research questions, search string, inclusion/exclusion criteria, per-stage modes, accumulated decision anchors, and taxonomy. Every agent in this plugin reads it before acting. It is read-only at runtime; updates happen only through checkpoint commits.

---

## 0. Meta

- **Topic:** `Agentic AI (LLM-based agents) for resource management decisions in Cloud, Edge, Fog, and the Edge-Cloud Continuum`
- **Repo:** `/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud`
- **Created:** `2026-04-25`
- **Current stage:** `00-new-review`

## 1. Locks (machine-readable)

Agents use this block to decide whether a given stage can run. A stage can only start when its predecessors are all `locked`.

```yaml
locks:
  00-new-review:                locked    # pending | locked
  01-research-questions:        pending
  02-search-string:             pending
  03-parse-references-metadata: pending
  04-title-screening:           pending
  05-abstract-screening:        pending
  06-full-text-screening:       pending
  07-taxonomy-development:      pending   # has intermediate `iterating` state during inductive loop
  08-analysis:                  pending
```

## 2. Theme

`<1–2 paragraphs describing the domain, its practical relevance, and the boundary of what this review covers and does not cover. Filled by /01-research-questions.>`

**Screening doctrine.** When in doubt at title or abstract stages, include. A false positive costs one extra read at the next stage; a false negative loses a relevant paper forever. This asymmetry is operationalized via the per-stage thresholds in `protocols/screening.yaml.stage_allocation` (permissive early, strict late) and the abstract-stage `insufficient_evidence` rule in `agents/_screening-protocol.md §5.2`. The adversarial sub-agent architecture (two opposed sub-agents + deterministic consolidator + human override in the spreadsheet) is specified in `agents/_screening-protocol.md`.

## 3. Research Questions

`<Hierarchical list, filled by /01-research-questions. The authoritative machine-readable form lives in protocols/screening.yaml; this section is its prose mirror. Each RQ has 1–3 sub-RQs covering dimensions of the same phenomenon (Padrão 1 — thematic decomposition).>`

- **RQ1:** `<...>`
  - **RQ1.1:** `<sub-RQ text>`
  - **RQ1.2:** `<sub-RQ text>`
- **RQ2:** `<...>`
  - **RQ2.1:** `<...>`
- **RQ3:** `<...>`
  - **RQ3.1:** `<...>`

## 4. Search String

```
<Boolean search string produced by /02-search-string, with operators in uppercase and terms quoted when needed.>
```

**Target databases:** `<Scopus, Web of Science, IEEE Xplore, ACM Digital Library, ...>`

**Search executed on:** `<YYYY-MM-DD, filled when the user runs /03-parse-references-metadata and reports the date of the manual search>`

**Notes on per-database adaptation:** `<If the string had to be adapted to each database's syntax, record the adaptations here. Filled by /02-search-string.>`

## 5. Inclusion Criteria (typed)

Criteria are typed (`thematic_rq` / `thematic_sub_rq` / `qa`) and weighted, declared once at stage 01, and locked alongside the rest of `protocols/screening.yaml`. This section is the readable mirror; the authoritative definition lives in the YAML. Each criterion is anchored to one or more RQ or sub-RQ ids via `refs`. When the protocol is reopened (`[01] checkpoint: revisit criteria`), this section is regenerated from the updated YAML.

### `thematic_rq` (ternary, applies at stage 04)

- **C1** — refs: `[RQ1]` — `<criterion text>` — weight: `null`
- **C2** — refs: `[RQ2]` — `<...>` — weight: `null`

### `thematic_sub_rq` (weighted, applies at stages 05 and 06)

- **C3** — refs: `[RQ1.1]` — `<criterion text>` — weight: `0.4`
- **C4** — refs: `[RQ1.2]` — `<...>` — weight: `0.3`
- **C5** — refs: `[RQ2.1]` — `<...>` — weight: `0.4`

### `qa` (weighted, applies at stage 06)

- **C6** — refs: `[RQ1, RQ2]` — `<reproducibility / methodological / reporting criterion>` — weight: `0.2`

## 6. Reserved

The v1 per-stage adversarial-mode toggle is gone. Stages 04/05/06 always run two adversarial sub-agents (inclusivist + exclusivist) by construction; there is nothing to opt into. Stage 07 keeps a per-axis adversarial mode at classification time (07b) — the choice is made at stage 07's opening ritual, not stored here.

## 7. Anchors

Decisions accepted at checkpoints become anchors for subsequent decisions in the same or later stages. Anchors are NOT a parallel criteria system — they are concrete examples the agent can cite when a borderline case resembles one already decided. Each anchor links to the commit that created it.

### Inclusion anchors

- `<paper-id>` — `<brief reason>` — commit `<hash>` — stage `<NN>`

### Exclusion anchors

- `<paper-id>` — `<brief reason>` — commit `<hash>` — stage `<NN>`

### Taxonomy anchors

Populated during `07-taxonomy-development`. Each anchor pins a paper to a prototypical position on one or more axes.

- `<paper-id>` — axis `<axis>` = `<value>` — `<reason>` — commit `<hash>`

## 8. Taxonomy

The taxonomy is built inductively in stage `07-taxonomy-development` and iterates until the user marks it locked. Until then, this section reflects the current iteration.

**Status:** `pending` | `iterating` (with current iteration number) | `locked`

### 8.1 Axes

`<Empty while pending. During iteration, lists candidate axes proposed by the open-coding + clustering loop. Each axis has a short description and the set of permitted values.>`

- **`<axis-name>`** — `<short description>`
  - Values: `<v1, v2, v3, ...>`

### 8.2 Code book

`<Definition of each value in each axis, with 1–2 sentences explaining when a paper fits that value. Emerges during the open-coding stage; refined during clustering.>`

- `<axis>` / `<value>`: `<definition>`

### 8.3 Iteration history

Each iteration of the taxonomy is a commit `[07] iteration-<k>`; the final state is `[07] lock`.

- **Iteration 1:** `<summary: e.g., "initial open coding produced 47 free codes over 38 papers">`
- **Iteration 2:** `<summary: e.g., "clustering proposed 5 axes; user merged two overlapping ones">`
- **Iteration k:** `<...>`
- **Locked:** commit `<hash>` — `<summary>`

## 9. Reserved

The v1 semantic-neighbor consistency check is gone. The v2 adversarial sub-agent architecture (two postures + halo-randomized criterion order + deterministic consolidator + per-stage Cohen's kappa) replaces it; spurious agreement across similar papers is no longer the controlling signal. Reviewers use the spreadsheet's per-stage tabs (sorted by sub-agent disagreement descending) to surface borderline papers.

## 10. Notes

`<Free-form notes about the review. Examples: venues to pay special attention to, authors with known conflicts of interest to flag, prior related reviews the user wants to avoid duplicating.>`

## 11. Reserved

Per-stage screening thresholds live in `protocols/screening.yaml.stage_allocation.<stage>.threshold` and are fixed at stage 01 lock. Overrides go through `[01] checkpoint: revisit weights` (which reopens stage 01 at level 4); they are no longer per-stage knobs. See `templates/protocols-schema.md §3.4` for the canonical defaults (title 0.5, abstract 0.6, full-text 0.6).

---

<!--
Change history: do not edit manually. The git log on this file is the authoritative history of
protocol changes. Inspect it with `git log -p CLAUDE.md` to see how criteria, modes, and taxonomy
evolved during the review.
-->
