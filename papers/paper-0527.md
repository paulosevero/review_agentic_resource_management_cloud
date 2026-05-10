---
id: paper-0527
title: Task Offloading and Resource Allocation Strategy Based on Deep Learning for Mobile Edge Computing
authors:
- Yu, Zijia
- Xu, Xu
- Zhou, Wei
venue: Computational Intelligence and Neuroscience
venue_type: journal
year: 2022
doi: 10.1155/2022/1427219
url: https://www.scopus.com/pages/publications/85137677831?origin=resultslist
publisher: Hindawi Limited
pages: ''
keywords:
- Algorithms
- Deep Learning
- Reinforcement, Psychology
- Resource Allocation
- computation offloading
- Deep learning
- Energy conservation
- Energy utilization
- Green computing
- Learning systems
- Mobile edge computing
- Reinforcement learning
- Calculation models
- Completion time
- Computation offloading
- Computing environments
- Multiservers
- Multiusers
- Objective functions
- Resource allocation strategies
- Resources allocation
- Task offloading
- algorithm
- resource allocation
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0527 — Task Offloading and Resource Allocation Strategy Based on Deep Learning for Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> For the problems of unreasonable computation offloading and uneven resource allocation in Mobile Edge Computing (MEC), this paper proposes a task offloading and resource allocation strategy based on deep learning for MEC. Firstly, in the multiuser multiserver MEC environment, a new objective function is designed by combining calculation model and communication model in the system, which can shorten the completion time of all computing tasks and minimize the energy consumption of all terminal devices under delay constraints. Then, based on the multiagent reinforcement learning system, system benefits and resource consumption are designed as rewards and losses in deep reinforcement learning. Dueling-DQN algorithm is used to solve the system problem model for obtaining resource allocation method with the highest reward. Finally, the experimental results show that when the learning rate is 0.001 and discount factor is 0.90, the performance of proposed strategy is the best. Furthermore, the proportions of reducing energy consumption and shortening completion time are 52.18% and 34.72%, respectively, which are better than other comparison strategies in terms of calculation amount and energy saving.  © 2022 Zijia Yu et al.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0527.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
