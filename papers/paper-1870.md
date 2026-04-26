---
id: "paper-1870"
title: "COMET: Towards Practical W4A4KV4 LLMs Serving"
authors: ["Liu, Lian", "Cheng, Long", "Ren, Haimeng", "Xu, Zhaohui", "Pan, Yudong", "Wang, Mengdi", "Li, Xiaowei", "Han, Yinhe", "Wang, Ying"]
year: 2025
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3676641.3716252"
url: "https://www.scopus.com/pages/publications/105002561495?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "131--146"
keywords: ["algorithm-system co-design", "large language models (llm) serving", "llm quantization"]
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

# paper-1870 — COMET: Towards Practical W4A4KV4 LLMs Serving

## Metadata

- **Authors:** Liu, Lian and Cheng, Long and Ren, Haimeng and Xu, Zhaohui and Pan, Yudong and Wang, Mengdi and Li, Xiaowei and Han, Yinhe and Wang, Ying
- **Year:** 2025
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3676641.3716252
- **URL:** https://www.scopus.com/pages/publications/105002561495?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 131--146
- **Language:** English
- **Keywords:** algorithm-system co-design; large language models (llm) serving; llm quantization

### Abstract

Quantization is a widely-used compression technology to reduce the overhead of serving large language models (LLMs) on terminal devices and in cloud data centers. However, prevalent quantization methods, such as 8-bit weight-activation or 4-bit weight-only quantization, achieve limited performance improvements due to poor support for low-precision (e.g., 4-bit) activation. This work, for the first time, realizes practical W4A4KV4 serving for LLMs, fully utilizing the INT4 tensor cores on modern GPUs and reducing the memory bottleneck caused by the KV cache. Specifically, we propose a novel fine-grained mixed-precision quantization algorithm (FMPQ) that compresses most activations into 4-bit with negligible accuracy loss. To support mixed-precision matrix multiplication for W4A4 and W4A8, we develop a highly optimized W4Ax kernel. Our approach introduces a novel mixed-precision data layout to facilitate access and fast dequantization for activation and weight tensors, utilizing the GPU's software pipeline to hide the overhead of data loading and conversion. Additionally, we propose fine-grained streaming multiprocessor (SM) scheduling to achieve load balance across different SMs. We integrate the optimized W4Ax kernel into our inference framework, COMET, and provide efficient management to support popular LLMs such as LLaMA-3-70B. Extensive evaluations demonstrate that, when running LLaMA family models on a single A100-80G-SMX4, COMET achieves a kernel-level speedup of 2.88x over cuBLAS and a 2.02x throughput improvement compared to TensorRT-LLM from an end-to-end framework perspective. © 2025 ACM.

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
