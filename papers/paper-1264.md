---
id: paper-1264
title: 'Toward Intelligent and Adaptive Task Scheduling for 6G: An Intent-Driven Framework'
authors:
- Wang, Qingqing
- Zou, Sai
- Sun, Yanglong
- Liwang, Minghui
- Wang, Xianbin
- Ni, Wei
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2024
doi: 10.1109/TCCN.2024.3391318
url: https://www.scopus.com/pages/publications/85190793062?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1975--1988
keywords:
- 6G
- cloud network
- energy efficiency
- intent-driven
- multi-agent PPO
- task scheduling
- time-sensitive
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1264 — Toward Intelligent and Adaptive Task Scheduling for 6G: An Intent-Driven Framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A cloud network schedules diverse tasks to multi-access edge computing (MEC) or cloud platforms within dynamic industrial Internet of Things (IIoT). The scheduling is influenced by the diverse intents of different parties, including the time-sensitive nature of device-generated tasks and the energy efficiency of servers. The complexity of this problem under dynamic network conditions is underscored by its nature as a Markov state transition process, typically classified as NP-hard. We introduce an intent-driven intelligent task scheduling approach (IITSA), which models a partially observable Markov decision process (POMDP) and introduces a multi-agent proximal policy optimization (MAPPO) method. We introduce a dynamic adaptive mechanism to effectively address conflicts arising from the temporal requirements and energy limitations associated with various tasks on MEC servers. This mechanism enhances the reward function of MAPPO, for which we offer comprehensive mathematical analysis to validate its convergence performance. Simulation results showcase that our proposed IITSA effectively achieves a harmonious trade-off between time-sensitive demands and infrastructure energy efficiency while exhibiting high adaptability. Compared to state-of-the-art algorithms like MADDPG and QMIX, IITSA reduces energy consumption by 11.68% and 7.07%, and enhances on-time completion numbers for time-sensitive tasks by 18.33% and 12.17%, respectively.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1264.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
