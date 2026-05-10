---
id: paper-0549
title: Communication-Efficient Allocation of Multiple Indivisible Resources in a Federated Multi-Agent System
authors:
- Alam, Syed Eqbal
- Shukla, Dhirendra
venue: Proceedings of the IEEE Conference on Decision and Control
venue_type: conference
year: 2023
doi: 10.1109/CDC49753.2023.10384067
url: https://www.scopus.com/pages/publications/85175230798?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5279--5285
keywords:
- Distributed optimization
- electric vehicle charging
- indivisible resources
- multi-resource allocation
- optimal control
- smart city
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-0549 — Communication-Efficient Allocation of Multiple Indivisible Resources in a Federated Multi-Agent System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A federated multi-agent system is a multi-agent system wherein agents collaborate with a central server to optimize system goals without sharing their private information. We develop a communication-efficient solution to resource allocation problems for a population of agents coupled through multiple indivisible shared resources in a federated multi-agent system. The agents demand resources in a probabilistic way based on their local computation and preferences, and the agents receive either one unit of a resource or do not receive it. The agents are not required to share their cost functions or derivatives of cost functions with other agents or the central server. Optimal control of a population of such agents, subject to capacity constraints, is widely found in many application domains, such as smart energy systems, intelligent transportation systems, and edge computing, to name a few. We present convergence results using multi-time scale stochastic approximation techniques and an example of electric vehicle charging point allocation illustrating the efficacy of the developed solution.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0549.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
