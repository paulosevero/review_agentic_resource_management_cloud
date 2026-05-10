---
id: paper-0453
title: Mobility-Aware Computation Offloading and Blockchain-based Handover in Vehicular Edge Computing Networks
authors:
- Lang, Ping
- Tian, Daxin
- Duan, Xuting
- Zhou, Jianshan
venue: IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC
venue_type: conference
year: 2022
doi: 10.1109/ITSC55140.2022.9922357
url: https://www.scopus.com/pages/publications/85141824266?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 176--182
keywords:
- Blockchain
- Deep learning
- Digital storage
- Markov processes
- Multi agent systems
- Reinforcement learning
- Vehicles
- Automated vehicles
- Block-chain
- Computation offloading
- Computing capacity
- Computing paradigm
- Edge computing
- Hand over
- High Speed
- Mobility-aware
- Roadside units
- computation offloading
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

# paper-0453 — Mobility-Aware Computation Offloading and Blockchain-based Handover in Vehicular Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a novel computing paradigm, vehicular edge computing (VEC) provides additional computing capacity to connected automated vehicles by deploying resources of computing and storage on base stations or roadside units. Vehicles migrate their tasks to VEC servers for execution through computation offloading (CO) to improve processing efficiency. However, the high-speed movement of vehicles causes handover among multiple VEC servers while raising the security issue of data sharing. In this paper, we design a mobility-aware CO and blockchain-based handover architecture to reduce the latency and improve the security of vehicular CO. A CO decision problem with models of mobility, CO, and blockchain-based handover is proposed to optimize the offloading decision of vehicles. Further, we transform this optimization into a Markov decision process (MDP) and construct a multi-agent deep reinforcement learning (MADRL) algorithm to solve it. The effectiveness and performance of the proposed method are verified by simulations.  © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0453.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
