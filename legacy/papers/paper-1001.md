---
id: "paper-1001"
title: "Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning"
authors: ["Lei, Chengjia", "Wu, Shaohua", "Yang, Yi", "Xue, Jiayin", "Zhang, Qinyu"]
year: 2024
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2024.3388499"
url: "https://www.scopus.com/pages/publications/85190735681?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "12328--12344"
keywords: ["automatic surface vehicle (ASV)", "efficiency", "fault-tolerant communication", "Maritime search and rescue (SAR)", "multi-agent reinforcement learning (MARL)", "unmanned aerial vehicle (UAV)"]
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

# paper-1001 — Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Lei, Chengjia and Wu, Shaohua and Yang, Yi and Xue, Jiayin and Zhang, Qinyu
- **Year:** 2024
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2024.3388499
- **URL:** https://www.scopus.com/pages/publications/85190735681?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 12328--12344
- **Language:** English
- **Keywords:** automatic surface vehicle (ASV); efficiency; fault-tolerant communication; Maritime search and rescue (SAR); multi-agent reinforcement learning (MARL); unmanned aerial vehicle (UAV)

### Abstract

Nowadays, multiple types of equipment, including unmanned aerial vehicles (UAVs) and automatic surface vehicles (ASVs), have been deployed in maritime search and rescue (SAR). However, due to the lack of base stations (BSs), how to complete rescue while maintaining communication between vehicles is an unresolved challenge. In this paper, we design an efficient and fault-tolerant communication solution by jointly optimizing vehicles' trajectory, offloading scheduling, and routing topology for a heterogeneous vehicle system. First, we model several essential factors in maritime SAR, including the impact of ocean currents, the observational behavior of UAVs, the fault tolerance of relay networks, resource management of mobile edge computing (MEC), and energy consumption. A multi-objective optimization problem is formulated, aiming at minimizing time and energy consumption while increasing the fault tolerance of relay networks. Then, we transfer the objective into a decentralized partially observable Markov Decision Process (Dec-POMDP) and introduce multi-agent reinforcement learning (MARL) to search for a collaborative strategy. Specifically, two MARL approaches with different training styles are evaluated, and three techniques are added for improving performance, including sharing parameters, normalized generalized-advantage-estimation (GAE), and preserving-outputs-precisely-while-adaptively-rescaling-targets (Pop-Art). Experimental results demonstrate that our proposed approach, named heterogeneous vehicles multi-agent proximal policy optimization (HVMAPPO), outperforms other baselines in efficiency and fault tolerance of communication. © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning
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
