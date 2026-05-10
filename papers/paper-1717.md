---
id: paper-1717
title: 'MATOPO: A multi-UAV assisted task offloading and path optimization method for moving edge computing; [多无人机辅助的移动边缘计算任务卸载及路径优化方法]'
authors:
- Ju, Tao
- Li, Linjuan
- Zhang, Wenjing
- Zhang, Yufei
- Huo, Jiuyuan
venue: Dianzi Keji Daxue Xuebao/Journal of the University of Electronic Science and Technology of China
venue_type: journal
year: 2025
doi: 10.12178/1001-0548.2023276
url: https://www.scopus.com/pages/publications/85216864138?origin=resultslist
publisher: University of Electronic Science and Technology of China
pages: 72--83
keywords:
- mobile edge computing
- multi-agent deep reinforcement learning
- multi-UAV network
- path optimization
- task offloading
language: Chinese
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

# paper-1717 — MATOPO: A multi-UAV assisted task offloading and path optimization method for moving edge computing; [多无人机辅助的移动边缘计算任务卸载及路径优化方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Aiming at solving the task offloading and path planning challenge of multi-UAV assisted mobile edge computing, a multi-agent deep reinforcement learning method for task offloading and path optimization is proposed to reduce the total energy consumption of the system and improve computing performance. Firstly, the model of multi-UAV assisted mobile edge computing system is designed, and the UAV network is centrally managed by software-defined network technology. Then, on the basis of considering the load of the UAV and the fairness of the associated service of the user equipment, taking the total energy consumption of the system as the optimization goal, the multi-agent depth deterministic strategy gradient algorithm is designed to complete the task unloading and the path management optimization of the UAV, so as to achieve load balancing and reduce the total energy consumption of the whole system. Simulation results show that compared with other benchmark algorithms, the proposed method can reduce system energy consumption and computing delay to a certain extent, ensure the efficiency, stability and reliability of the whole system, and better meet the service requests of mobile edge users on the basis of making full use of the computing resources of UAV-assisted mobile edge computing systems. © 2025 University of Electronic Science and Technology of China. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1717.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
