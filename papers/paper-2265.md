---
id: paper-2265
title: Joint offloading decision and resource allocation in vehicular edge computing networks
authors:
- Wang, Shumo
- Song, Xiaoqin
- Xu, Han
- Song, Tiecheng
- Zhang, Guowei
- Yang, Yang
venue: Digital Communications and Networks
venue_type: journal
year: 2025
doi: 10.1016/j.dcan.2023.03.006
url: https://www.scopus.com/pages/publications/86000739163?origin=resultslist
publisher: KeAi Communications Co.
pages: 71--82
keywords:
- Computation offloading
- Multi-agent deep deterministic policy gradient
- Potential game
- Resource allocation
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

# paper-2265 — Joint offloading decision and resource allocation in vehicular edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of Intelligent Transportation Systems (ITS), many new applications for Intelligent Connected Vehicles (ICVs) have sprung up. In order to tackle the conflict between delay-sensitive applications and resource-constrained vehicles, computation offloading paradigm that transfers computation tasks from ICVs to edge computing nodes has received extensive attention. However, the dynamic network conditions caused by the mobility of vehicles and the unbalanced computing load of edge nodes make ITS face challenges. In this paper, we propose a heterogeneous Vehicular Edge Computing (VEC) architecture with Task Vehicles (TaVs), Service Vehicles (SeVs) and Roadside Units (RSUs), and propose a distributed algorithm, namely PG-MRL, which jointly optimizes offloading decision and resource allocation. In the first stage, the offloading decisions of TaVs are obtained through a potential game. In the second stage, a multi-agent Deep Deterministic Policy Gradient (DDPG), one of deep reinforcement learning algorithms, with centralized training and distributed execution is proposed to optimize the real-time transmission power and subchannel selection. The simulation results show that the proposed PG-MRL algorithm has significant improvements over baseline algorithms in terms of system delay. © 2023 Chongqing University of Posts and Telecommunications

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2265.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
