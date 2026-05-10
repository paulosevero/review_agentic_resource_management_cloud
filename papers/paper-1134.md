---
id: paper-1134
title: DRL-Based Computation-Efficient Offloading and Power Control for UAV-Assisted MEC Networks
authors:
- Priya, B.
- Nandhini, J.M.
- Uma, S.
- Anuratha, K.
venue: Transactions on Emerging Telecommunications Technologies
venue_type: journal
year: 2024
doi: 10.1002/ett.70027
url: https://www.scopus.com/pages/publications/85210086273?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- MADPM algorithm
- MEC
- optimization
- UAV
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

# paper-1134 — DRL-Based Computation-Efficient Offloading and Power Control for UAV-Assisted MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) has achieved significant attention due to the availability of computational tasks in specific scenarios such as emergency applications like forest fire and earthquake remedies. The computationally demanding policy and user offloading policy are challenging problems to address in the energy constrained unmanned aerial vehicle (UAV) network. In this work, the computational task offloading, and power management is solved by using the multi-agent deterministic power management algorithm (MADPM) based on deep reinforcement learning. Every UAV works together as a team to understand the actor critic environment and to make decisions that will help achieve the goals. This involves transferring computational tasks from UAVs to more powerful ground stations or other UAVs to save energy and enhance performance. It requires intelligent decision-making to determine which tasks to offload and when. The joint optimization problem is verified with the simulation results and the proposed work is enabled with MEC in achieving the emergence of UAV related applications. Our simulations show that the MADPM algorithm, as suggested, enhances task offloading efficiency by 35% and reduces power consumption by 25% when compared with current methods. These findings underscore the ability of our method to greatly improve the UAV operational capacities. © 2024 John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1134.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
