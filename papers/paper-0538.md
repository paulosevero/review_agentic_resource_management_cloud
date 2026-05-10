---
id: paper-0538
title: '''fed-DRL'': A Timeliness Optimization Method for Dynamic Data Acquisition System Based on Mobile Edge Computing'
authors:
- Zheng, Huiji
- Yu, Sicong
- Qiu, Xinyuan
- Cui, Xiaolong
- Zhu, Li
venue: Mathematical Problems in Engineering
venue_type: journal
year: 2022
doi: 10.1155/2022/5719190
url: https://www.scopus.com/pages/publications/85135766023?origin=resultslist
publisher: Hindawi Limited
pages: ''
keywords:
- Computer terminals
- Data acquisition
- Deep learning
- Learning algorithms
- Mobile edge computing
- Mobile telecommunication systems
- Multi agent systems
- Data acquisition system
- Dynamic data
- Environmental data
- Environmental security
- Mobile terminal
- Optimization method
- Reinforcement learnings
- Target nodes
- Urban security
- Work study
- Reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0538 — 'fed-DRL': A Timeliness Optimization Method for Dynamic Data Acquisition System Based on Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Age of Information (AoI) is a metric to describe the timeliness of a system proposed in recent years. It measures the freshness of the latest received data from the perspective of the target node in the system. This work studies a kind of dynamic data acquisition system for urban security that can update and control the situation of urban environmental security by collecting environmental data. The collected data packets need to be uploaded to the cloud center in time for data update, which has high requirements on the timeliness of the system and freshness of data. However, due to the limited computing capacity of mobile terminals and the pressure of bandwidth for data transmission, problems such as high data execution delay and transmission interruption are caused. Emerging mobile edge computing (MEC), a new model of computing that extends cloud computing capabilities to the edge network, promises to solve these problems. This work focuses on the timeliness of the system, as measured by the average AoI across all mobile terminals. First, a timeliness optimization model is defined, and a multi-agent deep reinforcement learning (DRL) algorithm combined with an attention mechanism is proposed to carry out computing offloading and resource allocation through the continuous interaction between agent and environment; then, in order to improve algorithm performance and data security, the federated learning mode is proposed to train agents; finally, the proposed algorithm is compared with other main baseline algorithms based on deep reinforcement learning. The simulation results show that the proposed algorithm not only outperforms other algorithms in optimizing system timeliness, but also improves the stability of training.  © 2022 Huiji Zheng et al.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0538.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
