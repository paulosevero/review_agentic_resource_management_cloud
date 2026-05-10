---
id: paper-0293
title: A cloud-based computational platform to manage risk and resilience of buildings and infrastructure systems
authors:
- Hackl, Jürgen
venue: Proceedings of the 31st European Safety and Reliability Conference, ESREL 2021
venue_type: conference
year: 2021
doi: 10.3850/978-981-18-2016-8_054-cd
url: https://www.scopus.com/pages/publications/85135436766?origin=resultslist
publisher: Research Publishing, Singapore
pages: '369'
keywords:
- cloud computing
- computational modelling
- digital twin
- disaster response
- HPC
- infrastructure management
- multi-hazards
- natural hazards
- resilience
- risk
- simulation
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

# paper-0293 — A cloud-based computational platform to manage risk and resilience of buildings and infrastructure systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The primary responsibility of asset managers is to ensure that their assets, such as buildings and infrastructure systems, provide adequate service needed. They have the continuous task of executing interventions to help prevent the loss of service and to restore service after it is lost, which can happen, for example, due to natural hazards such as floods, landslides, and earthquakes. In other words, they have the continuous task of making their assets resilient. To provide optimal mitigation measures, the risk and resilience of buildings and infrastructure systems have to be assessed. Therefore, different computational models from different disciplines have to be executed, and their results have to be brought together in order to make profound quantitative statements. Nonetheless, conducting such assessments can be a particularly challenging task due to numerous scenarios and chains of interrelated events that require considerations, the modelling of these events, the relationships among them, and the availability of support tools to run the models in an integrated way. Cloud-based simulations offer a solution to this problem, by providing almost unlimited storage and computational resources; furthermore, the cloud enables and facilitates collaborative approaches, and provide a Digital Twin of the assets for prediction and disaster management. This paper introduces a computational platform which enables cloud-based simulations to estimate risk and resilience of buildings and infrastructure systems. The setup of the computational platform follows the principles and ideas of systems engineering and allows to incorporate and link different events. The platform is centred on the integration of the spatial and temporal attributes of the events that need to be modelled to estimate the risk and resilience. Furthermore, the platform supports the inclusion of the uncertainty of these events and the propagation of these uncertainties throughout the risk and resilience modelling. Through the modular implementation of the simulation platform, the updating and swapping of computational models from different disciplines-according to the needs of engineers and decision-makers-is supported. The platform enables high-performance computing for simulation-based risk and resilience assessments, considering the occurrence of time-varying multi-hazard events affecting buildings and infrastructure systems. Beyond the modelling of complex scenarios, the proposed computational platform provide technologies and tools to help decision-makers in determining the best mitigation policies. This is reached by collaborative technologies like data sharing, real-time collaboration, a continual process of creating, editing, and commenting, as well as a cheap and easy way of creating visuals and reports. © ESREL 2021. Published by Research Publishing, Singapore.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0293.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
