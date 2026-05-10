---
id: "paper-431"
title: "Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach"
authors: ["Huang, Xinyu", "He, Lijun", "Chen, Xing", "Wang, Liejun", "Li, Fan"]
year: 2022
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2021.3116108"
url: "https://www.scopus.com/pages/publications/85116853985?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "8852--8868"
keywords: ["Deep reinforcement learning", "multiagent deep deterministic policy gradient (MADDPG)", "resource allocation", "task offloading", "vehicle speed", "vehicle-to-vehicle (V2V) communication", "vehicular edge computing (VEC)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-431 — Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Huang, Xinyu and He, Lijun and Chen, Xing and Wang, Liejun and Li, Fan
- **Year:** 2022
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2021.3116108
- **URL:** https://www.scopus.com/pages/publications/85116853985?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 8852--8868
- **Language:** English
- **Keywords:** Deep reinforcement learning; multiagent deep deterministic policy gradient (MADDPG); resource allocation; task offloading; vehicle speed; vehicle-to-vehicle (V2V) communication; vehicular edge computing (VEC)

### Abstract

For in-vehicle application, task type and vehicle state information, i.e., vehicle speed, bear a significant impact on the task delay requirement. However, the joint impact of task type and vehicle speed on the task delay constraint has not been studied, and this lack of study may cause a mismatch between the requirement of the task delay and allocated computation and wireless resources. In this article, we propose a joint task type and vehicle speed-aware task offloading and resource allocation strategy to decrease the vehicle's energy cost for executing tasks and increase the revenue of the vehicle for processing tasks within the delay constraint. First, we establish the joint task type and vehicle speed-aware delay constraint model. Then, the delay, energy cost, and revenue for task execution in the vehicular edge computing (VEC) server, local terminal, and terminals of other vehicles are calculated. Based on the energy cost and revenue from task execution, the utility function of the vehicle is acquired. Next, we formulate a joint optimization of task offloading and resource allocation to maximize the utility level of the vehicles subject to the constraints of task delay, computation resources, and wireless resources. To obtain a near-optimal solution of the formulated problem, a joint offloading and resource allocation based on the multiagent deep deterministic policy gradient (JORA-MADDPG) algorithm is proposed to maximize the utility level of vehicles. Simulation results show that our algorithm can achieve superior performance in task completion delay, vehicles' energy cost, and processing revenue.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Revenue and Energy Efficiency-Driven Delay-Constrained Computing Task Offloading and Resource Allocation in a Vehicular Edge Computing Network: A Deep Reinforcement Learning Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
