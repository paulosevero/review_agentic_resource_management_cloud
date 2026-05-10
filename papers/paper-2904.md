---
id: paper-2904
title: 'Adaptive Load Balancing in Industrial Edge Computing: A Multi-agent Reinforcement Learning Approach'
authors:
- Zhang, Fenghui
- Xu, Yuhao
- Zong, Yu
- Xu, Qiu
- Algoos, Yousef
- Chang, Zhiqiang
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-7144-4_25
url: https://www.scopus.com/pages/publications/105035308149?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 270--282
keywords:
- Distributed edge computing
- load balancing
- multi-agent reinforcement learning
- stochastic game
- task scheduling
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

# paper-2904 — Adaptive Load Balancing in Industrial Edge Computing: A Multi-agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of Industrial Internet of Things (IIoT) applications presents significant challenges for distributed edge computing systems, particularly in managing unpredictable and uneven task arrivals that lead to increased latency and reduced system performance. To address this problem, we propose a decentralized Multi-Agent Reinforcement Learning (MARL) framework for adaptive load balancing in heterogeneous edge environments. In this framework, each edge server is modeled as an autonomous agent engaged in a stochastic game, enabling distributed task scheduling and local resource allocation without centralized coordination. The system accounts for realistic factors such as Poisson-distributed task arrivals and heterogeneous computational capacities. Using a Q-learning-based MARL strategy, agents learn to minimize long-term load imbalance through local observations, constrained action spaces, and decaying exploration mechanisms. Simulation results show that the proposed method significantly reduces task latency and load imbalance compared to traditional scheduling baselines, demonstrating its effectiveness in dynamic, large-scale IIoT scenarios. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2904.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
