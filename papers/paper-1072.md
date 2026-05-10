---
id: paper-1072
title: Enhacing Logistics with Computer Vision and Fog Computing-Driven Auto-ID Technologies
authors:
- Losada Del Olmo, Juan Jesus
- Gomez, Angel Luis Perales
- Lopez De Teruel Alcolea, Pedro E.
- Garcia, Alberto Ruiz
- Clemente, Felix J. Garcia
venue: 2024 9th International Conference on Fog and Mobile Edge Computing, FMEC 2024
venue_type: conference
year: 2024
doi: 10.1109/FMEC62297.2024.10710204
url: https://www.scopus.com/pages/publications/85208104267?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 220--227
keywords:
- Auto-identification
- Computer Vision
- Few-shot Learning
- Fog Computing
- Foundational Models
- Linear Probing
- Logistics
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

# paper-1072 — Enhacing Logistics with Computer Vision and Fog Computing-Driven Auto-ID Technologies

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper we propose a series of enhancements to a computer vision system specifically designed for auto-identification (Auto-ID) of loads in industrial and logistic settings using a fog computing architecture. The system effectively monitors multiple docks within a logistics warehousing management system, identifying loads on pallets in real-Time and providing immediate feedback to ensure proper truck loading. Its Auto-ID functionality has been expanded to include visual estimation of the class and approximate size of pallets, resulting in an efficient method for automatic image labeling that enables the creation of few-shot training datasets. Our experimental results show that these datasets are sufficient for leveraging on state-of-The-Art foundational computer vision models to obtain high accuracy and precision rates on both object classification and load size estimation by precise bounding box placement. Furthermore, our evaluation also demonstrates that employing simple techniques like linear probing significantly reduces the need for extensive processing and cloud-based training, perfectly aligning with the system's underlying fog computing architecture. This streamlined approach simplifies parameter calibration, eliminates the need for extensive data uploads, and facilitates flexible online updates as new load types and class samples are integrated into the system. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1072.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
