---
id: paper-2719
title: An energy-aware distributed federated soft actor-critic framework for intelligent task offloading in vehicular mobile edge computing networks
authors:
- Moghaddasi, Komeil
- Jurdak, Raja
venue: Ad Hoc Networks
venue_type: journal
year: 2026
doi: 10.1016/j.adhoc.2025.104043
url: https://www.scopus.com/pages/publications/105019251037?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Energy-Efficient Application
- Federated Learning
- Mobile edge computing
- Vehicular networks
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

# paper-2719 — An energy-aware distributed federated soft actor-critic framework for intelligent task offloading in vehicular mobile edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Today, modern intelligent transportation systems increasingly depend on Mobile Edge Computing (MEC) to process real-time data for perception and cooperative driving. However, meeting strict low-latency requirements is challenging because Electric Vehicles (EVs) have limited battery capacity, and must carefully balance the energy used for computation and communication with preserving driving range. While each operation may consume only a small amount of power, their combined effect can substantially reduce how far an EV can travel on a single charge. In this study, we introduce a distributed Federated Soft Actor–Critic (Fed-SAC) framework designed specifically for intelligent, energy-aware, low-latency task offloading in dynamic vehicular MEC networks. Our approach enables each agent to learn privacy-preserving offloading policies in situ, jointly optimizing execution location, transmit power, and offloading ratio through a multi-dimensional discrete action space, addressing both scalability and adaptability under strict latency and energy constraints. Simulations of mobility, wireless channels, and deadline-sensitive workloads show Fed-SAC reduces mean task delay by 77 %, energy use by 89 %, and combined cost by 93 % compared to state-of-the-art methods. Crown Copyright © 2025 Published by Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2719.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
