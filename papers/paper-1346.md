---
id: paper-1346
title: MAPPO based Single-hop Task Offloading with Dynamic Vehicle Prediction in RSU-assisted IoV
authors:
- Zhao, Wei
- Yang, Dongling
- Weng, Tangjie
- Xu, Xinwei
- Shao, Xun
- Liu, Zhi
venue: Proceedings - 2024 IEEE Smart World Congress, SWC 2024 - 2024 IEEE Ubiquitous Intelligence and Computing, Autonomous and Trusted Computing, Digital Twin, Metaverse, Privacy Computing and Data Security,
  Scalable Computing and Communications
venue_type: conference
year: 2024
doi: 10.1109/SWC62898.2024.00096
url: https://www.scopus.com/pages/publications/105002219306?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 472--478
keywords:
- MAPPO
- neighboring vehicle prediction
- RSU
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1346 — MAPPO based Single-hop Task Offloading with Dynamic Vehicle Prediction in RSU-assisted IoV

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the realm of Internet of Vehicles (IoV), Roadside Units (RSUs) play a vital role due to their advanced sensing and computing capabilities. They support Mobile Edge Computing (MEC) by enabling real-time data processing and reducing latency and energy consumption. Given the large volume of data and the limited computing capacity of RSUs, tasks are often offloaded to other nodes, such as the cloud, other RSUs, or vehicles. However, due to the environment dynamic caused by vehicle mobility, the set of neighboring nodes for each RSU frequently changes, and variations in neighboring nodes are not perceived timely. In such cases, RSUs need to predict changes in neighboring nodes to ensure effective task offloading. Moreover, since each RSU can only perceive the surrounding environment, it is difficult for a single node to make optimal offloading decisions for each task independently. To address these issues, this paper proposes a distributed task offloading scheme that incorporates vehicle trajectory prediction. First, each RSU uses the vehicle trajectories predicted by the Gated Recurrent Unit (GRU) model to determine neighboring vehicles and update the set of neighboring nodes. Then, to enable each RSU to select a suitable computing node and minimize computation delay and energy consumption for the task, we adopt a distributed approach where each RSU independently makes offloading decisions based on local observations. To achieve this goal, we establish a 01 mathematical model and transform it into a Markov Decision Process (MDP). Subsequently, we propose a solution based on Multi-Agent Proximal Policy Optimization (MAPPO). Through extensive simulation experiments, we demonstrate that the scheme effectively reduces both long-term average processing delay and energy consumption.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1346.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
