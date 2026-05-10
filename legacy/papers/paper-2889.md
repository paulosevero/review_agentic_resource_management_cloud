---
id: "paper-2889"
title: "Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks"
authors: ["Yin, Fangfang", "Liu, Qihong", "Liu, Danpu", "Jin, Libiao", "Li, Shufeng"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3628965"
url: "https://www.scopus.com/pages/publications/105020879353?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1440--1459"
keywords: ["Multiaccess edge computing (MEC)", "multiagent deep reinforcement learning (MADRL)", "resource allocation", "satellite\u2013terrestrial integrated networks (STINs)"]
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

# paper-2889 — Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks

## Metadata

- **Authors:** Yin, Fangfang and Liu, Qihong and Liu, Danpu and Jin, Libiao and Li, Shufeng
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3628965
- **URL:** https://www.scopus.com/pages/publications/105020879353?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1440--1459
- **Language:** English
- **Keywords:** Multiaccess edge computing (MEC); multiagent deep reinforcement learning (MADRL); resource allocation; satellite–terrestrial integrated networks (STINs)

### Abstract

This article investigates the mixed-timescale resource allocation problem in satellite–terrestrial integrated networks (STINs). Moreover, the multiaccess edge computing (MEC) technology and millimeter wave (mmWave) with rich spectrum resource are merged into the STIN to improve the network performance. A network utility maximization problem characterized by the achievable rate and backhaul reduction is formulated under the constraints of the maximum caching capacity, transmission power of mmWave small-cell base stations (SBSs) and quality of service (QoS) for Internet of Things (IoT) devices, where the caching placement, power allocation, and user-SBS association are jointly optimized. In order to tackle this mixed-integer nonlinear programming (MINLP) problem, we decompose the original problem into the long-term caching placement subproblem, and short-term power allocation and user-SBS association subproblems. Then, a multiagent deep reinforcement learning (MADRL)-based independent proximal policy optimization (IPPO) algorithm is proposed to solve the short-term user-SBS association subproblem. Meanwhile, the linear programming (LP) is used to solve the long-term caching placement subproblem. Furthermore, we derive the closed-form solution of the short-term power allocation subproblem through the Karush–Kuhn–Tucker (KKT) conditions. Simulation results are carried out to validate the effectiveness and scalability of the proposed joint approach. © 2014 IEEE.

## 04 — Title Screening

**Title:** Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks
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
