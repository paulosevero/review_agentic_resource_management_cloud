---
id: paper-1639
title: Online Offloading and Mobility Awareness of DAG Tasks for Vehicle Edge Computing
authors:
- He, Xiao
- Pang, Shanchen
- Gui, Haiyuan
- Zhang, Kuijie
- Wang, Nuanlai
- Yu, Shihang
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2025
doi: 10.1109/TNSM.2024.3470777
url: https://www.scopus.com/pages/publications/105001068348?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 675--690
keywords:
- deep reinforcement learning
- directed acyclic graph
- edge computing
- Internet of Vehicle
- Lyapunov optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1639 — Online Offloading and Mobility Awareness of DAG Tasks for Vehicle Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Achieving real-time processing of tasks has become a crucial objective in the Internet of Vehicles (IoV) field. During the online generation of tasks in IoV systems, many dependency tasks arrive randomly within continuous time frames, and it is impossible to predict the number of arriving tasks and the dependencies between sub-tasks. Offloading dependent tasks, which are quantity-intensive and have complex dependencies, to appropriate vehicle edge servers (VESs) for online processing of large-scale tasks remains a challenge. Firstly, we innovatively propose a VES task parallel processing framework incorporating a multi-level feedback queue to enhance the cross-slot parallel processing capabilities of the IoV system. Secondly, to reduce the complexity of problem-solving, we employ the Lyapunov optimization method to decouple the online task offloading control problem into single-stage mixed-integer nonlinear programming problem. Finally, we design an online task decision-making algorithm based on multi-agent reinforcement learning to achieve real-time task offloading decisions in complex dynamic IoV environments. To validate our algorithm’s superiority in dynamic IoV systems, we compare it with other online task offloading decision-making algorithms. Simulation results show that ours significantly reduces the all-task processing latency of IoV system by 15% compared to the comparison algorithms, and the task average latency time is reduced by 14%. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1639.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
