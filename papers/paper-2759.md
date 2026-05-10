---
id: paper-2759
title: Quality of Control-Based Control-Communication Co-Design for Collaborative Robotics
authors:
- Roy, Neelabhro
- Dhullipalla, Mani H.
- Sharma, Gourav Prateek
- Sandberg, Sara
- Dimarogonas, Dimos V.
- Gross, James
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2026
doi: 10.1109/TII.2026.3664663
url: https://www.scopus.com/pages/publications/105034080723?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- 5G
- collaborative robotics
- edge computing
- multiagent systems
- quality of control
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

# paper-2759 — Quality of Control-Based Control-Communication Co-Design for Collaborative Robotics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Motivated by the growing importance of flexible automation in industrial environments, this article investigates the impact of wireless solutions in collaborative robotics, toward which we provide a quality of control (QoC)-based abstraction and methodology that comprehensively captures the interplay between network-induced delays, reliability, and robotic workload parameters for wireless collaborative robotics (WCR). For such a setting, we formulate a joint control-communication co-design based optimization framework to maximize the QoC across all robots, for 5G resource dimensioning. This is crucial for identifying optimal co-design parameters maximizing the QoC for limited 5G bandwidth across different topologies of robotic connectivity, prior to the deployment of these WCRs, or when selecting appropriate connectivity priority levels. We compare the performance of our proposed algorithm to different state of the art schemes in the literature. Our simulation results highlight the latency-reliability tradeoff and its implications on the control performance. We also demonstrate that our abstraction can be utilized for control-communication co-design, identifying optimal latency-reliability points in conjunction with the maximum velocity the robots operate with, while highlighting the energy gains due to co-design as well. © 2005-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2759.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
