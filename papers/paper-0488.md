---
id: paper-0488
title: Inter-continental Data Centre Power Load Balancing for Renewable Energy Maximisation
authors:
- Rahmani, Rasoul
- Moser, Irene
- Cricenti, Antonio L.
venue: Electronics (Switzerland)
venue_type: journal
year: 2022
doi: 10.3390/electronics11101564
url: https://www.scopus.com/pages/publications/85129799727?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- data centre load balancing
- green data centre
- multi-agent systems
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

# paper-0488 — Inter-continental Data Centre Power Load Balancing for Renewable Energy Maximisation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The ever increasing popularity of Cloud and similar services pushes the demand for data centres, which have a high power consumption. In an attempt to increase the sustainability of the power generation, data centres have been fed by microgrids which include renewable generation— so-called ‘green data centres’. However, the peak load of data centres often does not coincide with solar generation, because demand mostly peaks in the evening. Shifting power to data centres incurs transmission losses; shifting the data transmission has no such drawback. We demonstrate the effec-tivity of computational load shifting between data centres located in different time zones using a case study that balances demands between three data centres on three continents. This study contributes a method that exploits the opportunities provided by the varied timing of peak solar generation across the globe, transferring computation load to data centres that have sufficient renewable energy whenever possible. Our study shows that balancing computation loads between three green data centres on three continents can improve the use of renewables by up to 22%. Assuming the grid energy does not include renewables, this amounts to a 13% reduction in CO<sub>2</sub> emissions. © 2022 by the authors. Licensee MDPI, Basel, Switzerland.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0488.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
