---
id: "paper-2628"
title: "Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents"
authors: ["Kapoor, Rahul", "Kas, Miray"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3675074"
url: "https://www.scopus.com/pages/publications/105033247089?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "43552--43568"
keywords: ["Active learning", "AIOps", "anomaly detection", "data center observability", "dynamic resolution", "large language models"]
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

# paper-2628 — Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents

## Metadata

- **Authors:** Kapoor, Rahul and Kas, Miray
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3675074
- **URL:** https://www.scopus.com/pages/publications/105033247089?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 43552--43568
- **Language:** English
- **Keywords:** Active learning; AIOps; anomaly detection; data center observability; dynamic resolution; large language models

### Abstract

The 'observability tax' - the escalating cost of telemetry in hyperscale data centers - forces a trade-off between expensive full-fidelity monitoring and low-cost sampling that misses critical 'gray failures.' While traditional AIOps models act as passive post-hoc analyzers, the novelty of this work lies in reformulating observability as an active, hypothesis-driven process. To achieve this, we propose a Dynamic Resolution Architecture where a Topology-Aware LLM Agent dynamically controls the telemetry resolution of the underlying infrastructure. Our Topology-Aware Active LLM Agent employs 'Sentinel Sampling,' monitoring 100% of nodes with low-cost essential metrics and only upgrading to high-resolution extended telemetry when semantically justified. Unlike rigid heuristics, the agent uses semantic reasoning to distinguish legitimate heavy workloads from pathological failures, even when root causes are hidden by layers of indirection in our physics-based simulation. Experimental results show the Active Agent achieves an F1 score of 0.95, significantly outperforming a cost-matched heuristic baseline (F1 0.65). Using a 'Skeptical Site Reliability Engineer (SRE)' protocol, the agent achieves 0.99 precision in distinguishing genuine failures from high-load noise. Our 'Wake-on-Anomaly' cost model shows an 84% reduction in telemetry bandwidth and a 12.5% reduction in Total Cost of Ownership compared to standard ingestion. This work demonstrates that observability is primarily a data selection, not data volume, problem, solvable via semantic active reasoning.  © 2013 IEEE.

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
