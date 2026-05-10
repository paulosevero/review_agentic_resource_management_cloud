---
id: paper-2659
title: DeepSet-Enhanced Edge Reinforcement Learning for UAV Autonomous Landing and Takeoff at Portable Vertiports
authors:
- Li, Zhirun
- Gao, Tiying
- Qu, Chengyi
venue: 2026 International Conference on Computing, Networking and Communications, ICNC 2026
venue_type: conference
year: 2026
doi: 10.1109/ICNC68183.2026.11416848
url: https://www.scopus.com/pages/publications/105035748001?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 775--780
keywords:
- Deep Reinforcement Learning
- Intelligent Collision Avoidance
- Multi-Access Edge Computing
- Unmanned Aerial Vehicles
- Vertiport Operations
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2659 — DeepSet-Enhanced Edge Reinforcement Learning for UAV Autonomous Landing and Takeoff at Portable Vertiports

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) are increasingly deployed for delivery, monitoring, and emergency response, yet their large-scale coordination in congested airspace remains constrained by latency, bandwidth limits, and collision risks. Portable vertiports offer a mobile infrastructure for energy replenishment and structured takeoff/landing, but simultaneous operations require ultra-reliable and low-latency decision-making across multiple agents. This paper presents DREAM (DeepSetenhanced Reinforcement learning for Edge-based control in Ambiguous and dynamic environMents), a distributed edge intelligence framework that integrates deep reinforcement learning (DRL) with multi-access edge computing (MEC) principles. Each UAV operates as an edge client that performs real-time inference locally while synchronizing its policy with nearby vertiport servers through lightweight model updates, enabling scalable coordination without dependence on cloud backhaul. The framework adopts a centralized-training-and-decentralized-execution (CTDE) paradigm with a permutation-invariant DeepSet encoder and a safety-constrained Proximal Policy Optimization (PPOGAE) network. Simulation results under variable network latency and dynamic obstacles demonstrate that DREAM achieves a 98% mission success rate, reduces collisions by over 90%, and sustains stable performance within 100 ms edge-to-UAV latency budgets. These results highlight the feasibility of edge-assisted multi-agent learning for autonomous vertiport operations and its potential integration into future 5G/6G-enabled aerial networks. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2659.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
