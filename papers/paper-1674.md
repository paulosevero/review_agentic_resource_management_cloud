---
id: paper-1674
title: Task Offloading Based on the Fusion of Model- and Data-Driven Intelligence for Vehicular Edge Computing Networks
authors:
- Huang, Xiujie
- Chen, Yuhao
- Liu, Zhiquan
- Zhao, Shancheng
- Li, Zhetao
- Chen, Renzhang
- Guan, Quanlong
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3546304
url: https://www.scopus.com/pages/publications/105000261693?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8525--8540
keywords:
- deep reinforcement learning
- multi-agent proximal policy optimization-based task and target selection algorithm (MAPPO-TTSA)
- task offloading
- Vehicular edge computing (VEC)
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

# paper-1674 — Task Offloading Based on the Fusion of Model- and Data-Driven Intelligence for Vehicular Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is an efficient solution to alleviate the limitations of local computing resources in vehicular networks. However, the high mobility of vehicles and the dynamic variability of network topologies make it significantly challengeable. In this work, we make a fusion of model-driven and data-driven intelligence to design a multi-agent deep reinforcement learning (DRL) solution for task offloading in urban VEC networks. First, computational models for task queue, transmission, computation, energy consumption, and expense are meticulously developed for the VEC network that integrates communication and computation. Vehicular tasks vary in type, urgency, size, and timeframe, leading to different latency requirements. Tasks may be executed locally within the vehicle, at a server after V2I offloading via cellular communications, or in a neighboring vehicle after V2V offloading via millimeter-wave (mmWave) communications. Each of these options incurs different levels of latency, energy consumption, and expense. Second, based on these models and the utility function that combines latency, energy consumption, and expense, an optimization problem for task offloading is formulated. This problem can be interpreted as a Markov decision process with a carefully designed reward function. Third, to address the offloading problem, we propose a multi-agent proximal policy optimization-based task and target selection algorithm (MAPPO-TTSA). This algorithm also utilizes convolutional neural networks to extract features from large-scale states, thereby enhancing their correlation. Fourth, comprehensive training is performed on the observational data to determine the optimal parameters for predicting task offloading. Finally, extensive experiments are conducted, and simulation results are provided to demonstrate that the proposed intelligent task offloading scheme offers significant advantages in terms of average task completion delay and utility level across various scenarios. © 2000-2011 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1674.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
