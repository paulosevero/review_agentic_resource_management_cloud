---
id: "paper-297"
title: "Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning"
authors: ["Hu, Shucheng", "Ren, Tao", "Niu, Jianwei", "Hu, Zheyuan", "Xing, Guoliang"]
year: 2021
venue: "Proceedings - 2021 17th International Conference on Mobility, Sensing and Networking, MSN 2021"
venue_type: "conference"
doi: "10.1109/MSN53354.2021.00089"
url: "https://www.scopus.com/pages/publications/85128718512?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "575--583"
keywords: ["mobile edge computing", "multi-agent deep reinforcement learning", "task offloading"]
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

# paper-297 — Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning

## Metadata

- **Authors:** Hu, Shucheng and Ren, Tao and Niu, Jianwei and Hu, Zheyuan and Xing, Guoliang
- **Year:** 2021
- **Venue:** Proceedings - 2021 17th International Conference on Mobility, Sensing and Networking, MSN 2021
- **DOI:** 10.1109/MSN53354.2021.00089
- **URL:** https://www.scopus.com/pages/publications/85128718512?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 575--583
- **Language:** English
- **Keywords:** mobile edge computing; multi-agent deep reinforcement learning; task offloading

### Abstract

Recent years have witnessed the increasing popularity of mobile applications, e.g., virtual reality, unmanned driving, which are generally computation-intensive and latency-sensitive, posing a major challenge for resource-limited user equipment (UE). Mobile edge computing (MEC) has been proposed as a promising approach to alleviate the problem, by offloading mobile tasks to the edge server (ES) deployed in close proximity to UE. However, most existing task offloading algorithms are primarily based on centralized scheduling, which could suffer from the 'curse of dimensionality' in large MEC environments. To address this issue, this paper proposes a fully distributed task offloading approach based on multi-agent deep reinforcement learning, whose critic and actor neural networks are trained under the assistance of global and local network states, respectively. In addition, we design a model parameter aggregation mechanism, along with a normalized fine-tuned reward function, to further improve the learning efficiency of the training process. Simulation results show that our proposed approach could achieve substantial performance improvements over baseline approaches.  © 2021 IEEE.

## 04 — Title Screening

**Title:** Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
