---
id: "paper-311"
title: "Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach"
authors: ["Lorido-Botran, Tania", "Bhatti, Muhammad Khurram"]
year: 2021
venue: "Lecture Notes in Networks and Systems"
venue_type: "conference"
doi: "10.1007/978-3-030-75078-7_57"
url: "https://www.scopus.com/pages/publications/85106414131?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "572--581"
keywords: ["Cloud computing", "Container scheduling", "Deep reinforcement learning"]
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

# paper-311 — Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Lorido-Botran, Tania and Bhatti, Muhammad Khurram
- **Year:** 2021
- **Venue:** Lecture Notes in Networks and Systems
- **DOI:** 10.1007/978-3-030-75078-7_57
- **URL:** https://www.scopus.com/pages/publications/85106414131?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 572--581
- **Language:** English
- **Keywords:** Cloud computing; Container scheduling; Deep reinforcement learning

### Abstract

Cloud data centers rely on virtualization to run a diverse set of applications. Container technology allows for a more lightweight execution, in comparison with popular Virtual Machines. Efficient scheduling of containers is still challenging due to varying request arrival patterns, application-specific resource consumption and resource heterogeneity in physical servers. Besides, containers are also more prone to resource contention and performance interference. Cloud providers need to overcome these challenges with a goal in mind: maximize resource utilization to satisfy as many requests as possible. This paper introduces RLSched, a deep reinforcement learning-based (DRL) scheduler that is self-adaptive and automatically captures the resource usage dynamics in the data center. The scheduler is based on a decentralized actor-critic multi-agent architecture that enables for parallel execution and faster convergence. RLSched relies on an enhanced network model with action shaping, which filters invalid actions and prevents the agent to fall into a sub-optimal policy. The proposed scheduler is compared against other state-of-the-art DRL methods on a simulated data center environment based on real traces from Microsoft Azure. The results show faster convergence and higher number of containers placed per session. © 2021, The Author(s), under exclusive license to Springer Nature Switzerland AG.

## 04 — Title Screening

**Title:** Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach
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
