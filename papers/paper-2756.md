---
id: "paper-2756"
title: "Resource Allocation in Cell-Free MEC Networks: A Hierarchical MADRL-Based Algorithm"
authors: ["Ren, Mengmeng", "Yang, Long", "Zhou, Yuchen", "Lv, Lu", "Chen, Jian", "Xiao, Pei", "Cavdar, Cicek", "Tafazolli, Rahim"]
year: 2026
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2025.3645433"
url: "https://www.scopus.com/pages/publications/105025452828?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4593--4609"
keywords: ["deep reinforcement learning", "Multi-access edge computing", "resource allocation", "user association"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2756 — Resource Allocation in Cell-Free MEC Networks: A Hierarchical MADRL-Based Algorithm

## Metadata

- **Authors:** Ren, Mengmeng and Yang, Long and Zhou, Yuchen and Lv, Lu and Chen, Jian and Xiao, Pei and Cavdar, Cicek and Tafazolli, Rahim
- **Year:** 2026
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2025.3645433
- **URL:** https://www.scopus.com/pages/publications/105025452828?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4593--4609
- **Language:** English
- **Keywords:** deep reinforcement learning; Multi-access edge computing; resource allocation; user association

### Abstract

This paper investigates a cell-free massive multiple-input multiple-output enabled multi-access edge computing (termed CF-MEC) system, where multiple users are served by multiple central processing units (CPUs) and their connected access points (APs), both of which are equipped with computation resources. For this system, a dynamic user-centric task offloading scheme is designed to provide seamless and efficient computation services for users. Based on this scheme, the joint optimization of user-centric AP clustering, edge server selection, communication and computation resources is formulated as a long-term problem to minimize the average energy consumption. The formulated problem is complicated non-convex due to the highly coupled time-varying discrete and continuous variables, resulting in high complexity and non-real-time to obtain the optimal solution. To tackle this challenging problem, we propose a multi-layer hierarchical multi-agent deep reinforcement learning (ML-HMADRL) based resource allocation algorithm. Specifically, the proposed algorithm incorporates a hierarchical structure with high, middle, and low-level agents that iteratively train the actor-critic networks to obtain discrete and continuous variables of the formulated problem. To further enhance the training effectiveness by leveraging the CF-MEC system, we design distinct actor-critic networks for the agents at different levels to facilitate centralized training and distributed execution. Simulation results validate the training stability of the proposed algorithm at each level, and demonstrate the superiority of the proposed algorithm over benchmark schemes in terms of the average energy consumption, providing a stable distributed framework for practical implementation in dynamic environments. © 2015 IEEE.

## 04 — Title Screening

**Title:** Resource Allocation in Cell-Free MEC Networks: A Hierarchical MADRL-Based Algorithm

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Resource Allocation in Cell-Free MEC Networks: A Hierarchical MADRL-Based Algorithm
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Resource Allocation in Cell-Free MEC Networks: A Hierarchical MADRL-Based Algorithm
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
