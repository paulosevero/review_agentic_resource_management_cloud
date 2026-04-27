---
id: "paper-2841"
title: "Multi-Agent Reinforcement Learning with Serverless Computing"
authors: ["Wei, Rui", "Yu, Hanfei", "Song, Xikang", "Li, Jian", "Tiwari, Devesh", "Mao, Ying", "Wang, Hao"]
year: 2026
venue: "SoCC 2025 - Proceedings of the 2025 ACM Symposium on Cloud Computing"
venue_type: "conference"
doi: "10.1145/3772052.3772227"
url: "https://www.scopus.com/pages/publications/105028609214?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "225--239"
keywords: ["Cloud Computing", "Multi-Agent Reinforcement Learning", "Serverless Computing"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2841 — Multi-Agent Reinforcement Learning with Serverless Computing

## Metadata

- **Authors:** Wei, Rui and Yu, Hanfei and Song, Xikang and Li, Jian and Tiwari, Devesh and Mao, Ying and Wang, Hao
- **Year:** 2026
- **Venue:** SoCC 2025 - Proceedings of the 2025 ACM Symposium on Cloud Computing
- **DOI:** 10.1145/3772052.3772227
- **URL:** https://www.scopus.com/pages/publications/105028609214?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 225--239
- **Language:** English
- **Keywords:** Cloud Computing; Multi-Agent Reinforcement Learning; Serverless Computing

### Abstract

Multi-agent reinforcement learning (MARL) has emerged as a promising approach for tasks requiring multiple agents for cooperation or competition, such as scientific simulation, multi-robot collaboration, and traffic control. Serverless computing, with its dynamic and flexible resource allocation, has demonstrated potential for improving training efficiency and cost-efficiency in RL workloads. However, existing serverless RL training systems focus primarily on single-agent scenarios, overlooking the unique characteristics and inherent complexities of MARL - such as dynamic inter-agent relationships and heterogeneous policy requirements across agents - leaving inefficient and even infeasible support to diverse and complex MARL algorithms.This paper introduces MARLess, the first serverless MARL framework designed to support general MARL algorithms. MARLess decomposes MARL algorithms into serverless functions. It further integrates a dynamic learner sharing mechanism that exploits agent similarities to reduce model update costs and employs actor scaling tailored to MARL tasks, minimizing unnecessary sampling costs based on the data requirements of agents' models. This design optimizes both training efficiency and costs without harming the training quality. Experiments on AWS EC2 testbeds show that MARLess outperforms SOTA MARL baselines with up to 1.27×faster training and 68% cost reduction. Large-scale evaluations on a 15-node cluster with a total of 1,920 vCPUs demonstrate MARLess's scalability and consistent performance under increasing workloads. For a real-world scientific application - turbulent flow simulation, MARLess achieves a 34% cost reduction and 1.1× speedup.  © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Multi-Agent Reinforcement Learning with Serverless Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning with Serverless Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning with Serverless Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
