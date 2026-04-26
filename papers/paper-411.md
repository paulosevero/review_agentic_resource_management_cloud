---
id: "paper-411"
title: "Titan: A Scheduler for Foundation Model Fine-tuning Workloads"
authors: ["Gao, Wei", "Sun, Peng", "Wen, Yonggang", "Zhang, Tianwei"]
year: 2022
venue: "SoCC 2022 - Proceedings of the 13th Symposium on Cloud Computing"
venue_type: "conference"
doi: "10.1145/3542929.3563460"
url: "https://www.scopus.com/pages/publications/85143255760?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "348--354"
keywords: ["cluster management system", "deep learning training", "foundation models", "GPU datacenter"]
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

# paper-411 — Titan: A Scheduler for Foundation Model Fine-tuning Workloads

## Metadata

- **Authors:** Gao, Wei and Sun, Peng and Wen, Yonggang and Zhang, Tianwei
- **Year:** 2022
- **Venue:** SoCC 2022 - Proceedings of the 13th Symposium on Cloud Computing
- **DOI:** 10.1145/3542929.3563460
- **URL:** https://www.scopus.com/pages/publications/85143255760?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 348--354
- **Language:** English
- **Keywords:** cluster management system; deep learning training; foundation models; GPU datacenter

### Abstract

The recent breakthrough of foundation model (FM) research raises a new trend to acquire efficient DL models by fine-tuning FMs with low-resource datasets. Current GPU clusters are mainly established to develop DL models by training from scratch. How to tailor a GPU cluster scheduler for FM fine-tuning workloads is still not explored. We propose Titan, a scheduler to improve the efficiency of FM fine-tuning workloads based on their three distinct features. (1) It takes full advantage of the fixed model structure to estimate the job duration accurately and configure the fine-tuning workload efficiently. (2) The multi-task adaptivity of FMs enables multiple fine-tuning workloads to share the same model parameters, which can significantly reduce the GPU resource consumption. (3) It considers the pipeline parallelism of FM fine-tuning workloads and concurrently executes the parameter transmission and gradient computation to hide the overhead of context switch. Preliminary simulation result validates the efficiency of Titan.  © 2022 Owner/Author.

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
