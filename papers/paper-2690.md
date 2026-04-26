---
id: "paper-2690"
title: "Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]"
authors: ["Liu, Jiahui", "Zou, Yuan", "Wu, Jinming", "Du, Guodong", "Sun, Wenjing"]
year: 2026
venue: "Qiche Gongcheng/Automotive Engineering"
venue_type: "journal"
doi: "10.19562/j.chinasae.qcgc.2026.01.002"
url: "https://www.scopus.com/pages/publications/105030473251?origin=resultslist"
publisher: "SAE-China"
pages: "13--23"
keywords: ["deep reinforcement learning", "mobile edge computing", "resource allocation", "task offloading", "vehicle platoon"]
language: "Chinese"
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2690 — Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]

## Metadata

- **Authors:** Liu, Jiahui and Zou, Yuan and Wu, Jinming and Du, Guodong and Sun, Wenjing
- **Year:** 2026
- **Venue:** Qiche Gongcheng/Automotive Engineering
- **DOI:** 10.19562/j.chinasae.qcgc.2026.01.002
- **URL:** https://www.scopus.com/pages/publications/105030473251?origin=resultslist
- **Publisher:** SAE-China
- **Pages:** 13--23
- **Language:** Chinese
- **Keywords:** deep reinforcement learning; mobile edge computing; resource allocation; task offloading; vehicle platoon

### Abstract

With the rapid advancement of Intelligent Connected Vehicles （ICV） and vehicle to infrastructure （V2I） technologies， in vehicle application increasingly demand greater computational capacity and lower response latency. Although Mobile Edge Computing （MEC） can alleviate these requirements by offloading tasks to  edge servers， its limited coverage and constrained resources struggle to meet high-density workloads. Vehicle platoon provides an effective solution by leveraging stable inter vehicular communication and shared computational resources. In this paper， for a MEC-assisted edge computing system for ICV platoon， an optimization model to minimize the comprehensive task execution cost is constructed and a two stage Task Offloading and Resource Allocation  algorithm （TS-TORA） is proposed. Based on the system’s “offload-then-execute” process， the algorithm decomposes the task offloading and resource allocation into two levels of optimization problems and heterogeneous scheduling  strategies are designed according to the node type. In the task offloading stage， the platoon leader （PL） employs  Multi-Agent Proximal Policy Optimization （MAPPO） to generate a global offloading strategy, in the resource allocation stage， platoon vehicles （PVs） apply a priority-based greedy algorithm for local resource allocation， while MEC  servers leverage a Double Deep Q-Network （DDQN） for dynamic multi-task scheduling， thus balancing global  scheduling efficiency and node execution flexibility. The simulation results show that TS-TORA consistently outperforms benchmark algorithms across varying platoon sizes， task complexities， and latency constraints. Specifically，  task success rates reach 97.06%， 84.62%， and 78.31% for platoons of 4， 6， and 8 PVs， respectively. Moreover，  the average cost decreases with increasing platoon size， demonstrating the algorithm’s adaptability and scalability. © 2026, SAE-China. All rights reserved.

## 04 — Title Screening

**Title:** Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]
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
