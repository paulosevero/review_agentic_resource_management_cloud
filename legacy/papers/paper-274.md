---
id: "paper-274"
title: "Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks"
authors: ["Chen, Xing", "Liu, Guizhong"]
year: 2021
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2021.3050804"
url: "https://www.scopus.com/pages/publications/85099563631?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "10843--10856"
keywords: ["Augmented reality (AR)", "Deep reinforcement learning", "Internet of Things (IoT)", "Mobile-edge computing (MEC)", "Multiagent deep deterministic policy gradient (MADDPG)", "Resource allocation", "Task offloading"]
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

# paper-274 — Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks

## Metadata

- **Authors:** Chen, Xing and Liu, Guizhong
- **Year:** 2021
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2021.3050804
- **URL:** https://www.scopus.com/pages/publications/85099563631?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 10843--10856
- **Language:** English
- **Keywords:** Augmented reality (AR); Deep reinforcement learning; Internet of Things (IoT); Mobile-edge computing (MEC); Multiagent deep deterministic policy gradient (MADDPG); Resource allocation; Task offloading

### Abstract

The augmented reality (AR) applications have been widely used in the field of Internet of Things (IoT) because of good immersion experience for users, but their ultralow delay demand and high energy consumption bring a huge challenge to the current communication system and terminal power. The emergence of mobile-edge computing (MEC) provides a good thinking to solve this challenge. In this article, we study an energy-efficient task offloading and resource allocation scheme for AR in both the single-MEC and multi-MEC systems. First, a more specific and detailed AR application model is established as a directed acyclic graph according to its internal functionality. Second, based on this AR model, a joint optimization problem of task offloading and resource allocation is formulated to minimize the energy consumption of each user subject to the latency requirement and the limited resources. The problem is a mixed multiuser competition and cooperation problem, which involves the task offloading decision, uplink/downlink transmission resources allocation, and computing resources allocation of users and MEC server. Since it is an NP-hard problem and the communication environment is dynamic, it is difficult for genetic algorithms or heuristic algorithms to solve. Therefore, we propose an intelligent and efficient resource allocation and task offloading algorithm based on the deep reinforcement learning framework of multiagent deep deterministic policy gradient (MADDPG) in a dynamic communication environment. Finally, simulation results show that the proposed algorithm can greatly reduce the energy consumption of each user terminal. © 2014 IEEE.

## 04 — Title Screening

**Title:** Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks
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
