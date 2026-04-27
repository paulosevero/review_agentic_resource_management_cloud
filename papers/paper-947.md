---
id: "paper-947"
title: "Multi-Agent Deep Reinforcement Learning Based Dynamic Task Offloading in a Device-to-Device Mobile-Edge Computing Network to Minimize Average Task Delay with Deadline Constraints"
authors: ["He, Huaiwen", "Yang, Xiangdong", "Mi, Xin", "Shen, Hong", "Liao, Xuefeng"]
year: 2024
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s24165141"
url: "https://www.scopus.com/pages/publications/85202622998?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["D2D", "delay constraint", "dynamic matching", "mobile edge computing", "multi-agent reinforcement learning"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-947 — Multi-Agent Deep Reinforcement Learning Based Dynamic Task Offloading in a Device-to-Device Mobile-Edge Computing Network to Minimize Average Task Delay with Deadline Constraints

## Metadata

- **Authors:** He, Huaiwen and Yang, Xiangdong and Mi, Xin and Shen, Hong and Liao, Xuefeng
- **Year:** 2024
- **Venue:** Sensors
- **DOI:** 10.3390/s24165141
- **URL:** https://www.scopus.com/pages/publications/85202622998?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** D2D; delay constraint; dynamic matching; mobile edge computing; multi-agent reinforcement learning

### Abstract

Device-to-device (D2D) is a pivotal technology in the next generation of communication, allowing for direct task offloading between mobile devices (MDs) to improve the efficient utilization of idle resources. This paper proposes a novel algorithm for dynamic task offloading between the active MDs and the idle MDs in a D2D–MEC (mobile edge computing) system by deploying multi-agent deep reinforcement learning (DRL) to minimize the long-term average delay of delay-sensitive tasks under deadline constraints. Our core innovation is a dynamic partitioning scheme for idle and active devices in the D2D–MEC system, accounting for stochastic task arrivals and multi-time-slot task execution, which has been insufficiently explored in the existing literature. We adopt a queue-based system to formulate a dynamic task offloading optimization problem. To address the challenges of large action space and the coupling of actions across time slots, we model the problem as a Markov decision process (MDP) and perform multi-agent DRL through multi-agent proximal policy optimization (MAPPO). We employ a centralized training with decentralized execution (CTDE) framework to enable each MD to make offloading decisions solely based on its local system state. Extensive simulations demonstrate the efficiency and fast convergence of our algorithm. In comparison to the existing sub-optimal results deploying single-agent DRL, our algorithm reduces the average task completion delay by 11.0% and the ratio of dropped tasks by 17.0%. Our proposed algorithm is particularly pertinent to sensor networks, where mobile devices equipped with sensors generate a substantial volume of data that requires timely processing to ensure quality of experience (QoE) and meet the service-level agreements (SLAs) of delay-sensitive applications. © 2024 by the authors.

## 04 — Title Screening

**Title:** Multi-Agent Deep Reinforcement Learning Based Dynamic Task Offloading in a Device-to-Device Mobile-Edge Computing Network to Minimize Average Task Delay with Deadline Constraints

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Deep Reinforcement Learning Based Dynamic Task Offloading in a Device-to-Device Mobile-Edge Computing Network to Minimize Average Task Delay with Deadline Constraints
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Deep Reinforcement Learning Based Dynamic Task Offloading in a Device-to-Device Mobile-Edge Computing Network to Minimize Average Task Delay with Deadline Constraints
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
