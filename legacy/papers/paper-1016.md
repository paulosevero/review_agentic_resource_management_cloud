---
id: "paper-1016"
title: "Deep reinforcement learning based trajectory design and resource allocation for task-aware multi-UAV enabled MEC networks"
authors: ["Li, Zewu", "Xu, Chen", "Zhang, Zhanpeng", "Wu, Runze"]
year: 2024
venue: "Computer Communications"
venue_type: "journal"
doi: "10.1016/j.comcom.2023.11.006"
url: "https://www.scopus.com/pages/publications/85176124855?origin=resultslist"
publisher: "Elsevier B.V."
pages: "88--98"
keywords: ["Cooperative computing", "Deep reinforcement learning", "Resource allocation", "Trajectory design", "UAV"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1016 — Deep reinforcement learning based trajectory design and resource allocation for task-aware multi-UAV enabled MEC networks

## Metadata

- **Authors:** Li, Zewu and Xu, Chen and Zhang, Zhanpeng and Wu, Runze
- **Year:** 2024
- **Venue:** Computer Communications
- **DOI:** 10.1016/j.comcom.2023.11.006
- **URL:** https://www.scopus.com/pages/publications/85176124855?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 88--98
- **Language:** English
- **Keywords:** Cooperative computing; Deep reinforcement learning; Resource allocation; Trajectory design; UAV

### Abstract

Computing tasks in the air is an important form of mobile edge computing (MEC) to improve the quality of service and enhance network coverage. In this paper, we investigate a multi-UAV cooperative computing model and massive devices access scenario in a service area without infrastructure. There are various types of ground devices with different tasks. Moreover, we consider that the UAV executing tasks of devices need to cache the content that task required. Therefore, we propose a multi-UAV enabled MEC network based on task awareness where each UAV caches some programs to execute tasks offloaded from devices. To minimize completion time, a joint UAV trajectory design, access decision and resource allocation problem is formulated. To address this intractable mixed integer non-linear programming problem, a multi-agent trajectory design and resource allocation (MATR) algorithm is proposed, where the multi-agent deep deterministic policy gradient (MADDPG) is applied. Considering the complexity of high-dimensional continuous action space, we introduce the particle swarm optimization (PSO) algorithm to jointly optimize access decisions, and computation resource allocation to reduce action space. In addition, we discuss the impact of the size of UAV cache space and the location of ground devices on the completion time. Simulation results show that the MATR algorithm can significantly reduce the completion time compared to the baselines. © 2023 Elsevier B.V.

## 04 — Title Screening

**Title:** Deep reinforcement learning based trajectory design and resource allocation for task-aware multi-UAV enabled MEC networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep reinforcement learning based trajectory design and resource allocation for task-aware multi-UAV enabled MEC networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep reinforcement learning based trajectory design and resource allocation for task-aware multi-UAV enabled MEC networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
