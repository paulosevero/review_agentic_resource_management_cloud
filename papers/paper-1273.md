---
id: paper-1273
title: A Model and Method for Computing Resource Scoring in Supercomputing Centers
authors:
- Wu, Gang
- Lv, Tianjing
- Li, Fang
- Fu, Quanlong
venue: Proceedings - 11th IEEE International Conference on Cyber Security and Cloud Computing, CSCloud 2024
venue_type: conference
year: 2024
doi: 10.1109/CSCloud62866.2024.00016
url: https://www.scopus.com/pages/publications/85201287151?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 48--52
keywords:
- computing resource scoring
- real-time data analysis
- resource allocation decision-making
- supercomputing centers
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

# paper-1273 — A Model and Method for Computing Resource Scoring in Supercomputing Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study introduces a novel model and method for scoring computing resources in supercomputing centers, aimed at overcoming the limitations of existing rule-based, heuristic, and intelligent agent-based approaches. Traditional methods struggle with adaptability, real-time performance, and universality, which are critical in dynamic computing environments. The proposed universal computing resource scoring model facilitates intelligent resource allocation, optimizes utilization, enables automated decision-making, and manages task priorities and costs effectively. It employs a sophisticated algorithm that processes real-time data on various computing parameters such as CPU/GPU processing power, utilization, memory capacity, and network performance. This model dynamically assesses and allocates resources based on the specific requirements of computing tasks, enhancing efficiency and effectiveness. The methodology encompasses parameter collection, normalization, weight assignment, and weighted scoring, leading to scenario-specific resource recommendations. This approach addresses computational complexity and uncertainties in real-world environments, offering a scalable and adaptable solution for resource management across diverse supercomputing settings. The model's universality and flexibility mark a significant advancement in computing resource management, with broad applications in data center management, resource allocation, and task scheduling. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1273.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
