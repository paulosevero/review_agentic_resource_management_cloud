---
id: paper-1121
title: 'HiDRA: A Hierarchical Decentralized Reactive Autoscaler for Spatio-temporal Bursts of Load'
authors:
- Park, EunChan
- Baek, KyeongDeok
- Ko, In-Young
venue: Proceedings of the IEEE International Conference on Web Services, ICWS
venue_type: conference
year: 2024
doi: 10.1109/ICWS62655.2024.00165
url: https://www.scopus.com/pages/publications/85210244477?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1347--1349
keywords:
- container orchestration
- fog services
- microservice autoscaling
- multi-agent reinforcement learning
- spatio-temporal bursts of load
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

# paper-1121 — HiDRA: A Hierarchical Decentralized Reactive Autoscaler for Spatio-temporal Bursts of Load

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> While the emergence of fog computing has shown promising results for reducing the network latency and congestion in the cloud, effective autoscaling to handle spatio-temporal bursts of load has become a timely problem. In this work, we propose HiDRA, a Hierarchical Decentralized Reactive Autoscaler that scales and places microservice instances based on multi-agent reinforcement learning. In HiDRA, the agents are divided into scaling and placement agents that collaborate with each other to effectively handle spatio-temporal bursts of load in fog computing. These hierarchical agents are trained solely based on their regional observations at runtime, eliminating the need for a centralized collection of metrics. We evaluated HiDRA in 20 simulated fog environments to show that HiDRA reduces the created number of instances by 36.70% while resulting in similar scaling performance in terms of response success rate.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1121.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
