---
id: "paper-835"
title: "Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks"
authors: ["Betalo, Mesfin Leranso", "Leng, Supeng", "Abishu, Hayla Nahom", "Seid, Abegaz Mohammed", "Fakirah, Maged", "Erbad, Aiman", "Guizani, Mohsen"]
year: 2024
venue: "IEEE Transactions on Network and Service Management"
venue_type: "journal"
doi: "10.1109/TNSM.2024.3454217"
url: "https://www.scopus.com/pages/publications/85203645296?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6527--6541"
keywords: ["Deep reinforcement learning", "energy harvesting", "laser technology", "mobile edge computing", "unmanned aerial vehicles", "wireless sensor networks"]
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
    human_decision: ""
    human_justification: ""

---

# paper-835 — Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks

## Metadata

- **Authors:** Betalo, Mesfin Leranso and Leng, Supeng and Abishu, Hayla Nahom and Seid, Abegaz Mohammed and Fakirah, Maged and Erbad, Aiman and Guizani, Mohsen
- **Year:** 2024
- **Venue:** IEEE Transactions on Network and Service Management
- **DOI:** 10.1109/TNSM.2024.3454217
- **URL:** https://www.scopus.com/pages/publications/85203645296?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6527--6541
- **Language:** English
- **Keywords:** Deep reinforcement learning; energy harvesting; laser technology; mobile edge computing; unmanned aerial vehicles; wireless sensor networks

### Abstract

In sixth-generation (6G) networks, unmanned aerial vehicles (UAVs) are expected to be widely used as aerial base stations (ABS) due to their adaptability, low deployment costs, and ultra-low latency responses. However, UAVs consume large amounts of power to collect data from multiple sensor nodes (SNs). This can limit their flight time and transmission efficiency, resulting in delays and low information freshness. In this paper, we present a multi-access edge computing (MEC)-integrated UAV-assisted wireless sensor network (WSN) with a laser technology-based energy harvesting (EH) system that makes the UAV act as a flying energy charger to address these issues. This work aims to minimize the age of information (AoI) and improve energy efficiency by jointly optimizing the UAV trajectories, EH, task scheduling, and data offloading. The joint optimization problem is formulated as a Markov decision process (MDP) and then transformed into a stochastic game model to handle the complexity and dynamics of the environment. We adopt a multi-agent deep Q-network (MADQN) algorithm to solve the formulated optimization problem. With the MADQN algorithm, UAVs can determine the best data collection and EH decisions to minimize their energy consumption and efficiently collect data from multiple SNs, leading to reduced AoI and improved energy efficiency. Compared to the benchmark algorithms such as deep deterministic policy gradient (DDPG), Dueling DQN, asynchronous advantage actor-critic (A3C) and Greedy, the MADQN algorithm has a lower average AoI and improves energy efficiency by 95.5%, 89.9%, 78.02% and 65.52% respectively.  © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks
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
