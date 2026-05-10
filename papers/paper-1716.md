---
id: paper-1716
title: A Multi-layer Distributed Edge Computing Task Dynamic Offloading Strategy in Internet of Vehicles; [多 层 分 布 式 车 联 网 边 缘 计 算 任 务 动 态 卸 载 策 略]
authors:
- Ju, Tao
- Zhang, Yufei
- Ma, Yaling
- Huo, Jiuyuan
venue: Hunan Daxue Xuebao/Journal of Hunan University Natural Sciences
venue_type: journal
year: 2025
doi: 10.16339/j.cnki.hdxbzkb.2025268
url: https://www.scopus.com/pages/publications/105004038511?origin=resultslist
publisher: Hunan University
pages: 79--90
keywords:
- deep reinforcement learning
- internet of vehicles（IoV)
- mobile edge computing
- software defined network
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

# paper-1716 — A Multi-layer Distributed Edge Computing Task Dynamic Offloading Strategy in Internet of Vehicles; [多 层 分 布 式 车 联 网 边 缘 计 算 任 务 动 态 卸 载 策 略]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of low offloading success rates and inefficient data transmission in the internet of vehicles（IoV），this paper proposes a multi-layer distributed dynamic offloading strategy for edge computing tasks in IoV based on multi-agent deep reinforcement learning. Firstly，a multi-layer distributed internet of vehicles edge computing system model is designed by integrating software defined network and mobile edge computing. The system model can realize collaborative scheduling optimization at different levels，which can better meet the needs of dynamic allocation of mobile vehicle resources and real-time processing of tasks. Then，considering the success rate of offloading and data transmission rate of vehicle computing tasks，a multi-agent deep reinforcement learning algorithm framework is proposed. The algorithm framework uses collaborative learning of multi-agent systems to enable the vehicle edge system to independently select the optimal task offloading decision. At the same time，the optimization of the action space search and the priority experience replay mechanism were introduced to further improve the effective search of the action space and the stability and accuracy of the task offloading decision. Finally，based on the above algorithm framework and optimization mechanism，a multi-layer distributed vehicle task offloading decision optimization algorithm is proposed. The algorithm can ensure that the vehicle can complete the computing task offloading with the minimum task transmission time and effective offloading success rate according to the current network status and task size. Simulation results show that，compared with the existing offloading methods，the proposed method improves the success rate of computing task offloading by 5%~ 20% and the efficiency of data transmission by 17.8% on average. © 2025 Hunan University. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1716.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
