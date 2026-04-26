---
id: "paper-1090"
title: "Securing AI Inference in the Cloud: Is CPU-GPU Confidential Computing Ready?"
authors: ["Mohan, Apoorve", "Ye, Mengmei", "Franke, Hubertus", "Srivatsa, Mudhakar", "Liu, Zhuoran", "Gonzalez, Nelson Mimura"]
year: 2024
venue: "IEEE International Conference on Cloud Computing, CLOUD"
venue_type: "conference"
doi: "10.1109/CLOUD62652.2024.00028"
url: "https://www.scopus.com/pages/publications/85203256755?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "164--175"
keywords: ["cloud computing", "cloud security", "confidential computing", "foundation models", "high performance computing", "large language models"]
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

# paper-1090 — Securing AI Inference in the Cloud: Is CPU-GPU Confidential Computing Ready?

## Metadata

- **Authors:** Mohan, Apoorve and Ye, Mengmei and Franke, Hubertus and Srivatsa, Mudhakar and Liu, Zhuoran and Gonzalez, Nelson Mimura
- **Year:** 2024
- **Venue:** IEEE International Conference on Cloud Computing, CLOUD
- **DOI:** 10.1109/CLOUD62652.2024.00028
- **URL:** https://www.scopus.com/pages/publications/85203256755?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 164--175
- **Language:** English
- **Keywords:** cloud computing; cloud security; confidential computing; foundation models; high performance computing; large language models

### Abstract

Many applications have been offloaded onto cloud environments to achieve higher agility, access to more powerful computational resources, and obtain better infrastructure management. Although cloud environments provide solid security solutions, users with highly sensitive data or regulatory compliance requirements, such as HIPAA (Health Insurance Portability and Accountability Act) and GDPR (General Data Protection Regulation), still hesitate to move such application domains to the cloud. To address these concerns, cloud service providers have started to offer solutions to protect data confidentiality and integrity through trusted execution environments (TEEs). While so far these were limited to CPU TEEs only, NVIDIA's Hopper architecture has shifted the landscape by enabling confidential computing features essential to protecting confidentiality and integrity for real-world applications offloaded to GPUs, such as large language models (LLMs). However, there lacks a sufficient study on how much performance overhead confidential computing introduces in a TEE comprised of a CPU-GPU configuration. In this paper we evaluate a confidential computing environment comprised of an Intel TDX system and NVIDIA H100 GPUs through various micro benchmarks and real workloads including BERT, LLaMA, and Granite large language models and provide discussions on the overhead incurred by confidential computing when GPUs are utilized. We show that while LLMs are sensitive to the model types and batch sizes, when larger models with pipelined processing are deployed, the performance of LLM inference in CPU-GPU TEEs can be close to par with their non-confidential setups.  © 2024 IEEE.

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
