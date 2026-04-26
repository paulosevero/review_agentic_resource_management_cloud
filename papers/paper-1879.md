---
id: "paper-1879"
title: "DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach"
authors: ["Liu, Zhang", "Du, Hongyang", "Lin, Junzhe", "Gao, Zhibin", "Huang, Lianfen", "Hosseinalipour, Seyyedali", "Niyato, Dusit"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2024.3486728"
url: "https://www.scopus.com/pages/publications/85208696098?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1945--1962"
keywords: ["deep reinforcement learning", "diffusion model", "DNN partitioning", "Lyapunov optimization", "resource allocation", "task offloading", "vehicular networks"]
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

# paper-1879 — DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach

## Metadata

- **Authors:** Liu, Zhang and Du, Hongyang and Lin, Junzhe and Gao, Zhibin and Huang, Lianfen and Hosseinalipour, Seyyedali and Niyato, Dusit
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2024.3486728
- **URL:** https://www.scopus.com/pages/publications/85208696098?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1945--1962
- **Language:** English
- **Keywords:** deep reinforcement learning; diffusion model; DNN partitioning; Lyapunov optimization; resource allocation; task offloading; vehicular networks

### Abstract

The rapid advancement of Artificial Intelligence (AI) has introduced Deep Neural Network (DNN)-based tasks to the ecosystem of vehicular networks. These tasks are often computation-intensive, requiring substantial computation resources, which are beyond the capability of a single vehicle. To address this challenge, Vehicular Edge Computing (VEC) has emerged as a solution, offering computing services for DNN-based tasks through resource pooling via Vehicle-to-Vehicle/Infrastructure (V2V/V2I) communications. In this paper, we formulate the problem of joint DNN partitioning, task offloading, and resource allocation in VEC as a dynamic long-term optimization. Our objective is to minimize the DNN-based task completion time while guaranteeing the system stability over time. To this end, we first leverage a Lyapunov optimization technique to decouple the original long-term optimization with stability constraints into a per-slot deterministic problem. Afterwards, we propose a Multi-Agent Diffusion-based Deep Reinforcement Learning (MAD2RL) algorithm, incorporating the innovative use of diffusion models to determine the optimal DNN partitioning and task offloading decisions. Furthermore, we integrate convex optimization techniques into MAD2RL as a subroutine to allocate computation resources, enhancing the learning efficiency. Through simulations under real-world movement traces of vehicles, we demonstrate the superior performance of our proposed algorithm compared to existing benchmark solutions. © 2024 IEEE.

## 04 — Title Screening

**Title:** DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
