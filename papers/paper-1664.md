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
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

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

**Title:** Redis-Based High-Concurrency Optimization for a Shooting Results System

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Redis-Based High-Concurrency Optimization for a Shooting Results System
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Redis-Based High-Concurrency Optimization for a Shooting Results System
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
