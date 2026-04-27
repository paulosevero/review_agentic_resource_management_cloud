---
id: "paper-994"
title: "Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance"
authors: ["Kumar, Harsh", "Tshakwanda, Petro M.", "Arzo, Sisay T.", "Devetsikiotis, Michael", "Granelli, Fabrizio"]
year: 2024
venue: "2024 IEEE 5th World AI IoT Congress, AIIoT 2024"
venue_type: "conference"
doi: "10.1109/AIIoT61789.2024.10578954"
url: "https://www.scopus.com/pages/publications/85198830012?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "38--44"
keywords: ["Artificial Intelligence", "Reinforcement Learning", "Role Delegation", "Software Defined Network"]
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
    final_score: 0.25
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-994 — Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance

## Metadata

- **Authors:** Kumar, Harsh and Tshakwanda, Petro M. and Arzo, Sisay T. and Devetsikiotis, Michael and Granelli, Fabrizio
- **Year:** 2024
- **Venue:** 2024 IEEE 5th World AI IoT Congress, AIIoT 2024
- **DOI:** 10.1109/AIIoT61789.2024.10578954
- **URL:** https://www.scopus.com/pages/publications/85198830012?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 38--44
- **Language:** English
- **Keywords:** Artificial Intelligence; Reinforcement Learning; Role Delegation; Software Defined Network

### Abstract

In this paper, we introduce a novel method for autonomously assigning routing traffic roles in Software Defined Networks (SDN) using reinforcement learning. Our approach centers around a cloud-hosted central SDN controller interacting with two sub-SDN controllers situated in edge data centers. Each sub-controller manages three layer 2 switches and one wireless access point, connecting to five wired or wireless hosts generating randomized traffic. By collecting network data from hostto-host communications across diverse applications, we train a reinforcement learning agent to facilitate adaptive routing role delegation. The agent is tailored to identify optimal links between the main controller and subcontrollers, minimizing traffic congestion and ensuring ultra-low latency and high reliability during traffic routing. Our research aims to achieve dynamic and adaptive optimal routing, accommodating fluctuating traffic patterns and new device additions to the network. Leveraging PyTorch, we implement a neural network for the agent and employ a Q-learning algorithm for training, optimizing a reward function based on observed traffic congestion. Once trained, the agent autonomously delegates routing traffic roles to the least congested sub-controller. Performance evaluation involves analyzing traffic load and latency metrics, demonstrating the agent's proficiency in identifying optimal links and enhancing network performance, as observed through extensive experimentation and evaluation across diverse SDN scenarios. Furthermore, to foster collaboration and reproducibility within the research community, we make our implementation code and dataset publicly available on GitHub at https://github.com/your_username/project_name. © 2024 IEEE.

## 04 — Title Screening

**Title:** Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance

### Machine Screening

- **Final Score:** 0.25 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
