---
id: "paper-1143"
title: "MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network"
authors: ["Qin, Peng", "Wang, Yifei", "Cai, Ziyuan", "Liu, Jiayan", "Li, Jinghan", "Zhao, Xiongwen"]
year: 2024
venue: "IEEE Transactions on Intelligent Transportation Systems"
venue_type: "journal"
doi: "10.1109/TITS.2023.3342271"
url: "https://www.scopus.com/pages/publications/85181580632?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6716--6729"
keywords: ["Air-ground vehicular cooperative computing network (AVA2N)", "multi-agent deep reinforcement learning (MADRL)", "task offloading", "URLLC-aware"]
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

# paper-1143 — MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network

## Metadata

- **Authors:** Qin, Peng and Wang, Yifei and Cai, Ziyuan and Liu, Jiayan and Li, Jinghan and Zhao, Xiongwen
- **Year:** 2024
- **Venue:** IEEE Transactions on Intelligent Transportation Systems
- **DOI:** 10.1109/TITS.2023.3342271
- **URL:** https://www.scopus.com/pages/publications/85181580632?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6716--6729
- **Language:** English
- **Keywords:** Air-ground vehicular cooperative computing network (AVA2N); multi-agent deep reinforcement learning (MADRL); task offloading; URLLC-aware

### Abstract

With the rapid development of 5G and Internet of Vehicles (IoV) technologies, vehicles have evolved from mere transportation devices to mobile living spaces for humans. Thus, the complexity of data processing is growing along with the increasing of vehicle applications, which makes relying solely on on-board processing capabilities insufficient. Traditional Roadside Units (RSUs)-based edge computing has limitations such as high deployment cost and finite coverage. To address those issues, we construct an Air-Ground Vehicular Cooperative Computing Network (AVC2N ) that introduces Cooperative Vehicles (CVs) to reduce deployment cost while incorporating Unmanned Aerial Vehicles (UAVs) to expand communication coverage. We aim to balance offloading efficiency and environmental sustainability by proposing a system cost minimization problem with weighted sum of delay and energy consumption. However, it faces new challenges such as the lack of Global State Information (GSI), and the Ultra-Reliable Low-Latency Communications (URLLC) queue delay constraints, rendering traditional methods inadequate. To address the coupling between immediate decision and long-term queuing constraints, we employ Lyapunov optimization to partition the initial problem into two distinct sub-problems. The first focuses on optimizing the system transmission cost, which is tackled using a collaborative Deep Reinforcement Learning (DRL) framework. Specifically, we design an algorithm based on Multi Agent Deep Deterministic Policy Gradient (MADDPG), which effectively addresses GSI uncertainty and ensures URLLC awareness. The second sub-problem addresses server-side computing resource optimization, and we propose a greedy algorithm to tackle it. Experimental results showcase the effectiveness of our approach, demonstrating notable achievement in terms of learning convergence speed, overall system cost, queue delay, and queue backlog.  © 2000-2011 IEEE.

## 04 — Title Screening

**Title:** MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network
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
