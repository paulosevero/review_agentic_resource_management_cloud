---
id: "paper-904"
title: "Caching Video by Distributed Multi-agent Reinforcement Learning"
authors: ["Fang, Lei", "Liu, Wenbin", "Wang, En", "Yang, Funing"]
year: 2024
venue: "2024 4th International Conference on Neural Networks, Information and Communication Engineering, NNICE 2024"
venue_type: "conference"
doi: "10.1109/NNICE61279.2024.10498437"
url: "https://www.scopus.com/pages/publications/85192507911?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "170--174"
keywords: ["decentralize training", "deep learning", "multi-agent reinforcement learning", "video chching"]
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

# paper-904 — Caching Video by Distributed Multi-agent Reinforcement Learning

## Metadata

- **Authors:** Fang, Lei and Liu, Wenbin and Wang, En and Yang, Funing
- **Year:** 2024
- **Venue:** 2024 4th International Conference on Neural Networks, Information and Communication Engineering, NNICE 2024
- **DOI:** 10.1109/NNICE61279.2024.10498437
- **URL:** https://www.scopus.com/pages/publications/85192507911?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 170--174
- **Language:** English
- **Keywords:** decentralize training; deep learning; multi-agent reinforcement learning; video chching

### Abstract

Mobile edge computing is a new paradigm to support video caching, aiming to optimize the user's viewing experience. However, existing works have focused on centralized algorithms, which require a powerful computing center to do scheduling to determine the video content that should be stored on which edge server closest to the user. Therefore, these approach put too much pressure on the backbone network, resulting in increased application costs and reducing its usefulness. To address the above limitation, we consider this scenario without any computing center and propose an innovative distributed video caching algorithm that is different from the previous centralized methods. In our scenario, we no longer need the support of the computing center, but only consider the information interaction between the edge nodes. Our objective is to reduce the average latency to improve the user experience. To this end, we propose a novel decentralized multi-agent reinforcement learning (MARL) algorithm, Distributed Algorithm Without Center (DAWC), implementing in decentralized training and decentralized execution. The main difference between our algorithm and the existing MARL algorithm is that our algorithm is trained distributed, while other algorithms are trained centrally. We further utilize a neural communication protocol to reduce information loss and non-stationary by introducing hidden state and differentiable message encoding and extracting functions. Extensive performance results show that the performance of DAWC is not significantly weaker than that of MARL algorithm with central participation in centralized learning, but other independent learning algorithm and random offloading strategy. © 2024 IEEE.

## 04 — Title Screening

**Title:** Caching Video by Distributed Multi-agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Caching Video by Distributed Multi-agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Caching Video by Distributed Multi-agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
