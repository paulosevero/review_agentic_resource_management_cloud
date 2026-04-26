---
id: "paper-2639"
title: "Bauhaus: Restructuring Vector Database for LLM Retrieval on CXL-Based Tiered Memory"
authors: ["Kim, Kyungbin", "Ahn, Sungsu", "Jeong, Wonjung", "Kim, Jongmin", "Choi, Sangun", "Gil, Minseong", "Kim, Minseong", "Jung, Dongha", "Hong, Yunjay", "Jung, Haekang", "Oh, Yunho"]
year: 2026
venue: "IEEE Transactions on Computers"
venue_type: "journal"
doi: "10.1109/TC.2026.3656215"
url: "https://www.scopus.com/pages/publications/105029168857?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1309--1322"
keywords: ["CXL-based tiered memory systems", "Embedding-aware memory management", "Retrieval-Augmented Generation"]
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

# paper-2639 — Bauhaus: Restructuring Vector Database for LLM Retrieval on CXL-Based Tiered Memory

## Metadata

- **Authors:** Kim, Kyungbin and Ahn, Sungsu and Jeong, Wonjung and Kim, Jongmin and Choi, Sangun and Gil, Minseong and Kim, Minseong and Jung, Dongha and Hong, Yunjay and Jung, Haekang and Oh, Yunho
- **Year:** 2026
- **Venue:** IEEE Transactions on Computers
- **DOI:** 10.1109/TC.2026.3656215
- **URL:** https://www.scopus.com/pages/publications/105029168857?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1309--1322
- **Language:** English
- **Keywords:** CXL-based tiered memory systems; Embedding-aware memory management; Retrieval-Augmented Generation

### Abstract

Retrieval-augmented generation pipelines store large volumes of embedding vectors in vector databases for semantic search. In Compute Express Link (CXL)-based tiered memory systems, page-level placement often promotes pages containing both hot and cold vectors, leaving many hot vectors in the long-latency, lower-bandwidth CXL tier. This imbalance increases memory access time, reduces throughput, and worsens tail latency. This paper presents Bauhaus, a software-based memory management technique that increases the share of hot vectors in host memory, thereby improving access efficiency, reducing backend stalls, and lowering tail latency. Bauhaus monitors and reorders embedding vectors at vector-level granularity using Processor Event-Based Sampling (PEBS) and Virtual Memory Area (VMA) metadata, clustering hot vectors into contiguous pages to raise hot-page density and enhance the effectiveness of page promotion. Bauhaus, integrated into the Heterogeneous Memory Software Development Kit (HMSDK) developed and publicly released by SK hynix, is evaluated on a production-grade CXL platform. Across various embedding models, datasets, and CXL-to-host memory ratios, Bauhaus achieves 42.0% higher throughput over the baseline and 15.8% over HMSDK. Bauhaus sustains high RAG performance under constrained host memory capacity, offering a practical solution for large-scale vector database deployments in modern datacenter environments. © 2026 IEEE. All rights reserved.

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
