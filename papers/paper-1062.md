---
id: paper-1062
title: QoS-aware task offloading and resource allocation optimization in vehicular edge computing networks via MADDPG
authors:
- Liu, Jingxian
- Wang, Yitian
- Pan, Duotao
- Yuan, Decheng
venue: Computer Networks
venue_type: journal
year: 2024
doi: 10.1016/j.comnet.2024.110282
url: https://www.scopus.com/pages/publications/85185550287?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Internet of vehicles
- Mobile edge computing
- Offloading strategy
- Resource allocation
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

# paper-1062 — QoS-aware task offloading and resource allocation optimization in vehicular edge computing networks via MADDPG

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To meet the stringent requirements for real-time performance of computing tasks on the Internet of Vehicles (IoV) scenario, the Mobile Edge Computing (MEC) technique is introduced to combine edge servers with vehicles that have storage and computing resources, thereby reducing latency. However, successfully accessing the channel and completing the offloading computation within the specified time remains a big challenge in scenarios with multitasking vehicles and multibase stations equipped with multiple channels. To address this problem, we propose the Multi-Agent Deep Deterministic Policy Gradient-based Offloading and Resource Allocation (MADDPG-RA) algorithm. First, a sub-optimal offloading strategy is determined using the MADDPG algorithm to minimize the sum of system latency and energy consumption. Specifically, this strategy determines whether each vehicle should perform local or offload computation, which MEC server to choose, and which channel to access if offloaded. Based on the above, a closed form expression for the optimal computational resource allocation for MEC is derived using Lagrange multipliers. The simulation results demonstrate that the proposed MADDPG-RA algorithm can effectively reduce the total system latency and energy consumption compared to the existing algorithms. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1062.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
