---
id: paper-1396
title: Optimal Revenue Maximization of Electric Vehicle Fleet under Charging and Computing Network
authors:
- Anuradhakannan
- Tumuluru, Vamsi Krishna
venue: International Conference on Engineering and Emerging Technologies, ICEET
venue_type: conference
year: 2025
doi: 10.1109/ICEET67911.2025.11423929
url: https://www.scopus.com/pages/publications/105035375808?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Charging
- Computation
- discharging
- edge server
- EV fleet
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1396 — Optimal Revenue Maximization of Electric Vehicle Fleet under Charging and Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Electric Vehicles (EVs) are projected to account for over 25% of global new vehicle sales by 2025 [1]. Beyond serving as energy consumers, EVs are increasingly being recognized for their role in real-time task offloading and data services. The emerging paradigm of EVs powered by charging and computation stations introduces an infrastructure that supports the bidirectional flow of both energy and information to and from EVs. These EVs are intended as mobile edge devices, capable of processing data streams from sensors, other vehicles, and nearby RSUs during transit as well as their parking periods. The vehicles can also participate in vehicle-to-grid (V2G) interactions. This work presents a joint optimization framework for the coordinated fleet-level scheduling of charging, discharging, and computation at geographically distributed charging and computation stations (CCS). The proposed model integrates time-of-use (TOU) energy pricing, state-of-charge (SOC) dynamics, and depot-level constraints to enable adaptive allocation of energy and computational workloads. The problem is formulated as a mixed integer linear programming model. The simulation results on a representative 3 EV fleets enhanced revenue maximization through strategic charging and discharging and also assisted the edge server in the CCS by offering its idle computing resources. The findings also illustrate the ability of electric vehicles to serve as mobile edge nodes, strengthening their role as dynamic cyber-physical agents in next-generation intelligent transportation systems. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1396.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
