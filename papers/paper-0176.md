---
id: paper-0176
title: A general framework for energy-efficient cloud computing mechanisms
authors:
- Antoniadis, Antonios
- Cristi, Andrés
- Oosterwijk, Tim
- Sgouritsa, Alkmini
venue: Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems, AAMAS
venue_type: conference
year: 2020
doi: ''
url: https://www.scopus.com/pages/publications/85096646968?origin=resultslist
publisher: International Foundation for Autonomous Agents and Multiagent Systems (IFAAMAS)
pages: 70--78
keywords:
- Cloud computing
- Dynamic speed scaling
- Energy efficiency
- Mechanism design
- Price of Anarchy
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0176 — A general framework for energy-efficient cloud computing mechanisms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We present a general model for the operation of a cloud computing server comprised of one or more speed-scalable processors. Typically, tasks are submitted to such a cloud computing server in an online fashion, and the server operator has to schedule the tasks and decides on payments without knowledge about the tasks arriving in the future. Although very natural, this cloud computing problem on speed-scalable processors has not been studied from a mechanism design perspective in the online setting. We provide a mechanism for this setting, both for a single and multiprocessor environment, that has several desirable properties: (1) the induced game admits a subgame perfect equilibrium in pure strategies and therefore a pure Nash equilibrium, (2) the Price of Anarchy is constant, (3) the mechanism is budget balanced, i.e., the sum of the payments of the agents is equal to the total energy costs, (4) the communication complexity is low, (5) the mechanism is computationally tractable for both the service operator and the agents, and (6) the agents' payment is also intuitive and easy to communicate to them. We also provide a second mechanism with a better Price of Anarchy, which in turn is more involved to implement. We are able to extend our mechanisms and results to the Bayesian setting, where the type of each agent is drawn independently from some underlying distribution and agents are minimizing their expected costs. In this setting we also show the same approximation factor of our mechanism as in the basic online setting in both the single and the multiprocessor environment. © 2020 International Foundation for Autonomous.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0176.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
