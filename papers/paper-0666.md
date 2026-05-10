---
id: paper-0666
title: Research on Performance Optimization Method of Test Management System Based on Microservices
authors:
- Lu, Zhijie
venue: 2023 4th International Conference on Computer Engineering and Application, ICCEA 2023
venue_type: conference
year: 2023
doi: 10.1109/ICCEA58433.2023.10135194
url: https://www.scopus.com/pages/publications/85162688200?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 445--451
keywords:
- Information Grid
- Micro-service
- Performance optimization methods
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0666 — Research on Performance Optimization Method of Test Management System Based on Microservices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the difficulty of optimizing the performance of microservice based exam management systems, this paper proposes a method based on system information grid optimization, which optimizes microservice performance in a closed-loop manner through microservice based layout and information grid paradigm decomposition. Firstly, a system information grid is established based on the deployment resources of the exam management system, and then the information map of the microservice system is derived from the system information grid. Then, the performance blocking points of the microservice system are obtained through stress testing, and corresponding intelligent agents are set up. The maximum entropy value of the information grid is obtained through intelligent agents and using the quartering method. This value is compared with the entropy value calculated through the gray scale table of the system information grid, The comparison results are then fed back to the microservice APM management control center, which adjusts the layout and paradigm decomposition of the system information grid in a set functional manner, forming a closed-loop optimization system to obtain the optimal state of the microservice performance of the exam management system under a given software, hardware, and network environment. The simulation application results show that the system service response time and other performance indicators optimized based on this method are reduced by an average of 36.58% compared to those before optimization, significantly improving the performance of the microservice-based exam management system.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0666.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
