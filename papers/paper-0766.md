---
id: paper-0766
title: 'Joint task offloading and resource optimization in NOMA-based vehicular edge computing: A game-theoretic DRL approach'
authors:
- Xu, Xincao
- Liu, Kai
- Dai, Penglin
- Jin, Feiyu
- Ren, Hualing
- Zhan, Choujun
- Guo, Songtao
venue: Journal of Systems Architecture
venue_type: journal
year: 2023
doi: 10.1016/j.sysarc.2022.102780
url: https://www.scopus.com/pages/publications/85142173953?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Exact potential game
- Heterogeneous resource allocation
- Real-time task offloading
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

# paper-0766 — Joint task offloading and resource optimization in NOMA-based vehicular edge computing: A game-theoretic DRL approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) becomes a promising paradigm for the development of emerging intelligent transportation systems. Nevertheless, the limited resources and massive transmission demands bring great challenges on implementing vehicular applications with stringent deadline requirements. This work presents a non-orthogonal multiple access (NOMA) based architecture in VEC, where heterogeneous edge nodes are cooperated for real-time task processing. We derive a vehicle-to-infrastructure (V2I) transmission model by considering both intra-edge and inter-edge interferences and formulate a cooperative resource optimization (CRO) problem by jointly optimizing the task offloading and resource allocation, aiming at maximizing the service ratio. Further, we decompose the CRO into two subproblems, namely, task offloading and resource allocation. In particular, the task offloading subproblem is modeled as an exact potential game (EPG), and a multi-agent distributed distributional deep deterministic policy gradient (MAD4PG) is proposed to achieve the Nash equilibrium. The resource allocation subproblem is divided into two independent convex optimization problems, and an optimal solution is proposed by using a gradient-based iterative method and KKT condition. Finally, we build the simulation model based on real-world vehicular trajectories and give a comprehensive performance evaluation, which conclusively demonstrates the superiority of the proposed solutions. © 2022 Elsevier B.V.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0766.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
