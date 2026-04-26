---
id: "paper-2724"
title: "Adaptive Request Scheduling and Load Balancing for Edge Deployed Large Language Models"
authors: ["Mou, Fangyi", "Tang, Zhiqing", "Jia, Weijia", "Zhao, Wei"]
year: 2026
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2026.3665250"
url: "https://www.scopus.com/pages/publications/105030692754?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["deep reinforcement learning", "Edge computing", "LLM inference", "load balancing", "task scheduling"]
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

# paper-2724 — Adaptive Request Scheduling and Load Balancing for Edge Deployed Large Language Models

## Metadata

- **Authors:** Mou, Fangyi and Tang, Zhiqing and Jia, Weijia and Zhao, Wei
- **Year:** 2026
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2026.3665250
- **URL:** https://www.scopus.com/pages/publications/105030692754?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning; Edge computing; LLM inference; load balancing; task scheduling

### Abstract

The inference services of Large Language Models (LLMs) play a crucial role in many fields. Deploying LLMs at the network edge can effectively reduce response latency and enhance domain-specific knowledge. However, due to the dynamic and unpredictable nature of edge user requests and the limited resources of edge servers, improper request scheduling can lead to server load imbalance and increased inference latency. To address this challenge, we model edge LLM inference under dynamic workloads and constrained edge resources by fully considering mutual influences and trade-offs between inference performance, inference latency, and edge resource utilization. We propose a Workload Prediction and Dynamic Request Scheduling (WPDS) algorithm for edge computing environments. The WPDS algorithm first evaluates and prioritizes heterogeneous requests by extracting features and importance scores from user requests. A Transformer-based encoder is used to extract load characteristics of edge servers over different time periods to predict future GPU resource demands. Then, a soft actor-critic reinforcement learning model dynamically schedules requests to appropriate LLM instances, capturing the dynamic relationship between request processing and edge resource utilization from complex state spaces. We evaluate our algorithm in a real Kubernetes-based edge inference prototype system. Experimental results indicate that our approach reduces average inference time by approximately 16.6% compared to the best-performing heuristic baseline algorithm, while also achieving more balanced GPU utilization across edge servers. © 2008-2012 IEEE.

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
