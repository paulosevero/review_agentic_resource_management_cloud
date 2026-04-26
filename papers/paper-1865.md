---
id: "paper-1865"
title: "Accelerating LLM Inference on RISC-V Edge Devices via Vector Extension Optimization"
authors: ["Liu, Zhilong", "Peng, Long", "Wang, Wenzhu", "Li, Ke", "Zeng, Binrui", "Yu, Jie", "Liu, Xiaodong"]
year: 2025
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-96-9869-1_43"
url: "https://www.scopus.com/pages/publications/105013060244?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "515--526"
keywords: ["Inference Acceleration", "Large Language Models", "Operator Optimization", "RISC-V Vector"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-1865 — Accelerating LLM Inference on RISC-V Edge Devices via Vector Extension Optimization

## Metadata

- **Authors:** Liu, Zhilong and Peng, Long and Wang, Wenzhu and Li, Ke and Zeng, Binrui and Yu, Jie and Liu, Xiaodong
- **Year:** 2025
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-96-9869-1_43
- **URL:** https://www.scopus.com/pages/publications/105013060244?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 515--526
- **Language:** English
- **Keywords:** Inference Acceleration; Large Language Models; Operator Optimization; RISC-V Vector

### Abstract

The deployment of large language models (LLMs) on edge devices faces significant challenges due to limited computational resources, memory bandwidth, and strict power constraints. While RISC-V architecture offers advantages in edge computing through its modularity, scalability, and open-source ecosystem, the LLM inference framework llama.cpp struggle to leverage the full potential of the RISC-V Vector Extension (RVV), leading to suboptimal performance. This study has achieved efficient LLM deployment in resource-constrained environments by optimizing critical operators in the llama.cpp framework using RVV instructions. We first identify performance bottlenecks, such as the f16 vector dot product and layer normalization, through runtime profiling. These operators are then redesigned with RVV’s SIMD capabilities, including half-precision floating-point support via the "zvfh" extension, to maximize parallel computation. Experimental results on a RISC-V-based BananaPi BPI-F3 platform demonstrate substantial improvements: the Gemma-2-2B model achieves a 1.7 × speedup in prefill prompt processing and a 53% acceleration in token generation during decoding, while the larger Llama-3.1-8B model shows 36% and 19% improvements in prefill and decode phases, respectively. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
