---
id: "paper-1690"
title: "FlowTracer: A Tool for Uncovering Network Path Usage Imbalance in AI Training Clusters"
authors: ["Jamil, Hasibul", "Alim, Abdul", "Schares, Laurent", "Maniotis, Pavlos", "Schour, Liran", "Sydney, Ali", "Kayi, Abdullah", "Kosar, Tevfik", "Karacali, Bengi"]
year: 2025
venue: "IEEE International Conference on Communications"
venue_type: "conference"
doi: "10.1109/ICC52391.2025.11160830"
url: "https://www.scopus.com/pages/publications/105018463532?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6988--6993"
keywords: ["cloud networking", "load balancing", "Network monitoring", "network visibility"]
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

# paper-1690 — FlowTracer: A Tool for Uncovering Network Path Usage Imbalance in AI Training Clusters

## Metadata

- **Authors:** Jamil, Hasibul and Alim, Abdul and Schares, Laurent and Maniotis, Pavlos and Schour, Liran and Sydney, Ali and Kayi, Abdullah and Kosar, Tevfik and Karacali, Bengi
- **Year:** 2025
- **Venue:** IEEE International Conference on Communications
- **DOI:** 10.1109/ICC52391.2025.11160830
- **URL:** https://www.scopus.com/pages/publications/105018463532?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6988--6993
- **Language:** English
- **Keywords:** cloud networking; load balancing; Network monitoring; network visibility

### Abstract

The increasing complexity of AI workloads, especially distributed Large Language Model (LLM) training, places significant strain on the networking infrastructure of parallel data centers and supercomputing systems. While Equal-Cost Multi-Path (ECMP) routing distributes traffic over parallel paths, hash collisions often lead to imbalanced network resource utilization and performance bottlenecks. This paper presents FlowTracer, a tool designed to analyze network path utilization and evaluate different routing strategies. Unlike tools that introduce additional traffic, FlowTracer aids in debugging network inefficiencies by passively monitoring and correlating user workload flows. As a result, FlowTracer does not interfere with ongoing data transfers, enabling analysis with minimal overhead, which is an important factor when debugging and fine-tuning routing schemes in production systems. FlowTracer can provide detailed insights into traffic distribution and can help identify the root causes of performance degradation, such as hash collisions. With FlowTracer's flow-level insights, system operators can optimize routing, reduce congestion, and improve the performance of distributed AI workloads. We use a RoCEv2-enabled cluster with a leaf-spine network and 16 400-Gbps nodes to demonstrate how FlowTracer can be used to compare the flow imbalances of ECMP routing against a statically configured network. The example showcases a 30% reduction in imbalance, as measured by a new metric we introduce.  © 2025 IEEE.

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
