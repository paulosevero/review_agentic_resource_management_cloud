---
id: paper-2184
title: 'Joint UAV Trajectory and Task Scheduling for Wireless Edge Networks: A Hybrid-Action Multi-Agent Reinforcement Learning Approach'
authors:
- Sun, Wenxue
- Zhao, Haitao
- Liu, Miao
- Li, Dapeng
- Pan, Guangliang
- Zhu, Hongbo
venue: 2025 17th International Conference on Wireless Communications and Signal Processing, WCSP 2025
venue_type: conference
year: 2025
doi: 10.1109/WCSP68525.2025.1010351
url: https://www.scopus.com/pages/publications/105033713689?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Air-ground integrated networks
- HA-MADDPG
- multi-UAV cooperative MEC
- offloading and migration
- trajectory control
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

# paper-2184 — Joint UAV Trajectory and Task Scheduling for Wireless Edge Networks: A Hybrid-Action Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the limited capacity and coverage of a single UAV, cooperative multi-UAV mobile edge computing (MEC) architectures have been increasingly applied to large-scale mobile terminals (MTs) scenarios. However, the high mobility of MTs and the limited resources of UAVs pose challenges such as resource contention, load imbalance, and service interruption. To address these issues, this paper proposes a joint optimization framework for multi-UAV task offloading and trajectory planning, aiming to minimize the total task completion delay. A non-convex hybrid optimization model is formulated to jointly address the coupling among task offloading, resource allocation, and migration decisions. Furthermore, we propose an enhanced hybrid-action multi-agent deep deterministic policy gradient (HA-MADDPG) algorithm that integrates the Gumbel-Softmax mechanism to enable hybrid action modeling and efficient policy learning. Simulation results show that our method significantly reduces task delay, improves resource utilization, and speeds up convergence, highlighting its adaptability and cooperative efficiency. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2184.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
