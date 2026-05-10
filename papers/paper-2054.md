---
id: paper-2054
title: Task Offloading and Resource Allocation Strategy in Non-Terrestrial Networks for Continuous Distributed Task Scenarios
authors:
- Qi, Yueming
- Du, Yu
- Guo, Yijun
- Hao, Jianjun
venue: Sensors
venue_type: journal
year: 2025
doi: 10.3390/s25196195
url: https://www.scopus.com/pages/publications/105018919078?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforce learning
- edge computing
- non-terrestrial network
- task offloading and resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2054 — Task Offloading and Resource Allocation Strategy in Non-Terrestrial Networks for Continuous Distributed Task Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Leveraging non-terrestrial networks for edge computing is crucial for the development of 6G, the Internet of Things, and ubiquitous digitalization. In such scenarios, diverse tasks often exhibit continuously distributed attributes, while existing research predominantly relies on qualitative thresholds for task classification, failing to accommodate quantitatively continuous task requirements. To address this issue, this paper models a multi-task scenario with continuously distributed attributes and proposes a three-tier cloud-edge collaborative offloading architecture comprising UAV-based edge nodes, LEO satellites, and ground cloud data centers. We further formulate a system cost minimization problem that integrates UAV network load balancing and satellite energy efficiency. To solve this non-convex, multi-stage optimization problem, a two-layer multi-type-agent deep reinforcement learning (TMDRL) algorithm is developed. This algorithm categorizes agents according to their functional roles in the Markov decision process and jointly optimizes task offloading and resource allocation by integrating DQN and DDPG frameworks. Simulation results demonstrate that the proposed algorithm reduces system cost by 7.82% compared to existing baseline methods. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2054.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
