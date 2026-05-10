---
id: paper-1085
title: Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks
authors:
- Men, Rui
- Fan, Xiumei
- Yau, Kok-Lim Alvin
- Shan, Axida
- Yuan, Gang
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2024
doi: 10.1109/TNSE.2024.3391382
url: https://www.scopus.com/pages/publications/85193244954?origin=resultslist
publisher: IEEE Computer Society
pages: 3891--3904
keywords:
- aerial computing
- lyapunov optimization
- MARL
- resource allocation
- Task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1085 — Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The upsurge of mobile service demands underscores the inevitability of the emergence of 6G technology. Amidst the challenges that accompany the 6G networks, the exponential growth of computation-intensive and delay-sensitive applications in vehicular networks poses a significant hurdle. Vehicular edge computing relying solely on terrestrial infrastructures cannot meet the performance requirements due to insufficient resources in edge servers. To address this challenge, we introduce a novel three-layer hierarchical architecture called the air-ground-end aerial computing (AGEAC) architecture, which consists of three types of resource providers, namely high-altitude platform stations, roadside units, and volunteer vehicles willing to share their underutilized resources. We select service vehicles based on the utilization rate of their underutilized resources to ensure fairness. Our objective is to minimize the average latency of all tasks in the long term, and it is formulated as a mixed-integer nonlinear programming problem for task offloading and resource allocation. The complicated intertwined problem is decomposed into four sub-problems by leveraging Lyapunov optimization method. A multi-agent reinforcement learning-based algorithm is designed to make offloading decisions, and convex optimization is introduced to allocate resources iteratively. Extensive simulations have been conducted to demonstrate the superiority of AGEAC in terms of convergence speed, average latency, and resource utilization.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1085.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
