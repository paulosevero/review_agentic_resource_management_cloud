---
id: paper-2725
title: 'Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models'
authors:
- Muller, Kilian
- Ruhland, Tim
- Guimaraes, Carlos
- Kaiser, Joachim
- Franchi, Norman
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2026
doi: 10.1109/OJCOMS.2026.3672750
url: https://www.scopus.com/pages/publications/105032783783?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2733--2764
keywords:
- Delay-tolerant networking
- edge computing
- Internet of Things (IoT)
- probabilistic forecasting
- task offloading
- time-series foundation models
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-2725 — Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low-power, resource-constrained Internet of Things (IoT) devices are increasingly used for remote monitoring and predictive maintenance, but many modern Machine Learning (ML) workloads exceed their compute and energy budgets. Offloading tasks to nearby edge servers is attractive, yet many real deployments rely on Delay-/Disruption-Tolerant Networking (DTN) via data mules such as public transport or Low Earth Orbit (LEO) satellites, where connectivity is intermittent, stochastic, and often difficult to predict. This paper introduces Firefly, an edge-driven, probabilistic task-offloading framework that enables constrained IoT devices to make deadline-aware offloading decisions over such DTN links. Firefly passively monitors bundle transmissions and aggregates them into contacts, time intervals during which the device can communicate with an edge node. At the edge, Time-Series Foundation Models (TSFMs) are used to forecast distributions over future contact start time, duration, and end-to-end latency for both uplink and downlink. These forecasts are compressed into small probabilistic lookup tables that are periodically sent to the devices. On-device, a lightweight probabilistic forecaster uses these tables to estimate the success probability and response-time distribution of offloading a given task under a configurable risk threshold and soft real-time deadline, and chooses between local execution and offload. We further derive analytical expressions for offloading success probability under our contact model, which we use to instantiate a simple greedy decision policy. We evaluate Firefly using event-driven simulations parametrized by real commuter-train timetables and real LEO satellite orbits. In our train-based DTN scenario, Firefly achieves up to 27% higher task-offloading success rates compared to a Schedule-Aware Bundle Routing (SABR) baseline, and in the satellite scenario up to 19% higher, while remaining executable on constrained devices without any on-device heavy ML.  © 2026 The Authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Foundation Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Foundation Models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Foundation Models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Foundation Models" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_foundation_model, matched_substring: "Foundation Models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2725.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
