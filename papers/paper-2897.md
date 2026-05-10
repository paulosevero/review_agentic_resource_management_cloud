---
id: paper-2897
title: Intelligent resource allocation for multiaccess edge computing in 5G ultra-dense slicing network using federated multiagent DDPG algorithm
authors:
- Yu, Gong
- Pengwei, Gong
- He, Jiang
- Wen, Xie
- Chenxi, Wang
- Peijun, Xu
venue: China Communications
venue_type: journal
year: 2026
doi: 10.23919/JCC.fa.2022-0187.202601
url: https://www.scopus.com/pages/publications/105029749623?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 273--289
keywords:
- federated learning
- multiaccess edge computing
- muti-agent deep reinforcement learning
- resource allocation
- ultra-dense slicing network
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

# paper-2897 — Intelligent resource allocation for multiaccess edge computing in 5G ultra-dense slicing network using federated multiagent DDPG algorithm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, advances in communication technology and cloud computing have spawned a variety of smart mobile devices, which will generate a great amount of computing-intensive businesses, and require corresponding resources of computation and communication. Multiaccess edge computing (MEC) can offload computing-intensive tasks to the nearby edge servers, which alleviates the pressure of devices. Ultra-dense network (UDN) can provide effective spectrum resources by deploying a large number of micro base stations. Furthermore, network slicing can support various applications in different communication scenarios. Therefore, this paper integrates the ultra-dense network slicing and the MEC technology, and introduces a hybrid computing offloading strategy in order to satisfy various quality of service (QoS) of edge devices. In order to dynamically allocate limited resources, the above problem is formulated as multiagent distributed deep reinforcement learning (DRL), which will achieve low overhead computation offloading strategy and real-time resource allocation decisions. In this context, federated learning is added to train DRL agents in a distributed manner, where each agent is dedicated to exploring actions composed of offloading decisions and allocating resources, so as to jointly optimize system delay and energy consumption. Simulation results show that the proposed learning algorithm has better performance compared with other strategies in literature. © 2013 China Institute of Communications.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2897.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
