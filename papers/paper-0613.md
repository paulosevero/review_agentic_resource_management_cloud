---
id: paper-0613
title: Digital Twin Assisted DAG Task Scheduling Via Evolutionary Selection MARL in Large-Scale Mobile Edge Network
authors:
- Huang, Jiayu
- Zhou, Fanqin
- Feng, Lei
- Li, Wenjing
- Zhao, Mingyu
- Yan, Xueqiang
- Xi, Yan
- Wu, Jianjun
venue: '2023 IEEE International Conference on Communications Workshops: Sustainable Communications for Renaissance, ICC Workshops 2023'
venue_type: conference
year: 2023
doi: 10.1109/ICCWorkshops57953.2023.10283633
url: https://www.scopus.com/pages/publications/85177825917?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 158--163
keywords:
- Digital Twin
- Evolutionary Selection
- Mobile Edge Computing
- Multi-Agent Reinforcement Learning
- Task Scheduling
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
    my_justification: RL
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

# paper-0613 — Digital Twin Assisted DAG Task Scheduling Via Evolutionary Selection MARL in Large-Scale Mobile Edge Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> 6G is envisioned to serve many compute-intensive and latency-sensitive applications which are now usually formed by functional components in the directed acyclic graphic (DAG) form. Mobile edge computing (MEC) is proven a promising way to offload computing tasks and reduce execution latency. However, the ever-increasing number and heterogeneity of edge computing nodes, as well as the dynamically changing resource state, hinder any centralized scheduler from getting the accurate and timely resource state in the huge number of edge nodes. In this paper, facing a large-scale MEC scenario, we propose a digital twin (DT) assisted multiagent-based task scheduling scheme to jointly optimize task offloading and resource allocation strategy for DAG tasks. The scheme exploits the evolutionary selection multi-agent reinforcement learning (ES-MARL) framework to expedite the training of a large number of agents, while the DT of the mobile edge network keeps the latest state data and enables the centralized training of these distributed agents. The simulation result shows that the proposed scheme can achieve the goals of reducing latency and energy consumption while improving the scheduling success rate, load balancing index, and training efficiency. © 2023 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0613.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
