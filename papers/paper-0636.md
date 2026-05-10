---
id: paper-0636
title: Blockchain-Based Cooperative Computation Offloading and Secure Handover in Vehicular Edge Computing Networks
authors:
- Lang, Ping
- Tian, Daxin
- Duan, Xuting
- Zhou, Jianshan
- Sheng, Zhengguo
- Leung, Victor C.M.
venue: IEEE Transactions on Intelligent Vehicles
venue_type: journal
year: 2023
doi: 10.1109/TIV.2023.3271367
url: https://www.scopus.com/pages/publications/85159654508?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3839--3853
keywords:
- blockchain
- cooperative computation offloading
- deep reinforcement learning
- Vehicular edge computing
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0636 — Blockchain-Based Cooperative Computation Offloading and Secure Handover in Vehicular Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Facing the requirements of intelligent vehicles for massive data processing, vehicular edge computing (VEC) utilizes computing resources deployed on the roadside infrastructure to provide proximity computing services for vehicles and forms a novel computing paradigm. Thus, vehicles can reduce the burden of local computing and improve computing efficiency by offloading tasks to roadside computing servers or neighboring resource-idle vehicles for execution via cooperative computation offloading (CO). However, dynamic communication channel states and data handover among multiple VEC servers caused by vehicle mobility pose challenges for CO decision-making and data security. This article applies blockchain to the cooperative CO of VEC and thus proposes a cooperative CO and secure handover framework with a consensus mechanism to guarantee the efficiency of cooperative CO and secure handover. In this framework, models for vehicle mobility and cooperative CO handover are constructed, and a consensus mechanism is proposed. This mechanism ensures the synchronization and immutability of offloaded data in the CO handover. A cooperative CO decision optimization is also formulated considering secure handover with blockchain technology to optimize the latency of vehicular computing tasks. To solve this complex problem, this optimization is transformed into a Markov decision process and a cooperative CO decision algorithm with multiagent deep reinforcement learning is designed, thus achieving the optimal solution. Extensive simulations verified the performance and effectiveness of the proposed method.  © 2016 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0636.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
