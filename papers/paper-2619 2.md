---
id: "paper-2619"
title: "Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents"
authors: ["Hwang, Raymoon", "Lee, Jaechul", "Kim, Junghwan", "Moon, Il", "Oh, Min"]
year: 2026
venue: "Energy and AI"
venue_type: "journal"
doi: "10.1016/j.egyai.2026.100727"
url: "https://www.scopus.com/pages/publications/105034738510?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Artificial intelligence agents", "Autonomous digital twin", "Gas turbine combined cycle", "Reinforcement learning", "Supervisory control loops"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2619 — Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents

## Metadata

- **Authors:** Hwang, Raymoon and Lee, Jaechul and Kim, Junghwan and Moon, Il and Oh, Min
- **Year:** 2026
- **Venue:** Energy and AI
- **DOI:** 10.1016/j.egyai.2026.100727
- **URL:** https://www.scopus.com/pages/publications/105034738510?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Artificial intelligence agents; Autonomous digital twin; Gas turbine combined cycle; Reinforcement learning; Supervisory control loops

### Abstract

AbstractGas turbine combined cycle plants are expected to remain central to low carbon power generation while meeting electricity demand from artificial intelligence and data centers. To address these challenges, gas turbine combined cycle operation must evolve beyond rule-based control toward autonomy. This study develops a proof-of-concept autonomous digital twin for supervisory control loops in a gas turbine combined cycle plant that integrates reinforcement learning with supervisory agents and uses this digital twin to perform a simulation-based comparative evaluation of controllers under three representative scenarios: load ramping, fuel switching, and sensor faults. The digital twin is anchored to a publicly documented natural gas combined cycle reference plant from the United States National Energy Technology Laboratory, providing transparent steady-state validation. Forward validation is additionally performed using operational data from a Korean commercial Gas Turbine Combined Cycle plant. Proportional integral and reinforcement learning controllers are implemented as baselines, while reinforcement learning with agents incorporates modules for constraint enforcement, sensor arbitration, and transition stabilization. Results show that proportional integral control maintains safety but is slow and lacks fault tolerance, whereas reinforcement learning improves adaptability but violates turbine inlet temperature constraints and fails under sensor anomalies. Reinforcement learning with agents uniquely balances speed, safety, and resilience, achieving smooth load ramps without violations, stable fuel transitions, and reliable recovery under faulty sensing. Synthesizing these results into an autonomy framework defined by adaptability, resilience, diagnostic accuracy, and robustness, the study demonstrates that reinforcement learning with agents overcomes the performance–safety trade-off and provides a reproducible pathway toward autonomous gas turbine combined cycle plants. © 2026 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

## 04 — Title Screening

**Title:** Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents
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
