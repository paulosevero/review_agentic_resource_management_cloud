---
id: paper-2619
title: 'Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents'
authors:
- Hwang, Raymoon
- Lee, Jaechul
- Kim, Junghwan
- Moon, Il
- Oh, Min
venue: Energy and AI
venue_type: journal
year: 2026
doi: 10.1016/j.egyai.2026.100727
url: https://www.scopus.com/pages/publications/105034738510?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Artificial intelligence agents
- Autonomous digital twin
- Gas turbine combined cycle
- Reinforcement learning
- Supervisory control loops
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2619 — Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integral control, reinforcement learning, and reinforcement learning with agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AbstractGas turbine combined cycle plants are expected to remain central to low carbon power generation while meeting electricity demand from artificial intelligence and data centers. To address these challenges, gas turbine combined cycle operation must evolve beyond rule-based control toward autonomy. This study develops a proof-of-concept autonomous digital twin for supervisory control loops in a gas turbine combined cycle plant that integrates reinforcement learning with supervisory agents and uses this digital twin to perform a simulation-based comparative evaluation of controllers under three representative scenarios: load ramping, fuel switching, and sensor faults. The digital twin is anchored to a publicly documented natural gas combined cycle reference plant from the United States National Energy Technology Laboratory, providing transparent steady-state validation. Forward validation is additionally performed using operational data from a Korean commercial Gas Turbine Combined Cycle plant. Proportional integral and reinforcement learning controllers are implemented as baselines, while reinforcement learning with agents incorporates modules for constraint enforcement, sensor arbitration, and transition stabilization. Results show that proportional integral control maintains safety but is slow and lacks fault tolerance, whereas reinforcement learning improves adaptability but violates turbine inlet temperature constraints and fails under sensor anomalies. Reinforcement learning with agents uniquely balances speed, safety, and resilience, achieving smooth load ramps without violations, stable fuel transitions, and reliable recovery under faulty sensing. Synthesizing these results into an autonomy framework defined by adaptability, resilience, diagnostic accuracy, and robustness, the study demonstrates that reinforcement learning with agents overcomes the performance–safety trade-off and provides a reproducible pathway toward autonomous gas turbine combined cycle plants. © 2026 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2619.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
