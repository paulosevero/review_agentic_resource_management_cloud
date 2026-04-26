---
id: "paper-536"
title: "Large-Scale Machine Learning Cluster Scheduling via Multi-Agent Graph Reinforcement Learning"
authors: ["Zhao, Xiaoyang", "Wu, Chuan"]
year: 2022
venue: "IEEE Transactions on Network and Service Management"
venue_type: "journal"
doi: "10.1109/TNSM.2021.3139607"
url: "https://www.scopus.com/pages/publications/85122580602?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4962--4974"
keywords: ["AI for management", "cluster scheduling", "distributed machine learning", "graph neural network", "multi-agent reinforcement learning"]
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

# paper-536 — Large-Scale Machine Learning Cluster Scheduling via Multi-Agent Graph Reinforcement Learning

## Metadata

- **Authors:** Zhao, Xiaoyang and Wu, Chuan
- **Year:** 2022
- **Venue:** IEEE Transactions on Network and Service Management
- **DOI:** 10.1109/TNSM.2021.3139607
- **URL:** https://www.scopus.com/pages/publications/85122580602?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4962--4974
- **Language:** English
- **Keywords:** AI for management; cluster scheduling; distributed machine learning; graph neural network; multi-agent reinforcement learning

### Abstract

Efficient scheduling of distributed deep learning (DL) jobs in large GPU clusters is crucial for resource efficiency and job performance. While server sharing among jobs improves resource utilization, interference among co-located DL jobs occurs due to resource contention. Interference-aware job placement has been studied, with white-box approaches based on explicit interference modeling and black-box schedulers with reinforcement learning. In today's clusters containing thousands of GPU servers, running a single scheduler to manage all arrival jobs in a timely and effective manner is challenging, due to the large workload scale. We adopt multiple schedulers in a large-scale cluster/data center, and propose a multi-agent reinforcement learning (MARL) scheduling framework to cooperatively learn fine-grained job placement policies, towards the objective of minimizing job completion time (JCT). To achieve topology-aware placements, our proposed framework uses hierarchical graph neural networks to encode the data center topology and server architecture. In view of a common lack of precise reward samples corresponding to different placements, a job interference model is further devised to predict interference levels in face of various co-locations, for training of the MARL schedulers. Testbed and trace-driven evaluations show that our scheduler framework outperforms representative scheduling schemes by more than 20% in terms of average JCT, and is adaptive to various machine learning cluster topologies.  © 2004-2012 IEEE.

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
