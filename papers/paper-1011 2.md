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
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

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

**Title:** CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
