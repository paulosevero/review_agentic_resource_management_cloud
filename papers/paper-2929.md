---
id: "paper-2929"
title: "HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network"
authors: ["Zhao, Haitao", "Zhang, Taiming", "Tang, Guijin", "Liu, Miao", "Chen, Shuaifei", "Wang, Chengxiang"]
year: 2026
venue: "IEEE Transactions on Communications"
venue_type: "journal"
doi: "10.1109/TCOMM.2026.3681581"
url: "https://www.scopus.com/pages/publications/105035405351?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AoI", "data offloading", "digital twin channel", "heterogeneous GNN", "layered UAVs", "MARL", "trajectory control"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2929 — HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network

## Metadata

- **Authors:** Zhao, Haitao and Zhang, Taiming and Tang, Guijin and Liu, Miao and Chen, Shuaifei and Wang, Chengxiang
- **Year:** 2026
- **Venue:** IEEE Transactions on Communications
- **DOI:** 10.1109/TCOMM.2026.3681581
- **URL:** https://www.scopus.com/pages/publications/105035405351?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AoI; data offloading; digital twin channel; heterogeneous GNN; layered UAVs; MARL; trajectory control

### Abstract

As a key paradigm in sixth-generation (6G) systems for enabling physical–virtual mapping and intelligent network management, Digital Twin (DT) networks demand high-precision, low-latency modeling and continuous updates of wireless environments. However, in dynamic urban scenarios, channel conditions are highly non-stationary, and traditional sensing schemes suffer from limitations in coverage, information timeliness, and scheduling efficiency. To address these challenges, this paper proposes an Integrated Communication-Computing-Intelligence-Controlling (ICCIC) network based on layered unmanned aerial vehicles (UAVs). The system comprises mobile edge servers (ESs) with trajectory control and scheduling capabilities, and statically deployed working UAVs responsible for wireless channel measurements. The collected data is offloaded to ESs for edge computing and local model construction, which supports subsequent DT channel modeling. A multi-objective optimization problem is formulated to jointly schedule UAV trajectories and data offloading, with Age of Information (AoI) and service delay as performance metrics. The optimization is subject to constraints including maximum task execution time and service fairness. To capture multi-type interactions among UAVs during sensing and coordination, we build a multi-relational heterogeneous graph and encode it with a graph neural network (GNN) to obtain structured system states. On this basis, we adopt a QMIX-based multi-agent reinforcement learning (MARL) framework under centralized training and decentralized execution (CTDE) is developed to learn cooperative scheduling policies. Simulation results demonstrate that the proposed method achieves superior performance in sensing timeliness, scheduling responsiveness, and policy convergence, providing robust support for efficient and reliable DT channel modeling. © 1972-2012 IEEE.

## 04 — Title Screening

**Title:** HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
