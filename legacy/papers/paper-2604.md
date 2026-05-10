---
id: "paper-2604"
title: "Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks"
authors: ["Hevesli, Muhammet", "Mohammed Seid, Abegaz", "Erbad, Aiman", "Abdallah, Mohamed"]
year: 2026
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2025.3555440"
url: "https://www.scopus.com/pages/publications/105001386163?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "217--236"
keywords: ["air-ground network", "edge network", "metaverse", "Mobile edge computing", "multi-agent deep reinforcement learning"]
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

# paper-2604 — Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks

## Metadata

- **Authors:** Hevesli, Muhammet and Mohammed Seid, Abegaz and Erbad, Aiman and Abdallah, Mohamed
- **Year:** 2026
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2025.3555440
- **URL:** https://www.scopus.com/pages/publications/105001386163?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 217--236
- **Language:** English
- **Keywords:** air-ground network; edge network; metaverse; Mobile edge computing; multi-agent deep reinforcement learning

### Abstract

Mobile edge computing (MEC)-enabled air-ground networks advance 6G wireless networks by utilizing aerial base stations (ABSs) such as autonomous aerial vehicles (AAVs) and high altitude platform stations (HAPS) to provide dynamic services to ground IoT devices (IoTDs). These IoTDs support real-time applications like multimedia and Metaverse services, which demand high computational resources and strict quality of service (QoS) guarantees, specifically in terms of latency and efficient task queue management. However, IoTDs often face constraints in energy and computational power, requiring efficient queue management and task scheduling to maintain QoS. To address these challenges, AAVs and HAPS are deployed to supplement the computational limitations of IoTDs by offloading tasks for distributed processing. Due to AAVs’ resource limitations, particularly in terms of power and coverage area, HAPS are used to enhance their capabilities and extend coverage. Overloaded AAVs may relay tasks to HAPS, creating a multi-tier computing system. This paper addresses the overall energy minimization problem in the MEC-enabled air-ground integrated network (MAGIN) by optimizing AAV trajectories, computing resource allocation, and queue-aware task offloading decisions. The optimization problem is highly complex due to the nonconvex and nonlinear nature of this hierarchical system, which traditional methods cannot effectively solve. To tackle this, we reformulate the problem as a multi-agent Markov decision process (MDP) with continuous action spaces and heterogeneous agents. We propose a novel variant of multi-agent proximal policy optimization (MAPPO) with Beta distribution (MAPPO-BD) to solve this problem. Extensive simulations show that MAPPO-BD significantly outperforms other baselines, achieving superior energy savings and efficient resource management in MAGIN, while adhering to constraints related to queue delays and edge computing capabilities. © 2015 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks
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
