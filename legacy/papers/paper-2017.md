---
id: "paper-2017"
title: "Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts"
authors: ["Park, Eun Chan", "Baek, Kyeong Deok", "Ko, In-Young"]
year: 2025
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2025.3617074"
url: "https://www.scopus.com/pages/publications/105018316050?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3865--3877"
keywords: ["autonomic services", "fog services", "Microservice autoscaling", "multi-agent reinforcement learning"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2017 — Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts

## Metadata

- **Authors:** Park, Eun Chan and Baek, Kyeong Deok and Ko, In-Young
- **Year:** 2025
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2025.3617074
- **URL:** https://www.scopus.com/pages/publications/105018316050?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3865--3877
- **Language:** English
- **Keywords:** autonomic services; fog services; Microservice autoscaling; multi-agent reinforcement learning

### Abstract

The emergence of fog computing has shown promising results for reducing network latency and congestion in the cloud. In this environment, effective autoscaling to handle spatio-temporal load bursts in geographically distributed and resource-constrained fog nodes has become a timely problem. A typical strategy for autoscaling is based on centralized monitoring of the fog nodes and the deployed service instances. However, centralized collection and analysis of the metrics for autoscaling can become infeasible with the increasing number of fog nodes. Moreover, the dynamic and fluctuating characteristics of the fog nodes make effective autoscaling challenging in fog computing environments. In this work, we propose HiDRA, a Hierarchical Decentralized Autoscaler that scales and places microservice instances based on multi-agent reinforcement learning. In HiDRA, agents are divided into scaling and placement agents that collaborate with each other to effectively handle spatio-temporal load bursts in fog computing. These Deep Q-Network-based autoscaling agents are trained solely based on their regional observations at runtime, eliminating the need for a centralized collection of metrics. We evaluated HiDRA in multiple simulated fog environments created using a real-world dataset. The environments were divided into three levels of sparsity, each consisting of 20, 15, and 10 initial instances and unstable nodes. The result shows that comparatively by ratio against the baseline, HiDRA increased the average request success rate by 10.7%, 16.4%, and 36.7% and reduced the number of created instances by 12.3%, 15.9%, and 16.8% in environments with 20, 15, and 10 initial instances and unstable nodes, respectively.  © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts
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
