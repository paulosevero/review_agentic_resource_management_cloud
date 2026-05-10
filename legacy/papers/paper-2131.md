---
id: "paper-2131"
title: "A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings"
authors: ["Shi, Shanrui", "Miyata, Shohei", "Akashi, Yasunori"]
year: 2025
venue: "Energy and Buildings"
venue_type: "journal"
doi: "10.1016/j.enbuild.2025.116089"
url: "https://www.scopus.com/pages/publications/105009829755?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Distributed optimal control", "Energy efficiency", "Indoor environmental quality", "Multi-agent system", "Multizone VAV system", "Nash optimization"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Out of scope"

---

# paper-2131 — A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings

## Metadata

- **Authors:** Shi, Shanrui and Miyata, Shohei and Akashi, Yasunori
- **Year:** 2025
- **Venue:** Energy and Buildings
- **DOI:** 10.1016/j.enbuild.2025.116089
- **URL:** https://www.scopus.com/pages/publications/105009829755?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Distributed optimal control; Energy efficiency; Indoor environmental quality; Multi-agent system; Multizone VAV system; Nash optimization

### Abstract

Multi-agent-based distributed optimal control can effectively balance indoor environmental quality and energy consumption in multizone variable air volume (VAV) systems, while reducing computational load and enhancing scalability. However, existing methods often optimize airflow setpoints without fully addressing the coupled dynamics in multizone VAV systems and frequently rely on simplified models. To overcome these limitations, this study proposes a hybrid multiagent distributed control strategy that directly optimizes actuators by jointly considering indoor air temperature, CO<sub>2</sub> concentration, and energy use. The strategy decomposes the optimization problem into subproblems assigned to zone-level and system-level agents. Each zone agent employs a metaheuristic-based framework for damper control, coordinated through a Nash equilibrium-based scheme. Meanwhile, a model-free system agent dynamically adjusts the supply fan and the outdoor air damper. Two test cases with different occupancy patterns are evaluated in a virtual testbed. Results show that under normal occupancy conditions, the distributed strategy performs comparably to the centralized controller, whereas under unbalanced occupant distributions, it outperforms the centralized approach in both indoor climate management and energy efficiency. In both cases, the average computational load is reduced by more than 80 % relative to the centralized method. Additionally, the proposed strategy offers a tunable trade-off between computational complexity and control performance, making it suitable for resource-constrained edge devices. By leveraging advancing edge-computing capabilities, this hybrid multiagent approach provides an effective and decentralized solution for multizone VAV control in smart building systems. © 2025 The Author(s)

## 04 — Title Screening

**Title:** A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
