---
id: "paper-652"
title: "Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning"
authors: ["Lin, Shaofu", "Chen, Yingying", "Li, Shuopeng"]
year: 2023
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s23239541"
url: "https://www.scopus.com/pages/publications/85178943481?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["mobile edge computing (MEC)", "multi-agent deep reinforcement learning (MADRL)", "multi-objective optimization (MOO)", "unmanned aerial vehicle (UAV)", "wireless power transfer (WPT)"]
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

# paper-652 — Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning

## Metadata

- **Authors:** Lin, Shaofu and Chen, Yingying and Li, Shuopeng
- **Year:** 2023
- **Venue:** Sensors
- **DOI:** 10.3390/s23239541
- **URL:** https://www.scopus.com/pages/publications/85178943481?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** mobile edge computing (MEC); multi-agent deep reinforcement learning (MADRL); multi-objective optimization (MOO); unmanned aerial vehicle (UAV); wireless power transfer (WPT)

### Abstract

With the advantages of real-time data processing and flexible deployment, unmanned aerial vehicle (UAV)-assisted mobile edge computing systems are widely used in both civil and military fields. However, due to limited energy, it is usually difficult for UAVs to stay in the air for long periods and to perform computational tasks. In this paper, we propose a full-duplex air-to-air communication system (A2ACS) model combining mobile edge computing and wireless power transfer technologies, aiming to effectively reduce the computational latency and energy consumption of UAVs, while ensuring that the UAVs do not interrupt the mission or leave the work area due to insufficient energy. In this system, UAVs collect energy from external air-edge energy servers (AEESs) to power onboard batteries and offload computational tasks to AEESs to reduce latency. To optimize the system’s performance and balance the four objectives, including the system throughput, the number of low-power alarms of UAVs, the total energy received by UAVs and the energy consumption of AEESs, we develop a multi-objective optimization framework. Considering that AEESs require rapid decision-making in a dynamic environment, an algorithm based on multi-agent deep deterministic policy gradient (MADDPG) is proposed, to optimize the AEESs’ service location and to control the power of energy transfer. While training, the agents learn the optimal policy given the optimization weight conditions. Furthermore, we adopt the K-means algorithm to determine the association between AEESs and UAVs to ensure fairness. Simulated experiment results show that the proposed MODDPG (multi-objective DDPG) algorithm has better performance than the baseline algorithms, such as the genetic algorithm and other deep reinforcement learning algorithms. © 2023 by the authors.

## 04 — Title Screening

**Title:** Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
