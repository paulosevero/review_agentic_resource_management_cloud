---
id: "paper-1802"
title: "Integrated and Fungible Scheduling of Deep Learning Workloads Using Multi-Agent Reinforcement Learning"
authors: ["Li, Jialun", "Xiao, Danyang", "Yang, Diying", "Mo, Xuan", "Wu, Weigang"]
year: 2025
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2024.3522333"
url: "https://www.scopus.com/pages/publications/85213277622?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "391--406"
keywords: ["deep learning workload", "GPU cluster", "MARL", "MLaaS", "task scheduling"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: ""
    human_justification: ""

---

# paper-1802 — Integrated and Fungible Scheduling of Deep Learning Workloads Using Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Li, Jialun and Xiao, Danyang and Yang, Diying and Mo, Xuan and Wu, Weigang
- **Year:** 2025
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2024.3522333
- **URL:** https://www.scopus.com/pages/publications/85213277622?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 391--406
- **Language:** English
- **Keywords:** deep learning workload; GPU cluster; MARL; MLaaS; task scheduling

### Abstract

—GPU clusters have been widely used to co-locate various deep learning (DL) workloads in a multi-tenant way. Although such resource sharing can significantly reduce training cost, resource contention and interference among co-located workloads make task scheduling very complex and challenging. To simplify the scheduling problem, existing algorithms usually divide the procedure of scheduling into two sub-tasks, i.e., task placement and resource allocation, and allocate resources according to pre-defined and fixed resource demands. However, such a paradigm significantly constrains the selection of potential scheduling solutions. In this article, we present MAIFS, a novel multi-agent reinforcement learning based scheduling algorithm that handles task placement and resource allocation integratedly, and allows fungible resource allocation based on resource sensitivity of DL workloads. The core of MAIFS lies in two mechanisms. The multi-agent attention mechanism is designed to learn and share inter-related resource state features observed from different agents, which enables agents to explore fungible resource allocation solutions. The dynamic coordination graph mechanism is designed for coordinating interactive task placement decisions of agents during integrated scheduling, so as to mitigate potential task conflicts. Simulated experiments using two large scale production DL workload traces and physical deployment experiments based on a Kubernetes based GPU cluster show that MAIFS can outperform state-of-the-art scheduling algorithms by up to 44% in terms of makespan and 46% in terms of job completion time (JCT). © 2025 IEEE Computer Society. All rights reserved.

## 04 — Title Screening

**Title:** Integrated and Fungible Scheduling of Deep Learning Workloads Using Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Integrated and Fungible Scheduling of Deep Learning Workloads Using Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Integrated and Fungible Scheduling of Deep Learning Workloads Using Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
