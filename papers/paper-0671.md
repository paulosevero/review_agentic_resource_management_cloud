---
id: paper-0671
title: Optimizing Task Completion Time in Disaster-Affected Regions with the WMDDPG-GSA Algorithm for UAV-Assisted MEC Systems
authors:
- Ma, Tianhao
- Yang, Yulu
- Xu, Han
- Song, Tiecheng
venue: Processes
venue_type: journal
year: 2023
doi: 10.3390/pr11103000
url: https://www.scopus.com/pages/publications/85174959274?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- Doppler Frequency Shift (DFS)
- Mobile Edge Computing (MEC)
- Multi-Agent Deep Reinforcement Learning
- UAV
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0671 — Optimizing Task Completion Time in Disaster-Affected Regions with the WMDDPG-GSA Algorithm for UAV-Assisted MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we investigate a UAV-assisted Mobile Edge Computing (MEC) system that is deployed with multiple UAVs to provide timely data processing services to disaster-stricken areas. In our model, since base stations are unavailable in disaster-affected areas, we solely employ UAVs as MEC servers, as well as enable real-time data transmission during UAV flights by estimating and compensating for the Doppler Frequency Shift (DFS). Subsequently, an optimization problem is formulated to jointly optimize the trajectories and offloading strategies of multiple UAVs to minimize the task completion time. We enhance the performance of the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm by using a weighted strategy algorithm, and we thus propose the Weighted-Strategy-Based Multi-Agent Deep Deterministic Policy Gradient (WMDDPG) algorithm for optimizing UAV trajectories. We employ the Greedy-Based Simulated Annealing (GSA) algorithm to overcome the limitations of the greedy algorithm and to obtain the best offloading strategy. The results demonstrate the effectiveness of the proposed WMDDPG-GSA algorithm, as it outperforms benchmark algorithms. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0671.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
