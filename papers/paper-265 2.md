---
id: "paper-265"
title: "Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing"
authors: ["Bai, Wenle", "Qian, Cheng"]
year: 2021
venue: "Proceedings of the IEEE International Conference on Software Engineering and Service Sciences, ICSESS"
venue_type: "conference"
doi: "10.1109/ICSESS52187.2021.9522334"
url: "https://www.scopus.com/pages/publications/85114963754?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "131--134"
keywords: ["deep reinforcement learning", "fog computing", "offloading"]
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

# paper-265 — Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing

## Metadata

- **Authors:** Bai, Wenle and Qian, Cheng
- **Year:** 2021
- **Venue:** Proceedings of the IEEE International Conference on Software Engineering and Service Sciences, ICSESS
- **DOI:** 10.1109/ICSESS52187.2021.9522334
- **URL:** https://www.scopus.com/pages/publications/85114963754?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 131--134
- **Language:** English
- **Keywords:** deep reinforcement learning; fog computing; offloading

### Abstract

The traditional cloud computing model can no longer satisfy the current demand due to the limitations of backhaul bandwidth and high latency. Therefore, a new fog computing architecture is proposed, which relieves the bandwidth load and energy pressure on the backhaul link by reducing the number of communications between the cloud computing center and the users. The latency is drastically reduced by proximity to the devices. However, the performance of fog computing is highly dependent on a variety of resource allocation strategies. Therefore, task offloading strategies and resource allocation strategies are a great challenge. In this paper, we use the advantage actor-critic (A2C) algorithm in Deep reinforcement learning (DRL) to jointly optimize the offloading strategy, and network resource allocation strategy to reduce latency for dependent computational tasks in fog computing. One of the major challenges of such problems is that there are multiple action dimensions, which makes it difficult to converge the network. Therefore, this paper uses the multi-Agent method to simplify the problem by splitting the complete offload decision action into three sub-Actions. We demonstrate through numerical simulations that the algorithm can effectively reduce the cost and also discuss the effects of the different number of devices and the different number of fog nodes on the cost.  © 2021 IEEE.

## 04 — Title Screening

**Title:** Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing
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
