---
id: "paper-340"
title: "Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach"
authors: ["Seid, Abegaz Mohammed", "Boateng, Gordon Owusu", "Anokye, Stephen", "Kwantwi, Thomas", "Sun, Guolin", "Liu, Guisong"]
year: 2021
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2021.3063188"
url: "https://www.scopus.com/pages/publications/85102274239?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "12203--12218"
keywords: ["Collaborative computation offloading", "deep reinforcement learning (DRL)", "Edge Internet of Things (EIoT)", "IoT network", "multi-UAV network", "resource allocation"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-340 — Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Seid, Abegaz Mohammed and Boateng, Gordon Owusu and Anokye, Stephen and Kwantwi, Thomas and Sun, Guolin and Liu, Guisong
- **Year:** 2021
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2021.3063188
- **URL:** https://www.scopus.com/pages/publications/85102274239?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 12203--12218
- **Language:** English
- **Keywords:** Collaborative computation offloading; deep reinforcement learning (DRL); Edge Internet of Things (EIoT); IoT network; multi-UAV network; resource allocation

### Abstract

In the fifth-generation (5G) wireless networks, Edge-Internet-of-Things (EIoT) devices are envisioned to generate huge amounts of data. Due to the limitation of computation capacity and battery life of devices, all tasks cannot be processed by these devices. However, mobile-edge computing (MEC) is a very promising solution enabling offloading of tasks to nearby MEC servers to improve quality of service. Also, during emergency situations in areas where network failure exists, unmanned aerial vehicles (UAVs) can be deployed to restore the network by acting as Aerial Base Stations and computational nodes for the edge network. In this article, we consider a central network controller who trains observations and broadcasts the trained data to a multi-UAV cluster network. Each UAV cluster head acts as an agent and autonomously allocates resources to EIoT devices in a decentralized fashion. We propose model-free deep reinforcement learning (DRL)-based collaborative computation offloading and resource allocation (CCORA-DRL) scheme in an aerial to ground (A2G) network for emergency situations, which can control the continuous action space. Each agent learns efficient computation offloading policies independently in the network and checks the statuses of the UAVs through Jain's Fairness index. The objective is minimizing task execution delay and energy consumption and acquiring an efficient solution by adaptive learning from the dynamic A2G network. Simulation results reveal that our scheme through deep deterministic policy gradient, effectively learns the optimal policy, outperforming A3C, deep $Q$ -network and greedy-based offloading for local computation in stochastic dynamic environments. © 2014 IEEE.

## 04 — Title Screening

**Title:** Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.5
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach
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
