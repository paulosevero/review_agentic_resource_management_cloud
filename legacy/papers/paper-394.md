---
id: "paper-394"
title: "Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks"
authors: ["Cheng, Zhipeng", "Liwang, Minghui", "Chen, Ning", "Huang, Lianfen", "Du, Xiaojiang", "Guizani, Mohsen"]
year: 2022
venue: "Computer Communications"
venue_type: "journal"
doi: "10.1016/j.comcom.2022.06.017"
url: "https://www.scopus.com/pages/publications/85132712026?origin=resultslist"
publisher: "Elsevier B.V."
pages: "234--244"
keywords: ["Laser", "MASAC", "Multi-agent Markov game", "SWIPT", "Task offloading", "UAV"]
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

# paper-394 — Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks

## Metadata

- **Authors:** Cheng, Zhipeng and Liwang, Minghui and Chen, Ning and Huang, Lianfen and Du, Xiaojiang and Guizani, Mohsen
- **Year:** 2022
- **Venue:** Computer Communications
- **DOI:** 10.1016/j.comcom.2022.06.017
- **URL:** https://www.scopus.com/pages/publications/85132712026?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 234--244
- **Language:** English
- **Keywords:** Laser; MASAC; Multi-agent Markov game; SWIPT; Task offloading; UAV

### Abstract

Edge networks are expected to play an important role in 6G where machine learning-based methods are widely applied, which promote the concept of Edge Intelligence. Meanwhile, Unmanned Aerial Vehicle (UAV)-enabled aerial network is significant in 6G networks to achieve seamless coverage and super-connectivity. To this end, a joint task and energy offloading problem is studied under a UAV-aided and energy-constrained intelligent edge network, consisting of a high altitude platform (HAP), multiple UAVs, and on-ground fog computing nodes (FCNs). To guarantee the energy supply of UAVs and FCNs, both simultaneous wireless information and power transfer (SWIPT), as well as laser charging techniques are considered. Specifically, we investigate a scenario where each UAV needs to execute a computation-intensive task during each time slot and can be powered by the laser beam transmitted from the HAP. Due to the limited computation resources, each UAV can offload part of the task and energy to the FCNs for collaborative computing, to reduce local energy consumption and the overall task execution delay by adopting SWIPT. Considering the dynamics of the network, e.g., the time-varying locations of UAVs and available computation resources of FCNs, the problem is formulated as a cooperative multi-agent Markov game for UAVs, which aims to maximize the total system utility, by optimizing the task partitioning and power allocation strategies of each UAV, regarding task size, average delay and energy consumption of task execution. To tackle this problem, we propose a multi-agent soft actor–critic (MASAC)-based approach to resolve the problem. Numerical simulation results prove the superiority of our proposed approach as compared with benchmark methods. © 2022 Elsevier B.V.

## 04 — Title Screening

**Title:** Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks
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
