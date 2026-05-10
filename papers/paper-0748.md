---
id: paper-0748
title: 'MADDPG: A task offloading algorithm based on multi-agent deep reinforcement learning in vehicle-edge computing'
authors:
- Wang, Xiaoer
- Ding, Shuang
- Zhang, Guoqing
venue: ACM International Conference Proceeding Series
venue_type: conference
year: 2023
doi: 10.1145/3640912.3640992
url: https://www.scopus.com/pages/publications/85186954116?origin=resultslist
publisher: Association for Computing Machinery
pages: 408--413
keywords:
- multi-agent deep reinforcement learning
- task offloading
- Vehicle-edge computing
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

# paper-0748 — MADDPG: A task offloading algorithm based on multi-agent deep reinforcement learning in vehicle-edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicle-edge computing has emerged as a new paradigm based on vehicular networking to provide computing resources for mobile vehicles. However, traditional binary offloading methods result in wastage of vehicle and server resources, as well as the mobility of vehicles and dynamic network changes pose significant challenges. To address those challenges, we propose a Multi-Agent Deep Deterministic Policy Gradient (MADDPG) task offloading algorithm, which considers the dynamics of the network. This algorithm enables each vehicle to make optimal offloading decisions to achieve the best long-term rewards. Specifically, we model the problem of mobile vehicle task offloading as a Markov Decision Process, which each mobile vehicle is treated as an agent and its information is encoded into the state space. Based on the current vehicle state, a mobile vehicle can choose an action to offload a task to a nearby edge server and receive a corresponding reward value. Subsequently, the mobile vehicle transitions to the next state. Through continuous learning and policy optimization, mobile vehicles can reduce the overall sum of system delay and energy consumption. Simulation results demonstrate that our proposed algorithm outperforms other benchmark algorithms on the overall sum of system delay and energy consumption.  © 2023 ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0748.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
