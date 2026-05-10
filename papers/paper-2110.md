---
id: paper-2110
title: Sustainable, Situation-Aware Multi Objective Spatial Load Scheduling for Data Centers
authors:
- Schiller, Jonas
- Pruckner, Marco
venue: E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems
venue_type: conference
year: 2025
doi: 10.1145/3679240.3735100
url: https://www.scopus.com/pages/publications/105016345706?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 874--881
keywords:
- Data Centers
- Green IT
- Large Language Model
- Linear Program
- Load Shifting
- Situation Aware Optimization
- Sustainability
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2110 — Sustainable, Situation-Aware Multi Objective Spatial Load Scheduling for Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data centers are already among the largest consumers of electricity worldwide and recent advancements in Large Language Models (LLM) will further increase this demand. Through their operation, they are responsible for large amounts of indirect carbon emissions as well as direct and indirect water consumption. This work proposes a novel multi-objective load shifting optimization focusing on low costs and reduced resource depletion. For the resource depletion we combine the long term effects of carbon emissions with the short term effects of water consumption, which in a novel approach is weighted based on a newly developed spatial and temporal drought risk indicator. We investigate a use case where we optimally shift the inference load of a LLM spatially when hosted in ten different European countries. Additionally, we extend previous research on the water intensity of the electric grid by providing the first automated framework called IntensityLib for calculating water intensity factors for the European electricity grid as well as integrating a flow-tracing algorithm which models the effect of imports and exports. We find that adjusting for water scarcity leads to entirely different solutions compared to simply minimizing water consumption and can prevent further stress on regions with reoccurring drought risks. © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2110.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
