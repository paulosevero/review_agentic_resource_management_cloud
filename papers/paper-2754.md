---
id: "paper-2754"
title: "A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles"
authors: ["Ren, Junjun", "Chen, Guoqiang", "Chai, Zheng-Yi", "Yuan, Dong"]
year: 2026
venue: "Computers, Materials and Continua"
venue_type: "journal"
doi: "10.32604/cmc.2025.068795"
url: "https://www.scopus.com/pages/publications/105028361798?origin=resultslist"
publisher: "Tech Science Press"
pages: ""
keywords: ["cloud-edge computing", "computation offloading", "Deep reinforcement learning", "internet of vehicles", "multi-objective optimization", "service caching"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2754 — A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles

## Metadata

- **Authors:** Ren, Junjun and Chen, Guoqiang and Chai, Zheng-Yi and Yuan, Dong
- **Year:** 2026
- **Venue:** Computers, Materials and Continua
- **DOI:** 10.32604/cmc.2025.068795
- **URL:** https://www.scopus.com/pages/publications/105028361798?origin=resultslist
- **Publisher:** Tech Science Press
- **Pages:** 
- **Language:** English
- **Keywords:** cloud-edge computing; computation offloading; Deep reinforcement learning; internet of vehicles; multi-objective optimization; service caching

### Abstract

Vehicle Edge Computing (VEC) and Cloud Computing (CC) significantly enhance the processing efficiency of delay-sensitive and computation-intensive applications by offloading compute-intensive tasks from resource-constrained onboard devices to nearby Roadside Unit (RSU), thereby achieving lower delay and energy consumption. However, due to the limited storage capacity and energy budget of RSUs, it is challenging to meet the demands of the highly dynamic Internet of Vehicles (IoV) environment. Therefore, determining reasonable service caching and computation offloading strategies is crucial. To address this, this paper proposes a joint service caching scheme for cloud-edge collaborative IoV computation offloading. By modeling the dynamic optimization problem using Markov Decision Processes (MDP), the scheme jointly optimizes task delay, energy consumption, load balancing, and privacy entropy to achieve better quality of service. Additionally, a dynamic adaptive multi-objective deep reinforcement learning algorithm is proposed. Each Double Deep Q-Network (DDQN) agent obtains rewards for different objectives based on distinct reward functions and dynamically updates the objective weights by learning the value changes between objectives using Radial Basis Function Networks (RBFN), thereby efficiently approximating the Pareto-optimal decisions for multiple objectives. Extensive experiments demonstrate that the proposed algorithm can better coordinate the three-tier computing resources of cloud, edge, and vehicles. Compared to existing algorithms, the proposed method reduces task delay and energy consumption by 10.64% and 5.1%, respectively. Copyright © 2025 The Authors.

## 04 — Title Screening

**Title:** A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles
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
