---
id: paper-0263
title: A novel robust smart energy management and demand reduction for smart homes based on internet of energy
authors:
- Alhasnawi, Bilal Naji
- Jasim, Basil H.
- Rahman, Zain-Aldeen S. A.
- Siano, Pierluigi
venue: Sensors
venue_type: journal
year: 2021
doi: 10.3390/s21144756
url: https://www.scopus.com/pages/publications/85109527584?origin=resultslist
publisher: MDPI AG
pages: ''
keywords:
- Dynamic electricity price
- Home devices
- Internet of things
- MQTT protocol
- Optimization algorithms
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0263 — A novel robust smart energy management and demand reduction for smart homes based on internet of energy

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In residential energy management (REM), Time of Use (ToU) of devices scheduling based on user-defined preferences is an essential task performed by the home energy management con-troller. This paper devised a robust REM technique capable of monitoring and controlling residential loads within a smart home. In this paper, a new distributed multi-agent framework based on the cloud layer computing architecture is developed for real-time microgrid economic dispatch and monitoring. In this paper the grey wolf optimizer (GWO), artificial bee colony (ABC) optimization algorithm-based Time of Use (ToU) pricing model is proposed to define the rates for shoulder-peak and on-peak hours. The results illustrate the effectiveness of the proposed the grey wolf optimizer (GWO), artificial bee colony (ABC) optimization algorithm based ToU pricing scheme. A Raspberry Pi3 based model of a well-known test grid topology is modified to support real-time communication with open-source IoE platform Node-Red used for cloud computing. Two levels communication system connects microgrid system, implemented in Raspberry Pi3, to cloud server. The local communication level utilizes IP/TCP and MQTT is used as a protocol for global communication level. The results demonstrate and validate the effectiveness of the proposed technique, as well as the capability to track the changes of load with the interactions in re-al-time and the fast convergence rate. © 2021 by the authors. Licensee MDPI, Basel, Switzerland.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0263.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
