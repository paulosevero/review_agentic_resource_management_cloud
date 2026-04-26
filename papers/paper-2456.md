---
id: "paper-2456"
title: "Split Fine-Tuning for Large Language Models in Wireless Networks"
authors: ["Zhang, Songge", "Cheng, Guoliang", "Wu, Wen", "Huang, Xinyu", "Song, Lingyang", "Shen, Xuemin"]
year: 2025
venue: "IEEE Journal on Selected Topics in Signal Processing"
venue_type: "journal"
doi: "10.1109/JSTSP.2025.3581484"
url: "https://www.scopus.com/pages/publications/105008922887?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1376--1391"
keywords: ["fine-tuning", "Large language models", "resource management", "split learning"]
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

# paper-2456 — Split Fine-Tuning for Large Language Models in Wireless Networks

## Metadata

- **Authors:** Zhang, Songge and Cheng, Guoliang and Wu, Wen and Huang, Xinyu and Song, Lingyang and Shen, Xuemin
- **Year:** 2025
- **Venue:** IEEE Journal on Selected Topics in Signal Processing
- **DOI:** 10.1109/JSTSP.2025.3581484
- **URL:** https://www.scopus.com/pages/publications/105008922887?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1376--1391
- **Language:** English
- **Keywords:** fine-tuning; Large language models; resource management; split learning

### Abstract

Fine-tuning is the process of adapting the pre-trained large language models (LLMs) for downstream tasks. Due to substantial model parameters, fine-tuning LLM on mobile devices demands considerable memory resources, and suffers from high communication overhead and fine-tuning delay. In this paper, we propose an efficient LLM fine-tuning scheme in wireless networks, named Split Fine-Tuning (SFT), which can accommodate LLM fine-tuning on mobile devices. Specifically, an LLM is split into a server-side part on the edge server and a device-side part on the mobile device to satisfy the device-side memory constraint. All devices share a server-side model and perform parallel fine-tuning to reduce fine-tuning delay. In addition, to reduce communication overhead incurred by data exchange between devices and the edge server, we propose an activation data compression scheme by jointly leveraging sparsification, stochastic quantization, and lossless encoding methods. Furthermore, we formulate a fine-tuning delay minimization problem under model accuracy and device-side memory constraints, taking device heterogeneity and channel dynamics into account. To solve the problem, the nonlinear mixed-integer problem is decoupled into two subproblems in different timescales. A two-timescale resource management algorithm is proposed to jointly optimize the compression rate and transformer block allocation in the large timescale using the augmented Lagrangian method, and determine spectrum resource allocation in the small timescale via sequential quadratic programming. Extensive simulation results demonstrate that the proposed scheme can reduce the fine-tuning delay by up to 66.4% and communication overhead by 93.6% compared to state-of-the-art benchmarks, while satisfying device-side memory and model accuracy constraints. © 2007-2012 IEEE.

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
