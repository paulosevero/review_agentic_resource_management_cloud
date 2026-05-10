---
id: "paper-1481"
title: "Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach"
authors: ["Chen, Juan", "Zhong, Jie", "Wu, Zongling", "Tian, Di", "Chen, Yujie"]
year: 2025
venue: "Journal of King Saud University - Computer and Information Sciences"
venue_type: "journal"
doi: "10.1007/s44443-025-00160-w"
url: "https://www.scopus.com/pages/publications/105013646560?origin=resultslist"
publisher: "Springer International Publishing"
pages: ""
keywords: ["Deep reinforcement learning", "Optimization of task delay and failure rate", "Satellite edge computing", "Task priority", "Task scheduling"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1481 — Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach

## Metadata

- **Authors:** Chen, Juan and Zhong, Jie and Wu, Zongling and Tian, Di and Chen, Yujie
- **Year:** 2025
- **Venue:** Journal of King Saud University - Computer and Information Sciences
- **DOI:** 10.1007/s44443-025-00160-w
- **URL:** https://www.scopus.com/pages/publications/105013646560?origin=resultslist
- **Publisher:** Springer International Publishing
- **Pages:** 
- **Language:** English
- **Keywords:** Deep reinforcement learning; Optimization of task delay and failure rate; Satellite edge computing; Task priority; Task scheduling

### Abstract

In the current data-driven era, satellite edge computing (SatEC) emerges as a novel computing paradigm that addresses the coverage limitations of terrestrial networks in remote areas by deploying computational resources on satellite networks. This provides a new avenue for real-time data processing on a global scale. However, effectively scheduling tasks to optimize resource utilization, reduce processing delay, and ensure the timeliness of task execution has become a critical issue in SatEC. Existing task scheduling algorithms often fail to fully consider task deadlines and priority orders, leading to deficiencies in handling urgent tasks and optimizing overall computational efficiency. In response to these issues, we propose a multi-agent advantage actor-critic (MA2C) algorithm based on deep reinforcement learning, aiming to effectively address the task scheduling challenges in SatEC. The MA2C algorithm employs two cooperative agents to optimize scheduling strategies: one agent is responsible for prioritizing tasks, while the other focuses on task offloading decisions. These two agents interact in real-time, dynamically adjusting their strategies to adapt to environmental changes, effectively enhancing scheduling efficiency. Furthermore, the agent design adopts an encoder-decoder architecture, combined with self-attention (SA) mechanisms and temporal convolutional network (TCN) technology to extract environmental features, achieving real-time optimization of task scheduling. The simulation results indicate that the MA2C algorithm outperforms existing algorithms across various scenarios. Compared with the baseline algorithms BDQN, DRTO, and GA, the MA2C algorithm reduces the task failure rate by 9.1%, 11.2%, and 16.9% respectively. © The Author(s) 2025.

## 04 — Title Screening

**Title:** Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
