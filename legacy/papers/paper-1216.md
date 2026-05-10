---
id: "paper-1216"
title: "Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning"
authors: ["Tan, Jing", "Khalili, Ramin", "Karl, Holger"]
year: 2024
venue: "IEEE Transactions on Intelligent Transportation Systems"
venue_type: "journal"
doi: "10.1109/TITS.2024.3378007"
url: "https://www.scopus.com/pages/publications/85189566821?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "10777--10789"
keywords: ["distributed systems", "multi-objective", "reinforcement learning", "V2X"]
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
    final_score: 0.25
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1216 — Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning

## Metadata

- **Authors:** Tan, Jing and Khalili, Ramin and Karl, Holger
- **Year:** 2024
- **Venue:** IEEE Transactions on Intelligent Transportation Systems
- **DOI:** 10.1109/TITS.2024.3378007
- **URL:** https://www.scopus.com/pages/publications/85189566821?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 10777--10789
- **Language:** English
- **Keywords:** distributed systems; multi-objective; reinforcement learning; V2X

### Abstract

The Intelligent Transportation System (ITS) environment is known to be dynamic and distributed, where participants (vehicle users, operators, etc.) have multiple, changing and possibly conflicting objectives. Although Reinforcement Learning (RL) algorithms are commonly applied to optimize ITS applications such as resource management and offloading, most RL algorithms focus on single objectives. In many situations, converting a multi-objective problem into a single-objective one is impossible, intractable or insufficient, making such RL algorithms inapplicable. We propose a multi-objective, multi-agent reinforcement learning (MARL) algorithm with high learning efficiency and low computational requirements, which automatically triggers adaptive few-shot learning in a dynamic, distributed and noisy environment with sparse and delayed reward. We test our algorithm in an ITS environment with edge cloud computing. Empirical results show that the algorithm is quick to adapt to new environments and performs better in all individual and system metrics compared to the state-of-the-art benchmark. Our algorithm also addresses various practical concerns with its modularized and asynchronous online training method. In addition to the cloud simulation, we test our algorithm on a single-board computer and show that it can make inference in 6 milliseconds.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning

### Machine Screening

- **Final Score:** 0.25 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
