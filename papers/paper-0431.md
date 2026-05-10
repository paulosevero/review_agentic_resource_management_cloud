---
id: paper-0431
title: 'Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach'
authors:
- Huang, Xinyu
- He, Lijun
- Chen, Xing
- Wang, Liejun
- Li, Fan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2021.3116108
url: https://www.scopus.com/pages/publications/85116853985?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8852--8868
keywords:
- Deep reinforcement learning
- multiagent deep deterministic policy gradient (MADDPG)
- resource allocation
- task offloading
- vehicle speed
- vehicle-to-vehicle (V2V) communication
- vehicular edge computing (VEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0431 — Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> For in-vehicle application, task type and vehicle state information, i.e., vehicle speed, bear a significant impact on the task delay requirement. However, the joint impact of task type and vehicle speed on the task delay constraint has not been studied, and this lack of study may cause a mismatch between the requirement of the task delay and allocated computation and wireless resources. In this article, we propose a joint task type and vehicle speed-aware task offloading and resource allocation strategy to decrease the vehicle's energy cost for executing tasks and increase the revenue of the vehicle for processing tasks within the delay constraint. First, we establish the joint task type and vehicle speed-aware delay constraint model. Then, the delay, energy cost, and revenue for task execution in the vehicular edge computing (VEC) server, local terminal, and terminals of other vehicles are calculated. Based on the energy cost and revenue from task execution, the utility function of the vehicle is acquired. Next, we formulate a joint optimization of task offloading and resource allocation to maximize the utility level of the vehicles subject to the constraints of task delay, computation resources, and wireless resources. To obtain a near-optimal solution of the formulated problem, a joint offloading and resource allocation based on the multiagent deep deterministic policy gradient (JORA-MADDPG) algorithm is proposed to maximize the utility level of vehicles. Simulation results show that our algorithm can achieve superior performance in task completion delay, vehicles' energy cost, and processing revenue.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0431.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
