---
id: paper-1107
title: 'Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach'
authors:
- Ning, Xiangrui
- Zeng, Ming
- Hua, Meng
- Fei, Zesong
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2024.3419554
url: https://www.scopus.com/pages/publications/85197093235?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17496--17509
keywords:
- multi-agent reinforcement learning
- reconfigurable intelligent surfaces
- service migration
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1107 — Multiple Reconfigurable Intelligent Surfaces Aided Vehicular Edge Computing Networks: A MAPPO-Based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Reconfigurable intelligent surface (RIS) is envisioned as a new technology to improve the quality-of-service in vehicular edge computing (VEC) networks due to its ability to change the wireless radio propagation environment. In this paper, we study multi-RIS-assisted VEC networks, where vehicle user equipments (VUEs) can offload tasks to nearby base stations (BSs) which offer efficient computation edge services (ESs). Meanwhile, the individual virtual machine (VM), which is defined as a software clone of the VUE's service environment containing the profile and application to run the VUE's tasks, need to be migrated to the same ES for offloaded task completion. Accordingly, we formulate a throughput maximization problem for multi-RIS-assisted VEC networks via jointly optimizing the selected ESs, the deployment locations of RISs, and reflection matrices of RISs, subject to the maximum tolerable delay. To solve the non-convex mixed-integer nonlinear optimization problem, we propose an efficient algorithm based on multi-agent proximal policy optimization (MAPPO) with the centralized training and decentralized execution (CTDE) framework, where two types of heterogeneous agents are considered. In particular, several tricks such as reward normalization, orthogonal initialization, and learning rate decay are adopted to accelerate the convergence of the proposed algorithm. Numerical simulation results show that the throughput obtained by the proposed MAPPO-based scheme outperforms that obtained by the scheme without multi-RIS 26.41% and that obtained by the scheme without service migration 23.65%, respectively. Moreover, compared to other conventional multi-agent reinforcement learning (MARL) algorithms, the proposed algorithm converges faster.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1107.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
