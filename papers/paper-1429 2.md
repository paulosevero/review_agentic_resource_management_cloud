---
id: "paper-1429"
title: "Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently"
authors: ["Bhaurao, Phole Kamal", "Sawant, S.B.", "Umayal, A.R.", "Surekha, Swarna", "Beg, Mirza Samiulla", "Gupta, Umang"]
year: 2025
venue: "Proceedings of 2025 10th International Conference on Science Technology, Engineering and Mathematics, ICONSTEM 2025"
venue_type: "conference"
doi: "10.1109/ICONSTEM65670.2025.11374729"
url: "https://www.scopus.com/pages/publications/105034484607?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["GNN", "Horovod", "Kubernetes", "MAPPO", "RLlib", "TensorRT"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-1429 — Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently

## Metadata

- **Authors:** Bhaurao, Phole Kamal and Sawant, S.B. and Umayal, A.R. and Surekha, Swarna and Beg, Mirza Samiulla and Gupta, Umang
- **Year:** 2025
- **Venue:** Proceedings of 2025 10th International Conference on Science Technology, Engineering and Mathematics, ICONSTEM 2025
- **DOI:** 10.1109/ICONSTEM65670.2025.11374729
- **URL:** https://www.scopus.com/pages/publications/105034484607?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** GNN; Horovod; Kubernetes; MAPPO; RLlib; TensorRT

### Abstract

In this research, we present Proximal Policy Optimization (PPO) framework for Multi-Agent Systems (MAPPO) with Graph Neural Network (GNN) for online cloud resource allocation on heterogeneous infrastructure. We also use Ray RLlib distributed training environment for this (with every server represented as an intelligent agent acting in decentralized mode (Centralized Training with Decentralized Execution (CTDE) paradigm). Interagent dependencies are modelled using attention mechanisms and policy gradient calculation is done by the architecture using entropy regularized Stable-Baselines3. Custom operators provide real-time decisions from the scheduling point of view to Kubernetes orchestration with a maximum of 100 thousand task requests per hour. It utilizes time-series forecasting to model prediction workload and TensorRT optimization for below 10 ms inference latency. Deployed on Google Cloud Platform with multi-regional cluster structure, the framework reduces the resource wastage by 67 percent and improve the SLA compliance by 54 percent as compared to traditional heuristic scheduler. Horovod has the feature of making synchronization of weights scalable with 128 training nodes. © 2025 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently
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
