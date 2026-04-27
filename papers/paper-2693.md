---
id: "paper-2693"
title: "DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization"
authors: ["Lotfolahi, Amin", "Ferng, Huei-Wen"]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2025.3584786"
url: "https://www.scopus.com/pages/publications/105010023342?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "469--484"
keywords: ["Industrial Internet of things (IIoT)", "mobile edge computing (MEC)", "multi-agent proximal policy optimization (MAPPO)", "non-orthogonal multiple access (NOMA)", "resource allocation", "Task offloading"]
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

# paper-2693 — DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization

## Metadata

- **Authors:** Lotfolahi, Amin and Ferng, Huei-Wen
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2025.3584786
- **URL:** https://www.scopus.com/pages/publications/105010023342?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 469--484
- **Language:** English
- **Keywords:** Industrial Internet of things (IIoT); mobile edge computing (MEC); multi-agent proximal policy optimization (MAPPO); non-orthogonal multiple access (NOMA); resource allocation; Task offloading

### Abstract

This paper addresses the joint optimization problem of computing and communication resource allocation in a non-orthogonal multiple access (NOMA) supported industrial Internet of things (IoT) system. We introduce a decentralized deep reinforcement learning (DRL) based mechanism that collaboratively maximizes energy productivity (EP). Specifically, optimizing EP involves maximizing the amount of successfully processed bits while simultaneously minimizing task processing delay, energy consumption, and task drop ratio. With this goal, we design a comprehensive model that incorporates multiple factors, including NOMA-specific constraints, task queueing, partial processing, and multitasking, where each device can handle multiple concurrent tasks. Next, we propose a dual-decentralized multi-agent proximal policy optimization (MAPPO) based algorithm, where one MAPPO algorithm focuses explicitly on computing resource allocation for task processing at the edge servers, while the other MAPPO algorithm precisely manages communication resource allocation. Additionally, each MAPPO algorithm is equipped with a small residual network (ResNet) and a recurrent neural network (RNN) to effectively capture spatial features from complex channel conditions and the evolving task flow. Through extensive simulations, we validate the effectiveness of our resultant mechanism under various environmental conditions and demonstrate its superiority over the closely related mechanisms in the literature. © 2025 IEEE. All rights reserved.

## 04 — Title Screening

**Title:** DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization
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
