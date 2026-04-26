---
id: "paper-1381"
title: "Think Fast, Infer Smart: A Hybrid Distributed LLMs Inference at the Wireless Edge"
authors: ["Albaseer, Abdullatif", "Bentafat, Elmahdi", "Hamood, Moqbel", "Abdallah, Mohamed", "Al-Fuqaha, Ala", "Hamdi, Mounir"]
year: 2025
venue: "IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC"
venue_type: "conference"
doi: "10.1109/PIMRC62392.2025.11274878"
url: "https://www.scopus.com/pages/publications/105030546202?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["and bandwidth optimization", "dynamic head-wise layer-wise partitioning", "Edge computing", "Large Language Models (LLMs)", "latency"]
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

# paper-1381 — Think Fast, Infer Smart: A Hybrid Distributed LLMs Inference at the Wireless Edge

## Metadata

- **Authors:** Albaseer, Abdullatif and Bentafat, Elmahdi and Hamood, Moqbel and Abdallah, Mohamed and Al-Fuqaha, Ala and Hamdi, Mounir
- **Year:** 2025
- **Venue:** IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC
- **DOI:** 10.1109/PIMRC62392.2025.11274878
- **URL:** https://www.scopus.com/pages/publications/105030546202?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** and bandwidth optimization; dynamic head-wise layer-wise partitioning; Edge computing; Large Language Models (LLMs); latency

### Abstract

Deploying large language models (LLMs) at the wireless edge is a promising solution to meet the low-latency, high-computation demands of next-generation AI applications. Although the existing literature has introduced approaches to enable distributed LLM inference, these methods largely overlook the distinct computational and communication characteristics of the two-phase LLM inference process - the pre-fill and decode phases. This oversight leads to suboptimal performance and limits scalability in real-world deployments. To address these issues, we propose a novel collaborative inference framework that strategically minimizes inference latency by optimally distributing computational loads across edge devices, the edge server, and the cloud. Our approach introduces a hybrid framework that combines head-wise parallel processing with layer-wise partitioning of LLM models, supported by a dual-phase optimization strategy. In the pre-fill phase, we optimize assigning attention heads to selected edge devices for parallel computation and efficient resource use. We then optimize for minimal latency by selecting participants, determining head assignments per device, and allocating bandwidth while meeting all constraints. In the de-code phase, our framework adaptively decides whether to execute computations locally on the edge server, offload them to the cloud, or redistribute tasks among edge devices, optimizing this decision based on the remaining latency budget and the sequential nature of the decode phase. The simulation results demonstrate that the proposed framework significantly outperforms the baseline methods, achieving a 56% reduction in inference latency, 40% improvement in bandwidth efficiency and 35% improvement in resource utilization.  © 2025 IEEE.

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
