---
id: paper-1811
title: Multi-agent deep reinforcement learning based multi-task partial computation offloading in mobile edge computing
authors:
- Li, Han
- Meng, Shunmei
- Sun, Jin
- Cai, Zhicheng
- Li, Qianmu
- Zhang, Xuyun
venue: Future Generation Computer Systems
venue_type: journal
year: 2025
doi: 10.1016/j.future.2025.107861
url: https://www.scopus.com/pages/publications/105003993245?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Load-balancing
- Mobile edge computing
- Multi-agent reinforcement learning
- Partial computation offloading
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-1811 — Multi-agent deep reinforcement learning based multi-task partial computation offloading in mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) can enhance the computation performance of end-devices by providing computation offloading service at the network edge. However, given that both end-devices and edge servers have finite computation resources, inefficient offloading policies may lead to overload, thereby increasing the computation delays of tasks. In this paper, we investigate a multi-task partial computation offloading problem combined with a queue model. Based on achieving load-balancing across the MEC system, our objective is to minimize the long-standing average task-processing cost of the end-devices while ensuring the delay thresholds of tasks. For this purpose, a distributed offloading algorithm utilizing the multi-agent deep reinforcement learning (MADRL) method is proposed. Specifically, through interacting with the MEC environment and accumulating experience data, the device agents can collaborate to optimize their local offloading decisions over continuous time-slots, which includes adjusting the transmission power and determining the tasks’ offloading ratios under the dynamic wireless channel conditions. Exhaustive experimental results demonstrate that in contrast with the baseline algorithms, the proposed offloading algorithm can not only better balance the computation loads between the end-devices and the MEC server, but also more effectively reduce the task-processing cost of the end-devices, as well as the percentage of timeout tasks. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1811.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
