---
id: paper-2828
title: 'Joint caching-trajectory optimization for dynamic UAV-MEC networks: Context-aware game combined MADDPG'
authors:
- Wang, Zilin
- Chen, Liming
- Chen, Pengxian
- Zheng, Yifeng
- Zhang, Wenjie
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112267
url: https://www.scopus.com/pages/publications/105034471085?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Dynamic trajectory
- Mobile edge computing (MEC)
- Multi-Agent deep deterministic policy gradient (MADDPG)
- Resource allocation
- Service caching
- Unmanned aerial vehicle(UAV)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2828 — Joint caching-trajectory optimization for dynamic UAV-MEC networks: Context-aware game combined MADDPG

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Despite the growing attention toward Unmanned Aerial Vehicle (UAV)-assisted Mobile Edge Computing (MEC), the inherent energy constraints of UAVs and the requirement for low task delay remain significant challenges for its practical application. This paper investigates the joint optimization of task offloading, service caching, trajectory planning and resource allocation in the multi-UAV-assisted MEC system to minimize long-term average execution delay. We formulate the problem as a Mixed-Integer Nonlinear Programming (MINLP) problem and propose a Context-Aware Potential-Game-based Multi-Agent Deep Deterministic Policy Gradient (CAPG-MADDPG) algorithm to tackle the coupled discrete-continuous optimization and complex action space. The original problem is decoupled into three subproblems. Specifically, the task offloading subproblem is solved using Potential Game (PG) algorithm; then, the service caching subproblem is addressed by Contextual Combinatorial Multi-Armed Bandit (CCMAB) algorithm; finally, the UAV trajectory planning and resource allocation subproblem is jointly optimized via MADDPG algorithm. Experimental results demonstrate that the proposed CAPG-MADDPG algorithm outperforms other Deep Reinforcement Learning (DRL) and caching algorithms in terms of long-term completion delay, while also exhibiting fast convergence and better training stability. © 2026 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2828.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
