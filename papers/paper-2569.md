---
id: "paper-2569"
title: "Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems"
authors: ["Fang, Juan", "Wang, Xinghao", "Liu, Yaqi", "Tang, Heng", "Li, Xiaolin"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3674519"
url: "https://www.scopus.com/pages/publications/105033241203?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Collaborative Inference", "Edge Computing", "Large-Scale Models", "Multi-Agent", "Proximal Policy Optimization"]
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

# paper-2569 — Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems

## Metadata

- **Authors:** Fang, Juan and Wang, Xinghao and Liu, Yaqi and Tang, Heng and Li, Xiaolin
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3674519
- **URL:** https://www.scopus.com/pages/publications/105033241203?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Collaborative Inference; Edge Computing; Large-Scale Models; Multi-Agent; Proximal Policy Optimization

### Abstract

Deploying large deep neural networks (DNNs) on resource-constrained Internet of Things (IoT) devices is often limited by high inference latency and energy consumption. This paper studies collaborative inference between user devices and edge servers, where a DNN is partitioned and executed across both sides under shared wireless resources. We jointly optimize the partition point across layers, uplink channel allocation, and transmission power control, and formulate the coupled decisions as a markov decision process (MDP). Under centralized training with decentralized execution (CTDE), we develop a multi-agent proximal policy optimization (MAPPO) framework with a multi-head critic and profiling-aware state design to stabilize learning under large hybrid action spaces. To validate practicality, we implement a containerized experimental platform that emulates resource-limited IoT devices and GPU enabled edge servers, enabling repeatable measurements of end-to-end latency and energy. Experiments with representative DNNs show that the proposed method consistently improves the latency–energy trade-off over baseline algorithms, achieving lower end-to-end latency and comparable or lower energy consumption across diverse model structures and computation patterns. © 2014 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
