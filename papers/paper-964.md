---
id: "paper-964"
title: "Benchmarking Edge AI Platforms for High-Performance ML Inference"
authors: ["Jayanth, Rakshith", "Gupta, Neelesh", "Prasanna, Viktor"]
year: 2024
venue: "2024 IEEE High Performance Extreme Computing Conference, HPEC 2024"
venue_type: "conference"
doi: "10.1109/HPEC62836.2024.10938499"
url: "https://www.scopus.com/pages/publications/105002720861?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["edge computing", "heterogeneous computing", "linear algebra", "neural network inference", "neural processing unit"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-964 — Benchmarking Edge AI Platforms for High-Performance ML Inference

## Metadata

- **Authors:** Jayanth, Rakshith and Gupta, Neelesh and Prasanna, Viktor
- **Year:** 2024
- **Venue:** 2024 IEEE High Performance Extreme Computing Conference, HPEC 2024
- **DOI:** 10.1109/HPEC62836.2024.10938499
- **URL:** https://www.scopus.com/pages/publications/105002720861?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; heterogeneous computing; linear algebra; neural network inference; neural processing unit

### Abstract

Edge computing's growing prominence, due to its ability to reduce communication latency and enable real-time processing, is promoting the rise of high-performance, heteroge-neous System-on-Chip solutions. While current approaches often involve scaling down modern hardware, the performance characteristics of neural network workloads on these platforms can vary significantly, especially when it comes to parallel processing, which is a critical consideration for edge deployments. To address this, we conduct a comprehensive study comparing the latency and throughput of various linear algebra and neural network inference tasks across CPU-only, CPU/GPU, and CPU/NPU integrated solutions. We find that the Neural Processing Unit (NPU) excels in matrix-vector multiplication (58.6% faster) and some neural network tasks (3.2 ×faster for video classification and large language models). GPU outperforms in matrix multiplication (22.6% faster) and LSTM networks (2.7× faster) while CPU excels at less parallel operations like dot product. NPU-based inference offers a balance of latency and throughput at lower power consumption. GPU-based inference, though more energy-intensive, performs best with large dimensions and batch sizes. We highlight the potential of heterogeneous computing solutions for edge AI, where diverse compute units can be strategically leveraged to boost accurate and real-time inference. © 2024 IEEE.

## 04 — Title Screening

**Title:** Benchmarking Edge AI Platforms for High-Performance ML Inference

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Benchmarking Edge AI Platforms for High-Performance ML Inference
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Benchmarking Edge AI Platforms for High-Performance ML Inference
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
