---
id: "paper-2309"
title: "Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market"
authors: ["Xiang, Yuxing", "Li, Xue", "Qian, Kun", "Yang, Yufan", "Zhu, Diwen", "Yu, Wenyuan", "Zhai, Ennan", "Liu, Xuanzhe", "Jin, Xin", "Zhou, Jingren"]
year: 2025
venue: "SOSP 2025 - Proceedings of the 2025 ACM SIGOPS 31st Symposium on Operating Systems Principles"
venue_type: "conference"
doi: "10.1145/3731569.3764815"
url: "https://www.scopus.com/pages/publications/105020848222?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "1030--1045"
keywords: ["GPU pooling", "large language models", "multi-model serving", "serverless computing"]
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

# paper-2309 — Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market

## Metadata

- **Authors:** Xiang, Yuxing and Li, Xue and Qian, Kun and Yang, Yufan and Zhu, Diwen and Yu, Wenyuan and Zhai, Ennan and Liu, Xuanzhe and Jin, Xin and Zhou, Jingren
- **Year:** 2025
- **Venue:** SOSP 2025 - Proceedings of the 2025 ACM SIGOPS 31st Symposium on Operating Systems Principles
- **DOI:** 10.1145/3731569.3764815
- **URL:** https://www.scopus.com/pages/publications/105020848222?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 1030--1045
- **Language:** English
- **Keywords:** GPU pooling; large language models; multi-model serving; serverless computing

### Abstract

Model markets (e.g., Hugging Face) feature a wide variety of models with unique characteristics and varying levels of popularity. Serving sporadic and unpredictable requests in concurrent inference workloads with dedicated GPU instances results in substantial resource waste. While existing multi-model serving solutions use GPU pooling and server-less computing to improve resource efficiency, their effective-ness is limited to supporting at most two or three models per GPU, which is inadequate for fully utilizing GPU resources.We propose Aegaeon, a multi-model serving system that performs model auto-scaling at the token granularity to achieve effective GPU pooling. Aegaeon schedules multimodel requests and makes auto-scaling decisions on a per-token basis to maximize service quality. It reduces auto-scaling overhead by 97% through component reuse, explicit memory management, and fine-grained KV cache synchronization. Experiments show that Aegaeon sustains 2-2.5× higher request arrival rates or 1.5-9× more goodput compared to existing solutions. Aegaeon has been beta deployed in our model marketplace and currently serves tens of models. Deployment results show that Aegaeon reduces the number of GPUs required for serving these models from 1,192 to 213, highlighting an 82% GPU resource saving. © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

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
