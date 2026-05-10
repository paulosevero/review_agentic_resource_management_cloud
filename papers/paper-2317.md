---
id: paper-2317
title: Cache-assisted task offloading strategy based on multi-agent deep reinforcement learning
authors:
- Xie, Mande
- Li, Longchen
- Ni, Xueping
venue: Computer Networks
venue_type: journal
year: 2025
doi: 10.1016/j.comnet.2025.111483
url: https://www.scopus.com/pages/publications/105009613099?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Content caching
- Deep reinforcement learning
- Mobile edge computing
- Task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2317 — Cache-assisted task offloading strategy based on multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the context of 5G architecture, mobile edge computing (MEC) has emerged as a promising computing paradigm within this framework. It involves deploying servers at the edge of the network with computing and storage resources to meet the low-latency and high-energy requirements of emerging applications. While many studies have focused on task offloading decisions in MEC, the performance improvement brought by content caching has often been neglected. In this paper, the joint optimization problem of task offloading and content caching in a multi-user, multi-server MEC system is investigated. An offloading method based on multi-agent deep reinforcement learning is proposed, which integrates self-attention with multi-agent deep deterministic policy gradient (MADDPG) to determine task offloading policies. To further enhance the performance of offloading tasks, a dynamic cache decision optimization algorithm (DCDOA) is developed for more effective content caching decisions. The simulation results demonstrate that the proposed method outperforms other baseline algorithms in different scenarios. Specifically, the proposed method reduces the long-term average user cost by 45.4%, 22.2%, 10.6%, and 8%, respectively, compared to the all-cloud execution method, the random offloading method, the DDPG method, and the MADDPG method. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2317.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
