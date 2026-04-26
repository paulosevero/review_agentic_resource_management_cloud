---
id: "paper-2500"
title: "Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference"
authors: ["Ahn, Juncheol", "Son, Yubin", "Kim, Daemin", "Park, Sejin"]
year: 2026
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s26041101"
url: "https://www.scopus.com/pages/publications/105031370407?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["cloud inference", "edge computing", "GPU scheduling", "IoT", "large language models", "micro-batching", "pipeline parallelism"]
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

# paper-2500 — Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference

## Metadata

- **Authors:** Ahn, Juncheol and Son, Yubin and Kim, Daemin and Park, Sejin
- **Year:** 2026
- **Venue:** Sensors
- **DOI:** 10.3390/s26041101
- **URL:** https://www.scopus.com/pages/publications/105031370407?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** cloud inference; edge computing; GPU scheduling; IoT; large language models; micro-batching; pipeline parallelism

### Abstract

Large language models in IoT–edge–cloud settings face bursty, heterogeneous requests that make pipeline-parallel inference prone to micro-batch imbalance and communication stalls, causing GPU idle time and SLO violations. We propose a runtime-adaptive scheduler that jointly tunes token budgets and micro-batch counts to balance prefill/decode workloads and minimize pipeline bubbles under changing compute and network conditions. On a four-node pipeline-parallel cluster across Llama-2-13b and Qwen2.5-14b at 100/1000 Mbps, our method outperforms vLLM and SGLang, reducing GPU idle time by up to 55% and improving throughput by up to 1.61 × while improving TTFT/ITL SLO satisfaction. These results show that dynamic scheduling is essential for scalable, latency-stable LLM inference in IoT–edge–cloud environments. © 2026 by the authors.

## 04 — Title Screening

**Title:** Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference
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
