---
id: paper-0448
title: Adaptive Computation Offloading Policy for Multi-Access Edge Computing in Heterogeneous Wireless Networks
authors:
- Ke, Hongchang
- Wang, Hui
- Sun, Weijia
- Sun, Hongbin
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2022
doi: 10.1109/TNSM.2021.3118696
url: https://www.scopus.com/pages/publications/85117123852?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 289--305
keywords:
- cost minimization
- deep reinforcement learning
- Multi-access edge computing
- quality of service
- unmanned aerial vehicle
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0448 — Adaptive Computation Offloading Policy for Multi-Access Edge Computing in Heterogeneous Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In heterogeneous wireless networks, massive mobile terminals randomly generate a large number of computation tasks (payloads). How to better manage these mobile terminals located in wireless networks to achieve acceptable quality of service (QoS) such as latency minimization, energy consumption minimization is crucial. A multi-access edge computing (MEC) server can be leveraged to execute the offloaded payloads generated from mobile terminals owing to its powerful processing power and location proximity features. However, an MEC server cannot tackle all offloaded tasks from multiple mobile terminals, and its energy consumption needs further consideration. We introduce an edge server model combined with the unmanned aerial vehicle (UAV) and equipped with the macro base station (MBS-MEC) to process the arrival payloads, and all UAVs and MBS-MECs can harvest renewable energy by using energy harvesting equipment. Furthermore, we model the computation offloading as a deep reinforcement learning scheme without priori knowledge. Considering the infeasibility of deep-reinforcement learning-based centralized learning for the proposed edge computing framework, we propose a distributed computation offloading scheme based on deep reinforcement learning (DCODRL) to minimize the weighted average cost, including the latency cost and the energy cost. Each mobile terminal can be regarded as a learning agent for the DCODRL. To compensate for the lack of cooperation of the DCODRL, we propose a gated-recurrent-unit-assisted multi-agent computation offloading scheme based on deep reinforcement learning (MCODRL) to improve the offloading policy by obtaining global observation information and designing a common reward for all agents. Comprehensive numerical results reflect the convergence and effectiveness of the DCODRL and MCODRL, and the efficacy of the proposed algorithms is further verified through comparisons with two baseline algorithms. © 2004-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0448.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
