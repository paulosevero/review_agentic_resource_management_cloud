---
id: "paper-865"
title: "OTAS: An Elastic Transformer Serving System via Token Adaptation"
authors: ["Chen, Jinyu", "Xu, Wenchao", "Hong, Zicong", "Guo, Song", "Wang, Haozhao", "Zhang, Jie", "Zeng, Deze"]
year: 2024
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM52122.2024.10621087"
url: "https://www.scopus.com/pages/publications/85201819755?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1021--1030"
keywords: ["cloud computing", "elastic computing", "model serving", "transformer"]
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

# paper-865 — OTAS: An Elastic Transformer Serving System via Token Adaptation

## Metadata

- **Authors:** Chen, Jinyu and Xu, Wenchao and Hong, Zicong and Guo, Song and Wang, Haozhao and Zhang, Jie and Zeng, Deze
- **Year:** 2024
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM52122.2024.10621087
- **URL:** https://www.scopus.com/pages/publications/85201819755?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1021--1030
- **Language:** English
- **Keywords:** cloud computing; elastic computing; model serving; transformer

### Abstract

Transformer model empowered architectures have become a pillar of cloud services that keeps reshaping our society. However, the dynamic query loads and heterogeneous user requirements severely challenge current transformer serving systems, which rely on pre-training multiple variants of a foundation model, i.e., with different sizes, to accommodate varying service demands. Unfortunately, such a mechanism is unsuitable for large transformer models due to the additional training costs and excessive I/O delay. In this paper, we introduce OTAS, the first elastic serving system specially tailored for transformer models by exploring lightweight token management. We develop a novel idea called token adaptation that adds prompting tokens to improve accuracy and removes redundant tokens to accelerate inference. To cope with fluctuating query loads and diverse user requests, we enhance OTAS with application-aware selective batching and online token adaptation. OTAS first batches incoming queries with similar service-level objectives to improve the ingress throughput. Then, to strike a tradeoff between the overhead of token increment and the potentials for accuracy improvement, OTAS adaptively adjusts the token execution strategy by solving an optimization problem. We implement and evaluate a prototype of OTAS with multiple datasets, which show that OTAS improves the system utility by at least 18.2%. © 2024 IEEE.

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
