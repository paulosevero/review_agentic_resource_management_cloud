---
id: "paper-805"
title: "Distributed Deep Multi-Agent Reinforcement Learning for Cooperative Edge Caching in Internet-of-Vehicles"
authors: ["Zhou, Huan", "Jiang, Kai", "He, Shibo", "Min, Geyong", "Wu, Jie"]
year: 2023
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2023.3272348"
url: "https://www.scopus.com/pages/publications/85162891664?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "9595--9609"
keywords: ["cache replacement", "content delivery", "Edge caching", "Internet-of-Vehicles", "multi-agent reinforcement learning"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-805 — Distributed Deep Multi-Agent Reinforcement Learning for Cooperative Edge Caching in Internet-of-Vehicles

## Metadata

- **Authors:** Zhou, Huan and Jiang, Kai and He, Shibo and Min, Geyong and Wu, Jie
- **Year:** 2023
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2023.3272348
- **URL:** https://www.scopus.com/pages/publications/85162891664?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 9595--9609
- **Language:** English
- **Keywords:** cache replacement; content delivery; Edge caching; Internet-of-Vehicles; multi-agent reinforcement learning

### Abstract

Edge caching is a promising approach to reduce duplicate content transmission in Internet-of-Vehicles (IoVs). Several Reinforcement Learning (RL) based edge caching methods have been proposed to improve the resource utilization and reduce the backhaul traffic load. However, they only obtain the local sub-optimal solution, as they neglect the influence from environments by other agents. This paper investigates the edge caching strategies with consideration of the content delivery and cache replacement by exploiting the distributed Multi-Agent Reinforcement Learning (MARL). A hierarchical edge caching architecture for IoVs is proposed and the corresponding problem is formulated with the goal to minimize the long-term content access cost in the system. Then, we extend the Markov Decision Process (MDP) in the single agent RL to the context of a multi-agent system, and tackle the corresponding combinatorial multi-armed bandit problem based on the framework of a stochastic game. Specifically, we firstly propose a Distributed MARL-based Edge caching method (DMRE), where each agent can adaptively learn its best behaviour in conjunction with other agents for intelligent caching. Meanwhile, we attempt to reduce the computation complexity of DMRE by parameter approximation, which legitimately simplifies the training targets. However, DMRE is enabled to represent and update the parameter by creating a lookup table, essentially a tabular-based method, which generally performs inefficiently in large-scale scenarios. To circumvent the issue and make more expressive parametric models, we incorporate the technical advantage of the Deep- Q Network into DMRE, and further develop a computationally efficient method (DeepDMRE) with neural network-based Nash equilibria approximation. Extensive simulations are conducted to verify the effectiveness of the proposed methods. Especially, DeepDMRE outperforms DMRE, Q -learning, LFU, and LRU, and the edge hit rate is improved by roughly 5%, 19%, 40%, and 35%, respectively, when the cache capacity reaches 1, 000 MB.  © 2002-2012 IEEE.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
