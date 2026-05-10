---
id: paper-1271
title: Task-Oriented Satellite-UAV Networks With Mobile-Edge Computing
authors:
- Wei, Peng
- Feng, Wei
- Chen, Yunfei
- Ge, Ning
- Xiang, Wei
- Mao, Shiwen
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2024
doi: 10.1109/OJCOMS.2023.3341251
url: https://www.scopus.com/pages/publications/85179833140?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 202--220
keywords:
- Offloading
- reinforcement learning
- resource allocation
- satellite-UAV network
- velocity control
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

# paper-1271 — Task-Oriented Satellite-UAV Networks With Mobile-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Networked robots have become crucial for unmanned applications since they can collaborate to complete complex tasks in remote/hazardous/depopulated areas. Due to the cost inefficiency of deploying cellular network infrastructure in these areas, hybrid satellite-UAV networks emerge as a promising solution. These networks provide seamless and on-demand connectivity for multiple robots with various task requirements, and support computation-intensive and latency-sensitive services through mobile edge computing (MEC)-based offloading. However, to complete tasks in limited times, the rapid collective movement of mobile robots may cause frequent service migration, and a large number of gathered robots may compete for limited bandwidth resources in satellite and UAV communications. As a result, offloading latency may increase significantly. To address this issue, the average completion time of multi-robot offloading in task-oriented satellite-UAV networks with MEC is formulated as an optimization problem. Unlike conventional mobility-aware MEC-based offloading schemes, joint optimization of mobility control, data offloading, and resource allocation is proposed using velocity control of multiple robots. According to Lyapunov optimization, the original optimization problem is simplified into minimizing the average completion time of offloading for all robots within UAV and satellite coverage. A multi-agent Q-learning algorithm, including multi-group dual-agent Q-learning, is proposed based on local state observation and global reward calculation. In each dual-agent Q-learning, one agent is responsible for velocity control and communication resource allocation, while the other is responsible for data offloading and computational resource allocation. The convergence of the proposed multi-agent Q-learning algorithm is also theoretically analyzed. Simulation results show that the proposed scheme can effectively reduce the offloading latency by up to 35% in the multi-robot environment over its conventional counterparts. © 2020 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1271.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
