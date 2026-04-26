---
id: "paper-1089"
title: "SpotServe: Serving Generative Large Language Models on Preemptible Instances"
authors: ["Miao, Xupeng", "Shi, Chunan", "Duan, Jiangfei", "Xi, Xiaoli", "Lin, Dahua", "Cui, Bin", "Jia, Zhihao"]
year: 2024
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3620665.3640411"
url: "https://www.scopus.com/pages/publications/85181495776?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "1112--1127"
keywords: ["cloud computing", "large language model serving", "preemptible instances"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-1089 — SpotServe: Serving Generative Large Language Models on Preemptible Instances

## Metadata

- **Authors:** Miao, Xupeng and Shi, Chunan and Duan, Jiangfei and Xi, Xiaoli and Lin, Dahua and Cui, Bin and Jia, Zhihao
- **Year:** 2024
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3620665.3640411
- **URL:** https://www.scopus.com/pages/publications/85181495776?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 1112--1127
- **Language:** English
- **Keywords:** cloud computing; large language model serving; preemptible instances

### Abstract

The high computational and memory requirements of generative large language models (LLMs) make it challenging to serve them cheaply. This paper aims to reduce the monetary cost for serving LLMs by leveraging preemptible GPU instances on modern clouds, which offer accesses to spare GPU resources at a much cheaper price than regular instances but may be preempted by the cloud provider at any time. Serving LLMs on preemptible instances requires addressing challenges induced by frequent instance preemptions and the necessity of migrating instances to handle the preemptions.This paper presents SpotServe, the first distributed LLM serving system on preemptible instances. Several key techniques of SpotServe realize fast and reliable serving of generative LLMs on cheap preemptible instances. First, SpotServe dynamically adapts the LLM parallelization configuration for dynamic instance availability and fluctuating workload, while balancing the trade-off among the overall throughput, inference latency and monetary costs. Second, to minimize the cost of migrating instances for dynamic reparallelization, the task of migrating instances is formulated as a bipartite graph matching problem in SpotServe, which uses the Kuhn-Munkres algorithm to identify an optimal migration plan that minimizes communication cost. Finally, to take advantage of the grace period offered by modern cloud platforms, we introduce stateful inference recovery, a new inference mechanism that commits inference progress at a much finer granularity and allows SpotServe to cheaply resume inference upon preemption. We evaluate SpotServe on real spot instance preemption traces and various popular LLMs and show that SpotServe can reduce the P99 tail latency by 2.4 - 9.1× compared with the best existing LLM serving systems. We also show that SpotServe can leverage the price advantage of preemptive instances, saving 54% monetary cost compared with only using on-demand instances. The code is publicly available at: https://github.com/Hsword/SpotServe. © 2024 Association for Computing Machinery. All rights reserved.

## 04 — Title Screening

**Title:** SpotServe: Serving Generative Large Language Models on Preemptible Instances

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SpotServe: Serving Generative Large Language Models on Preemptible Instances
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SpotServe: Serving Generative Large Language Models on Preemptible Instances
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
