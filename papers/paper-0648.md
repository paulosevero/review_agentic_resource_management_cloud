---
id: paper-0648
title: 'Joint Trajectory Planning, Application Placement, and Energy Renewal for UAV-Assisted MEC: A Triple-Learner-Based Approach'
authors:
- Li, Jialiuyuan
- Yi, Changyan
- Chen, Jiayuan
- Zhu, Kun
- Cai, Jun
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3262687
url: https://www.scopus.com/pages/publications/85151550104?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13622--13636
keywords:
- Long-term optimization
- mobile-edge computing (MEC)
- reinforcement learning
- stochastic game
- unmanned aerial vehicle (UAV)
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

# paper-0648 — Joint Trajectory Planning, Application Placement, and Energy Renewal for UAV-Assisted MEC: A Triple-Learner-Based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this article, an energy-efficient scheduling problem for multiple unmanned aerial vehicle (UAV)-assisted mobile-edge computing (MEC) is studied. In the considered model, UAVs act as mobile edge servers to provide computing services to end-users with task offloading requests. Unlike existing works, we allow UAVs to determine not only their trajectories but also the decisions of whether returning to the depot for replenishing energies and updating application placements (due to their limited batteries and storage capacities). With the aim of maximizing the long-term energy efficiency of all UAVs, i.e., the total amount of offloaded tasks computed by all UAVs over their total energy consumption, a joint optimization of UAVs' trajectory planning, energy renewal, and application placement is formulated. Taking into account the underlying cooperation and competition among intelligent UAVs, we reformulate such optimization problem as three coupled multiagent stochastic games. Since the prior environment information is unavailable to UAVs, we propose a novel triple-learner-based reinforcement learning (TLRL) approach, integrating a trajectory learner, an energy learner, and an application learner, for reaching equilibriums. Moreover, we analyze the convergence and the complexity of the proposed solution. Simulations are conducted to evaluate the performance of the proposed TLRL approach, and demonstrate its superiority over counterparts.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0648.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
