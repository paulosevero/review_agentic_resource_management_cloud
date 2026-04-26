---
id: "paper-2813"
title: "DP-Prox: A Robust and Differentially Private Framework for Federated Instruction Tuning of Small LLMs on 8 GB Edge Devices"
authors: ["Venkatesh, Vinay", "Liu, Yichen"]
year: 2026
venue: "2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026"
venue_type: "conference"
doi: "10.1109/CCWC67433.2026.11393831"
url: "https://www.scopus.com/pages/publications/105035589499?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "620--626"
keywords: ["Differential Privacy", "Edge Computing", "Fed-Prox", "Federated Learning", "Instruction Tuning", "IoT", "Phi-3", "QLoRA"]
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

# paper-2813 — DP-Prox: A Robust and Differentially Private Framework for Federated Instruction Tuning of Small LLMs on 8 GB Edge Devices

## Metadata

- **Authors:** Venkatesh, Vinay and Liu, Yichen
- **Year:** 2026
- **Venue:** 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
- **DOI:** 10.1109/CCWC67433.2026.11393831
- **URL:** https://www.scopus.com/pages/publications/105035589499?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 620--626
- **Language:** English
- **Keywords:** Differential Privacy; Edge Computing; Fed-Prox; Federated Learning; Instruction Tuning; IoT; Phi-3; QLoRA

### Abstract

This paper introduces DP-Prox, an end-to-end framework for robust and differentially private federated instruction tuning of small Large Language Models (LLMs) on 8 GB edge devices. DP-Prox is instantiated using the 3.8 billionparameter Phi-3-mini model with 4-bit Quantized Low-Rank Adaptation (QLoRA), and combines (i) FedProx-style proximal regularization on low-rank adapters to stabilize optimization under highly Non-IID smart-home data, and (ii) Differentially Private SGD (DP-SGD) applied directly to adapter gradients to provide user-level (ϵ, δ) -differential privacy against an honest-but-curious server. In a realistic IoT instruction-following benchmark with Dirichlet-skewed clients (α=0.3), DP-Prox improves F1-score from 0.80 (Edge-FIT with FedAvg) to 0.82 while reducing convergence rounds from T=50 to T ≈ 40. Under a strict privacy budget (ϵ=5, δ=10<sup>-5</sup>), DP-Prox maintains an F1-score of 0.77 with only +15%-20% local overhead, and preserves the communication efficiency of QLoRA-based federated training. Qualitative analyses further show that DP-Prox yields more consistent instruction-following behavior across heterogeneous homes, especially on multi-device routines and privacy-sensitive queries. Together, these results position DP-Prox as a practical and regulation-ready blueprint for deploying small, edge-resident LLMs in smart-home IoT environments. © 2026 IEEE.

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
