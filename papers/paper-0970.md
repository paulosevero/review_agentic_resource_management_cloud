---
id: paper-0970
title: A Task Offloading and Resource Allocation Strategy Based on Multi-Agent Reinforcement Learning in Mobile Edge Computing
authors:
- Jiang, Guiwen
- Huang, Rongxi
- Bao, Zhiming
- Wang, Gaocai
venue: Future Internet
venue_type: journal
year: 2024
doi: 10.3390/fi16090333
url: https://www.scopus.com/pages/publications/85205267477?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- computing offloading
- mobile edge computing
- multi-agent
- resource allocation
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

# paper-0970 — A Task Offloading and Resource Allocation Strategy Based on Multi-Agent Reinforcement Learning in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task offloading and resource allocation is a research hotspot in cloud-edge collaborative computing. Many existing pieces of research adopted single-agent reinforcement learning to solve this problem, which has some defects such as low robustness, large decision space, and ignoring delayed rewards. In view of the above deficiencies, this paper constructs a cloud-edge collaborative computing model, and related task queue, delay, and energy consumption model, and gives joint optimization problem modeling for task offloading and resource allocation with multiple constraints. Then, in order to solve the joint optimization problem, this paper designs a decentralized offloading and scheduling scheme based on “task-oriented” multi-agent reinforcement learning. In this scheme, we present information synchronization protocols and offloading scheduling rules and use edge servers as agents to construct a multi-agent system based on the Actor–Critic framework. In order to solve delayed rewards, this paper models the offloading and scheduling problem as a “task-oriented” Markov decision process. This process abandons the commonly used equidistant time slot model but uses dynamic and parallel slots in the step of task processing time. Finally, an offloading decision algorithm TOMAC-PPO is proposed. The algorithm applies the proximal policy optimization to the multi-agent system and combines the Transformer neural network model to realize the memory and prediction of network state information. Experimental results show that this algorithm has better convergence speed and can effectively reduce the service cost, energy consumption, and task drop rate under high load and high failure rates. For example, the proposed TOMAC-PPO can reduce the average cost by from 19.4% to 66.6% compared to other offloading schemes under the same network load. In addition, the drop rate of some baseline algorithms with 50 users can achieve 62.5% for critical tasks, while the proposed TOMAC-PPO only has 5.5%. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0970.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
