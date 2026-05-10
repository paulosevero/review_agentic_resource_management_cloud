---
id: paper-2486
title: Online Function Scheduling for Dual-Heterogeneous Serverless Vehicular Edge Computing
authors:
- Zhu, Lei
- Huang, Hanzhong
- Zhang, Zhizhong
- Zhuang, Ling
- Hou, Chengjie
venue: IEEE Transactions on Intelligent Vehicles
venue_type: journal
year: 2025
doi: 10.1109/TIV.2024.3384184
url: https://www.scopus.com/pages/publications/85189631326?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2748--2764
keywords:
- function scheduling
- Heterogeneous vehicular edge computing
- multi-agent reinforcement learning
- serverless edge computing
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

# paper-2486 — Online Function Scheduling for Dual-Heterogeneous Serverless Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular service providers bear a heavy burden of scalability and service load balancing problems in traditional edge computing systems. By abstracting the service computing granularity to a higher function level, the nascent serverless edge computing is envisioned to leave the burdensome scheduling and management issues to computing vendors. Nevertheless, the traditional terrestrial-based edge system's features, such as heterogeneity, scattered deployments, and environment dynamics, significantly complicate the function scheduling process for computing vendors. Specifically, inhomogeneous load distribution caused by these features leads to edge servers' concurrent performance bottlenecks and low resource efficiency issues. Further, it is crucial to develop an efficient scheduling scheme for the serverless vehicular edge computing network with heterogeneous function requirements/edge configurations and without prior environment evolution knowledge. To this end, we propose a dual-heterogeneous serverless vehicular edge computing network to facilitate the function scheduling within two-scale ranges. We formulate the joint function scheduling problem considering the closely coupled request dispatching, function placement, and computation resource allocation as a cooperative partially observable Markov game. Then, a model-free multi-agent reinforcement learning is introduced to acquire an online scheduling strategy. Simulation experiments show that the proposed approach can guarantee more completed function requests than other baselines.  © 2016 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2486.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
