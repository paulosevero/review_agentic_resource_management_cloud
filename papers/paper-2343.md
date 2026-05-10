---
id: paper-2343
title: Air Pollutant Traceability Based on Federated Learning of Edge Intelligent Perception Agents
authors:
- Xue, Jinping
- Hu, Xin
- Liu, Qiang
- Yin, Congbo
- Ni, Peitao
- Bo, Xinyu
venue: Sensors
venue_type: journal
year: 2025
doi: 10.3390/s25196119
url: https://www.scopus.com/pages/publications/105018893338?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- air pollutant traceability
- edge intelligent perception agent
- environmental perception
- Federated Learning
- long short-term memory
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

# paper-2343 — Air Pollutant Traceability Based on Federated Learning of Edge Intelligent Perception Agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Tracing the source of air pollution presents a significant challenge, especially in densely populated urban areas, because of the unpredictable and complex nature of aerodynamics. To address this issue, intelligent lamp posts have been developed with smart sensors and edge computing capabilities. These lamp posts serve as nodes in the EIPA (Edge Intelligent Perception Agent) network within urban campuses. These lamp posts aim to track air pollutants by employing a tracking algorithm that utilizes big data learning and Gaussian diffusion models. This approach focuses on monitoring the quality of urban air and identifying pollution sources, rather than relying solely on traditional CFD simulations for air pollution dispersion. The algorithm comprises three primary components: (1) the Federated Learning framework built on the EIPA system; (2) the LSTM model implemented on the edge nodes of the EIPA system; and (3) a genetic algorithm utilized for optimizing the model parameters. By using CFD simulations in a simulated city park, training data on air dynamic movements is gathered. The usefulness of the method for tracing air pollutants based on federated learning of edge intelligent perception agents is demonstrated by the outcomes of algorithm training. Experimental results show that, compared to the traditional genetic algorithm (GA) and LSTM + genetic algorithm, the proposed FL + LSTM + GA method significantly improves the pollution source positioning accuracy to 99.5% and reduces the average absolute error (MAE) of Gaussian model parameter estimation to 0.20. © 2025 by the authors.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2343.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
