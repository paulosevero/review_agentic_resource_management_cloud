---
id: "paper-2840"
title: "UniOrch: A Unified Mixed Framework for High-Efficiency LLM Training on Heterogeneous AI Chips"
authors: ["Wang, Jingyi", "Wang, Jia", "Gao, Jun", "Cao, Yan", "Zhai, Yang", "Wang, Haojie", "Song, Wanxin", "Kong, Dezhi", "Liu, Liu", "Li, Wei", "He, Zhaofeng"]
year: 2026
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2026.3668647"
url: "https://www.scopus.com/pages/publications/105031591900?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["AI Chips", "Data Centers", "Distributed Training", "Energy Efficiency", "Heterogeneous Computing", "Large Language Models"]
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

# paper-2840 — UniOrch: A Unified Mixed Framework for High-Efficiency LLM Training on Heterogeneous AI Chips

## Metadata

- **Authors:** Wang, Jingyi and Wang, Jia and Gao, Jun and Cao, Yan and Zhai, Yang and Wang, Haojie and Song, Wanxin and Kong, Dezhi and Liu, Liu and Li, Wei and He, Zhaofeng
- **Year:** 2026
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2026.3668647
- **URL:** https://www.scopus.com/pages/publications/105031591900?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** AI Chips; Data Centers; Distributed Training; Energy Efficiency; Heterogeneous Computing; Large Language Models

### Abstract

Efficient coordination of heterogeneous AI chips (GPU/NPU/DCU) in data centers is crucial for Large Language Model (LLM) training, but this process is hindered by architectural mismatches, protocol fragmentation, and network partitioning. Existing solutions fail to achieve unified resource management across different chips, resulting in severe resource fragmentation and reduced allreduce efficiency. To overcome these limitations, this paper proposes the unified coordination framework UniOrch, which not only integrates three core functionalities, including hardware abstraction, software standardization, and communication coordination, but also enables the training and inference of large models across heterogeneous AI chips. UniOrch's hardware-agnostic bare-metal cloud eliminates virtualization overhead through Border Gateway Protocol Ethernet Virtual Private Network (BGP EVPN) overlay networks and gateway-based chip integration; its PyTorch-based adaptation layer masks hardware differences and reduces migration costs; the Transformer Collective Communication Library (TCCL) unifies NCCL, HCCL, and OpenMPI protocols to support seamless hybrid parallel training. Furthermore, the framework ’ s core scheduling mechanism is the Heterogeneous Hybrid Estimation Model (HHEM), which employs a twostage cost model combining static analysis with dynamic runtime feedback to dynamically allocate computing power based on Transformer task loads, ensuring cross-chip task synchronization, resource pooling, and dynamic allocation. Deployment verification in real-world production environments (e.g., China Construction Bank) shows that UniOrch achieves significant improvements: resource utilization of heterogeneous AI infrastructure is increased by 35%, cross-chip latency is reduced by 42%, accuracy loss in heterogeneous environments is <1.5%, the GLM-130B model achieves near-linear scalability across heterogeneous AI chips (with 116.7 tokens processed per card per second). Notably, it realizes the first cross-vendor LLM training on diversified hybrid NPU-GPU clusters with convergence error <0.8%. © 1990-2012 IEEE.

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
