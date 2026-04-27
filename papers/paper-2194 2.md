---
id: "paper-2194"
title: "Performance and Cost Optimization of Federated LLM Agents in Edge Computing Environments"
authors: ["Tadi, Goutam", "Mittal, Akshay"]
year: 2025
venue: "2025 3rd International Conference on Foundation and Large Language Models, FLLM 2025"
venue_type: "conference"
doi: "10.1109/FLLM67465.2025.11391052"
url: "https://www.scopus.com/pages/publications/105035915042?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1267--1274"
keywords: ["AI Agents", "Edge Computing", "Federated Learning", "K3s", "Kubernetes", "Large Language Models", "Performance Optimization"]
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

# paper-2194 — Performance and Cost Optimization of Federated LLM Agents in Edge Computing Environments

## Metadata

- **Authors:** Tadi, Goutam and Mittal, Akshay
- **Year:** 2025
- **Venue:** 2025 3rd International Conference on Foundation and Large Language Models, FLLM 2025
- **DOI:** 10.1109/FLLM67465.2025.11391052
- **URL:** https://www.scopus.com/pages/publications/105035915042?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1267--1274
- **Language:** English
- **Keywords:** AI Agents; Edge Computing; Federated Learning; K3s; Kubernetes; Large Language Models; Performance Optimization

### Abstract

The deployment of Large Language Model (LLM) agents is shifting from centralized cloud infrastructures to decentralized edge computing environments to achieve reduced latency and enhanced data privacy. This transition is driven by the emergence of edge AI applications such as autonomous vehicle command recognition, industrial process monitoring with natural language interfaces, and conversational AI on resource-constrained IoT devices. However, this shift introduces significant challenges due to edge devices' limited computational resources, storage capacity, and network bandwidth, which severely magnify the performance bottlenecks observed in well-resourced data centers. This paper addresses these challenges by extending cloud-based LLM optimization techniques to the unique constraints of edge computing. We present a comprehensive experimental analysis of federated LLM agent workloads deployed on a Kubernetes (K3s) cluster that simulates a realistic heterogeneous edge environment. Through a systematic ablation study, we evaluate the effectiveness of multiple optimization strategies, including advanced model quantization, distributed caching, and network-aware orchestration, measuring their impact on critical performance metrics such as time-to-first-token (TTFT), model synchronization overhead, and energy consumption. Our results demonstrate that while traditional storage and memory optimizations remain important, network-aware scheduling and adaptive model loading strategies are crucial for achieving practical edge deployment. The proposed optimization framework delivers substantial improvements over naive deployment approaches: a 75% reduction in network bandwidth consumption, a 45% improvement in end-to-end inference latency, and a 61% decrease in energy usage per inference, while maintaining acceptable model quality as measured by perplexity. © 2025 IEEE.

## 04 — Title Screening

**Title:** Performance and Cost Optimization of Federated LLM Agents in Edge Computing Environments

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Performance and Cost Optimization of Federated LLM Agents in Edge Computing Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Performance and Cost Optimization of Federated LLM Agents in Edge Computing Environments
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
