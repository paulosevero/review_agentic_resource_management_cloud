---
id: paper-1660
title: DRL and Game Theory-Based Trajectory Optimization and Task Offloading in Multi-UAV-Assisted MEC
authors:
- Hu, Zhihao
- Chen, Ying
- Chen, Zhuoyue
- Guo, Yuran
- Huang, Jiwei
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2025
doi: 10.1109/TSC.2025.3611295
url: https://www.scopus.com/pages/publications/105016484748?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3696--3709
keywords:
- deep reinforcement learning
- Multi-access edge computing
- stackelberg game
- task offloading
- uncrewed aerial vehicle
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

# paper-1660 — DRL and Game Theory-Based Trajectory Optimization and Task Offloading in Multi-UAV-Assisted MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In UAV-assisted Multi-access Edge Computing (MEC) systems, UAV trajectories and resource pricing directly determine system utility - improper UAV positioning will lead to increased delay and energy costs for users, while inappropriate pricing will result in insufficient task offloading or UAV overload. This article aims to optimize UAVs' trajectories, pricing strategies and users' offloading decisions, enabling UAVs to move to suitable locations and provide computing offloading services at appropriate prices, thereby reducing delay and energy, and enhancing the utilities of both UAV and users. The user utility specifically consist of throughput, energy consumption, delay penalties, and expenditures on purchasing computing resources. The UAV's utility consists of computing energy consumption, delay penalties, and revenue from selling computing resources as incentives. We formulate the pre-offloading problem to solve users' offloading selection, and transform the problem into a multi-user non-cooperative game using game theory while proving the existence of Nash equilibrium. Then we model the interaction between UAV and users using Stackelberg game model and prove the existence of Stackelberg equilibrium. We use multi-agent deep reinforcement learning (MADRL) and propose DRL and Game Theory-based Trajectory Optimization and Task Offloading (DGTT) algorithm to solve UAVs' trajectories and obtain the Stackelberg equilibrium solution. We sequentially solve for the pricing strategy and offloading decisions, thereby obtaining the optimized utilities of both UAV and users. Finally, we conduct simulation experiments to verify the feasibility of DGTT algorithm, along with comparative experiments that demonstrate our proposed DGTT algorithm's excellent performance in optimizing UAV and user utilities, while reducing system energy consumption and delay. © 2008-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1660.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
