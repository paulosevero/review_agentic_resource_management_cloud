---
id: "paper-1346"
title: "MAPPO based Single-hop Task Offloading with Dynamic Vehicle Prediction in RSU-assisted IoV"
authors: ["Zhao, Wei", "Yang, Dongling", "Weng, Tangjie", "Xu, Xinwei", "Shao, Xun", "Liu, Zhi"]
year: 2024
venue: "Proceedings - 2024 IEEE Smart World Congress, SWC 2024 - 2024 IEEE Ubiquitous Intelligence and Computing, Autonomous and Trusted Computing, Digital Twin, Metaverse, Privacy Computing and Data Security, Scalable Computing and Communications"
venue_type: "conference"
doi: "10.1109/SWC62898.2024.00096"
url: "https://www.scopus.com/pages/publications/105002219306?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "472--478"
keywords: ["MAPPO", "neighboring vehicle prediction", "RSU", "task offloading"]
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

# paper-1346 — MAPPO based Single-hop Task Offloading with Dynamic Vehicle Prediction in RSU-assisted IoV

## Metadata

- **Authors:** Zhao, Wei and Yang, Dongling and Weng, Tangjie and Xu, Xinwei and Shao, Xun and Liu, Zhi
- **Year:** 2024
- **Venue:** Proceedings - 2024 IEEE Smart World Congress, SWC 2024 - 2024 IEEE Ubiquitous Intelligence and Computing, Autonomous and Trusted Computing, Digital Twin, Metaverse, Privacy Computing and Data Security, Scalable Computing and Communications
- **DOI:** 10.1109/SWC62898.2024.00096
- **URL:** https://www.scopus.com/pages/publications/105002219306?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 472--478
- **Language:** English
- **Keywords:** MAPPO; neighboring vehicle prediction; RSU; task offloading

### Abstract

In the realm of Internet of Vehicles (IoV), Roadside Units (RSUs) play a vital role due to their advanced sensing and computing capabilities. They support Mobile Edge Computing (MEC) by enabling real-time data processing and reducing latency and energy consumption. Given the large volume of data and the limited computing capacity of RSUs, tasks are often offloaded to other nodes, such as the cloud, other RSUs, or vehicles. However, due to the environment dynamic caused by vehicle mobility, the set of neighboring nodes for each RSU frequently changes, and variations in neighboring nodes are not perceived timely. In such cases, RSUs need to predict changes in neighboring nodes to ensure effective task offloading. Moreover, since each RSU can only perceive the surrounding environment, it is difficult for a single node to make optimal offloading decisions for each task independently. To address these issues, this paper proposes a distributed task offloading scheme that incorporates vehicle trajectory prediction. First, each RSU uses the vehicle trajectories predicted by the Gated Recurrent Unit (GRU) model to determine neighboring vehicles and update the set of neighboring nodes. Then, to enable each RSU to select a suitable computing node and minimize computation delay and energy consumption for the task, we adopt a distributed approach where each RSU independently makes offloading decisions based on local observations. To achieve this goal, we establish a 01 mathematical model and transform it into a Markov Decision Process (MDP). Subsequently, we propose a solution based on Multi-Agent Proximal Policy Optimization (MAPPO). Through extensive simulation experiments, we demonstrate that the scheme effectively reduces both long-term average processing delay and energy consumption.  © 2024 IEEE.

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
