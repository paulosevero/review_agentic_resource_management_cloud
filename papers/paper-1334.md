---
id: paper-1334
title: Energy Efficiency Maximization for Multi-UAV-IRS-Assisted Marine Vehicle Systems
authors:
- Zhang, Chaoyue
- Lin, Bin
- Li, Chao
- Qi, Shuang
venue: Journal of Marine Science and Engineering
venue_type: journal
year: 2024
doi: 10.3390/jmse12101761
url: https://www.scopus.com/pages/publications/85207494220?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning
- energy efficiency
- marine vehicle systems
- unmanned aerial vehicle
- unmanned surface vehicle
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1334 — Energy Efficiency Maximization for Multi-UAV-IRS-Assisted Marine Vehicle Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing is envisioned as a prospective technology for supporting time-sensitive and computation-intensive applications in marine vehicle systems. However, the offloading performance is highly impacted by the poor wireless channel. Recently, an Unmanned Aerial Vehicle (UAV) equipped with an Intelligent Reflecting Surface (IRS), i.e., UIRS, has drawn attention due to its capability to control wireless signals so as to improve the data rate. In this paper, we consider a multi-UIRS-assisted marine vehicle system where UIRSs are deployed to assist in the computation offloading of Unmanned Surface Vehicles (USVs). To improve energy efficiency, the optimization problem of the association relationships, computation resources of USVs, multi-UIRS phase shifts, and multi-UIRS trajectories is formulated. To solve the mixed-integer nonlinear programming problem, we decompose it into two layers and propose an integrated convex optimization and deep reinforcement learning algorithm to attain the near-optimal solution. Specifically, the inner layer solves the discrete variables by using the convex optimization based on Dinkelbach and relaxation methods, and the outer layer optimizes the continuous variables based on the Multi-Agent Twin Delayed Deep Deterministic Policy Gradient (MATD3). The numerical results demonstrate that the proposed algorithm can effectively improve the energy efficiency of the multi-UIRS-assisted marine vehicle system in comparison with the benchmarks. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1334.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
