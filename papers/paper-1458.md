---
id: "paper-1458"
title: "Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration"
authors: ["Che, Chang", "Xiang, Luping", "Hu, Jie", "Yang, Kun"]
year: 2025
venue: "International Conference on Communication Technology Proceedings, ICCT"
venue_type: "conference"
doi: "10.1109/ICCT67417.2025.11374267"
url: "https://www.scopus.com/pages/publications/105034107938?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1913--1918"
keywords: ["causal inference", "Digital twin", "large-scale networks", "multi-agent reinforcement learning", "service migration"]
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

# paper-1458 — Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration

## Metadata

- **Authors:** Che, Chang and Xiang, Luping and Hu, Jie and Yang, Kun
- **Year:** 2025
- **Venue:** International Conference on Communication Technology Proceedings, ICCT
- **DOI:** 10.1109/ICCT67417.2025.11374267
- **URL:** https://www.scopus.com/pages/publications/105034107938?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1913--1918
- **Language:** English
- **Keywords:** causal inference; Digital twin; large-scale networks; multi-agent reinforcement learning; service migration

### Abstract

Dynamic service migration is essential for guaranteeing quality of service (QoS) for mobile users in multi-access edge computing (MEC). However, conventional reinforcement learning and other strategies frequently result in suboptimal policies. These methods are unable to differentiate between actual cause-and-effect relationships and fake patterns due to their reliance on correlational data, resulting in inefficient and expensive migrations. This paper introduces a novel digital twinassisted causal multi-agent reinforcement learning (DT-CausalMARL) framework to address this fundamental limitation. We change the optimization objective from minimizing direct system cost to maximizing the causal gain of migration actions. This is accomplished by employing a digital twin as a counterfactual analysis engine to assess the actual consequences of decisions in comparison to a baseline policy. This causal gain is subsequently employed as a robust reward signal by a causal multi-agent deep deterministic policy gradient (Causal-MADDPG) algorithm to train cooperative agents. Our framework outperforms standard MARL baselines by reducing harmful 'regretful migrations' and improving system stability under dynamic traffic loads. © 2025 IEEE.

## 04 — Title Screening

**Title:** Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration
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
