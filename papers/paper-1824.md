---
id: "paper-1824"
title: "SimpleScale: Simplifying the Training of an LLM Model Using 1024 GPUs"
authors: ["Li, Tianfa", "Pan, Jingshan", "Ma, Siwei", "Raikov, Aleksandr", "Arkhipov, Alexander"]
year: 2025
venue: "Applied Sciences (Switzerland)"
venue_type: "journal"
doi: "10.3390/app15158265"
url: "https://www.scopus.com/pages/publications/105013195766?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["dynamic hybrid shared strategy", "flash attention", "FSDP", "Slurm", "training"]
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

# paper-1824 — SimpleScale: Simplifying the Training of an LLM Model Using 1024 GPUs

## Metadata

- **Authors:** Li, Tianfa and Pan, Jingshan and Ma, Siwei and Raikov, Aleksandr and Arkhipov, Alexander
- **Year:** 2025
- **Venue:** Applied Sciences (Switzerland)
- **DOI:** 10.3390/app15158265
- **URL:** https://www.scopus.com/pages/publications/105013195766?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** dynamic hybrid shared strategy; flash attention; FSDP; Slurm; training

### Abstract

LLMs are trained using many thousands of GPUs in well-known conventional models. It is necessary to address numerous issues in the training process, such as manual data collection organization, data parallel, model parallel, evaluation, testing, deployment, transferring large data streams, detecting errors, ongoing maintenance, and project management. A team of dozens of engineers is required to handle system problems in the training process. Therefore, it is time-consuming and expensive to build an efficient and fault-tolerant system based on Kubernetes. This paper develops SimpleScale for building LLMs based on FSDP and Slurm, which is a simple and efficient training system that includes the training agent, the efficient parallel strategy, the optimal step of checkpoint, and so on. Using the proposed system enables us to significantly accelerate the process of building the LLM without incurring substantial time spent on various manual issues. The proposed 1024-GPU cluster was tested on TinyLlama, which has 1.1 billion parameters and 300 billion tokens. For example, utilizing a 16-H100 GPU cluster accelerated the traditional TinyLlama training time costs from 89.05 days to 39.05 days. In the future, the project team plans to integrate Flash-Attention3, aiming for an MFU of more than 60% while maintaining the acceleration achieved in the present work. © 2025 by the authors.

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
