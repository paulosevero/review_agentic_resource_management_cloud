---
id: paper-0519
title: Design of intelligent operation inspection platform based on the multi-agent system for live line measurement of substation
authors:
- Xuefeng, Ning
- Yao, Guo
venue: 'Journal of Physics: Conference Series'
venue_type: conference
year: 2022
doi: 10.1088/1742-6596/2401/1/012088
url: https://www.scopus.com/pages/publications/85145210412?origin=resultslist
publisher: Institute of Physics
pages: ''
keywords:
- Computer architecture
- Data handling
- Edge computing
- Electric substations
- Fixed platforms
- Inspection
- Intelligent agents
- Markov processes
- Network architecture
- Edge computing
- Inspection platform
- Inspection software
- Intelligent operations
- Layer data
- Live line measurement
- Measurement device
- Measurements of
- Physical architecture
- Platform design
- Multi agent systems
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0519 — Design of intelligent operation inspection platform based on the multi-agent system for live line measurement of substation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> At present, substations are developing vigorously in an intelligent direction. In this paper, an intelligent operation inspection platform based on a multi-agent system is designed. The platform's design includes the design of its physical architecture and its operation architecture. The physical architecture of the platform includes a substation main control server, fixed live line measurement device, intelligent operation inspection software, intelligent data centralization device, intelligent interface conversion device, wireless communication channel, etc. In terms of platform operation architecture, an operation framework based on a multi-agent system is designed, including the "environment"layer, data sensing layer, data processing layer, and analysis and decision layer, and the whole platform is built based on the concept of edge computing. To solve the task allocation problem of edge computing, a Markov decision model is designed to minimize time consumption and maximize resource utilization, and the deep Q network (DQN) algorithm is used to solve the problem. The design aims at being effective, practical, safe, compatible, easy to upgrade, and extensible, and builds an intelligent operation inspection platform for live line measurement of substation equipment based on a multi-agent system, to improve the intelligent automation level of substation operation inspection. © Published under licence by IOP Publishing Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0519.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
