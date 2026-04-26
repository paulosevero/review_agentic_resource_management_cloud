---
id: "paper-1664"
title: "Redis-Based High-Concurrency Optimization for a Shooting Results System"
authors: ["Hu, Linwei", "Cheng, Meng", "Sun, Weixing", "Fu, Lijun"]
year: 2025
venue: "Proceedings of the IEEE International Conference on Computer and Communications, ICCC"
venue_type: "conference"
doi: "10.1109/ICCC68654.2025.11437585"
url: "https://www.scopus.com/pages/publications/105035765591?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "348--352"
keywords: ["distributed cache", "high concurrency", "hotspot detection", "load balancing", "Redis"]
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

# paper-1664 — Redis-Based High-Concurrency Optimization for a Shooting Results System

## Metadata

- **Authors:** Hu, Linwei and Cheng, Meng and Sun, Weixing and Fu, Lijun
- **Year:** 2025
- **Venue:** Proceedings of the IEEE International Conference on Computer and Communications, ICCC
- **DOI:** 10.1109/ICCC68654.2025.11437585
- **URL:** https://www.scopus.com/pages/publications/105035765591?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 348--352
- **Language:** English
- **Keywords:** distributed cache; high concurrency; hotspot detection; load balancing; Redis

### Abstract

Shooting-event management platforms experience bursty, extremely skewed read traffic during moments such as results release or registration deadlines. Conventional Redis clusters struggle to balance hotspot-slot overload against resource waste. This paper proposes an intelligent cache optimization tailored to periodic high-concurrency scenarios: (1) Hot-cold data identification and prediction via time-series features and a lightweight large language model (LLM) with a federated inference scheme, enabling millisecond-level hotspot-key prediction and prewarming; (2) Access-aware elastic scaling by combining a dynamic hotspot-replica scheduler with a Kubernetes-based Redis Cluster HPA to automatically adjust node scale and topology under load. On a representative shooting dataset, the approach increases peak throughput from 30k to 86k QPS, reduces hotspotread P99 latency by 62%, and saves 43% cache resources during off-peak periods. The study offers an elastic-cache path that jointly optimizes availability and resource efficiency for periodic hotspot workloads. © 2025 IEEE.

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
