---
id: "paper-709"
title: "Multi-Agent RL for SDN-Based Resource Allocation in HAPS-Assisted IoV Networks"
authors: ["Seid, Abegaz Mohammed", "Erbad, Aiman"]
year: 2023
venue: "IEEE International Conference on Communications"
venue_type: "conference"
doi: "10.1109/ICC45041.2023.10279229"
url: "https://www.scopus.com/pages/publications/85178309455?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1664--1669"
keywords: ["HAPS", "Internet of Vehicles", "MARL", "Resource allocation", "software-defined networks"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-709 — Multi-Agent RL for SDN-Based Resource Allocation in HAPS-Assisted IoV Networks

## Metadata

- **Authors:** Seid, Abegaz Mohammed and Erbad, Aiman
- **Year:** 2023
- **Venue:** IEEE International Conference on Communications
- **DOI:** 10.1109/ICC45041.2023.10279229
- **URL:** https://www.scopus.com/pages/publications/85178309455?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1664--1669
- **Language:** English
- **Keywords:** HAPS; Internet of Vehicles; MARL; Resource allocation; software-defined networks

### Abstract

The high-altitude platform station (HAPS) is a promising 6G network technology that can meet the stringent requirements for high reliability, ultra-reliable low latency, and large-capacity communications, particularly in vehicular networks. HAPS with aerial computing and intelligent aerial software-defined networks (A-SDN) is a prominent solution to empower vehicles with limited resources. It allows vehicles in any geographical area to offload tasks and allocate resources within the dynamic infrastructure. The traditional MEC-based Internet of Vehicles (IoV) network is suffering from offloading various high data-rate real-time applications to B5G and the upcoming 6G networks. To handle this issue, we propose an intelligent HAPS-enabled IoV network to provide network connectivity, allocate resources, and allow computation in IoV networks. The HAPS is equipped with an aerial computing server and SDN, connected to the backhaul network of satellites and the cloud. The main objective is to maximize the utility of HAPS by jointly optimizing the association and resource allocation strategies of vehicles and other mobile devices. We formulate the optimization problem as a Stackelberg game. However, the formulated problem is complex to solve directly due to dynamism and multi-objective problems. Therefore, we transform it into a stochastic game model and utilize a distributed multi-agent deep reinforcement learning (MADRL) approach. In the proposed MADRL-based HAPS-assisted IoV network, the HAPS and vehicles are intelligent agents. We utilize a multi-agent deep deterministic policy gradient (MADDPG) algorithm to manage the continuous state-action. The simulation results prove that the proposed framework maximizes the network's utility and optimizes the association and resource allocation.  © 2023 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent RL for SDN-Based Resource Allocation in HAPS-Assisted IoV Networks

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent RL for SDN-Based Resource Allocation in HAPS-Assisted IoV Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent RL for SDN-Based Resource Allocation in HAPS-Assisted IoV Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
