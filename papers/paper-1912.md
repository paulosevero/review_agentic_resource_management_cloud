---
id: paper-1912
title: Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint
authors:
- Lu, Xiaoli
- Guo, Gaizhi
- Yu, Zongzuo
- Zhang, Pengjv
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-9901-8_39
url: https://www.scopus.com/pages/publications/105012244851?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 472--483
keywords:
- Entropy Constraint
- Mobile Edge Computing
- Multi-head Self-attention
- Multi-objective Reinforcement Learning
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

# paper-1912 — Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the task offloading scenario of edge computing, user devices commonly suffer from resource constraints. It is difficult for traditional task offloading mechanisms to make efficient decisions when facing complex environments such as dynamically changing network resources and parallel scheduling of multiple tasks. Reinforcement learning methods face the problem of balance between exploration and exploitation in practical applications. To this end, we propose a multi-objective reinforcement learning mechanism based on SAE-PPO, which is an improvement of the traditional Proximal Policy Optimization (PPO) algorithm to achieve efficient task offloading. First, for the dynamics of network resources and the demand of multi-task scheduling, we design an Actor-Critic network model incorporating a multi-head self-attention (MHSA) mechanism. It can capture the complex association between task features and resource distribution, and thus optimize the matching strategy between tasks and resources. Second, to address the balance between exploration and exploitation, we construct an intelligent exploration strategy with entropy constraint by introducing an entropy regularization in the objective function. The strategy prevents premature convergence to a local optimum and adapts to different load and network conditions. Experimental results show that the proposed method outperforms the UCB1, SPEA/R, and NSGA-III algorithms in latency and energy consumption, achieving a 70% reduction in latency and a 46% reduction in energy consumption in complex MEC environments. This paper provides an effective solution for resource scheduling in complex edge environments. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1912.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
