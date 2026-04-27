---
id: "paper-972"
title: "SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference"
authors: ["Jiang, Peiwen", "Wang, Haoxin", "Cai, Zinuo", "Gao, Lintao", "Zhang, Weishan", "Ma, Ruhui", "Zhou, Xiaokang"]
year: 2024
venue: "IEEE Transactions on Computational Social Systems"
venue_type: "journal"
doi: "10.1109/TCSS.2024.3423749"
url: "https://www.scopus.com/pages/publications/85206387767?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "7941--7951"
keywords: ["Heterogeneous GPU clusters", "inference service", "large language models", "parallel algorithms"]
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

# paper-972 — SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference

## Metadata

- **Authors:** Jiang, Peiwen and Wang, Haoxin and Cai, Zinuo and Gao, Lintao and Zhang, Weishan and Ma, Ruhui and Zhou, Xiaokang
- **Year:** 2024
- **Venue:** IEEE Transactions on Computational Social Systems
- **DOI:** 10.1109/TCSS.2024.3423749
- **URL:** https://www.scopus.com/pages/publications/85206387767?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 7941--7951
- **Language:** English
- **Keywords:** Heterogeneous GPU clusters; inference service; large language models; parallel algorithms

### Abstract

Large language models (LLMs) are becoming powerful engines for social productivity in the manufacturing lifecycle. Existing application-level LLMs inference services focus on large datacenter and small edge intelligence (EI) scenarios, adopting iteration-level batch schedulers to solve resource utilization and inference speed problems. However, these services are incompatible with the scene of medium-sized local heterogeneous graphics processing unit (GPU) clusters with specific patterns, whose scale is between the two aforementioned scenarios. This type of scene proposes tradeoff problems for inference resource and speed, as well as user satisfaction problems for the semisparse frequency of queries with streaming responses. We propose suboptimal load balancing (SLoB), a distributed LLMs inference service scheduler in medium-sized local heterogeneous GPU clusters. SLoB leverages a multilevel adapter to accommodate LLMs usage patterns of scenes and balance resource utilization with inference efficiency. For semisparse problems, it adopts a mixed-priority pipeline scheduler with the least-padding principle to improve users' satisfaction, a metric considering the weights of different tokens in streaming responses. Based on the system prototype, our experiments under simulated workloads demonstrate that SLoB gains a maximum improvement of 29.4× under the satisfaction metric compared with the traditional run-to-completion scheduling solution while improving by up to 3.0× compared with the state-of-the-art (SOTA) solution Orca. © 2024 IEEE.

## 04 — Title Screening

**Title:** SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference
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
