---
id: "paper-1107"
title: "Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach"
authors: ["Ning, Xiangrui", "Zeng, Ming", "Hua, Meng", "Fei, Zesong"]
year: 2024
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2024.3419554"
url: "https://www.scopus.com/pages/publications/85197093235?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "17496--17509"
keywords: ["multi-agent reinforcement learning", "reconfigurable intelligent surfaces", "service migration", "Vehicular edge computing"]
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
    human_justification: "RL"

---

# paper-1107 — Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach

## Metadata

- **Authors:** Ning, Xiangrui and Zeng, Ming and Hua, Meng and Fei, Zesong
- **Year:** 2024
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2024.3419554
- **URL:** https://www.scopus.com/pages/publications/85197093235?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 17496--17509
- **Language:** English
- **Keywords:** multi-agent reinforcement learning; reconfigurable intelligent surfaces; service migration; Vehicular edge computing

### Abstract

Reconfigurable intelligent surface (RIS) is envisioned as a new technology to improve the quality-of-service in vehicular edge computing (VEC) networks due to its ability to change the wireless radio propagation environment. In this paper, we study multi-RIS-assisted VEC networks, where vehicle user equipments (VUEs) can offload tasks to nearby base stations (BSs) which offer efficient computation edge services (ESs). Meanwhile, the individual virtual machine (VM), which is defined as a software clone of the VUE's service environment containing the profile and application to run the VUE's tasks, need to be migrated to the same ES for offloaded task completion. Accordingly, we formulate a throughput maximization problem for multi-RIS-assisted VEC networks via jointly optimizing the selected ESs, the deployment locations of RISs, and reflection matrices of RISs, subject to the maximum tolerable delay. To solve the non-convex mixed-integer nonlinear optimization problem, we propose an efficient algorithm based on multi-agent proximal policy optimization (MAPPO) with the centralized training and decentralized execution (CTDE) framework, where two types of heterogeneous agents are considered. In particular, several tricks such as reward normalization, orthogonal initialization, and learning rate decay are adopted to accelerate the convergence of the proposed algorithm. Numerical simulation results show that the throughput obtained by the proposed MAPPO-based scheme outperforms that obtained by the scheme without multi-RIS 26.41% and that obtained by the scheme without service migration 23.65%, respectively. Moreover, compared to other conventional multi-agent reinforcement learning (MARL) algorithms, the proposed algorithm converges faster.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
