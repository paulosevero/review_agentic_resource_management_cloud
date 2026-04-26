---
id: "paper-2057"
title: "Tri-AFLLM: Resource-Efficient Adaptive Asynchronous Accelerated Federated LLMs"
authors: ["Qiao, Dewen", "Ao, Xiang", "Liu, Yu", "Chen, Xuetao", "Song, Fuyuan", "Qin, Zheng", "Jin, Wenqiang"]
year: 2025
venue: "IEEE Transactions on Circuits and Systems for Video Technology"
venue_type: "journal"
doi: "10.1109/TCSVT.2024.3519790"
url: "https://www.scopus.com/pages/publications/85212758037?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4198--4211"
keywords: ["edge intelligence", "Federated learning", "large language models", "momentum gradient descent", "resource efficiency"]
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

# paper-2057 — Tri-AFLLM: Resource-Efficient Adaptive Asynchronous Accelerated Federated LLMs

## Metadata

- **Authors:** Qiao, Dewen and Ao, Xiang and Liu, Yu and Chen, Xuetao and Song, Fuyuan and Qin, Zheng and Jin, Wenqiang
- **Year:** 2025
- **Venue:** IEEE Transactions on Circuits and Systems for Video Technology
- **DOI:** 10.1109/TCSVT.2024.3519790
- **URL:** https://www.scopus.com/pages/publications/85212758037?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4198--4211
- **Language:** English
- **Keywords:** edge intelligence; Federated learning; large language models; momentum gradient descent; resource efficiency

### Abstract

The local deployment of federated large language models (FLLM) has further advanced the development of edge intelligence. However, the resource constraints of end devices, device heterogeneity, and the non-independent and identically distributed (Non-IID) nature of data pose significant challenges to the application of FLLM. To address this issue, we propose an Adaptive Asynchronous Accelerated FLLM (Tri-AFLLM) algorithm to achieve the efficient utilization of limited resources and improve model accuracy in the edge computing (EC) scenarios. Specifically, Tri-AFLLM first ships an off-the-shelf LLM, i.e., CLIP, to each end device, keeping the backbone parameters frozen and updating only the parameters of the adapter containing two linear transformation layers by using momentum gradient descent (MGD). Next, a toy example is provided to illustrate the necessity of using different numbers of local iterations for heterogeneous devices in resource-constrained environments. Subsequently, the convergence bound of the Tri-AFLLM under a given resource budget is discussed. Then, we formulated the bound into a resource consumption minimization problem with the number of local iterations as the optimization variable under a given model accuracy to mitigate the contribution disparity of local models to the global aggregation. Finally, extensive experiments are conducted to validate the superiority of Tri-AFLLM in terms of resource consumption, model accuracy, and addressing the Non-IID problem. © 1991-2012 IEEE.

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
