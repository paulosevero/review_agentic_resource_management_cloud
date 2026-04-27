---
id: "paper-2347"
title: "Offloading in V2X with road side units: Deep reinforcement learning"
authors: ["Yahya, Widhi", "Lin, Ying-Dar", "Marzuk, Faysal", "Cho\u0142da, Piotr", "Lai, Yuan-Cheng"]
year: 2025
venue: "Vehicular Communications"
venue_type: "journal"
doi: "10.1016/j.vehcom.2024.100862"
url: "https://www.scopus.com/pages/publications/85211235560?origin=resultslist"
publisher: "Elsevier Inc."
pages: ""
keywords: ["5G", "AI", "Mobile edge computing", "Offloading", "Reinforcement learning", "V2X"]
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

# paper-2347 — Offloading in V2X with road side units: Deep reinforcement learning

## Metadata

- **Authors:** Yahya, Widhi and Lin, Ying-Dar and Marzuk, Faysal and Chołda, Piotr and Lai, Yuan-Cheng
- **Year:** 2025
- **Venue:** Vehicular Communications
- **DOI:** 10.1016/j.vehcom.2024.100862
- **URL:** https://www.scopus.com/pages/publications/85211235560?origin=resultslist
- **Publisher:** Elsevier Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 5G; AI; Mobile edge computing; Offloading; Reinforcement learning; V2X

### Abstract

Traffic offloading is crucial for reducing computing latency in distributed edge systems such as vehicle-to-everything (V2X) networks, which use roadside units (RSUs) and access network mobile edge computing (AN-MEC) with ML agents. Traffic offloading is part of the control plane problem, which requires fast decision-making in complex V2X systems. This study presents a novel ratio-based offloading strategy using the twin delayed deep deterministic policy gradient (TD3) algorithm to optimize offloading ratios in a two-tier V2X system, enabling computation at both RSUs and the edge. The offloading optimization covers both vertical and horizontal offloading, introducing a continuous search space that needs fast decision-making to accommodate fluctuating traffic in complex V2X systems. We developed a V2X environment to evaluate the performance of the offloading agent, incorporating latency models, state and action definitions, and reward structures. A comparative analysis with metaheuristic simulated annealing (SA) is conducted, and the impact of single versus multiple offloading agents with deployment options at a centralized central office (CO) is examined. Evaluation results indicate that TD3's decision time is five orders of magnitude faster than SA. For 10 and 50 sites, SA takes 602 and 20,421 seconds, respectively, while single-agent TD3 requires 4 to 24 milliseconds and multi-agent TD3 takes 1 to 3 milliseconds. The average latency for SA ranges from 0.18 to 0.32 milliseconds, single-agent TD3 from 0.26 to 0.5 milliseconds, and multi-agent TD3 from 0.22 to 0.45 milliseconds, demonstrating that TD3 approximates SA performance with initial training. © 2024 Elsevier Inc.

## 04 — Title Screening

**Title:** Offloading in V2X with road side units: Deep reinforcement learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Offloading in V2X with road side units: Deep reinforcement learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Offloading in V2X with road side units: Deep reinforcement learning
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
