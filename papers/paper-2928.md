---
id: "paper-2928"
title: "Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers"
authors: ["Zhao, Yu", "Wang, Cheng", "Yan, Chungang", "Li, Xiaoli", "Jiang, Changjun"]
year: 2026
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2026.3656552"
url: "https://www.scopus.com/pages/publications/105028437042?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Computing service scheduling", "data augmentation", "distributed data centers", "heuristic guidance", "multi-agent deep reinforcement learning"]
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

# paper-2928 — Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers

## Metadata

- **Authors:** Zhao, Yu and Wang, Cheng and Yan, Chungang and Li, Xiaoli and Jiang, Changjun
- **Year:** 2026
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2026.3656552
- **URL:** https://www.scopus.com/pages/publications/105028437042?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Computing service scheduling; data augmentation; distributed data centers; heuristic guidance; multi-agent deep reinforcement learning

### Abstract

With the rapid growth of computing services in distributed data centers, efficient scheduling needs to consider workload dynamics, resource fluctuations, and diverse optimization preferences while maintaining service quality and system efficiency. Multi-Agent Deep Reinforcement Learning (MADRL) offers a decentralized and adaptive paradigm that enables agents to learn local scheduling policies aligned with individual objectives while collectively improving global performance. However, existing MADRL approaches often suffer from low sample efficiency and limited generalization under dynamic and heterogeneous conditions. This paper proposes a Heuristic-guided Multi-Agent deep Reinforcement learning (H-MAR) approach for computing service scheduling. H-MAR is a novel multi-agent learning framework where heuristic functions act as structured priors to guide personalized policy optimization, and data augmentation is employed to enhance experience coverage and policy robustness. Moreover, we provide a modified Decentralized Partially Observable Markov Decision Process (Dec-POMDP) formulation to support the theoretical analysis of H-MAR. Experiments on real-world Alibaba cluster traces show that H-MAR outperforms representative baselines in the success rate of instance creation, load balancing, and energy consumption, validating its effectiveness for adaptive and robust computing service delivery. © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers
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
