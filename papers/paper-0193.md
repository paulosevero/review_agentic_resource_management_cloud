---
id: paper-0193
title: Real-time monitoring and operation of microgrid using distributed cloud–fog architecture
authors:
- Dabbaghjamanesh, Morteza
- Moeini, Amirhossein
- Kavousi-Fard, Abdollah
- Jolfaei, Alireza
venue: Journal of Parallel and Distributed Computing
venue_type: journal
year: 2020
doi: 10.1016/j.jpdc.2020.06.006
url: https://www.scopus.com/pages/publications/85088396418?origin=resultslist
publisher: Academic Press Inc.
pages: 15--24
keywords:
- Consensus
- Distributed optimization
- Energy management
- Fog computing
- Microgrid
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0193 — Real-time monitoring and operation of microgrid using distributed cloud–fog architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, a new distributed multi-agent framework based on the three layers’ fog computing architecture is developed for real-time microgrid economic dispatch and monitoring. To this end, the changes of load at any time will be tracked by the proposed technique, considering unit sudden exits and entries. Moreover, to make the system more realistic, different renewable energies, including photovoltaics (PVs), wind turbines (WTs), fuel cells (FCs), and microturbines (MT) are considered in the proposed technique. To overcome the complexity of the problem, by using advantages of fog computing, a new fast consensus-based optimization algorithm is used, which is modified based on the fuzzy adaptive leader technique. Finally, the proposed technique is simulated and tested on microgrids with 6 and 14 buses, respectively. Simulation results demonstrate and validate the effectiveness of the proposed technique, as well as the capability to track the changes of load with the interactions in real-time and the fast convergence rate. © 2020 Elsevier Inc.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0193.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
