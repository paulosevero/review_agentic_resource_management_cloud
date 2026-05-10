---
id: paper-0883
title: The Autonomous Scheduling Problem in Satellite Constellations for EO Missions. A Robust Distributed Optimization Approach
authors:
- De Angelis, Giulio
- Pietropaolo, Andrea
venue: Proceedings of the International Astronautical Congress, IAC
venue_type: conference
year: 2024
doi: 10.52202/078367-0039
url: https://www.scopus.com/pages/publications/85218441101?origin=resultslist
publisher: International Astronautical Federation, IAF
pages: 372--386
keywords:
- distributed intelligence
- Earth Observation operations
- inter-satellite link
- multi-agent optimization
- onboard computing
- robust optimization
- space autonomy
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0883 — The Autonomous Scheduling Problem in Satellite Constellations for EO Missions. A Robust Distributed Optimization Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Satellite operations, including tasking and commanding, are traditionally managed by ground-based mission control and planning centers. These centers leverage a comprehensive, system-wide perspective to determine operations and dispatch telecommands to orbiting satellites via TT&C ground stations. Accurate knowledge of the system’s status is crucial for scheduling and planning; however, as the scale of satellite constellations expands, maintaining this level of coordination becomes increasingly challenging, particularly in highly dynamic environments. Managing real-time status updates and future task scheduling for a large number of satellites becomes more demanding for a central coordinator. The rise of large-scale and mega-constellations in remote sensing and telecommunications calls for a significant shift in operational strategies. Advanced mission control and planning approaches must evolve beyond traditional centralized models. Critical enabling technologies, such as onboard satellite computing and inter-satellite communications, now make distributed and autonomous system operations feasible. By utilizing space-edge and cloud computing, intelligence can be decentralized across the constellation, reducing the dependence on a central control structure. This paper discusses the application of distributed optimization methods in multi-agent systems, where communication networks evolve dynamically based on orbital mechanics. Integer linear programming is employed to minimize system latency in Earth Observation missions by optimizing image acquisition and data downlink, with a robust version that accounts for uncertainties in local satellite constraints. We perform numerical simulations that model constellation dynamics, acquisition, downlink, and communications to provide a comprehensive assessment of system performance. © 2024 International Astronautical Federation, IAF. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0883.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
