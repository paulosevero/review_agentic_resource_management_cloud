---
id: paper-0762
title: Collaborative Scheduling Algorithm for Dependent Tasks based on Multi-Agent RL in VEC Environment
authors:
- Xu, Pengfei
- Ding, Xu
- Zheng, Xiang
- Zhang, Bixun
- Lyu, Qingzhou
- Liang, Tao
- Shi, Lei
venue: 'Journal of Physics: Conference Series'
venue_type: conference
year: 2023
doi: 10.1088/1742-6596/2670/1/012021
url: https://www.scopus.com/pages/publications/85181174352?origin=resultslist
publisher: Institute of Physics
pages: ''
keywords:
- Computational complexity
- Computing power
- Fertilizers
- Multi agent systems
- Multitasking
- Reinforcement learning
- Resource allocation
- Scheduling algorithms
- Vehicles
- Collaborative scheduling
- Computing environments
- Computing power
- Dependent tasks
- Edge computing
- Edge nodes
- Multi agent
- Multi-agent reinforcement learning
- Reinforcement learning approach
- Task-based
- Optimization
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0762 — Collaborative Scheduling Algorithm for Dependent Tasks based on Multi-Agent RL in VEC Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the problem of limited computing power of vehicles, Vehicle Edge Computing (VEC) allows vehicles to schedule tasks to edge nodes with sufficient resources. In this paper, we propose a multi-agent reinforcement learning (MARL) approach to solve the multi-task scheduling problem in a dynamic VEC environment. First, we model the cooperative scheduling problem of dependent tasks in the VEC environment, considering the task priority and edge node load balancing in the task scheduling process. We define the optimization objective as minimizing the task processing delay and find it is an NP-hard problem. Then, we design a distributed algorithm SCMA based on MARL. The algorithm enables vehicles to find the optimal scheduling strategy by cooperating and sharing resources with each other. Finally, we use SUMO to simulate the road network topology and generate vehicle traffic trajectories. We construct heterogeneous vehicular applications for simulation experiments using the DAG generator. Compared with existing algorithms, the simulation results validate the superiority of the SCMA algorithm.  © Published under licence by IOP Publishing Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0762.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
