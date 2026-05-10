---
id: paper-1250
title: Joint computation offloading and resource allocation for end-edge collaboration in internet of vehicles via multi-agent reinforcement learning
authors:
- Wang, Cong
- Wang, Yaoming
- Yuan, Ying
- Peng, Sancheng
- Li, Guorui
- Yin, Pengfei
venue: Neural Networks
venue_type: journal
year: 2024
doi: 10.1016/j.neunet.2024.106621
url: https://www.scopus.com/pages/publications/85201314014?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Attention mechanism
- Heterogeneous resource allocation
- Multi-agent DRL
- Real-time task offloading
- Recurrent neural networks
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

# paper-1250 — Joint computation offloading and resource allocation for end-edge collaboration in internet of vehicles via multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC), a promising paradigm for the development of emerging intelligent transportation systems, can provide lower service latency for vehicular applications. However, it is still a challenge to fulfill the requirements of such applications with stringent latency requirements in the VEC system with limited resources. In addition, existing methods focus on handling the offloading task in a certain time slot with statically allocated resources, but ignore the heterogeneous tasks’ different resource requirements, resulting in resource wastage. To solve the real-time task offloading and heterogeneous resource allocation problem in VEC system, we propose a decentralized solution based on the attention mechanism and recurrent neural networks (RNN) with a multi-agent distributed deep deterministic policy gradient (AR-MAD4PG). First, to address the partial observability of agents, we construct a shared agent graph and propose a periodic communication mechanism that enables edge nodes to aggregate information from other edge nodes. Second, to help agents better understand the current system state, we design an RNN-based feature extraction network to capture the historical state and resource allocation information of the VEC system. Thirdly, to tackle the challenges of excessive joint observation-action space and ineffective information interference, we adopt the multi-head attention mechanism to compress the dimension of the observation-action space of agents. Finally, we build a simulation model based on the actual vehicle trajectories, and the experimental results show that our proposed method outperforms the existing approaches. © 2024

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1250.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
