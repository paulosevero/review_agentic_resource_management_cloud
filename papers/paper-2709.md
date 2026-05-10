---
id: paper-2709
title: Deadline-aware service scheduling via multi-head MARL in device-edge-cloud environments
authors:
- Mahjoubi, Ayeh
- Ramaswamy, Arunselvan
- Grinnemo, Karl-Johan
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112019
url: https://www.scopus.com/pages/publications/105027734962?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cellular IoT (CIoT)
- Deadline-aware scheduling
- Deep reinforcement learning (DRL)
- Mobile edge computing (MEC)
- Multi-agent reinforcement learning (MARL)
- Resource allocation
- Task offloading
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

# paper-2709 — Deadline-aware service scheduling via multi-head MARL in device-edge-cloud environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) enables latency-sensitive Internet of Things (IoT) applications by offloading computation to nearby edge servers. However, most existing intelligent scheduling approaches either neglect the full three-tier device-edge-cloud architecture or fail to account for heterogeneous IoT services composed of multiple dependent tasks with diverse deadlines and resource demands. These gaps hinder adaptability under dynamic network conditions. We propose a multi-agent reinforcement learning (MARL) framework in which cellular IoT devices and the edge server act as cooperative agents to optimize task offloading and scheduling. Each agent employs a multi-head deep Q-network (MH-DQN)-with one head per service type-to efficiently manage heterogeneous service workflows. We further implement a multi-head Double DQN (MH-DDQN) variant to improve stability and convergence. In addition, we benchmark our approach against four heuristic baselines and an adaptive simulated annealing (SA) scheduler. Simulation results demonstrate that both MH-DQN and MH-DDQN substantially outperform the heuristic baselines, and that the learned policies match or slightly exceed the SA acceptance ratio while achieving noticeably lower processing times, maintaining high deadline compliance (up to approximately 85% acceptance at heavy load), and reducing latency. MH-DDQN achieves the fastest convergence, greater stability, and slightly lower delays, highlighting its advantage for adaptive scheduling in complex MEC environments. © 2026

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2709.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
