---
id: paper-0374
title: An Edge Federated MARL Approach for Timeliness Maintenance in MEC Collaboration
authors:
- Zhu, Zheqi
- Wan, Shuo
- Fan, Pingyi
- Letaief, Khaled B.
venue: 2021 IEEE International Conference on Communications Workshops, ICC Workshops 2021 - Proceedings
venue_type: conference
year: 2021
doi: 10.1109/ICCWorkshops50388.2021.9473729
url: https://www.scopus.com/pages/publications/85112810882?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- actor-critic
- federated learning
- MEC collaboration
- multi-agent deep reinforcement learning
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

# paper-0374 — An Edge Federated MARL Approach for Timeliness Maintenance in MEC Collaboration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) has been widely studied to provide new schemes for communication-computing systems such as industrial Internet of Things (IoTs), vehicular networks, smart city applications, etc. In this work, we mainly investigate on the timeliness maintenance of the MEC systems where the freshness of the data and computation tasks plays a significant role. We firstly formulate the average age of information (AoI) minimization problem of the UAV-assisted MEC systems. To maintain the system timeliness, we propose a novel multi-agent reinforcement learning (MARL) approach, called edge federated multi-agent actor-critic (MAAC), for joint trajectory planning, data scheduling and resource management in the investigated MEC systems. Through the proposed online learning method, edge devices and center controller learn the interactive policies through local observations and carry out the model-wise communication. We build up a simulation platform for time sensitive MEC systems as a gym environment module and implement the proposed algorithm. Furthermore, the comparisons with a popular MARL solution, MADDPG, show that the proposed approach achieves better performance in terms of data freshness and system stability. © 2021 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0374.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
