---
id: paper-0480
title: Aerial-Assisted Intelligent Resource Allocation
authors:
- Peng, Haixia
- Ye, Qiang
- Shen, Xuemin Sherman
venue: Wireless Networks (United Kingdom)
venue_type: book-chapter
year: 2022
doi: 10.1007/978-3-030-96507-5_5
url: https://www.scopus.com/pages/publications/85127863219?origin=resultslist
publisher: Springer Nature
pages: 111--143
keywords:
- Multi-access edge computing
- Multi-agent DDPG
- Multi-dimensional resource management
- Single-agent DDPG
- Unmanned aerial vehicle
- Vehicular networks
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

# paper-0480 — Aerial-Assisted Intelligent Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this chapter, we investigate multi-dimensional resource management for UAV-assisted MVNETs. To efficiently provide on-demand resource access, the MeNB and UAV, both mounted with MEC servers, cooperatively make association decisions and allocate proper amounts of resources to vehicles. First, we introduce an SADDPG-based scheme to centrally allocate the multi-dimensional resources by considering a central controller installed at the MeNB. Also, to avoid extra time and spectrum consumption on communications between MEC servers and a central controller, we formulate the resource allocation at the MEC servers as a distributive optimization problem with the objective of maximizing the number of offloaded tasks while satisfying their heterogeneous QoS requirements. Then, we solve the formulated distributive problem with an MADDPG-based method. Through centrally training the MADDPG model offline, the MEC servers, acting as learning agents, can rapidly make vehicle-server association and resource allocation decisions during the online execution stage. From our simulation results, the MADDPG-based method can converge within 200 training episodes, comparable to the SADDPG-based one. Moreover, the proposed SADDPG-based and MADDPG-based resource management scheme can achieve higher delay/QoS satisfaction ratios than the random scheme. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0480.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
