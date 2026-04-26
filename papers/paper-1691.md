---
id: "paper-1691"
title: "Analyzing quantized small language models for efficient edge deployment"
authors: ["Jangw, Sooyoung", "Yang, Seungho", "Choi, Changbeom"]
year: 2025
venue: "Journal of Korean Institute of Communications and Information Sciences"
venue_type: "journal"
doi: "10.7840/kics.2025.50.9.1364"
url: "https://www.scopus.com/pages/publications/105019188399?origin=resultslist"
publisher: "Korean Institute of Communications and Information Sciences"
pages: "1364--1380"
keywords: ["Edge AI Deployment", "Edge Computing", "MMLU-Pro", "Quantization", "Small Language Models"]
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

# paper-1691 — Analyzing quantized small language models for efficient edge deployment

## Metadata

- **Authors:** Jangw, Sooyoung and Yang, Seungho and Choi, Changbeom
- **Year:** 2025
- **Venue:** Journal of Korean Institute of Communications and Information Sciences
- **DOI:** 10.7840/kics.2025.50.9.1364
- **URL:** https://www.scopus.com/pages/publications/105019188399?origin=resultslist
- **Publisher:** Korean Institute of Communications and Information Sciences
- **Pages:** 1364--1380
- **Language:** English
- **Keywords:** Edge AI Deployment; Edge Computing; MMLU-Pro; Quantization; Small Language Models

### Abstract

Quantized small language models (SLMs) offer a promising approach for deploying advanced natural language process- ing (NLP) services on resource-constrained edge devices. However, an in-depth examination of how different quantization configurations influence accuracy and efficiency remains underexplored. This paper systematically evaluates 72 quantized variants of Llama 3.2 (1B and 3B parameters) and Qwen 2.5 (1.5B and 3B parameters) across 13 quantization configura- tions, ranging from q2_K to q6_K. We use the MMLU-Pro benchmark to measure the accuracy (including and excluding random guesses), inference time, resource utilization, and power consumption on an NVIDIA Jetson Orin Nano. Our findings reveal that low-bit quantized models often rely heavily on random guessing, with modest accuracy improvements observed when these are excluded. Furthermore, Qwen 2.5 models generally yield superior accuracy and lower latency than Llama 3.2, albeit with higher sensitivity to quantization, whereas Llama 3.2 exhibits more consistent performance across quantization configurations. CPU utilization remains low (approximately 1-4%), with GPU utilization peaking up to 90% and power consumption ranging from 9.2 W to 11.5 W. Variability across different domains (computer science, engineering, and math) underscores the importance of selecting the appropriate model family, parameter size, and quantization configuration for specific applications. We conclude by outlining future directions for improving on-device NLP, including mixed-precision quantization, hardware-specific optimizations, and broader assessments covering multilingual or multimodal tasks. © 2025, Korean Institute of Communications and Information Sciences. All rights reserved.

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
