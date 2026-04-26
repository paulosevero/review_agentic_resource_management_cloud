---
id: "paper-1356"
title: "Decomposition-based learning in drone-assisted wireless-powered mobile edge computing networks"
authors: ["Zhou, Xiaoyi", "Huang, Liang", "Ye, Tong", "Sun, Weiqiang"]
year: 2024
venue: "Digital Communications and Networks"
venue_type: "journal"
doi: "10.1016/j.dcan.2023.11.010"
url: "https://www.scopus.com/pages/publications/85208762624?origin=resultslist"
publisher: "KeAi Communications Co."
pages: "1769--1781"
keywords: ["Mobile-edge computing", "Multi-agent reinforcement learning", "Offloading decision", "Trajectory planning", "Unmanned aerial vehicle", "Wireless power transfer"]
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

# paper-1356 — Decomposition-based learning in drone-assisted wireless-powered mobile edge computing networks

## Metadata

- **Authors:** Zhou, Xiaoyi and Huang, Liang and Ye, Tong and Sun, Weiqiang
- **Year:** 2024
- **Venue:** Digital Communications and Networks
- **DOI:** 10.1016/j.dcan.2023.11.010
- **URL:** https://www.scopus.com/pages/publications/85208762624?origin=resultslist
- **Publisher:** KeAi Communications Co.
- **Pages:** 1769--1781
- **Language:** English
- **Keywords:** Mobile-edge computing; Multi-agent reinforcement learning; Offloading decision; Trajectory planning; Unmanned aerial vehicle; Wireless power transfer

### Abstract

This paper investigates the multi-Unmanned Aerial Vehicle (UAV)-assisted wireless-powered Mobile Edge Computing (MEC) system, where UAVs provide computation and powering services to mobile terminals. We aim to maximize the number of completed computation tasks by jointly optimizing the offloading decisions of all terminals and the trajectory planning of all UAVs. The action space of the system is extremely large and grows exponentially with the number of UAVs. In this case, single-agent learning will require an overlarge neural network, resulting in insufficient exploration. However, the offloading decisions and trajectory planning are two subproblems performed by different executants, providing an opportunity for problem-solving. We thus adopt the idea of decomposition and propose a 2-Tiered Multi-agent Soft Actor-Critic (2T-MSAC) algorithm, decomposing a single neural network into multiple small-scale networks. In the first tier, a single agent is used for offloading decisions, and an online pretrained model based on imitation learning is specially designed to accelerate the training process of this agent. In the second tier, UAVs utilize multiple agents to plan their trajectories. Each agent exerts its influence on the parameter update of other agents through actions and rewards, thereby achieving joint optimization. Simulation results demonstrate that the proposed algorithm can be applied to scenarios with various location distributions of terminals, outperforming existing benchmarks that perform well only in specific scenarios. In particular, 2T-MSAC increases the number of completed tasks by 45.5% in the scenario with uneven terminal distributions. Moreover, the pretrained model based on imitation learning reduces the convergence time of 2T-MSAC by 58.2%. © 2023 Chongqing University of Posts and Telecommunications

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
