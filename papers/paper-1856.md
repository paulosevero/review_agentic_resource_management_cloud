---
id: paper-1856
title: Method of Joint Optimization for Multi-UAV Energy Transfer and Edge Computing Based on Deep Reinforcement Learning
authors:
- Lin, Shaofu
- Chen, Yingying
- Li, Shuopeng
venue: Jisuanji Gongcheng/Computer Engineering
venue_type: journal
year: 2025
doi: 10.19678/j.issn.1000-3428.0068675
url: https://www.scopus.com/pages/publications/105002061745?origin=resultslist
publisher: Editorial Office of Computer Engineering
pages: 144--154
keywords:
- Deep Reinforcement
- dynamic resource allocation
- Learning(DRL)
- Mobile Edge Computing(MEC)
- multiple Unmanned Aerial Vehicle (UAV)
- wireless power transfer
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1856 — Method of Joint Optimization for Multi-UAV Energy Transfer and Edge Computing Based on Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to limited on-board resources and endurance, UAVs have limited residence time in the air and cannot perform computation-intensive tasks continuously. To satisfy the continuous task execution requirements of UAVs in continuous operation scenarios, a multi-UAV edge computing system based on wireless energy transfer is designed. This system uses a group of large UAVs as an Air-Edge Energy Server(AEES) to provide energy and computing resources, ensuring the efficient execution of the missions of the UAVs. A joint optimization model is established for multi-UAV energy and computing by combining the 3D position, power, and task volume information of the UAVs to maximize the system throughput and energy transfer efficiency, while minimizing the energy consumption of the AEES. A Multi-Agent Deep Q-Network(MADQN) algorithm is used to determine the service location point and energy emission power for the AEES to achieve the optimization goals. Simulation results show that the proposed MADQN algorithm effectively optimizes the service location and energy consumption of the AEES and that it can efficiently provide computing, energy, and other resources for the UAVs. Compared with heuristic learning algorithms and other baseline methods, such as the greedy algorithm, the proposed MADQN significantly improves the energy transfer efficiency and system throughput and successfully balances multiple optimization objectives, including energy transfer, energy consumption, and throughput. © 2025, Editorial Office of Computer Engineering. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1856.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
