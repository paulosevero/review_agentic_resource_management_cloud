---
id: paper-0407
title: A Research on Collaborative UAVs Intelligent Decision Optimization for AoI-driven Federated Learning; [数据新鲜度驱动的协作式无人机联邦学习智能决策优化研究]
authors:
- Fan, Wen
- Wei, Qian
- Zhou, Zhi
- Yu, Shuai
- Chen, Xu
venue: Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
venue_type: journal
year: 2022
doi: 10.11999/JEIT211406
url: https://www.scopus.com/pages/publications/85139318744?origin=resultslist
publisher: Science Press
pages: 2994--3003
keywords:
- Age-of-Information (AoI)
- Deep reinforcement learning
- Federated learning
- Mobile Edge Computing (MEC)
- Unmanned Aerial Vehicle (UAV)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0407 — A Research on Collaborative UAVs Intelligent Decision Optimization for AoI-driven Federated Learning; [数据新鲜度驱动的协作式无人机联邦学习智能决策优化研究]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated learning is one of the key technologies of 6G, which can use cross-device data to train a usable and safe sharing model on the premise of protecting data privacy. However, most end devices have limited processing capabilities and can not support complex machine learning model training processes. In the framework of Mobile Edge Computing (MEC) in a heterogeneous network convergence environment, multiple Unmanned Aerial Vehicles (UAVs) are used as aerial edge servers to move flexibly within the target area in a collaborative manner, and collect fresh data in time for federated learning and local training to ensure real-time data learning. Multiple factors, such as data freshness, communication cost and model quality, are considered, and the flight trajectories of UAVs, the communication decisions with the user equipment, and the collaborative work between UAVs are comprehensively optimized. Moreover, a priority-based decomposable multi-agent deep reinforcement learning algorithm is used to solve the continuous online decision-making problem of multiple UAVs federated learning to achieve effective collaboration and control. By using multiple real data sets for simulation experiments, simulation results verify that the proposed algorithm can achieve superior performance under different data distributions and in rapidly changing complex dynamic environments. © 2022 Science Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0407.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
