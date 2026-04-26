---
id: "paper-2662"
title: "Exploring Image Similarity to Optimize Resource Provisioning in Container-Enabled Edge Computing"
authors: ["Li, Sisi", "Zhou, Ao", "Ma, Xiao", "Zhang, Yiran", "Wen, Jinfeng", "Wang, Shangguang"]
year: 2026
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2026.3668419"
url: "https://www.scopus.com/pages/publications/105031942629?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1234--1247"
keywords: ["Container", "edge computing", "resource provisioning", "service deployment"]
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

# paper-2662 — Exploring Image Similarity to Optimize Resource Provisioning in Container-Enabled Edge Computing

## Metadata

- **Authors:** Li, Sisi and Zhou, Ao and Ma, Xiao and Zhang, Yiran and Wen, Jinfeng and Wang, Shangguang
- **Year:** 2026
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2026.3668419
- **URL:** https://www.scopus.com/pages/publications/105031942629?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1234--1247
- **Language:** English
- **Keywords:** Container; edge computing; resource provisioning; service deployment

### Abstract

Containerization offers great flexibility and agility for resource provisioning in edge clouds. However, this benefit is not freely available, as substantial network traffic incurred by container image pulling heavily burdens the back-haul networks. Our in-depth measurements on 516.3 GB images from Docker Hub reveal that many similar images share identical layers, with only 11.21% having no shared layers. Building on this, we investigate the resource provisioning problem by leveraging image similarity to avoid repeated layer transmissions, aiming to reduce network traffic and improve overall performance. We formulate resource provisioning as a mixed-integer non-linear programming problem, which is challenging due to the coupling of four issues and their conflicting effects on overall performance, including offloading decisions, container instance deployment, image pulling, and resource allocation. To tackle these complexities, we propose a novel Similarity-Aware Resource Provisioning approach, which decomposes the problem into independent sub-problems using counterfactual multi-agent deep reinforcement learning and then solves sub-problems individually with convex optimization and fractional programming techniques. We conduct extensive evaluations with images from Docker Hub. The results show that our approach enables up to 32.6% traffic reduction and 19.9% utility improvement, outperforming the state-of-the-art solutions. © 2026 IEEE.

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
