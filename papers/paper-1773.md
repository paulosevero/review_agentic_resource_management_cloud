---
id: "paper-1773"
title: "A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing"
authors: ["Li, Jialiuyuan", "Shi, You", "Dai, Chen", "Yi, Changyan", "Yang, Yuxiao", "Zhai, Xiangping", "Zhu, Kun"]
year: 2025
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2025.3540964"
url: "https://www.scopus.com/pages/publications/85218714770?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "9717--9733"
keywords: ["energy efficiency", "game", "reinforcement learning", "space\u2013air\u2013ground integrated networks", "UAV"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1773 — A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing

## Metadata

- **Authors:** Li, Jialiuyuan and Shi, You and Dai, Chen and Yi, Changyan and Yang, Yuxiao and Zhai, Xiangping and Zhu, Kun
- **Year:** 2025
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2025.3540964
- **URL:** https://www.scopus.com/pages/publications/85218714770?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 9717--9733
- **Language:** English
- **Keywords:** energy efficiency; game; reinforcement learning; space–air–ground integrated networks; UAV

### Abstract

In this paper, we study the energy-efficient unmanned aerial vehicle (UAV) and low earth orbital (LEO) satellite assisted mobile edge computing (MEC) in space–air–ground integrated networks (SAGINs). The key challenge involves how to efficiently execute tasks offloaded from IoT devices, given limited on-board computation capabilities of UAVs and delay constraints of tasks. To address it, UAVs are first allowed to adjust their trajectories to accommodate as many tasks as possible from IoT devices. Subsequently, UAVs compute a portion of these tasks while delegating the rest to LEO satellites for further execution. Accordingly, we formulate a joint optimization problem including UAV trajectory planning, task offloading, and bandwidth allocations, aiming to maximize the long-term energy efficiency of UAVs and LEO satellites (i.e., the total data size in computation offloading divided by energy consumption of UAVs and LEO satellites). Considering the interactions among intelligent UAVs, this problem is reformulated as a set of interconnected multi-agent stochastic games, and the existence of corresponding Nash Equilibrium (NE) is theoretically proved. To obtain the NE, a multi-agent reinforcement learning-based algorithm, namely UTPTR, is developed concerning system dynamics and uncertainties. Simulations evaluate the performance of the UTPTR and demonstrate its superiority compared to existing approaches. © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing
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
