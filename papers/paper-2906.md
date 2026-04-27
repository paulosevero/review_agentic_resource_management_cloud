---
id: "paper-2906"
title: "Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing"
authors: ["Zhang, Han", "Liang, Hongbin", "Ale, Laha", "Mao, Guotao", "Hong, Xintao", "Jia, Qiong", "Zhao, Dongmei"]
year: 2026
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2025.3602016"
url: "https://www.scopus.com/pages/publications/105014641042?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2209--2223"
keywords: ["autonomous aerial vehicles", "Computation offloading", "deep reinforcement learning", "resource allocation", "vehicle edge computing"]
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

# paper-2906 — Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing

## Metadata

- **Authors:** Zhang, Han and Liang, Hongbin and Ale, Laha and Mao, Guotao and Hong, Xintao and Jia, Qiong and Zhao, Dongmei
- **Year:** 2026
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2025.3602016
- **URL:** https://www.scopus.com/pages/publications/105014641042?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2209--2223
- **Language:** English
- **Keywords:** autonomous aerial vehicles; Computation offloading; deep reinforcement learning; resource allocation; vehicle edge computing

### Abstract

The rapid growth of compute-intensive and delay-sensitive applications in the Internet of Vehicles (IoV) has brought new challenges to traditional Vehicle Edge Computing (VEC). Especially during peak traffic periods, fixed base stations (BSs), due to their static deployment and limited coverage, struggle to elastically scale computing resources to meet the dynamically changing computational demands of vehicular users, which to some extent affects the overall quality of service and efficiency of system resource utilization. In this paper, we propose a hybrid edge computing framework that integrates Autonomous Aerial Vehicles (AAVs) as mobile computing nodes to complement fixed base stations. For this AAV-BS hybrid edge computing environment, we design and optimize a computation offloading model considering heterogeneous task types and AAV trajectory planning. The proposed model tackles the joint optimization of system revenue, service delay, and energy consumption, while considering practical constraints such as AAV energy limitations and base station capacity. To address this multi-objective optimization challenge, we construct a Markov Decision Process (MDP) model and develop a multi-head self-attention enhanced Multi-Agent Deep Dirichlet Deterministic Policy Gradient (MHSA-MAD3PG) algorithm. The multi-head self-attention mechanism enables agents to capture complex dependencies and interactions in the environment, leading to more effective collaborative decision-making. Comprehensive simulation results demonstrate that our proposed approach achieves superior performance in terms of system revenue, service delay, and energy efficiency compared to baseline methods.  © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing
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
