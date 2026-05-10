---
id: paper-2754
title: A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles
authors:
- Ren, Junjun
- Chen, Guoqiang
- Chai, Zheng-Yi
- Yuan, Dong
venue: Computers, Materials and Continua
venue_type: journal
year: 2026
doi: 10.32604/cmc.2025.068795
url: https://www.scopus.com/pages/publications/105028361798?origin=resultslist
publisher: Tech Science Press
pages: ''
keywords:
- cloud-edge computing
- computation offloading
- Deep reinforcement learning
- internet of vehicles
- multi-objective optimization
- service caching
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2754 — A Multi-Objective Deep Reinforcement Learning Algorithm for Computation Offloading in Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicle Edge Computing (VEC) and Cloud Computing (CC) significantly enhance the processing efficiency of delay-sensitive and computation-intensive applications by offloading compute-intensive tasks from resource-constrained onboard devices to nearby Roadside Unit (RSU), thereby achieving lower delay and energy consumption. However, due to the limited storage capacity and energy budget of RSUs, it is challenging to meet the demands of the highly dynamic Internet of Vehicles (IoV) environment. Therefore, determining reasonable service caching and computation offloading strategies is crucial. To address this, this paper proposes a joint service caching scheme for cloud-edge collaborative IoV computation offloading. By modeling the dynamic optimization problem using Markov Decision Processes (MDP), the scheme jointly optimizes task delay, energy consumption, load balancing, and privacy entropy to achieve better quality of service. Additionally, a dynamic adaptive multi-objective deep reinforcement learning algorithm is proposed. Each Double Deep Q-Network (DDQN) agent obtains rewards for different objectives based on distinct reward functions and dynamically updates the objective weights by learning the value changes between objectives using Radial Basis Function Networks (RBFN), thereby efficiently approximating the Pareto-optimal decisions for multiple objectives. Extensive experiments demonstrate that the proposed algorithm can better coordinate the three-tier computing resources of cloud, edge, and vehicles. Compared to existing algorithms, the proposed method reduces task delay and energy consumption by 10.64% and 5.1%, respectively. Copyright © 2025 The Authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2754.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
