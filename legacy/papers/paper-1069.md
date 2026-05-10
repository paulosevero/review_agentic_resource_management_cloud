---
id: "paper-1069"
title: "Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach"
authors: ["Liu, Wenshuai", "Fu, Yaru", "Guo, Yongna", "Lee Wang, Fu", "Sun, Wen", "Zhang, Yan"]
year: 2024
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2024.3452689"
url: "https://www.scopus.com/pages/publications/85204248889?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "17294--17309"
keywords: ["Digital twin (DT)", "DT migration", "DT synchronization", "heterogeneous agent proximal policy optimization (HAPPO)", "multi-access edge computing (MEC)", "resource allocation"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1069 — Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Liu, Wenshuai and Fu, Yaru and Guo, Yongna and Lee Wang, Fu and Sun, Wen and Zhang, Yan
- **Year:** 2024
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2024.3452689
- **URL:** https://www.scopus.com/pages/publications/85204248889?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 17294--17309
- **Language:** English
- **Keywords:** Digital twin (DT); DT migration; DT synchronization; heterogeneous agent proximal policy optimization (HAPPO); multi-access edge computing (MEC); resource allocation

### Abstract

Digital twins (DTs) have emerged as a promising enabler for representing the real-time states of physical worlds and realizing self-sustaining systems. In practice, DTs of physical devices, such as mobile users (MUs), are commonly deployed in multi-access edge computing (MEC) networks for the sake of reducing latency. To ensure the accuracy and fidelity of DTs, it is essential for MUs to regularly synchronize their status with their DTs. However, MU mobility introduces significant challenges to DT synchronization. Firstly, MU mobility triggers DT migration which could cause synchronization failures. Secondly, MUs require frequent synchronization with their DTs to ensure DT fidelity. Nonetheless, DT migration among MEC servers, caused by MU mobility, may occur infrequently. Accordingly, we propose a two-timescale DT synchronization and migration framework with reliability consideration by establishing a non-convex stochastic problem to minimize the long-term average energy consumption of MUs. We use Lyapunov theory to convert the reliability constraints and reformulate the new problem as a partially observable Markov decision-making process (POMDP). Furthermore, we develop a heterogeneous agent proximal policy optimization with Beta distribution (Beta-HAPPO) method to solve it. Numerical results show that our proposed Beta-HAPPO method achieves significant improvements in energy savings when compared with other benchmarks.  © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach
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
