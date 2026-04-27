---
id: "paper-426"
title: "Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles"
authors: ["He, Hang", "Ren, Tao", "Cui, Meng", "Liu, Dong", "Niu, Jianwei"]
year: 2022
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-3-031-19211-1_40"
url: "https://www.scopus.com/pages/publications/85142880064?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "481--494"
keywords: ["Computation offloading", "Deep reinforcement learning", "Mobile edge computing", "Proximal policy optimization", "Unmanned aerial vehicle"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-426 — Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles

## Metadata

- **Authors:** He, Hang and Ren, Tao and Cui, Meng and Liu, Dong and Niu, Jianwei
- **Year:** 2022
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-3-031-19211-1_40
- **URL:** https://www.scopus.com/pages/publications/85142880064?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 481--494
- **Language:** English
- **Keywords:** Computation offloading; Deep reinforcement learning; Mobile edge computing; Proximal policy optimization; Unmanned aerial vehicle

### Abstract

Compared with traditional mobile edge computing (MEC), heterogeneous MEC (H-MEC), which is assisted by ground vehicles (GVs) and unmanned aerial vehicles (UAVs) simultaneously, is attracting more and more attention from both academia and industry. By deploying base stations (along with edge servers) on GVs or UAVs, H-MEC is more suitable for access-demand dynamically-changing network environments, e.g., sports matches, traffic management, and emergency rescue. However, it is non-trivial to perform real-time user association and resource allocation in large-scale H-MEC environments. Motivated by this, we propose a shared multi-agent proximal policy optimization (SMAPPO) algorithm based on the centralized training and distributed execution framework. Due to the NP-hard difficulty of jointly optimizing user association and resource allocation for H-MEC, we adopt the actor-critic-based online-policy gradient (PG) algorithm to obtain near-optimal solutions with low scheduling complexities. In addition, considering the low sampling efficiency of PG, we introduce proximal policy optimization to increase the training efficiency by importance sampling. Moreover, we leverage the idea of centralized training and distributed execution to improve the training efficiency and reduce scheduling complexity, so that each mobile device makes decisions based only on local observation and learns other MDs’ experience from a shared replay buffer. Extensive simulation results demonstrate that SMAPPO can achieve more satisfactory performances than traditional algorithms. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

## 04 — Title Screening

**Title:** Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
