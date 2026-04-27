---
id: "paper-763"
title: "Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning"
authors: ["Xu, Chi", "Tang, Zixuan", "Yu, Haibin", "Zeng, Peng", "Kong, Linghe"]
year: 2023
venue: "IEEE Journal on Selected Areas in Communications"
venue_type: "journal"
doi: "10.1109/JSAC.2023.3310066"
url: "https://www.scopus.com/pages/publications/85169672081?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3056--3069"
keywords: ["collaborative scheduling", "Digital twin", "edge computing", "multi-Agent deep reinforcement learning", "task offloading"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-763 — Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning

## Metadata

- **Authors:** Xu, Chi and Tang, Zixuan and Yu, Haibin and Zeng, Peng and Kong, Linghe
- **Year:** 2023
- **Venue:** IEEE Journal on Selected Areas in Communications
- **DOI:** 10.1109/JSAC.2023.3310066
- **URL:** https://www.scopus.com/pages/publications/85169672081?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3056--3069
- **Language:** English
- **Keywords:** collaborative scheduling; Digital twin; edge computing; multi-Agent deep reinforcement learning; task offloading

### Abstract

With the interdisciplinary advances of mobile communication and edge computing, massive heterogeneous tasks are accessing wireless networks and competing for the edge-end computing and communication resources. Digital twin (DT), which establishes the digital models of physical objects for simulation, analysis and optimization, provides a promising method for network scheduling and management. This paper proposes a DT-driven edge-end collaborative scheduling algorithm for heterogeneous tasks and heterogeneous computing/communication resources. Specifically, multiple end devices (EDs) cooperate with each other to accomplish a complex job, where each ED can offload individual task to multiple edge servers (ESs) for parallel computing. By fully considering deadline requirements of heterogeneous tasks, maximum computing capabilities of ESs and EDs, computing resource estimation deviations of DT, maximum transmit powers of EDs and tolerable peak interference powers to coexisting EDs, we formulate a job completion time minimization problem to jointly optimize the edge-end task division, transmit power control, computing resource type matching and allocation. To solve this non-convex problem, we first reformulate it by multi-Agent Markov decision process, where a compound reward leveraging latency reward and deadline reward according to the task criticality is designed. Then, we propose a multi-Agent deep reinforcement learning-based scheduling algorithm, where Actor-Critic framework with estimation and target networks is designed for policy and value iterations. Meanwhile, a step-by-step-greedy algorithm is proposed to balance exploration and exploitation, avoiding local optimal trap. Through offline centralized training by DT and online distributed execution by EDs, we realize edge-end collaborative computing for heterogeneous tasks. Experimental results demonstrate that, comparing with typical benchmark algorithms, the proposed algorithm converges with the highest reward and achieves the smallest job completion time, where the deadlines of heterogeneous tasks can be well satisfied respectively.  © 1983-2012 IEEE.

## 04 — Title Screening

**Title:** Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
