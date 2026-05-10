---
id: paper-0395
title: Intelligent user-collaborative edge device APC-based MEC 5G IoT for computational offloading and resource allocation
authors:
- Chidume, Chidiebere Sunday
- Nnamani, Christantus O.
venue: Journal of Parallel and Distributed Computing
venue_type: journal
year: 2022
doi: 10.1016/j.jpdc.2022.07.007
url: https://www.scopus.com/pages/publications/85135539140?origin=resultslist
publisher: Academic Press Inc.
pages: 286--300
keywords:
- Available processing capacity (APC)
- Internet of Things (IoT)
- Mobile edge computing (MEC)
- Natural actor-critic deep reinforcement learning
- Resource allocation
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0395 — Intelligent user-collaborative edge device APC-based MEC 5G IoT for computational offloading and resource allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) supports delay-sensitive and excellent processing capacity services on the 5G Internet of Things (IoT) network. This research proposes an intelligent resource allocation policy to minimize average service latency and average energy consumption for an IoT system while maximizing the available processing capacity (APC). We express the APC as a function of communication and computation resources at the user and task edge devices. We demonstrated that reducing execution delay and energy usage could improve overall system service performance. We evaluate the savings in average latency and average energy consumption when we reduce execution delay by allocating resources to maximize APC. The 5G IoT network uses natural actor-critic deep reinforcement learning to tackle complicated resource allocation decisions, and the simulation shows that reducing execution time improves overall system performance. Our results improved execution time and energy usage compared to random search, greedy search, and deep Q-learning. In addition, our single centralized agent DRL outperforms Multi-agent DRL for the number of rewards and completed task achievable under different episodes. © 2022 Elsevier Inc.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0395.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
