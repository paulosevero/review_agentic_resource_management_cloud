---
id: "paper-1283"
title: "Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing"
authors: ["Wu, Changmao", "Xu, Zhengwei", "He, Xiaoming", "Lou, Qi", "Xia, Yuanyuan", "Huang, Shuman"]
year: 2024
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2024.3406027"
url: "https://www.scopus.com/pages/publications/85194843074?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1387--1399"
keywords: ["6G", "deep reinforcement learning", "distributed edge computing", "multi-agent learning architecture", "proactive caching"]
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
    human_justification: "RL"

---

# paper-1283 — Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing

## Metadata

- **Authors:** Wu, Changmao and Xu, Zhengwei and He, Xiaoming and Lou, Qi and Xia, Yuanyuan and Huang, Shuman
- **Year:** 2024
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2024.3406027
- **URL:** https://www.scopus.com/pages/publications/85194843074?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1387--1399
- **Language:** English
- **Keywords:** 6G; deep reinforcement learning; distributed edge computing; multi-agent learning architecture; proactive caching

### Abstract

Proactive caching in 6G cloud-edge collaboration scenarios, intelligently and periodically updating the cached contents, can either alleviate the traffic congestion of backhaul link and edge cooperative link or bring multimedia services to mobile users. To further improve the network performance of 6G cloud-edge, we consider the issue of multi-objective joint optimization, i.e., maximizing edge hit ratio while minimizing content access latency and traffic cost. To solve this complex problem, we focus on the distributed deep reinforcement learning (DRL)-based method for proactive caching, including content prediction and content decision-making. Specifically, since the prior information of user requests is seldom available practically in the current time period, a novel method named temporal convolution sequence network (TCSN) based on the temporal convolution network (TCN) and attention model is used to improve the accuracy of content prediction. Furthermore, according to the value of content prediction, the distributional deep Q network (DDQN) seeks to build a distribution model on returns to optimize the policy of content decision-making. The generative adversarial network (GAN) is adapted in a distributed fashion, emphasizing learning the data distribution and generating compelling data across multiple nodes. In addition, the prioritized experience replay (PER) is helpful to learn from the most effective sample. So we propose a multivariate fusion algorithm called PG-DDQN. Finally, faced with such a complex scenario, a distributed learning architecture, i.e., multi-agent learning architecture is efficiently used to learn DRL-based methods in a manner of centralized training and distributed inference. The experiments prove that our proposal achieves satisfactory performance in terms of edge hit ratio, traffic cost and content access latency. © 2024 IEEE.

## 04 — Title Screening

**Title:** Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing
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
