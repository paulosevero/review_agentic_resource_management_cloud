---
id: paper-0492
title: Federated learning based energy efficient scheme for MEC with NOMA underlaying UAV
authors:
- Sharma, Himanshu
- Budhiraja, Ishan
- Consul, Prakhar
- Kumar, Neeraj
- Garg, Deepak
- Zhao, Liang
- Liu, Lie
venue: DroneCom 2022 - Proceedings of the 5th International ACM Mobicom Workshop on Drone Assisted Wireless Communications for 5G and Beyond
venue_type: conference
year: 2022
doi: 10.1145/3555661.3560867
url: https://www.scopus.com/pages/publications/85141861708?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 73--78
keywords:
- energy efficiency
- federated learning
- mobile edge computing (MEC)
- NOMA
- UAV
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0492 — Federated learning based energy efficient scheme for MEC with NOMA underlaying UAV

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicle (UAV) enabled Mobile Edge Computing (MEC) brings the on-demand task computation services close to the user equipment (UE) by reducing the latency and enhancing the quality-of-service (QoS). However, the energy consumption remains a major issue in the system, since both mobile devices (MDs) and UAVs have limited power battery storage. Also in 5G and beyond 5G (B5G) networks, in which UEs' task requests and positions change frequently, stationary edge network implementation may increase the overall energy consumption. This article aims to minimize the overall energy consumption for MEC with Non-Orthogonal Multiple Access (NOMA) underlaying UAV systems. We have used Markov decision process (MDP) to convert the optimization problem into multi-agent reinforcement learning (MARL) problem. Then to achieve optimal policy and reduce the overall energy consumption of the system, we propose a multi-agent federated reinforcement learning (MAFRL) scheme. Simulation results show the effectiveness of the proposed scheme in reducing the overall energy consumption with respect to other state-of-art schemes. © 2022 ACM.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0492.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
