---
id: "paper-1938"
title: "A scalable machine learning strategy for resource allocation in database"
authors: ["Manhary, Fady Nashat", "Mohamed, Marghny H.", "Farouk, Mamdouh"]
year: 2025
venue: "Scientific Reports"
venue_type: "journal"
doi: "10.1038/s41598-025-14962-5"
url: "https://www.scopus.com/pages/publications/105013798868?origin=resultslist"
publisher: "Nature Research"
pages: ""
keywords: ["Cloud computing", "Energy efficiency", "Multi-Agent Reinforcement Learning", "Resource allocation", "Scalability", "Workload forecasting"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1938 — A scalable machine learning strategy for resource allocation in database

## Metadata

- **Authors:** Manhary, Fady Nashat and Mohamed, Marghny H. and Farouk, Mamdouh
- **Year:** 2025
- **Venue:** Scientific Reports
- **DOI:** 10.1038/s41598-025-14962-5
- **URL:** https://www.scopus.com/pages/publications/105013798868?origin=resultslist
- **Publisher:** Nature Research
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud computing; Energy efficiency; Multi-Agent Reinforcement Learning; Resource allocation; Scalability; Workload forecasting

### Abstract

Modern cloud computing systems require intelligent resource allocation strategies that balance quality-of-service (QoS), operational costs, and energy sustainability. Existing deep Q-learning (DQN) methods suffer from sample inefficiency, centralization bottlenecks, and reactive decision-making during workload spikes. Transformer-based forecasting models such as Temporal Fusion Transformer (TFT) offer improved accuracy but introduce computational overhead, limiting real-time deployment. We propose LSTM-MARL-Ape-X, a novel framework integrating bidirectional Long Short-Term Memory (BiLSTM) for workload forecasting with Multi-Agent Reinforcement Learning (MARL) in a distributed Ape-X architecture. This approach enables proactive, decentralized, and scalable resource management through three innovations: high-accuracy forecasting using BiLSTM with feature-wise attention, variance-regularized credit assignment for stable multi-agent coordination, and faster convergence via adaptive prioritized replay. Experimental validation on real-world traces demonstrates 94.6% SLA compliance, 22% reduction in energy consumption, and linear scalability to over 5,000 nodes with sub-100 ms decision latency. The framework converges 3.2 faster than uniform sampling baselines and outperforms transformer-based models in both accuracy and inference speed. Unlike decoupled prediction-action frameworks, our method provides end-to-end optimization, enabling robust and sustainable cloud orchestration at scale. © The Author(s) 2025.

## 04 — Title Screening

**Title:** A scalable machine learning strategy for resource allocation in database

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A scalable machine learning strategy for resource allocation in database
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A scalable machine learning strategy for resource allocation in database
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
