---
id: paper-0742
title: 'Energy-AOI-Aware UAV-Assisted Data Collection: A Multi-Agent Deep Reinforcement Learning-Based Trajectory Optimization'
authors:
- Wan, Liangtian
- Zhang, Kun
- Sun, Lu
- Xu, Gang
- Wang, Xianpeng
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2023
doi: 10.1109/ICCT59356.2023.10419500
url: https://www.scopus.com/pages/publications/85186099542?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 176--180
keywords:
- Age of Information
- data collection
- deep rein-forcement learning
- unmanned aerial vehicle (UAV) trajectory planning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-0742 — Energy-AOI-Aware UAV-Assisted Data Collection: A Multi-Agent Deep Reinforcement Learning-Based Trajectory Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of Internet of Things (IoT) technology, sensor networks are widely used for data collection in various IoT scenarios. Traditional sensors use multi-hop communication to transmit data back to the data center, which can lead to excessive energy consumption in some nodes and cause the collapse of sensor networks. Solving the data transmission problem in sensor networks has become a critical issue. In recent years, unmanned aerial vehicles (UAVs) capable of hovering have been increasingly applied in military and civilian fields, such as smart logistics, edge computing, and wireless power transfer (WPT). UAVs, with their strong controllability and high mobility, can effectively perform the task of data transmission in sensor networks. In the task of UAV -assisted sensor data collection, UAVs can establish communication connections with ground sensors through small communication devices and act as mobile aggregation nodes to collect data from the ground wireless sensor network. To achieve energy balance among sensor network nodes as much as possible while ensuring service quality based on information age, we propose a combinatorial optimization problem. Ultimately, we solve the combinatorial optimization problem by optimizing the trajectory of UAV flight. As the problem is a mixed-integer non-convex optimization which is difficult to solve, we propose a UAV swarm-based sensor trajectory planning algorithm using multi-agent reinforcement learning. Simulation results show that the proposed algorithm has a better effect than baseline approaches on optimization objective. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0742.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
