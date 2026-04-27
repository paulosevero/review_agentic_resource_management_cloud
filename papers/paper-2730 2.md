---
id: "paper-2730"
title: "An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants"
authors: ["Ni, Haochen", "Wang, Yonghua", "Tang, Xinfa", "Wang, Jingjing"]
year: 2026
venue: "Processes"
venue_type: "journal"
doi: "10.3390/pr14050743"
url: "https://www.scopus.com/pages/publications/105032755008?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["adaptive exploration", "carbon emission reduction", "deep reinforcement learning", "MEVPPs", "two-stage scheduling"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2730 — An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants

## Metadata

- **Authors:** Ni, Haochen and Wang, Yonghua and Tang, Xinfa and Wang, Jingjing
- **Year:** 2026
- **Venue:** Processes
- **DOI:** 10.3390/pr14050743
- **URL:** https://www.scopus.com/pages/publications/105032755008?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** adaptive exploration; carbon emission reduction; deep reinforcement learning; MEVPPs; two-stage scheduling

### Abstract

To address the challenge of coordinating economic and environmental objectives for Multi-energy Virtual Power Plants (MEVPPs), particularly under ambitious decarbonization policies such as China’s “dual carbon” goals, this paper proposes a novel two-stage scheduling framework that integrates Deep Reinforcement Learning (DRL) with Model Predictive Control (MPC). The core innovations include the following: (1) high-fidelity physical models capturing wind turbulence correction, photovoltaic temperature-irradiation coupling, and state-of-charge-dependent energy storage efficiency, improving equipment dynamic characterization accuracy by 12.7% compared to conventional models; (2) an enhanced Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm incorporating priority experience replay and adaptive noise exploration, which accelerates convergence by 15.6%; (3) a pioneering coordination architecture of “Day-Ahead MADDPG—Real-Time MPC” that manages uncertainties through bidirectional feedback, where real-time deviations refine the long-term policy via experience replay. Simulation results using historical data from a North China industrial park demonstrate that the framework reduces operating costs by 13.3% and carbon emissions by 17.7% compared to particle swarm optimization, outperforms standard DDPG with 3.2% lower operating costs, 5.8% lower carbon emissions, and a 3.3% higher renewable utilization rate (88.6%), and achieves 55% renewable penetration with only 4.1% curtailment. These results validate the framework’s scalability for high-renewable penetration grids and its real-time feasibility, as confirmed by edge computing deployment with latency below 50 ms. This study offers a technically viable and scalable solution for the operation of low-carbon virtual power plants (VPPs), supporting the transition towards sustainable power systems. © 2026 by the authors.

## 04 — Title Screening

**Title:** An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
