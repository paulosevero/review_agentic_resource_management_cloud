---
id: "paper-1610"
title: "Generative diffusion model-based QMIX for joint task offloading and resource allocation in VEC systems"
authors: ["Guo, Liang", "Tham, Chen-Khong", "Jia, Jie", "Chen, Jian", "Wang, Xingwei"]
year: 2025
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2025.111516"
url: "https://www.scopus.com/pages/publications/105011204791?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Age of information (AoI)", "Generative diffusion model (GDM)", "Multi-agent deep reinforcement learning (MADRL)", "Vehicular edge computing (VEC)"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1610 — Generative diffusion model-based QMIX for joint task offloading and resource allocation in VEC systems

## Metadata

- **Authors:** Guo, Liang and Tham, Chen-Khong and Jia, Jie and Chen, Jian and Wang, Xingwei
- **Year:** 2025
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2025.111516
- **URL:** https://www.scopus.com/pages/publications/105011204791?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Age of information (AoI); Generative diffusion model (GDM); Multi-agent deep reinforcement learning (MADRL); Vehicular edge computing (VEC)

### Abstract

To cope with the high computing demand and latency requirements of emerging vehicular applications, vehicular edge computing (VEC) has been regarded as a promising computing paradigm that improves vehicular performance by introducing edge computation offloading for resource-constrained vehicles. Compared to the conventional delay metric, information freshness is more crucial for applications, such as automatic driving, auto navigation, etc., which can effectively avoid potential accidents caused by outdated data. Therefore, we apply the age of information (AoI) to measure the freshness of all vehicles’ tasks. Then, a long-term average AoI minimization problem is formulated by jointly optimizing the edge-cloud cooperation task offloading and resource allocation under time-varying environments. To solve this problem, we propose an optimization-oriented multi-agent deep reinforcement learning (MADRL) framework. Specifically, we propose a generative diffusion model (GDM)-based value function decomposition MADRL algorithm, named GDM-QMIX, to learn power allocation and offloading policies for multiple vehicle agents. Meanwhile, the closed-form solution of the wired transmission rate and computing resources allocation is derived based on Karush-Kuhn–Tucker (KKT) conditions to evaluate the quality of actions of GDM-QMIX, thereby avoiding a huge action space and achieving joint optimization. Simulation results demonstrate the effectiveness of the proposed algorithm in solving the dynamic task offloading and resource allocation problem and the superiority of the proposed algorithm over the benchmark schemes in terms of the average AoI. © 2025

## 04 — Title Screening

**Title:** Generative diffusion model-based QMIX for joint task offloading and resource allocation in VEC systems

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Generative diffusion model-based QMIX for joint task offloading and resource allocation in VEC systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Generative diffusion model-based QMIX for joint task offloading and resource allocation in VEC systems
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
