---
id: "paper-2012"
title: "Burst-Aware Weighted Fair Queueing for Serverless Inference: Mitigating Noisy Neighbor Effects in Multi-Tenant Systems"
authors: ["Pandey, Rajesh Kumar", "Soni, Jubin Abhishek", "Anand, Amit"]
year: 2025
venue: "Journal of Soft Computing and Data Mining"
venue_type: "journal"
doi: "10.30880/jscdm.2025.06.03.022"
url: "https://www.scopus.com/pages/publications/105027645350?origin=resultslist"
publisher: "Penerbit UTHM"
pages: "356--369"
keywords: ["fair queueing", "machine learning inference", "multi-tenancy", "resource scheduling", "Serverless computing"]
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

# paper-2012 — Burst-Aware Weighted Fair Queueing for Serverless Inference: Mitigating Noisy Neighbor Effects in Multi-Tenant Systems

## Metadata

- **Authors:** Pandey, Rajesh Kumar and Soni, Jubin Abhishek and Anand, Amit
- **Year:** 2025
- **Venue:** Journal of Soft Computing and Data Mining
- **DOI:** 10.30880/jscdm.2025.06.03.022
- **URL:** https://www.scopus.com/pages/publications/105027645350?origin=resultslist
- **Publisher:** Penerbit UTHM
- **Pages:** 356--369
- **Language:** English
- **Keywords:** fair queueing; machine learning inference; multi-tenancy; resource scheduling; Serverless computing

### Abstract

Multi-tenant serverless inference often devolves into noisy-neighbor scenarios where a single tenant’s bursty LLM batch floods the fleet, pushing interactive calls beyond their latency budgets. We propose Burst-Aware Weighted Fair Queueing (BWFQ), a scheduler that requires only two counters per tenant (tokens earned, tokens spent) and a constant-time heap pop to select the next invocation. In BWFQ, we use a token bucket in which tokens accumulate at a tenant-specific base rate and are depleted on each dispatch. When a tenant exhausts all its tokens, its requests are queued, giving chances to other quieter tenants to run. Techniques described in other papers, such as Dominant-Resource Fairness and BWFQ, require neither per-invocation resource profiling nor multi-dimensional share accounting, making them easy to integrate with existing Lambda-style dispatchers. To evaluate our algorithm, we built a prototype using AWS Lambda and observed that BWFQ reduces the P99 latency gap between interactive and batch tenants from 8.5s to 2.1s; a 4.0X improvement, while preserving 94% of the throughput achieved by First-Come-First-Serve. The algorithm adds only 35 µs of scheduling overhead per decision and fits in approximately 150 lines of Go code. These results demonstrate that token-bucket fair queueing provides a practical, immediately deployable solution for production serverless inference. © 2025, Penerbit UTHM. All rights reserved.

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
