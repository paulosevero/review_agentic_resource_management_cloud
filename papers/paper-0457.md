---
id: paper-0457
title: A Graph Attention Mechanism-Based Multiagent Reinforcement-Learning Method for Task Scheduling in Edge Computing
authors:
- Li, Yinong
- Li, Jianbo
- Pang, Junjie
venue: Electronics (Switzerland)
venue_type: journal
year: 2022
doi: 10.3390/electronics11091357
url: https://www.scopus.com/pages/publications/85128755273?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- computation offloading
- deep Q-learning
- deep reinforcement learning
- graph neural networks
- multi-access edge computing
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

# paper-0457 — A Graph Attention Mechanism-Based Multiagent Reinforcement-Learning Method for Task Scheduling in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) enables end devices with limited computing power to provide effective solutions while dealing with tasks that are computationally challenging. When each end device in an MEC scenario generates multiple tasks, how to reasonably and effectively schedule these tasks is a large-scale discrete action space problem. In addition, how to exploit the objectively existing spatial structure relationships in the given scenario is also an important factor to be considered in task-scheduling algorithms. In this work, we consider indivisible, time-sensitive tasks under this scenario and formalize the task-scheduling problem to minimize the long-term losses. We propose a multiagent collaborative deep reinforcement learning (DRL)-based distributed scheduling algorithm based on graph attention neural networks (GATs) to solve task-scheduling problems in the MEC scenario. Each end device creates a graph representation agent to extract potential spatial features in the scenario and a scheduling agent to extract the timing-related features of the tasks and make scheduling decisions using a gated recurrent unit (GRU). The simulation results show that, compared with several baseline algorithms, our proposed algorithm can take advantage of the spatial positional relationship of devices in the environment, significantly reduce the average delay and drop rate, and improve link utilization. © 2022 by the authors. Licensee MDPI, Basel, Switzerland.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0457.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
