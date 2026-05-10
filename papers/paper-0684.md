---
id: paper-0684
title: Multi-objective fuzzy approach to scheduling and offloading workflow tasks in Fog–Cloud computing
authors:
- Mokni, Marwa
- Yassa, Sonia
- Hajlaoui, Jalel Eddine
- Omri, Mohamed Nazih
- Chelouah, Rachid
venue: Simulation Modelling Practice and Theory
venue_type: journal
year: 2023
doi: 10.1016/j.simpat.2022.102687
url: https://www.scopus.com/pages/publications/85142754400?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cloud computing
- Fog computing
- Fuzzy inference system
- MAS
- Negotiation
- Optimization
- QoS
- Scheduling
- Workflow
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

# paper-0684 — Multi-objective fuzzy approach to scheduling and offloading workflow tasks in Fog–Cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog–Cloud computing environments have become attractive focus areas for scheduling workflow automation of different processes in different domains. The planning of workflow containing tasks having different characteristics, in Fog-Cloud computing, can affect the gain in terms of resources. The main objective of this article is to efficiently schedule a workflow in such heterogeneous environments under conflicting constraints between the user and the resource provider. In this paper, we propose a new approach to designing an environment that combines partitioning, sequencing, and scheduling algorithms while guaranteeing a multi-objective optimization of users’ and providers’ conflicting requirements. Our approach also integrates a distributed resolution with Multi-Agent System (MAS), in order to reduce the complexity of the problem, and a fuzzy inference system to deal with the uncertainty problem. To study and confirm the effectiveness of our approach, we conducted an experimental study on different data collections. We compared our approach with the main related approaches that we studied. The analysis of the obtained results clearly shows the limits of these studied approaches and confirms the performance of our approach, as well as its effectiveness in planning workflows on Fog–Cloud computing while taking into account the utilization of resources. In terms of Makespan, our solution recorded a reduction of 48% compared to the Energy Makespan Multi-Objective Optimization (EM-MOO) approach, and 41% compared to the Multi-Agent System based Genetic Algorithm (MAS-GA), while respecting the time constraint. © 2022 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0684.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
