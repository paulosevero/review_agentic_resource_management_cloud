---
id: "paper-390"
title: "Distributed Data Center Cooling control based on Multi-Agent Reinforcement Learning"
authors: ["Chen, Ding", "Wan, Jianxiong", "Li, Leixiao", "Liu, Chuyi"]
year: 2022
venue: "2022 4th International Conference on Frontiers Technology of Information and Computer, ICFTIC 2022"
venue_type: "conference"
doi: "10.1109/ICFTIC57696.2022.10075260"
url: "https://www.scopus.com/pages/publications/85152191723?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "456--461"
keywords: ["data center cooling control", "energy optimization", "multi-agent reinforcement learning"]
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

# paper-390 — Distributed Data Center Cooling control based on Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Chen, Ding and Wan, Jianxiong and Li, Leixiao and Liu, Chuyi
- **Year:** 2022
- **Venue:** 2022 4th International Conference on Frontiers Technology of Information and Computer, ICFTIC 2022
- **DOI:** 10.1109/ICFTIC57696.2022.10075260
- **URL:** https://www.scopus.com/pages/publications/85152191723?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 456--461
- **Language:** English
- **Keywords:** data center cooling control; energy optimization; multi-agent reinforcement learning

### Abstract

The data center cooling system is a complex-structured system integrated with a large number of components. Traditional centralized control methods are hard to apply in production data centers due to scalability issues. This paper studies the distributed cooling control problem where the data center is cooled by multiple Computer Room Air Conditioners (CRACs) to minimize the energy consumption. To characterize the interactions of CRACs, we formulate the distributed data center cooling control problem as a stochastic game, where each CRAC acts as an agent to learn the optimal local cooling policy. We propose a Multi-Agent Reinforcement Learning (MARL) framework based on the Counterfactual Multi-Agent (COMA). Specifically, we policies based on the agents' observations of the global state. After the implementation of these policies, they will receive their own rewards, then evaluate the quality of the policies. Simulation results show that compared with the Independent Q-Learning (IQL) method, this algorithm reduces the power consumption of CRACs by 6.2%.  © 2022 IEEE.

## 04 — Title Screening

**Title:** Distributed Data Center Cooling control based on Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Distributed Data Center Cooling control based on Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Distributed Data Center Cooling control based on Multi-Agent Reinforcement Learning
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
