---
id: "paper-1011"
title: "CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices"
authors: ["Li, Jinrong", "Han, Biao", "Li, Sudan", "Wang, Xiaoyan", "Li, Jie"]
year: 2024
venue: "2024 IEEE/CIC International Conference on Communications in China, ICCC 2024"
venue_type: "conference"
doi: "10.1109/ICCC62479.2024.10681712"
url: "https://www.scopus.com/pages/publications/85206484279?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "185--190"
keywords: ["collaborative inference", "large language model", "resource-constrained"]
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

# paper-1011 — CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices

## Metadata

- **Authors:** Li, Jinrong and Han, Biao and Li, Sudan and Wang, Xiaoyan and Li, Jie
- **Year:** 2024
- **Venue:** 2024 IEEE/CIC International Conference on Communications in China, ICCC 2024
- **DOI:** 10.1109/ICCC62479.2024.10681712
- **URL:** https://www.scopus.com/pages/publications/85206484279?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 185--190
- **Language:** English
- **Keywords:** collaborative inference; large language model; resource-constrained

### Abstract

Over the past few years, there has been notable advancement in Large Language Models (LLMs), leading to their extensive utilisation across various domains. Running large-scale LLMs usually necessitates processing capacity at the level of data-centers, which deters numerous potential applications from researchers. However, certain applications with great potential in LLM, such as the Internet of Things(IoT) data analysis and multi-robot collaboration, are typically constrained by lack of resources, specifically graphics processing units(GPUs). As a result, these devices fail to execute LLM inference. To tackle the aforementioned issues, we first investigate the problem of 'Compute Bound' in devices with constrained resources, which are unavailable for hierarchical partitioning models. Furthermore, utilising the LLM tensor parallelization, we present a collaborative LLM inference framework on resource-constrained devices called CoLLM. In addition, we propose a minimal latency algorithm and an adaptive load balancing algorithm to optimize inference latency and balance energy consumption. (1) By considering the LLM model's size, device resources, and network conditions, we can calculate the optimum number of collaborative devices to minimise inference latency. (2) CoLLM is capable of dynamically distributing computational workloads based on the target device's status, balancing power consumption to extend overall working time. Experiments are conducted when the Llama2 model is executed on GPU-free devices such as Raspberry Pis. Evaluation results show that end-to-end inference speed outperforms current hierarchical LLM inference methods by a factor of 1.9 x-2.3 x. © 2024 IEEE.

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
