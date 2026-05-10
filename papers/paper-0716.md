---
id: paper-0716
title: 'EdgeMatrix: A Resource-Redefined Scheduling Framework for SLA-Guaranteed Multi-Tier Edge-Cloud Computing Systems'
authors:
- Shen, Shihao
- Ren, Yuanming
- Ju, Yanli
- Wang, Xiaofei
- Wang, Wenyu
- Leung, Victor C. M.
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2023
doi: 10.1109/JSAC.2022.3229444
url: https://www.scopus.com/pages/publications/85146237215?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 820--834
keywords:
- Multi-tier computing
- request dispatch
- resource customization
- service orchestration
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

# paper-0716 — EdgeMatrix: A Resource-Redefined Scheduling Framework for SLA-Guaranteed Multi-Tier Edge-Cloud Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of networking technology, the computing system has evolved towards the multi-tier paradigm gradually. However, challenges, such as multi-resource heterogeneity of devices, resource competition of services, and networked system dynamics, make it difficult to guarantee service-level agreement (SLA) for the applications. In this paper, we propose a multi-tier edge-cloud computing framework, EdgeMatrix, to maximize the throughput of the system while guaranteeing different SLA priorities. First, in order to reduce the impact of physical resource heterogeneity, EdgeMatrix introduces the Networked Multi-agent Actor-Critic (NMAC) algorithm to re-define physical resources with the same quality of service as logically isolated resource units and combinations, i.e., cells and channels. In addition, a multi-task mechanism is designed in EdgeMatrix to solve the problem of Joint Service Orchestration and Request Dispatch (JSORD) for matching the requests and services, which can significantly reduce the optimization runtime. For integrating above two algorithms, EdgeMatrix is designed with two time-scales, i.e., coordinating services and resources at the larger time-scale, and dispatching requests at the smaller time-scale. Realistic trace-based experiments proves that the overall throughput of EdgeMatrix is 36.7% better than that of the closest baseline, while the SLA priorities are guaranteed still.  © 1983-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0716.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
