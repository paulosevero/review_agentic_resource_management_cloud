---
id: "paper-165"
title: "Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning"
authors: ["Wang, Yuandou", "Liu, Hang", "Zheng, Wanbo", "Xia, Yunni", "Li, Yawen", "Chen, Peng", "Guo, Kunyin", "Xie, Hong"]
year: 2019
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2019.2902846"
url: "https://www.scopus.com/pages/publications/85064241175?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "39974--39982"
keywords: ["deep-Q-network (DQN)", "infrastructure-as-a-service (IaaS) cloud", "multi-agent reinforcement learning (MARL)", "Multi-objective workflow scheduling", "quality-of-service (QoS)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-165 — Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning

## Metadata

- **Authors:** Wang, Yuandou and Liu, Hang and Zheng, Wanbo and Xia, Yunni and Li, Yawen and Chen, Peng and Guo, Kunyin and Xie, Hong
- **Year:** 2019
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2019.2902846
- **URL:** https://www.scopus.com/pages/publications/85064241175?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 39974--39982
- **Language:** English
- **Keywords:** deep-Q-network (DQN); infrastructure-as-a-service (IaaS) cloud; multi-agent reinforcement learning (MARL); Multi-objective workflow scheduling; quality-of-service (QoS)

### Abstract

Cloud Computing provides an effective platform for executing large-scale and complex workflow applications with a pay-as-you-go model. Nevertheless, various challenges, especially its optimal scheduling for multiple conflicting objectives, are yet to be addressed properly. The existing multi-objective workflow scheduling approaches are still limited in many ways, e.g., encoding is restricted by prior experts' knowledge when handling a dynamic real-time problem, which strongly influences the performance of scheduling. In this paper, we apply a deep-Q-network model in a multi-agent reinforcement learning setting to guide the scheduling of multi-workflows over infrastructure-as-a-service clouds. To optimize multi-workflow completion time and user's cost, we consider a Markov game model, which takes the number of workflow applications and heterogeneous virtual machines as state input and the maximum completion time and cost as rewards. The game model is capable of seeking for correlated equilibrium between make-span and cost criteria without prior experts' knowledge and converges to the correlated equilibrium policy in a dynamic real-time environment. To validate our proposed approach, we conduct extensive case studies based on multiple well-known scientific workflow templates and Amazon EC2 cloud. The experimental results clearly suggest that our proposed approach outperforms traditional ones, e.g., non-dominated sorting genetic algorithm-II, multi-objective particle swarm optimization, and game-theoretic-based greedy algorithms, in terms of optimality of scheduling plans generated. © 2013 IEEE.

## 04 — Title Screening

**Title:** Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
