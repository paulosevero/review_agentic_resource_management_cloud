---
id: paper-1897
title: 'Semantic-Aware Resource Allocation in MEC-Assisted SAGIN: A Deep Reinforcement Learning-based Approach'
authors:
- Liu, Yuexin
- Yin, Fangfang
- Liu, Qihong
- Liu, Danpu
- Jin, Libiao
- Li, Shufeng
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2025
doi: 10.1109/VTC2025-Fall65116.2025.11310140
url: https://www.scopus.com/pages/publications/105032416156?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- Multi-access edge computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1897 — Semantic-Aware Resource Allocation in MEC-Assisted SAGIN: A Deep Reinforcement Learning-based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we propose a semantic communication framework facilitated by multi-access edge computing (MEC)assisted satellite-air-ground integrated networks (SAGIN), which comprises of LEO satellites, unmanned aerial vehicles (UAVs), and macro-cell base stations (MBSs). Considering the limited wireless resources and diversified quality of service (QoS) requirements of semantic tasks, an optimization problem with the goal of minimizing system cost in terms of the task latency and energy consumption is formulated. In order to address the mixed-integer nonlinear programming (MINLP) problem, we propose an alternating optimization algorithm that tackles UAV deployment sub-problem with the successive convex approximation (SCA) method, task offloading, semantic compression, power allocation and computation resource allocation optimization with deep reinforcement learning (DRL)-based multi-agent proximal policy optimization (MAPPO) method. Simulation results demonstrate that our proposed algorithm outperformes other reinforcement learning algorithms, i.e., about 5.12%, 23.72% and 35.64% over PPO, DDPG, and A2C, respectively.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1897.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
