---
id: paper-0951
title: Deep reinforcement learning-based task offloading and service migrating policies in service caching-assisted mobile edge computing
authors:
- Hongchang, Ke
- Hui, Wang
- Hongbin, Sun
- Yang, Halvin
venue: China Communications
venue_type: journal
year: 2024
doi: 10.23919/JCC.fa.2023-0474.202404
url: https://www.scopus.com/pages/publications/85192185808?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 88--103
keywords:
- deep reinforcement learning
- mobile edge computing
- service caching
- service migrating
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0951 — Deep reinforcement learning-based task offloading and service migrating policies in service caching-assisted mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Emerging mobile edge computing (MEC) is considered a feasible solution for offloading the computation-intensive request tasks generated from mobile wireless equipment (MWE) with limited computational resources and energy. Due to the homogeneity of request tasks from one MWE during a long-term time period, it is vital to predeploy the particular service cachings required by the request tasks at the MEC server. In this paper, we model a service caching-assisted MEC framework that takes into account the constraint on the number of service cachings hosted by each edge server and the migration of request tasks from the current edge server to another edge server with service caching required by tasks. Furthermore, we propose a multiagent deep reinforcement learning-based computation offloading and task migrating decision-making scheme (MBOMS) to minimize the long-term average weighted cost. The proposed MBOMS can learn the near-optimal offloading and migrating decision-making policy by centralized training and decentralized execution. Systematic and comprehensive simulation results reveal that our proposed MBOMS can converge well after training and outperforms the other five baseline algorithms.  © 2013 China Institute of Communications.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0951.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
