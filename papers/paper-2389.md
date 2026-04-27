---
id: "paper-2389"
title: "Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing"
authors: ["You, Feiran", "Yuan, Xin", "Ni, Wei", "Jamalipour, Abbas"]
year: 2025
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2024.3499342"
url: "https://www.scopus.com/pages/publications/85210284778?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1887--1901"
keywords: ["game theory", "local differential privacy (LDP)", "Multi-access edge computing (MEC)", "multi-agent deep deterministic policy gradient (MADDPG)"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2389 — Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing

## Metadata

- **Authors:** You, Feiran and Yuan, Xin and Ni, Wei and Jamalipour, Abbas
- **Year:** 2025
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2024.3499342
- **URL:** https://www.scopus.com/pages/publications/85210284778?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1887--1901
- **Language:** English
- **Keywords:** game theory; local differential privacy (LDP); Multi-access edge computing (MEC); multi-agent deep deterministic policy gradient (MADDPG)

### Abstract

Multi-access edge computing (MEC) offloads services for mobile users to facilitate the integration of idle cloudlet resources and bring cloud services closer to users. Existing studies have focused primarily on task coordination and resource allocation with strict time constraints, and typically overlooked the potential privacy leakage of users’ participation strategies in MEC. This paper proposes a novel solution to computation offloading and privacy protection in MEC networks using a Multi-agent Deep Deterministic Policy Gradient (MADDPG) framework. Our approach utilizes game theory to encourage computation offloading by modeling the interaction between cloudlets, Data Center Operators (DCOs), and users as a stochastic auction game. We formulate the computation offloading as an auction game with multiple bidders and incomplete information, and use MADDPG to find an optimal solution. To ensure privacy protection, we design a local Differential Privacy (DP) method in the MADDPG algorithm. With an (∈, δ) -DP mechanism, the local DP ensures that the sampled transitions, including the information on users’ actions, states, and corresponding rewards, are protected from exploitation. Analyses corroborate the effectiveness of our approach in satisfying DP and converging to an equilibrium. Simulations demonstrate the approach achieves 126.75% better quality-of-experience than a knapsack-based benchmark, when there are 60 cloudlets and up to 100 users. © 2015 IEEE.

## 04 — Title Screening

**Title:** Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
