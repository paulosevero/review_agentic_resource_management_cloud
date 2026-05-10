---
id: "paper-305"
title: "Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing"
authors: ["Kim, Yohan", "Lim, Hyuk"]
year: 2021
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2021.3072435"
url: "https://www.scopus.com/pages/publications/85104255617?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "56178--56190"
keywords: ["5G", "multi-access edge computing", "multi-agent reinforcement learning", "network resource management", "network slicing"]
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

# paper-305 — Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing

## Metadata

- **Authors:** Kim, Yohan and Lim, Hyuk
- **Year:** 2021
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2021.3072435
- **URL:** https://www.scopus.com/pages/publications/85104255617?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 56178--56190
- **Language:** English
- **Keywords:** 5G; multi-access edge computing; multi-agent reinforcement learning; network resource management; network slicing

### Abstract

To meet the explosive growth of mobile traffic, the 5G network is designed to be flexible and support multi-access edge computing (MEC), thereby improving the end-to-end quality of service (QoS). In particular, 5G network slicing, which allows a physical infrastructure to split into multiple logical networks, keeps the balance of network resource allocation among different service types with on-demand resource requests. However, achieving effective resource allocation across the end-to-end network is difficult due to the dynamic characteristics of slicing requests such as uncertain real-time resource demand and heterogeneous requirements. In this paper, we develop a reinforcement learning (RL)-based dynamic resource allocation framework for end-to-end network slicing with heterogeneous requirements in multi-layer MEC environments. We first design a hierarchical MEC architecture and formulate a resource allocation problem for the end-to-end network slicing as an optimization problem using the Markov decision process (MDP). Using proximal policy optimization (PPO), we develop independently-collaborative and jointly-collaborative dynamic resource allocation algorithms to maximize resource efficiency while satisfying the QoS of slices. Experimental results show that the proposed algorithms can recognize the characteristics of slice requests and coming resource demands and efficiently allocate resources with a high QoS satisfaction rate.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing
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
