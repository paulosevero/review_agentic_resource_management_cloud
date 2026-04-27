---
id: "paper-2891"
title: "Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV"
authors: ["Yin, Peng", "Liang, Wentao", "Wen, Jinbo", "Kang, Jiawen", "Chen, Junlong", "Niyato, Dusit"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3672525"
url: "https://www.scopus.com/pages/publications/105032780889?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["6G", "DM-MAPPO", "IoV", "LSTM-based Transformer", "multi-objective VT migration"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-2891 — Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV

## Metadata

- **Authors:** Yin, Peng and Liang, Wentao and Wen, Jinbo and Kang, Jiawen and Chen, Junlong and Niyato, Dusit
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3672525
- **URL:** https://www.scopus.com/pages/publications/105032780889?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 6G; DM-MAPPO; IoV; LSTM-based Transformer; multi-objective VT migration

### Abstract

Sixth Generation (6G)-enabled Internet of Vehicles (IoV) facilitates efficient data synchronization through ultra-fast bandwidth and high-density connectivity, enabling the emergence of Vehicle Twins (VTs). As highly accurate replicas of vehicles, VTs can support intelligent vehicular applications for occupants in 6G-enabled IoV. Thanks to the full coverage capability of 6G, resource-constrained vehicles can offload VTs to edge servers, such as roadside units, unmanned aerial vehicles, and satellites, utilizing their computing and storage resources for VT construction and updates. However, communication between vehicles and edge servers with limited coverage is prone to interruptions due to the dynamic mobility of vehicles. Consequently, VTs must be migrated among edge servers to maintain uninterrupted and high-quality services for users. In this paper, we introduce a VT migration framework in 6G-enabled IoV. Specifically, we first propose a Long Short-Term Memory (LSTM)-based Transformer model to accurately predict long-term workloads of edge servers for migration decision-making. Then, we propose a Dynamic Mask Multi-Agent Proximal Policy Optimization (DM-MAPPO) algorithm to identify optimal migration routes in the highly complex environment of 6G-enabled IoV. Finally, we develop a practical platform to validate the effectiveness of the proposed scheme using real datasets. Simulation results demonstrate that the proposed DM-MAPPO algorithm significantly reduces migration latency by 20.82% and packet loss by 75.07% compared with traditional deep reinforcement learning algorithms. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
