---
id: "paper-1463"
title: "CrossPipe: Towards Optimal Pipeline Schedules for Cross-Datacenter Training"
authors: ["Chen, Tiancheng", "Kubicek, Ales", "Huang, Langwen", "Hoefler, Torsten"]
year: 2025
venue: "Proceedings of the 2025 USENIX Annual Technical Conference, ATC 2025"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/105011583988?origin=resultslist"
publisher: "USENIX Association"
pages: "1089--1108"
keywords: ["Modeling languages", "Optimization", "Pipelines", "Scheduling algorithms", "Datacenter", "Language model", "Limited bandwidth", "Memory constraints", "Model training", "Network latencies", "Overlapping data", "Pipeline parallelisms", "Unified analysis", "Unified optimizations", "Bandwidth"]
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

# paper-1463 — CrossPipe: Towards Optimal Pipeline Schedules for Cross-Datacenter Training

## Metadata

- **Authors:** Chen, Tiancheng and Kubicek, Ales and Huang, Langwen and Hoefler, Torsten
- **Year:** 2025
- **Venue:** Proceedings of the 2025 USENIX Annual Technical Conference, ATC 2025
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/105011583988?origin=resultslist
- **Publisher:** USENIX Association
- **Pages:** 1089--1108
- **Language:** English
- **Keywords:** Modeling languages; Optimization; Pipelines; Scheduling algorithms; Datacenter; Language model; Limited bandwidth; Memory constraints; Model training; Network latencies; Overlapping data; Pipeline parallelisms; Unified analysis; Unified optimizations; Bandwidth

### Abstract

>Training large language models (LLMs) now requires resources that exceed a single datacenter, making cross-datacenter strategies increasingly crucial. We present CrossPipe, a framework designed to optimize model training across geographically distributed datacenters by explicitly modeling and mitigating the impact of network latency and limited bandwidth. It enables unified analysis and optimization incorporating both pipeline parallelism (PP) and opportunities for overlapping data parallelism (DP) communication. CrossPipe generates optimized pipeline schedules using either solver-based optimal or fast near-optimal greedy algorithms, built upon a flexible execution engine that separates scheduling logic from communication details. Our evaluation shows that CrossPipe reduces training time by up to 33.6% compared to traditional pipeline schedules under identical memory constraints. When memory constraints are relaxed, CrossPipe maintains strong performance despite communication delays, approaching the efficiency of idealized schedules without delays. CrossPipe offers improved scalability and resource utilization, particularly in environments with high network latency or limited bandwidth. © 2025 by The USENIX Association. All rights reserved.

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
