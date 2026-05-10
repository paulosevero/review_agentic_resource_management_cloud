---
id: "paper-510"
title: "Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach"
authors: ["Waqar, Noor", "Hassan, Syed Ali", "Mahmood, Aamir", "Dev, Kapal", "Do, Dinh-Thuan", "Gidlund, Mikael"]
year: 2022
venue: "IEEE Transactions on Intelligent Transportation Systems"
venue_type: "journal"
doi: "10.1109/TITS.2022.3179987"
url: "https://www.scopus.com/pages/publications/85132757893?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "21478--21491"
keywords: ["integrated aerial-terrestrial networks", "mobile edge computing (MEC)", "multi-agent reinforcement learning", "Sixth generation (6G)", "vehicular communication"]
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

# paper-510 — Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach

## Metadata

- **Authors:** Waqar, Noor and Hassan, Syed Ali and Mahmood, Aamir and Dev, Kapal and Do, Dinh-Thuan and Gidlund, Mikael
- **Year:** 2022
- **Venue:** IEEE Transactions on Intelligent Transportation Systems
- **DOI:** 10.1109/TITS.2022.3179987
- **URL:** https://www.scopus.com/pages/publications/85132757893?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 21478--21491
- **Language:** English
- **Keywords:** integrated aerial-terrestrial networks; mobile edge computing (MEC); multi-agent reinforcement learning; Sixth generation (6G); vehicular communication

### Abstract

As important services of the future sixth-generation (6G) wireless networks, vehicular communication and mobile edge computing (MEC) have received considerable interest in recent years for their significant potential applications in intelligent transportation systems. However, MEC-enabled vehicular networks depend heavily on network access and communication infrastructure, often unavailable in remote areas, making computation offloading susceptible to breaking down. To address this issue, we propose an MEC-enabled vehicular network assisted through aerial-terrestrial connectivity to provide network access and high data-rate entertainment services to a vehicular network. We present a time-varying, dynamic system model where high altitude platforms (HAPs) equipped with MEC servers, connected to a backhaul system of low-earth orbit (LEO) satellites, are used to provide computation offloading capability to the vehicles, as well as to provide network access for vehicle-to-vehicle (V2V) communications. Our main objective is to minimize the total computation and communication overhead of the joint computation offloading and resource allocation strategies for the system of vehicles. Since our formulated optimization problem is a mixed-integer non-linear programming (MINLP) problem, which is NP-hard, we propose a decentralized value-iteration-based reinforcement learning (RL) approach as a solution. In our Q-learning-assisted analysis, each vehicle acts as an intelligent agent to form optimal strategies for offloading and resource allocation. We further extend our solution to deep Q-learning (DQL) and double deep Q-learning to overcome the issues of dimensionality and the over-estimation of the value functions, as in Q-learning. Simulation results prove the effectiveness of our solution in successfully reducing system costs compared to baseline schemes.  © 2000-2011 IEEE.

## 04 — Title Screening

**Title:** Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach
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
