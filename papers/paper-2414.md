---
id: "paper-2414"
title: "A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks"
authors: ["Zhang, Yiwei", "Li, Yaping", "Lee, Yong", "Yan, Qing", "Yang, Yang"]
year: 2025
venue: "2025 17th International Conference on Wireless Communications and Signal Processing, WCSP 2025"
venue_type: "conference"
doi: "10.1109/WCSP68525.2025.1010647"
url: "https://www.scopus.com/pages/publications/105033702220?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["deep deterministic policy gradient", "Drone-enabled edge computing systems", "energy consumption", "latency", "prioritized experience replay"]
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

# paper-2414 — A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks

## Metadata

- **Authors:** Zhang, Yiwei and Li, Yaping and Lee, Yong and Yan, Qing and Yang, Yang
- **Year:** 2025
- **Venue:** 2025 17th International Conference on Wireless Communications and Signal Processing, WCSP 2025
- **DOI:** 10.1109/WCSP68525.2025.1010647
- **URL:** https://www.scopus.com/pages/publications/105033702220?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** deep deterministic policy gradient; Drone-enabled edge computing systems; energy consumption; latency; prioritized experience replay

### Abstract

With their mobility and flexibility, drones can serve as edge computing nodes to effectively enlarge the traditional mobile edge computing (MEC) coverage. However, the requirements of high energy efficiency and low latency seriously constrain the performance of drone-enabled MEC systems. In this paper, we investigate a deep reinforcement learning (DRL) scheme for minimizing the latency and energy consumption in drone-enabled MEC systems, where the computational tasks can be intelligently offloaded in two tiers between ground users (GUs), drones, and base stations (BSs), respectively. Specifically, a multi-agent (MA) deep deterministic policy gradient (DDPG) is employed to jointly allocate the power and reduce the offloading latency. Due to the randomness of tasks' arrival, the computational cost is formulated as a non-convex optimization problem of both latency and energy consumption cost, which satisfies the power constraints and maximum computation capacity. Further, a heterogeneous MA prioritized experience replay (PER) DDPGbased power allocation (HMP-DPA) algorithm is proposed, which operates by decentralized training and decentralized execution (DTDE) to avoid exponential growth of action space. Especially, PER can accelerate the algorithm convergence and the reward is designed to enhance the DRL training stability. Simulation results demonstrate that the proposed HMP-DPA can effectively explore an optimal task offloading strategy to minimize the latency and energy consumption in different tiers, and significantly outperform other baselines with an average computation cost reduction of 17.35%, 18.94%, and 28.17 % under different weights. © 2025 IEEE.

## 04 — Title Screening

**Title:** A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks
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
