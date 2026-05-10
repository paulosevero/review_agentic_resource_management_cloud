---
id: paper-1080
title: An UAVs-Assisted Edge Computing Network with Multi-agent Reinforcement Learning
authors:
- Ma, Zhichao
- Miao, Jingyu
- Peng, Liang
- Liu, Bin
- Zhang, Limin
venue: Lecture Notes in Electrical Engineering
venue_type: conference
year: 2024
doi: 10.1007/978-981-97-2757-5_15
url: https://www.scopus.com/pages/publications/85192499593?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 135--143
keywords:
- mobile edge computing
- path planning
- reinforcement learning
- UAV communication
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1080 — An UAVs-Assisted Edge Computing Network with Multi-agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> After installing a wireless communication module and computing equipment on the UAV (Unmanned Aerial Vehicle), the UAV can provide better communication coverage and even edge computing services for ground nodes by taking advantage of its high maneuverability and altitude advantages. According to the characteristics of user mobility and energy sensitivity, the edge computing problem of an intensive intelligent terminal network is presented. In this paper path planning and task computing strategy optimization are studied. For multi-UAV scenarios, a multi-agent reinforcement learning algorithm combined with initial UAV deployment is proposed. Specifically, the GAK (Genetic Algorithm k-means) algorithm is used to optimize the initial deployment positions of all UAVs. Then, using the multi-agent reinforcement learning algorithm MADDPG solves the optimization problems of track planning and task calculation strategies in dynamic environments. The simulation results indicate that the GAK-MADDPG algorithm can effectively utilize the local computing power of UAV and intelligent terminal by reasonably planning the trajectory and task calculation strategy of UAV, thus saving energy consumption on the user side to the greatest extent. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1080.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
