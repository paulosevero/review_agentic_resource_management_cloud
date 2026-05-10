---
id: paper-2524
title: 'FALCON: Fanet-Aware Learning and digital twin CONtrol framework'
authors:
- Caruso, Andrea
- Grasso, Christian
- Raftopoulos, Raoul
- Schembra, Giovanni
venue: Computer Communications
venue_type: journal
year: 2026
doi: 10.1016/j.comcom.2026.108481
url: https://www.scopus.com/pages/publications/105033412337?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cloud
- Edge
- FANET
- Network digital twin
- Smart agents
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2524 — FALCON: Fanet-Aware Learning and digital twin CONtrol framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid evolution of telecommunication networks is leading to increasingly complex systems, requiring adaptive, flexible, and intelligent mechanisms for resource management, orchestration, and access control. In this context, the Network Digital Twin (NDT) paradigm emerges as a powerful tool to model the behavior of devices, communication links, operating environments, and applications in complex networks. This paper introduces FALCON, a Digital-Twin-based orchestration framework designed to optimize horizontal offloading in UAV-based Flying Ad Hoc Networks (FANETs) providing edge computing services to ground devices in remote areas. FALCON integrates multiple Smart Agents (DQN, A2C, PPO) running concurrently on the Digital Twin to dynamically determine the optimal offloading probabilities. A proof-of-concept demonstrates how the framework performs real-time What-if Scenario analyses and adapts to varying workload and channel conditions. Numerical results highlight the gains achieved through coordinated model selection and reuse, showing reduced end-to-end delay and faster convergence compared to standalone DRL-based controllers. © 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2524.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
