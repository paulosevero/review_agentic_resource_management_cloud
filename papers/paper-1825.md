---
id: "paper-1825"
title: "SLED: A Speculative LLM Decoding Framework for Efficient Edge Serving"
authors: ["Li, Xiangchen", "Spatharakis, Dimitris", "Ghafouri, Saeid", "Fan, Jiakun", "Vandierendonck, Hans", "John, Deepu", "Ji, Bo", "Nikolopoulos, Dimitrios S."]
year: 2025
venue: "SEC 2025 - Proceedings of the 2025 10th ACM/IEEE Symposium on Edge Computing"
venue_type: "conference"
doi: "10.1145/3769102.3770608"
url: "https://www.scopus.com/pages/publications/105024939100?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: ""
keywords: ["Distributed Inference", "Edge Computing", "Large Language Models", "Resource-Aware Serving", "Speculative Decoding", "Token Verification"]
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

# paper-1825 — SLED: A Speculative LLM Decoding Framework for Efficient Edge Serving

## Metadata

- **Authors:** Li, Xiangchen and Spatharakis, Dimitris and Ghafouri, Saeid and Fan, Jiakun and Vandierendonck, Hans and John, Deepu and Ji, Bo and Nikolopoulos, Dimitrios S.
- **Year:** 2025
- **Venue:** SEC 2025 - Proceedings of the 2025 10th ACM/IEEE Symposium on Edge Computing
- **DOI:** 10.1145/3769102.3770608
- **URL:** https://www.scopus.com/pages/publications/105024939100?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 
- **Language:** English
- **Keywords:** Distributed Inference; Edge Computing; Large Language Models; Resource-Aware Serving; Speculative Decoding; Token Verification

### Abstract

The growing gap between the increasing complexity of large language models (LLMs) and the limited computational budgets of edge devices poses a key challenge for efficient on-device inference, despite gradual improvements in hardware capabilities. Existing strategies, such as aggressive quantization, pruning, or remote inference, trade accuracy for efficiency or lead to substantial cost burdens. This position paper introduces a new framework that leverages speculative decoding, previously viewed primarily as a decoding acceleration technique for autoregressive generation of LLMs, as a promising approach specifically adapted for edge computing by orchestrating computation across heterogeneous devices. We propose SLED, a framework that allows lightweight edge devices to draft multiple candidate tokens locally using diverse draft models, while a single, shared edge server verifies the tokens utilizing a more precise target model. To further increase the efficiency of verification, the edge server batches the diverse verification requests from devices. This approach supports heterogeneous devices and reduces server-side memory footprint by sharing a single upstream target model across devices. Our initial experiments with Jetson Orin Nano, Raspberry Pi 4B/5, and an edge server equipped with 4 Nvidia A100 GPUs indicate substantial benefits: ×2.2 higher system throughput, ×2.8 higher system capacity, and better cost efficiency, all without sacrificing model accuracy. © 2025 Copyright held by the owner/author(s).

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
