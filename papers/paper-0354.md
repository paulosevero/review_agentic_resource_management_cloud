---
id: paper-0354
title: Resource Allocation in Vehicular Networks with Multi-UAV Served Edge Computing
authors:
- Wang, Yuhang
- He, Ying
- Dong, Minhui
venue: Proceedings - International Conference on Network Protocols, ICNP
venue_type: conference
year: 2021
doi: 10.1109/ICNP52444.2021.9651916
url: https://www.scopus.com/pages/publications/85124246440?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- attention mechanism
- multi-agent reinforcement learning
- multi-UAV
- resources allocation
- security constraints
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

# paper-0354 — Resource Allocation in Vehicular Networks with Multi-UAV Served Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of intelligent transportation systems, there is an increasingly strong demand for low-latency and high-bandwidth vehicular services, such as automatic driving assistance, emergency alarm, and infotainment. However, in some cases (e.g., traffic congestion, remote areas), the ground communication networks alone cannot meet the vast needs of vehicles. Unmanned aerial vehicles (UAVs) are flexible and deployable, which can be used as a supplement to the ground networks, to relieve the communication pressure on ground facilities, such as base stations. In this paper, we use multiple UAVs to provide services for vehicles and model the multi-UAV scenario as a collaborative multi-agent system. All UAVs share limited bandwidth resources and equip with edge computing servers to serve the vehicles. In addition, serious consequences may be caused if the delay requirements of vehicles are not satisfied. Therefore, we take vehicle safety as the top priority and the delay requirement as the constraints. Then we exploit the Lagrange multiplier to combine the constraint function and cost function, so as to reduce the resource consumption as much as possible on the premise of ensuring the safety of the vehicles. The influence of channel efficiency and computing power should also be taken into account when allocating resources. We adopt the multi-agent reinforcement learning to train the UAVs, and meanwhile introduce the attention mechanism so that each UAV can optimize itself better with the information of other UAVs. Through a large number of experiments, the effectiveness of our proposed method is verified. Particularly, in the case of strictly limiting bandwidth resources, resources can still be allocated according to vehicle needs under the premise of ensuring vehicle safety.  © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0354.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
