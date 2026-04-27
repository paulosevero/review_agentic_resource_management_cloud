---
id: "paper-2197"
title: "Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning"
authors: ["Tan, Ling", "Song, Jing", "Sun, Lei", "Wang, Haifeng", "Xu, Hai"]
year: 2025
venue: "Physical Communication"
venue_type: "journal"
doi: "10.1016/j.phycom.2025.102916"
url: "https://www.scopus.com/pages/publications/105021850374?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["DPTL inspection network", "Edge computing", "Load balancing", "Multi-agent reinforcement learning"]
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

# paper-2197 — Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning

## Metadata

- **Authors:** Tan, Ling and Song, Jing and Sun, Lei and Wang, Haifeng and Xu, Hai
- **Year:** 2025
- **Venue:** Physical Communication
- **DOI:** 10.1016/j.phycom.2025.102916
- **URL:** https://www.scopus.com/pages/publications/105021850374?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** DPTL inspection network; Edge computing; Load balancing; Multi-agent reinforcement learning

### Abstract

The high dense power transmission line (DPTL), as transmission hubs, are characterized by complex line layouts and difficulty in inspection. We have designed a DPTL inspection network, in which obstacle-traversable inspection robots (OTIR) move on transmission lines and act as sensing and computing nodes to achieve full-coverage inspection of transmission lines. To improve inspection efficiency, the network integrates Mobile Edge Computing (MEC) and Device-to-Device (D2D) communication technologies to facilitate task offloading. We formulate an optimization problem for task offloading to achieve energy consumption balance and minimization objectives. Considering the dynamic and time-varying environment, we use the Lyapunov dynamic energy queue optimization scheme to transform the stochastic optimization problem into independent decisions for each time slot. In addition, we propose a multi-agent reinforcement learning algorithm based on an adaptive reward mechanism. This algorithm integrates digital twin technology to real-time perceive the dynamic states of the DPTL network, optimizing task scheduling through collaborative communication, thereby improving the overall efficiency and stability of the system. The simulation results demonstrate that the proposed algorithm exhibits good convergence performance. Compared with adaptive reward multi-agent advantage actor-critic(AR-MAA2C) and the deep deterministic policy gradient (DDPG) algorithms, the total inspection energy consumption of OTIRs is reduced by approximately 10.4% and 13.7%, respectively. Moreover, energy utilization efficiency is improved by about 5.6% and 7.3%, and the energy consumption balance reaches nearly 0.98, indicating that the proposed method effectively achieves high energy optimization and load balancing. © 2025

## 04 — Title Screening

**Title:** Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning
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
