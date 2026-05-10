---
id: paper-1486
title: Cooperative Schemes for Joint Latency and Energy Consumption Minimization in UAV-MEC Networks †
authors:
- Cheng, Ming
- He, Saifei
- Pan, Yijin
- Lin, Min
- Zhu, Wei-Ping
venue: Sensors
venue_type: journal
year: 2025
doi: 10.3390/s25175234
url: https://www.scopus.com/pages/publications/105015894372?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- closed-form enhanced multi-armed bandit (CF-MAB)
- energy consumption
- latency
- mobile edge computing (MEC)
- multi-agent proximal policy optimization (MAPPO)
- multi-UAV networks
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

# paper-1486 — Cooperative Schemes for Joint Latency and Energy Consumption Minimization in UAV-MEC Networks †

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Internet of Things (IoT) has promoted emerging applications that require massive device collaboration, heavy computation, and stringent latency. Unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) systems can provide flexible services for user devices (UDs) with wide coverage. The optimization of both latency and energy consumption remains a critical yet challenging task due to the inherent trade-off between them. Joint association, offloading, and computing resource allocation are essential to achieving satisfying system performance. However, these processes are difficult due to the highly dynamic environment and the exponentially increasing complexity of large-scale networks. To address these challenges, we introduce a carefully designed cost function to balance the latency and the energy consumption, formulate the joint problem into a partially observable Markov decision process, and propose two multi-agent deep-reinforcement-learning-based schemes to tackle the long-term problem. Specifically, the multi-agent proximal policy optimization (MAPPO)-based scheme uses centralized learning and decentralized execution, while the closed-form enhanced multi-armed bandit (CF-MAB)-based scheme decouples association from offloading and computing resource allocation. In both schemes, UDs act as independent agents that learn from environmental interactions and historic decisions, make decision to maximize its individual reward function, and achieve implicit collaboration through the reward mechanism. The numerical results validate the effectiveness and show the superiority of our proposed schemes. The MAPPO-based scheme enables collaborative agent decisions for high performance in complex dynamic environments, while the CF-MAB-based scheme supports independent rapid response decisions. © 2025 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1486.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
