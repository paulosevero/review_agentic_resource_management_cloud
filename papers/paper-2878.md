---
id: "paper-2878"
title: "Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing"
authors: ["Yang, Lei", "Gan, Shuying", "Wang, Xijun", "Liu, Jing", "Chen, Xiang"]
year: 2026
venue: "Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST"
venue_type: "conference"
doi: "10.1007/978-3-032-14681-6_4"
url: "https://www.scopus.com/pages/publications/105030651417?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "41--52"
keywords: ["edge computing", "large language models", "reinforcement learning"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2878 — Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing

## Metadata

- **Authors:** Yang, Lei and Gan, Shuying and Wang, Xijun and Liu, Jing and Chen, Xiang
- **Year:** 2026
- **Venue:** Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
- **DOI:** 10.1007/978-3-032-14681-6_4
- **URL:** https://www.scopus.com/pages/publications/105030651417?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 41--52
- **Language:** English
- **Keywords:** edge computing; large language models; reinforcement learning

### Abstract

Large Language Models (LLMs) have revolutionized artificial intelligence, showcasing unprecedented capabilities across a wide range of tasks and significantly enhancing edge computing. However, deploying LLMs on edge devices presents challenges due to the distributed nature of users across edge nodes and the complexity of request types. To address these challenges, this paper first establishes an LLM inference model within an edge computing system and formulates an optimization problem aimed at maximizing the number of requests processed per unit time while satisfying user demands. To solve this problem, we model the system as a Semi-Markov Decision Process (SMDP) and employ reinforcement learning methods to propose the Dynamic Inference Separable Proximal Policy Optimization (DISPPO) algorithm. This algorithm dynamically adjusts the order of the prefill and decode stages. We evaluate the performance of DISPPO in edge-based LLM inference by comparing it with traditional inference methods. Simulation results demonstrate that DISPPO outperforms traditional methods in LLM inference scenarios. Additionally, we explore the algorithm’s performance across different batch sizes. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2026.

## 04 — Title Screening

**Title:** Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
