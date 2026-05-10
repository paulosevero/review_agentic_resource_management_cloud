---
id: "paper-1479"
title: "Optimizing LLM Inference on Edge Devices Using SIMD Accelerations"
authors: ["Chen, Feiyu"]
year: 2025
venue: "Proceedings of 2025 IEEE 7th International Conference on Civil Aviation Safety and Information Technology, ICCASIT 2025"
venue_type: "conference"
doi: "10.1109/ICCASIT66611.2025.11348646"
url: "https://www.scopus.com/pages/publications/105033215141?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1272--1279"
keywords: ["Edge Devices", "LLM Inference", "SIMD Accelerations"]
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
    human_justification: "LLM as workload"

---

# paper-1479 — Optimizing LLM Inference on Edge Devices Using SIMD Accelerations

## Metadata

- **Authors:** Chen, Feiyu
- **Year:** 2025
- **Venue:** Proceedings of 2025 IEEE 7th International Conference on Civil Aviation Safety and Information Technology, ICCASIT 2025
- **DOI:** 10.1109/ICCASIT66611.2025.11348646
- **URL:** https://www.scopus.com/pages/publications/105033215141?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1272--1279
- **Language:** English
- **Keywords:** Edge Devices; LLM Inference; SIMD Accelerations

### Abstract

This paper addresses the computational challenges of deploying large language models (LLMs) on edge devices, which typically lack high-performance GPUs but possess increasingly capable CPUs with SIMD instruction set extensions. We propose a portable, SIMD-accelerated library designed to optimize low-level LLM inference primitives. Our approach leverages AVX2 intrinsics for floating-point operations, with a design for future expansion to quantized integer formats and other instruction sets across diverse Intel and ARM CPUs. Performance is validated through micro-benchmarks on individual operations and detailed binary inspection of optimized kernels. Significant speedups are demonstrated for core operations such as matrix multiplication and layer normalization. While gains for other operations, such as element-wise multiplication and softmax, are less pronounced due this work offers a practical solution for enhancing LLM inference efficiency on a wide range of edge computing platforms. © 2025 IEEE.

## 04 — Title Screening

**Title:** Optimizing LLM Inference on Edge Devices Using SIMD Accelerations

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Optimizing LLM Inference on Edge Devices Using SIMD Accelerations
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimizing LLM Inference on Edge Devices Using SIMD Accelerations
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
