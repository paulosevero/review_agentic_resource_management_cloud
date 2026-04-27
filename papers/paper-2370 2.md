---
id: "paper-2370"
title: "Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts"
authors: ["Yang, Jin", "Wu, Qiong", "Feng, Zhiying", "Zhou, Zhi", "Guo, Deke", "Chen, Xu"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3590969"
url: "https://www.scopus.com/pages/publications/105012355291?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "13648--13662"
keywords: ["deep reinforcement learning (DRL)", "edge computing", "expert routing", "Large language models (LLMs)"]
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

# paper-2370 — Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts

## Metadata

- **Authors:** Yang, Jin and Wu, Qiong and Feng, Zhiying and Zhou, Zhi and Guo, Deke and Chen, Xu
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3590969
- **URL:** https://www.scopus.com/pages/publications/105012355291?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 13648--13662
- **Language:** English
- **Keywords:** deep reinforcement learning (DRL); edge computing; expert routing; Large language models (LLMs)

### Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities, leading to a significant increase in user demand for LLM services. However, cloud-based LLM services often suffer from high latency, unstable responsiveness, and privacy concerns. Therefore, multiple LLMs are usually deployed at the network edge to boost real-time responsiveness and protect data privacy, particularly for many emerging smart mobile and IoT applications. Given the varying response quality and latency of LLM services, a critical issue is how to route user requests from mobile and IoT devices to an appropriate LLM service (i.e., edge LLM expert) to ensure acceptable quality-of-service (QoS). Existing routing algorithms fail to simultaneously address the heterogeneity of LLM services, the interference among requests, and the dynamic workloads necessary for maintaining long-term stable QoS. To meet these challenges, in this paper we propose a novel deep reinforcement learning (DRL)-based QoS-aware LLM routing framework for sustained high-quality LLM services. Due to the dynamic nature of the global state, we propose a dynamic state abstraction technique to compactly represent global state features with a heterogeneous graph attention network (HAN). Additionally, we introduce an action impact estimator and a tailored reward function to guide the DRL agent in maximizing QoS and preventing latency violations. Extensive experiments on both Poisson and real-world workloads demonstrate that our proposed algorithm significantly improves average QoS and computing resource efficiency compared to existing baselines.  © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Quality-of-Service Aware LLM Routing for Edge Computing with Multiple Experts
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
