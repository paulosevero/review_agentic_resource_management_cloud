---
id: paper-0982
title: Medley deep reinforcement learning-based workload offloading and cache placement decision in UAV-enabled MEC networks
authors:
- Ke, Hongchang
- Wang, Hui
- Sun, Hongbin
venue: Complex and Intelligent Systems
venue_type: journal
year: 2024
doi: 10.1007/s40747-023-01318-7
url: https://www.scopus.com/pages/publications/85181967776?origin=resultslist
publisher: Springer International Publishing
pages: 3003--3023
keywords:
- Deep reinforcement learning
- Mobile edge computing
- Service caching
- Unmanned aerial vehicle
- Workload offloading
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

# paper-0982 — Medley deep reinforcement learning-based workload offloading and cache placement decision in UAV-enabled MEC networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet of Things devices generate a large number of heterogeneous workloads in real-time that require specific application to tackle, and the inability to communicate between devices and communication base stations due to complex scenarios is a thorny issue. Service caching play a key role in managing specific-request workload from devices, and unmanned aerial vehicles with computation and communication functions can effectively solve communication barrier between devices and ground base stations. In addition, the joint optimization of workload offloading and service cache placement is a key issue. Accordingly, we design an unmanned aerial vehicle-enabled mobile edge computing system with multiple devices, unmanned aerial vehicles and edge servers. The proposed framework takes into account the randomness of workload arrival, the time-varying nature of channel states, the limitations of the hosting service caching, and wireless communication blocking. Furthermore, we designed workload offloading and service caching hosting decision-making optimization problems to minimize the long-term weighted average latency and energy consumption costs. To tackle this joint optimization problem, we propose a request-specific workload offloading and service caching decision-making scheme based on the medley deep reinforcement learning scheme. To this end, the proposed scheme is decomposed into two-stage optimization subproblems: the workload offloading decision-making problem and the service caching hosting selection problem. In terms of the first subproblem, we model each device as a learning agent and propose the workloads offloading decision-making scheme based on multi-agent deep deterministic policy gradient. For the second subproblem, we present the decentralized double deep Q-learning scheme to tackle the service caching hosting policy. According to the comprehensive experimental results, the proposed scheme is able to converge rapidly on various parameter configurations and whose performance surpasses the other four baseline learning algorithms. © The Author(s) 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0982.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
