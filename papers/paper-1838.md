---
id: paper-1838
title: Joint Optimization of Task Offloading and Service Caching for Spatiotemporal Differentiated Requirements; [面向时空差异化需求的任务卸载和服务缓存联合优化]
authors:
- Liang, Jishen
- Zhang, Dongxue
- Yu, Gang
- Wang, Bi
- Shan, Hongjiu
venue: Lujun Gongcheng Daxue Xuebao/Journal of Army Engineering University of PLA
venue_type: journal
year: 2025
doi: 10.12018/j.issn.2097-0730.20240830002
url: https://www.scopus.com/pages/publications/105000368147?origin=resultslist
publisher: ARMY ENGINEERING UNIVERSITY OF PLA
pages: 10--19
keywords:
- edge computing
- resource allocation
- service caching
- service differentiation
- task offloading
language: Chinese
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1838 — Joint Optimization of Task Offloading and Service Caching for Spatiotemporal Differentiated Requirements; [面向时空差异化需求的任务卸载和服务缓存联合优化]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) can effectively address the issues of increasing business demands and greater processing difficulties for mobile users. However, users' service demands have differentiated characteristics in time and space. At the same time, network characteristics such as deep uncertainty in the network environment also restrict the efficiency of network edge task processing and service caching. In response to these challenges, this paper studies the users' service offloading and service caching issues in a multi-user and multi-edge server MEC system. To address the differentiated service requirements of users in both time and space, with the optimization goal of minimizing the average delay and energy consumption cost for all users under the base station, a joint optimization of task offloading and service caching based on the differentiated needs in time and space is established. Taking into consideration the characteristics of the network environment with deep uncertainty, a multi-agent deep reinforcement learning algorithm based on graph neural networks and long short-term memory networks is further proposed for autonomous learning and decision-making of user task offloading, resource allocation, and service caching strategies. Finally, simulations have verified that the proposed algorithm has good convergence and energy efficiency. © 2025 ARMY ENGINEERING UNIVERSITY OF PLA. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1838.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
