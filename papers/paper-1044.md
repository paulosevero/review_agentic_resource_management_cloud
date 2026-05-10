---
id: paper-1044
title: Rethinking Low-Carbon Edge Computing System Design with Renewable Energy Sharing
authors:
- Liao, Hanlong
- Tang, Guoming
- Guo, Deke
- Wang, Yi
- Cao, Ruide
venue: ACM International Conference Proceeding Series
venue_type: conference
year: 2024
doi: 10.1145/3673038.3673080
url: https://www.scopus.com/pages/publications/85202438540?origin=resultslist
publisher: Association for Computing Machinery
pages: 950--960
keywords:
- Low-carbon edge computing
- multi-agent deep reinforcement learning
- renewable energy sharing
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1044 — Rethinking Low-Carbon Edge Computing System Design with Renewable Energy Sharing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The geographically distributed edge servers can naturally draw power from nearby renewable energy (RE) generators. Complemented by the dynamic scheduling of energy storage batteries, edge service providers (ESPs) can thus build low- or even zero-carbon edge computing systems. Nevertheless, the distributed and heterogeneous nature of edge computing systems, as well as the limited information sharing among ESPs, leads to a more complex battery planning problem than that in cloud computing. The unpredictability of RE resources further complicates the problem, making conventional model-based approaches ineffective. To this end, we propose a multi-agent deep reinforcement learning (MADRL) approach for the independent decision making of individual ESPs. Particularly, MADRL takes privacy into account by ensuring that no sensitive information is disclosed among ESPs. For better model training, we further customize the invalid action masking and develop action transformation techniques based on segmented linear optimization. Extensive experiments demonstrate that, with our proposed approach, the overall carbon emission of edge computing systems can be significantly reduced (by over 60%) while maintaining acceptable operation costs in battery scheduling.  © 2024 Owner/Author.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1044.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
