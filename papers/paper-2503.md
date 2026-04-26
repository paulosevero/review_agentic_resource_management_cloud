---
id: "paper-2503"
title: "Mission-Aware Resource Allocation and Safe Trajectory Control for Multi-UAV Edge-Enabled Sensing Networks"
authors: ["Alazzwi, Abee", "Tshakwanda, Petro M.", "Tsegaye, Henok B.", "Devetsikiotis, Michael", "Kumar, Harsh"]
year: 2026
venue: "2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026"
venue_type: "conference"
doi: "10.1109/CCWC67433.2026.11393718"
url: "https://www.scopus.com/pages/publications/105035600726?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "633--639"
keywords: ["edge computing", "hierarchical PPO", "mission-aware resource allocation", "multi-agent reinforcement learning (MARL)", "Multi-UAV networks", "safe trajectory control", "safety-critical systems", "zeroing control barrier functions (ZCBF)"]
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

# paper-2503 — Mission-Aware Resource Allocation and Safe Trajectory Control for Multi-UAV Edge-Enabled Sensing Networks

## Metadata

- **Authors:** Alazzwi, Abee and Tshakwanda, Petro M. and Tsegaye, Henok B. and Devetsikiotis, Michael and Kumar, Harsh
- **Year:** 2026
- **Venue:** 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
- **DOI:** 10.1109/CCWC67433.2026.11393718
- **URL:** https://www.scopus.com/pages/publications/105035600726?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 633--639
- **Language:** English
- **Keywords:** edge computing; hierarchical PPO; mission-aware resource allocation; multi-agent reinforcement learning (MARL); Multi-UAV networks; safe trajectory control; safety-critical systems; zeroing control barrier functions (ZCBF)

### Abstract

We present HSPPO (Hierarchical Safe Proximal Policy Optimization), a mission-aware multi-agent reinforcement learning (MARL) framework that integrates resource allocation and safe trajectory control for cooperative unmanned aerial vehicles (UAVs) in edge-enabled sensing networks. Rather than introducing new barrier-function theory, HSPPO tightly couples discrete-time zeroing control barrier functions (ZCBFs) with PPO training by embedding safety filtering directly within rollouts and augmenting policy updates with a safety-imitation loss. This design aligns learning with formally safe actions while optimizing deadline-driven latency, energy consumption, and mission utility. Each UAV autonomously selects motion, missionzone association, and computation-communication splitting via a safety-constrained actor-critic, while a hierarchical structure combines a mission-aware scheduler with low-level controllers under centralized training and decentralized execution. We evaluate HSPPO in a simulation-based multi-UAV MEC environment across varying fleet sizes, mission-zone scales, priority distributions, and propagation conditions. In a nominal 1000 × 1000 m scenario with six UAVs and eight mission zones, HSPPO achieves an 83.7% mission completion rate with only 0.5 safety violations per episode, yielding 96% fewer collisions than a greedy heuristic baseline. It further attains 0.72 normalized latency and 0.75 normalized energy, improving completion by 9.2 percentage points relative to PPO without safety (83.7% vs. 74.5%) and reducing latency and energy by approximately 15-16%. Ablation and scalability studies, including safety-parameter sweeps, fallback-mechanism variants, and mission-context removal, indicate that safety-in-the-loop MARL can enable reliable and deadline-compliant coordination for multi-UAV edge-sensing missions under realistic system constraints. © 2026 IEEE.

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
