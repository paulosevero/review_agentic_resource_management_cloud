---
id: paper-0627
title: Deep Reinforcement Learning-based Power Control and Bandwidth Allocation Policy for Weighted Cost Minimization in Wireless Networks
authors:
- Ke, Hongchang
- Wang, Hui
- Sun, Hongbin
venue: Applied Intelligence
venue_type: journal
year: 2023
doi: 10.1007/s10489-023-04929-2
url: https://www.scopus.com/pages/publications/85169561261?origin=resultslist
publisher: Springer
pages: 26885--26906
keywords:
- Cost minimization
- Deep reinforcement learning
- Markov decision process
- Mobile edge computing
- Power allocation
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0627 — Deep Reinforcement Learning-based Power Control and Bandwidth Allocation Policy for Weighted Cost Minimization in Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) can dispatch its powerful servers close by to assist with the computation workloads that intelligent wireless terminals have offloaded. The MEC server’s physical location is closer to the intelligent wireless terminals, which can satisfy the low latency and high reliability demands. In this paper, we formulate an MEC framework with multiple vehicles and service devices that considers the priority and randomness of arriving workloads from roadside units (RSUs), cameras, laser radars (Lidar) and the time-varying channel state between the service device and MEC server (MEC-S). To minimize the long-term weighted average cost of the proposed MEC system, we transit this issue (cost minimization problem) into the Markov decision process (MDP). Furthermore, considering the difficulty realizing the state transition probability matrix, the dimensional complexity of the state space, and the continuity of the action space, we propose a deterministic policy gradient (MADDPG)-based bandwidth partition and power allocation optimization policy. The proposed MADDPG-based policy is a model-free deep reinforcement learning (DRL) method, which can effectively deal with continuous action space and further guide multi-agent to execute decision-making. The comprehensive results verify that the proposed MADDPG-based optimization scheme has fine convergence and performance that is better than that of the other four baseline algorithms. © 2023, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0627.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
