---
id: paper-1481
title: 'Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach'
authors:
- Chen, Juan
- Zhong, Jie
- Wu, Zongling
- Tian, Di
- Chen, Yujie
venue: Journal of King Saud University - Computer and Information Sciences
venue_type: journal
year: 2025
doi: 10.1007/s44443-025-00160-w
url: https://www.scopus.com/pages/publications/105013646560?origin=resultslist
publisher: Springer International Publishing
pages: ''
keywords:
- Deep reinforcement learning
- Optimization of task delay and failure rate
- Satellite edge computing
- Task priority
- Task scheduling
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

# paper-1481 — Priority-aware task offloading for LEO satellite edge computing network: a multi-agent deep reinforcement learning-based approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the current data-driven era, satellite edge computing (SatEC) emerges as a novel computing paradigm that addresses the coverage limitations of terrestrial networks in remote areas by deploying computational resources on satellite networks. This provides a new avenue for real-time data processing on a global scale. However, effectively scheduling tasks to optimize resource utilization, reduce processing delay, and ensure the timeliness of task execution has become a critical issue in SatEC. Existing task scheduling algorithms often fail to fully consider task deadlines and priority orders, leading to deficiencies in handling urgent tasks and optimizing overall computational efficiency. In response to these issues, we propose a multi-agent advantage actor-critic (MA2C) algorithm based on deep reinforcement learning, aiming to effectively address the task scheduling challenges in SatEC. The MA2C algorithm employs two cooperative agents to optimize scheduling strategies: one agent is responsible for prioritizing tasks, while the other focuses on task offloading decisions. These two agents interact in real-time, dynamically adjusting their strategies to adapt to environmental changes, effectively enhancing scheduling efficiency. Furthermore, the agent design adopts an encoder-decoder architecture, combined with self-attention (SA) mechanisms and temporal convolutional network (TCN) technology to extract environmental features, achieving real-time optimization of task scheduling. The simulation results indicate that the MA2C algorithm outperforms existing algorithms across various scenarios. Compared with the baseline algorithms BDQN, DRTO, and GA, the MA2C algorithm reduces the task failure rate by 9.1%, 11.2%, and 16.9% respectively. © The Author(s) 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1481.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
