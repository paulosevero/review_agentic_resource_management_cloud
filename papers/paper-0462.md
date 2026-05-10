---
id: paper-0462
title: Multiagent Reinforcement Learning for Task Offloading of Space/Aerial-Assisted Edge Computing
authors:
- Li, Yanlong
- Liang, Lei
- Fu, Jielin
- Wang, Junyi
venue: Security and Communication Networks
venue_type: journal
year: 2022
doi: 10.1155/2022/4193365
url: https://www.scopus.com/pages/publications/85130404107?origin=resultslist
publisher: Hindawi Limited
pages: ''
keywords:
- Antennas
- Convex optimization
- Edge computing
- Energy utilization
- Markov processes
- Multi agent systems
- Network architecture
- Quality of service
- Reinforcement learning
- Stochastic systems
- Computation costs
- Convex optimization problems
- Edge computing
- Edge server
- Energy-consumption
- Integrated networks
- Multi-agent reinforcement learning
- Nonconvex optimization
- NP-hard
- Task offloading
- Deep learning
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

# paper-0462 — Multiagent Reinforcement Learning for Task Offloading of Space/Aerial-Assisted Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The task offloading in space-aerial-ground integrated network (SAGIN) has been envisioned as a challenging issue. In this paper, we investigate a space/aerial-assisted edge computing network architecture considering whether to take advantage of edge server mounted on the unmanned aerial vehicle and satellite for task offloading or not. By optimizing the energy consumption and completion delay, we formulate a NP-hard and non-convex optimization problem to minimize the computation cost, limited by the computation capacity and energy availability constraints. By formulating the problem as a Markov decision process (MDP), we propose a multiagent deep reinforcement learning (MADRL)-based scheme to obtain the optimal task offloading policies considering dynamic computation request and stochastic time-varying channel conditions, while ensuring the quality-of-service requirements. Finally, simulation results demonstrate the task offloading scheme learned from our proposed algorithm that can substantially reduce the average cost as compared to the other three single agent deep reinforcement learning schemes.  © 2022 Yanlong Li et al.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0462.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
