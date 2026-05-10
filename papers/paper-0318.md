---
id: paper-0318
title: 'Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Munir, Md. Shirajum
- Abedin, Sarder Fakhrul
- Tran, Nguyen H.
- Han, Zhu
- Huh, Eui-Nam
- Hong, Choong Seon
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2021
doi: 10.1109/TNSM.2021.3049381
url: https://www.scopus.com/pages/publications/85099423791?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3476--3497
keywords:
- conditional value-at-risk (CVaR)
- demand-response (DR)
- microgrid
- Multi-access edge computing (MEC)
- multi-agent deep reinforcement learning
- stochastic game
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

# paper-0318 — Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, multi-access edge computing (MEC) is a key enabler for handling the massive expansion of Internet of Things (IoT) applications and services. However, energy consumption of a MEC network depends on volatile tasks that induces risk for energy demand estimations. As an energy supplier, a microgrid can facilitate seamless energy supply. However, the risk associated with energy supply is also increased due to unpredictable energy generation from renewable and non-renewable sources. Especially, the risk of energy shortfall is involved with uncertainties in both energy consumption and generation. In this article, we study a risk-aware energy scheduling problem for a microgrid-powered MEC network. First, we formulate an optimization problem considering the conditional value-at-risk (CVaR) measurement for both energy consumption and generation, where the objective is to minimize the expected residual of scheduled energy for the MEC networks and we show this problem is an NP-hard problem. Second, we analyze our formulated problem using a multi-agent stochastic game that ensures the joint policy Nash equilibrium, and show the convergence of the proposed model. Third, we derive the solution by applying a multi-agent deep reinforcement learning (MADRL)-based asynchronous advantage actor-critic (A3C) algorithm with shared neural networks. This method mitigates the curse of dimensionality of the state space and chooses the best policy among the agents for the proposed problem. Finally, the experimental results establish a significant performance gain by considering CVaR for high accuracy energy scheduling of the proposed model than both the single and random agent models.  © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0318.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
