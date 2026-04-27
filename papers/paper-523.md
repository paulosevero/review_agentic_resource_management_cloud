---
id: "paper-523"
title: "Learning Distributed and Fair Policies for Network Load Balancing as Markov Potential Game"
authors: ["Yao, Zhiyuan", "Ding, Zihan"]
year: 2022
venue: "Advances in Neural Information Processing Systems"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/85163149673?origin=resultslist"
publisher: "Neural information processing systems foundation"
pages: ""
keywords: ["Computer architecture", "Fertilizers", "Multi agent systems", "Datacenter", "Distributed networking systems", "Load balancer", "Load balancing problem", "Load-balancing algorithm", "Multi-agent reinforcement learning", "Network load balancing", "Potential games", "Production load", "Real-world system", "Reinforcement learning"]
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

# paper-523 — Learning Distributed and Fair Policies for Network Load Balancing as Markov Potential Game

## Metadata

- **Authors:** Yao, Zhiyuan and Ding, Zihan
- **Year:** 2022
- **Venue:** Advances in Neural Information Processing Systems
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/85163149673?origin=resultslist
- **Publisher:** Neural information processing systems foundation
- **Pages:** 
- **Language:** English
- **Keywords:** Computer architecture; Fertilizers; Multi agent systems; Datacenter; Distributed networking systems; Load balancer; Load balancing problem; Load-balancing algorithm; Multi-agent reinforcement learning; Network load balancing; Potential games; Production load; Real-world system; Reinforcement learning

### Abstract

This paper investigates the network load balancing problem in data centers (DCs) where multiple load balancers (LBs) are deployed, using the multi-agent reinforcement learning (MARL) framework. The challenges of this problem consist of the heterogeneous processing architecture and dynamic environments, as well as limited and partial observability of each LB agent in distributed networking systems, which can largely degrade the performance of in-production load balancing algorithms in real-world setups. Centralised-training-decentralised-execution (CTDE) RL scheme has been proposed to improve MARL performance, yet it incurs - especially in distributed networking systems, which prefer distributed and plug-and-play design schemes - additional communication and management overhead among agents. We formulate the multi-agent load balancing problem as a Markov potential game, with a carefully and properly designed workload distribution fairness as the potential function. A fully distributed MARL algorithm is proposed to approximate the Nash equilibrium of the game. Experimental evaluations involve both an event-driven simulator and real-world system, where the proposed MARL load balancing algorithm shows close-to-optimal performance in simulations, and superior results over in-production LBs in the real-world system. © 2022 Neural information processing systems foundation. All rights reserved.

## 04 — Title Screening

**Title:** Learning Distributed and Fair Policies for Network Load Balancing as Markov Potential Game

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Learning Distributed and Fair Policies for Network Load Balancing as Markov Potential Game
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Learning Distributed and Fair Policies for Network Load Balancing as Markov Potential Game
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
