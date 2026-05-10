---
id: paper-0404
title: Vehicle-Road Cooperative Task Offloading with Task Migration in MEC-Enabled IoV
authors:
- Du, Jiarong
- Wang, Liang
- Lin, Yaguang
- Qian, Pengcheng
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2022
doi: 10.1007/978-3-031-19211-1_22
url: https://www.scopus.com/pages/publications/85142864275?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 261--272
keywords:
- Internet of vehicles
- Mobile edge computing
- Multi-agent deep Q-learning network
- Task offloading
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

# paper-0404 — Vehicle-Road Cooperative Task Offloading with Task Migration in MEC-Enabled IoV

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is considered as a key technology for addressing computation-intensive and delay-critical applications in the Internet of vehicles (IoV). In MEC-enabled IoV, vehicles lighten their computing load by offloading tasks to edge servers. However, the high speed mobility of vehicles and time-varying network environment brings tough challenges to task offloading. In addition, considering only roadside units (RSUs) or vehicles as offloading objects lead to the waste of computing resources and increase the process delay of task. To this end, we formulate the reduction of task processing delay and improvement of service reliability as an utility maximization problem and propose a distributed vehicle-road cooperative task offloading scheme with task migration. Then we use RSUs and surrounding vehicles as offloading objects and divide offloading tasks into multiple subtasks for offloading objects and local parallel processing, which improves the utilization rate of computing resources. Meanwhile, we reduce the task processing failure by migrating the computing results of offloading subtasks. The offloading scheme is formulated as a mixed-integer nonlinear optimization problem, and a multi-agent deep Q-learning network (MADQN) algorithm is proposed to find the near-optimal offloading objects and number of offloading subtasks. Simulation results show that the proposed approach significantly improves the total task processing speed and service reliability. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0404.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
