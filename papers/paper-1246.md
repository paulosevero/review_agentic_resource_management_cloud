---
id: "paper-1246"
title: "FaaSConf: QoS-aware Hybrid Resources Configuration for Serverless Workflows"
authors: ["Wang, Yilun", "Chen, Pengfei", "Dou, Hui", "Zhang, Yiwen", "Yu, Guangba", "He, Zilong", "Huang, Haiyu"]
year: 2024
venue: "Proceedings - 2024 39th ACM/IEEE International Conference on Automated Software Engineering, ASE 2024"
venue_type: "conference"
doi: "10.1145/3691620.3695477"
url: "https://www.scopus.com/pages/publications/85212438715?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "957--969"
keywords: ["configuration tuning", "MARL", "serverless computing"]
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

# paper-1246 — FaaSConf: QoS-aware Hybrid Resources Configuration for Serverless Workflows

## Metadata

- **Authors:** Wang, Yilun and Chen, Pengfei and Dou, Hui and Zhang, Yiwen and Yu, Guangba and He, Zilong and Huang, Haiyu
- **Year:** 2024
- **Venue:** Proceedings - 2024 39th ACM/IEEE International Conference on Automated Software Engineering, ASE 2024
- **DOI:** 10.1145/3691620.3695477
- **URL:** https://www.scopus.com/pages/publications/85212438715?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 957--969
- **Language:** English
- **Keywords:** configuration tuning; MARL; serverless computing

### Abstract

Serverless computing, also known as Function-as-a-Service (FaaS), is a significant development trend in modern software system architecture. The workflow composition of multiple short-lived functions has emerged as a prominent pattern in FaaS, exposing a considerable resources configuration challenge compared to individual independent serverless functions. This challenge unfolds in two ways. Firstly, workflows frequently encounter dynamic and concurrent user workloads, increasing the risk of QoS violations. Secondly, the performance of a function can be affected by the resource reprovision of other functions within the workflow.With the popularity of the mode of concurrent processing in one single instance, concurrency limit as a critical configuration parameter imposes restrictions on the capacity of requests per instance. In this study, we present FaaSConf, a QoS-aware hybrid resource configuration approach that uses multi-agent reinforcement learning (MARL) to configure hybrid resources, including hardware resources and concurrency, thereby ensuring end-to-end QoS while minimizing resource costs. To enhance decision-making, we employ an attention technique in MARL to capture the complex performance dependencies between functions. We further propose a safe exploration strategy to mitigate QoS violations, resulting in a safer and efficient configuration exploration. The experimental results demonstrate that FaaSConf outperforms state-of-the-art approaches significantly. On average, it achieves a 26.5% cost reduction while exhibiting robustness to dynamic load changes. © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

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
