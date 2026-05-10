---
id: paper-2548
title: An enhanced MADDPG framework for joint energy and QoS optimization in UAV-assisted vehicular edge computing system
authors:
- Dai, Cheng
- Pan, Junqi
- Liu, Xianggen
- Garg, Sahil
- Moussa, Sherif
- Kandouci, Chahinaz
venue: Applied Energy
venue_type: journal
year: 2026
doi: 10.1016/j.apenergy.2026.127370
url: https://www.scopus.com/pages/publications/105028511456?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Energy saving
- Multi-agent reinforcement learning
- Quality of service
- Task offloading
- Vehicle networking
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

# paper-2548 — An enhanced MADDPG framework for joint energy and QoS optimization in UAV-assisted vehicular edge computing system

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The objective of this study is to address the challenges posed by high energy overhead and the complexity of ensuring quality of service (QoS) for vehicular edge computing in dynamic environments. To this end, this paper investigates the task offloading problem for vehicular edge computing networks in urban areas where there are task offloading hotspots. The objective is twofold: first, to minimize the system energy expenditure, and second, to ensure the service quality. To this end, Unmanned Aerial Vehicles (UAVs) are introduced as mobile offloading nodes to physically reduce the signal transmission distance and lower the system energy consumption. To this end, we propose a resource allocation optimization framework centered on a novel Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm. Our algorithm's novelty lies in its integration of a dual-critic mechanism for robust and stable Q-value estimation and a maximum entropy framework to enhance exploration efficiency in complex environments. This intelligent algorithm is synergistically coupled with a clustering-based UAV deployment strategy to handle this dynamic problem. This strategy dynamically and autonomously achieves the optimal resource allocation and UAV deployment, with the objective of reducing the system energy overhead and guaranteeing the QoS. Simulation results demonstrate that this framework significantly enhances resource allocation efficiency. Compared to the original MADDPG algorithm, it reduces task costs by 24%, and compared to the fixed offloading position scheme, it reduces task costs by 31.3%. This study offers a valuable reference point and practical insights for reducing energy overhead and optimizing resource allocation in edge computing for vehicular networking. © 2026 Elsevier Ltd

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2548.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
