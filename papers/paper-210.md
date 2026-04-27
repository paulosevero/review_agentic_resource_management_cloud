---
id: "paper-210"
title: "Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge"
authors: ["Jaleel, Abdul", "Hassan, Muhammad Awais", "Mahmood, Tayyeb", "Ghani, Muhammad Usman", "Ur Rehman, Atta"]
year: 2020
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2020.3037348"
url: "https://www.scopus.com/pages/publications/85102812386?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "205396--205410"
keywords: ["Artificial intelligence", "Collaborative signaling", "Deep Q-networks", "Distributed computing", "Embedded machine learning", "Proximal Policy Optimization", "Traffic congestion"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-210 — Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge

## Metadata

- **Authors:** Jaleel, Abdul and Hassan, Muhammad Awais and Mahmood, Tayyeb and Ghani, Muhammad Usman and Ur Rehman, Atta
- **Year:** 2020
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2020.3037348
- **URL:** https://www.scopus.com/pages/publications/85102812386?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 205396--205410
- **Language:** English
- **Keywords:** Artificial intelligence; Collaborative signaling; Deep Q-networks; Distributed computing; Embedded machine learning; Proximal Policy Optimization; Traffic congestion

### Abstract

The advancements in Edge computing have paved the way for deep learning in real-time systems. One of the beneficiaries is an adaptive traffic control system that responds to real-time traffic observations by governing the signal phase and timings. Reinforcement Learning (RL) is extensively utilized in the literature in order to decrease traffic congestion in a road network. However, most of the previous works leverage centralized and cloud-based RL due to the computational complexity of underlying deep neural networks (DNN). Therefore, a persistent challenge towards adopting Edge learning is in devising a Multi-Agent RL in which agents are simplified, and their state spaces are localized but they perform comparable to the centralized RL. This article presents a Collaborative and Adaptive Signaling on the Edge (CASE), a novel Multi-Agent RL approach to control the traffic signals' phase and timing. Each signalized intersection in the road network is provided with an Edge Learning Platform which hosts an RL-Agent that observes local traffic states and learns an optimum signal policy. Moreover, CASE allows collaboration among RL-Agents by sharing their signal phase and timings to achieve convergence and performance. This collaboration is limited to one's direct neighbours only to minimize the computational complexity. We performed rigorous evaluations in terms of the choice of RL methods and their state space/reward and found that our collaborative state-space has resulted in a performance comparable to a centralized RL yet with a cost similar to the decentralized RL. Finally, a performance comparison of the CASE controller ported to the state-of-the-art Edge learning platforms is presented in this article. The results show that the proposed CASE controller can achieve real-time performance when ported to a general-purpose GPU-based platform. This arrangement achieves more than 8 times improvement in computational time over conventional embedded platforms. © 2020 Institute of Electrical and Electronics Engineers Inc.. All rights reserved.

## 04 — Title Screening

**Title:** Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
