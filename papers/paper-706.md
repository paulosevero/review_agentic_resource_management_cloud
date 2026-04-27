---
id: "paper-706"
title: "Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning"
authors: ["Rossi, Fabiana", "Cardellini, Valeria", "Lo Presti, Francesco", "Nardelli, Matteo"]
year: 2023
venue: "IEEE Transactions on Cloud Computing"
venue_type: "journal"
doi: "10.1109/TCC.2022.3163357"
url: "https://www.scopus.com/pages/publications/85127477181?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1807--1821"
keywords: ["deep Q-learning", "Elasticity", "microservice architecture", "reinforcement learning", "self-adaptation"]
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
    final_score: 0.1666
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-706 — Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning

## Metadata

- **Authors:** Rossi, Fabiana and Cardellini, Valeria and Lo Presti, Francesco and Nardelli, Matteo
- **Year:** 2023
- **Venue:** IEEE Transactions on Cloud Computing
- **DOI:** 10.1109/TCC.2022.3163357
- **URL:** https://www.scopus.com/pages/publications/85127477181?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1807--1821
- **Language:** English
- **Keywords:** deep Q-learning; Elasticity; microservice architecture; reinforcement learning; self-adaptation

### Abstract

—Cloud-native applications increasingly adopt the microservices architecture, which favors elasticity to satisfy the application performance requirements in face of variable workloads. To simplify the elasticity management, the trend is to create an auto-scaler instance per microservice, which controls its horizontal scalability by using the classic threshold-based policy. Although easy to implement, setting manually the scaling thresholds, which are usually statically-defined on a single metric, may lead to poor scaling decisions when applications are heterogeneous in terms of resource consumption. In this article, we study dynamic multi-metric threshold-based scaling policies, that exploit Reinforcement Learning (RL) to autonomously update the scaling thresholds, one per controlled resource (CPU and memory). The proposed RL approaches (i.e., QL, MB, and DQL Threshold) use different degrees of knowledge about the system dynamics. To model the thresholds’ adaptation actions, we consider two RL-based architectures. In the single-agent architecture, one agent drives the updates of both scaling thresholds. To speed-up the learning, the multi-agent architecture adopts a distinct agent per threshold. Simulation- and prototype-based results show the benefits of the proposed solutions when compared to the state-of-the-art policies and highlight the advantages of multi-agent MB Threshold and DQL Threshold approaches, in terms of deployment objectives and execution times. © 2023 Institute of Electrical and Electronics Engineers Inc.. All rights reserved.

## 04 — Title Screening

**Title:** Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning

### Machine Screening

- **Final Score:** 0.1666 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
