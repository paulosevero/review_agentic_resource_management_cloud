---
id: "paper-2059"
title: "Joint Request Batching and Worker Assignment in AI-RAN Edge Inference Systems"
authors: ["Qiu, Ningyuan", "Gan, Shuying", "Wang, Xijun", "Feng, Chenyuan", "Chen, Xiang", "Han, Shuangfeng", "Wang, Xiaoyun"]
year: 2025
venue: "2025 International Conference on Future Communications and Networks, FCN 2025 - Proceedings"
venue_type: "conference"
doi: "10.1109/FCN66513.2025.11296658"
url: "https://www.scopus.com/pages/publications/105031773523?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["deep reinforcement learning", "edge computing", "Large language model"]
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

# paper-2059 — Joint Request Batching and Worker Assignment in AI-RAN Edge Inference Systems

## Metadata

- **Authors:** Qiu, Ningyuan and Gan, Shuying and Wang, Xijun and Feng, Chenyuan and Chen, Xiang and Han, Shuangfeng and Wang, Xiaoyun
- **Year:** 2025
- **Venue:** 2025 International Conference on Future Communications and Networks, FCN 2025 - Proceedings
- **DOI:** 10.1109/FCN66513.2025.11296658
- **URL:** https://www.scopus.com/pages/publications/105031773523?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning; edge computing; Large language model

### Abstract

With the rapid development of AI-driven Radio Access Network (AI-RAN) technologies, the integration of Large Language Models (LLMs) into RAN Intelligent Controllers (RICs) has emerged as a promising approach to enabling intelligent telecom edge services such as AI inference. However, achieving timely responses while meeting stringent Service Level Objectives (SLOs) poses a significant challenge, particularly in multi-user edge scenarios. The dynamic nature of request arrivals, heterogeneous latency requirements, and limited computational resources further complicate efficient resource management. In this work, we address the problem of request batching and scheduling under variable arrival times and diverse deadlines, with the goal of maximizing the number of requests completed within their respective SLOs. Our approach jointly considers batch formation and worker assignment, and models the scheduling process as a Markov Decision Process (MDP). To effectively tackle the high-dimensional state space, we develop a deep reinforcement learning (DRL)-based algorithm that learns optimal batching and scheduling strategies. Extensive simulation results demonstrate that our proposed DRL-based approach significantly outperforms existing baseline methods, substantially increasing the proportion of requests completed within SLO constraints in multi-user edge LLM scenarios.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Joint Request Batching and Worker Assignment in AI-RAN Edge Inference Systems

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Joint Request Batching and Worker Assignment in AI-RAN Edge Inference Systems
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint Request Batching and Worker Assignment in AI-RAN Edge Inference Systems
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
