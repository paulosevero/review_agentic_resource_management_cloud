---
id: paper-0643
title: Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System
authors:
- Li, Si
- Li, Wei
- Shi, Huaguang
- Yan, Wenhao
- Zhou, Yi
venue: ACM International Conference Proceeding Series
venue_type: conference
year: 2023
doi: 10.1145/3640912.3640991
url: https://www.scopus.com/pages/publications/85186955718?origin=resultslist
publisher: Association for Computing Machinery
pages: 403--407
keywords:
- reinforcement learning
- task offload
- trajectory optimization
- Unmanned air vehicle
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

# paper-0643 — Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) equipped with Multi-Access Edge Computing (MEC) servers can assist Terminal Devices (TDs) in offloading data tasks. In this paper, we investigate a resource allocation and trajectory optimization problem of multiple UAVs assisting TDs in task computation, and our main goal is to improve the task computation efficiency of the system to meet the high-quality experience of TDs. We consider the fairness of TD's computing data volume and the fairness of UAV energy consumption. The problem is transformed into a Partially Observable Markov Decision Process (POMDP). The large action space generated during the UAV flight and resource allocation decision-making process leads to a policy overfitting problem for Multi-Agent Proximal Policy Optimization (MAPPO) method. Policy overfitting causes the UAV to update the policy gradient in the suboptimization direction, preventing it from exploring better flight trajectories. To meet this challenge, we propose a novel method of policy regularization, NV-MAPPO. Simulation results show that NV-MAPPO has significant advantages in latency and energy consumption.  © 2023 ACM.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0643.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
