---
id: paper-0634
title: 'Task Offloading and Resource Allocation in Vehicular Networks: A Lyapunov-Based Deep Reinforcement Learning Approach'
authors:
- Kumar, Anitha Saravana
- Zhao, Lian
- Fernando, Xavier
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2023.3271613
url: https://www.scopus.com/pages/publications/85159819876?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13360--13373
keywords:
- Lyapunov optimization
- multi-agent DDPG
- reinforcement learning
- resource management
- VEC
- vehicle edge computing
- vehicular networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0634 — Task Offloading and Resource Allocation in Vehicular Networks: A Lyapunov-Based Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular Edge Computing (VEC) has gained popularity due to its ability to enhance vehicular networks. VEC servers located at Roadside Units (RSUs) allow low-power vehicles to offload computation-intensive and delay-sensitive applications, making it a promising solution. However, optimal resource allocation between edge servers is a complex issue due to vehicle mobility and dynamic data traffic. To address this issue, we propose a Lyapunov-based Multi-Agent Deep Deterministic Policy Gradient (L-MADDPG) method that jointly optimizes computing task distribution and radio resource allocation to minimize energy consumption and delay requirements. We evaluate the trade-offs between the performance of the optimization algorithm, queuing model, and energy consumption. We first examine delay, queue and energy models for task execution at the vehicle or RSU, followed by the L-MADDPG algorithm for jointly optimizing task offloading and resource allocation problems to reduce energy consumption without compromising performance. Our simulation results show that our algorithm can reduce energy consumption while maintaining system performance compared to existing algorithms.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0634.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
