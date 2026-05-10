---
id: paper-0036
title: 'Cantav: A cloud centric framework for navigation and control of autonomous road vehicles'
authors:
- Sandeep, P.R.
- Yerragudi, V.S.
- Gangadhar, N.D.
venue: Proceedings - 2017 IEEE International Conference on Cloud Computing in Emerging Markets, CCEM 2017
venue_type: conference
year: 2017
doi: 10.1109/CCEM.2017.20
url: https://www.scopus.com/pages/publications/85049674963?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 99--106
keywords:
- Agent
- Autonomous vehicle
- Cloud computing
- Distributed control
- Dynamic routing
- Framework
- Navigation
- Obstacle avoidance
- Simulation
- Traffic Control
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0036 — Cantav: A cloud centric framework for navigation and control of autonomous road vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Autonomous vehicles are becoming a new trend in automotive industry. The rapid developments in this field portend to a future where current vehicles are replaced by autonomous ones. There is a need for sophisticated and responsive traffic control mechanisms for such future systems. There is also a need for generic framework for developing and studying autonomous road traffic systems. This paper describes the design and development of a Cloud centric Architecture and simulation framework for Navigation and Traffic control of Autonomous Vehicles (CANTAV) for developing navigation and control systems for automated vehicles and vehicular traffic. The framework is based on message passing which is extensible. It is designed to provide facilities for navigating the vehicle, clear traffic congestion by re-routing traffic. As interfacing such an architecture with real world autonomous vehicles is not feasible, and no existing simulation framework supports such an architecture, an agent based simulation framework, CANTAV simulation framework, is developed for simulation and visualisation of road networks and autonomous vehicular traffic on them. The developed system was tested and validated successfully using several scenarios. Performance of the system is analysed from the system and vehicle perspectives for different transportation network and vehicle arrangements in the system. © 2017 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0036.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
