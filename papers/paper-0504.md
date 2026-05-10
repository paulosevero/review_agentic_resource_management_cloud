---
id: paper-0504
title: Collaborative Edge Computing for Social Internet of Vehicles to Alleviate Traffic Congestion
authors:
- Wang, Tong
- Hussain, Azhar
- Zhang, Lejun
- Zhao, Chen
venue: IEEE Transactions on Computational Social Systems
venue_type: journal
year: 2022
doi: 10.1109/TCSS.2021.3074038
url: https://www.scopus.com/pages/publications/85105871308?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 184--196
keywords:
- Deep reinforcement learning (DRL)
- edge computing
- intelligent connected vehicles
- orchestration
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

# paper-0504 — Collaborative Edge Computing for Social Internet of Vehicles to Alleviate Traffic Congestion

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing in vehicles is emerging as an essential candidate for the Internet of Vehicles (IoV) to improve traffic efficiency. The proliferation of IoV pushes the horizon of edge computing. The social features and connections among vehicles are significant for traffic efficiency solutions. However, it is quite challenging to perform collaborative edge computing (CEC) for social IoV systems because of network heterogeneity, vehicle mobility, user selfishness, privacy, and so on. This article focuses on the CEC, in the social IoV system to alleviate urban traffic congestion. Recent research reveals that intelligent traffic lights control through city-wide mobile edge computing (MEC) servers can reduce vehicles' average waiting time at signal intersections. This article has focused on a CEC-based traffic management system (CEC-TMS) to reduce the average waiting time. It utilizes multiagent-based deep reinforcement learning (DRL) for the MEC servers that interact with IoV and traffic lights to generate dynamic green waves at congested intersections. Results demonstrate the effectiveness of the proposed system under the paradigm of multiagent DRL.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0504.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
