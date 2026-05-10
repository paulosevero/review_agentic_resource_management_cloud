---
id: paper-1304
title: Joint Energy and AoI Optimization in UAV-Assisted MEC-WET Systems
authors:
- Yang, Yulu
- Song, Tiecheng
- Yang, Jingce
- Xu, Han
- Xing, Song
venue: IEEE Sensors Journal
venue_type: journal
year: 2024
doi: 10.1109/JSEN.2024.3378844
url: https://www.scopus.com/pages/publications/85189513460?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15110--15124
keywords:
- Age of information (AoI)
- mobile edge computing (MEC)
- multiagent deep reinforcement learning
- unmanned aerial vehicle (UAV)
- wireless energy transfer (WET)
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

# paper-1304 — Joint Energy and AoI Optimization in UAV-Assisted MEC-WET Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this article, we propose an unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) and wireless energy transfer (WET) network in disaster scenarios, where both the data-processing UAVs (DP-UAVs) and the energy-transferring UAVs (ET-UAVs) are deployed. To ensure the freshness of data, the age of information (AoI) is utilized on both user equipment (UE) and the data center (DC). An optimization problem is formulated to minimize the AoI and the energy consumption of the UAVs by jointly optimizing the UAVs' trajectories and offloading strategies. To find the optimal solution, the problem is decomposed into two optimization subproblems: the trajectory planning and offloading policy design. Then, the modified multiagent deep deterministic policy gradient (M2DDPG) algorithm and the traversal-based greedy (TG) algorithm are proposed to solve the two subproblems, respectively, where the cooperation of the UAVs and the greedy-choice property of the problem are fully utilized. Simulation results validate the effectiveness of the proposed M2DDPG-TG algorithm and demonstrate that it performs better than the baseline algorithms and the traditional MADDPG algorithm. The scalability of the proposed algorithms is also verified by extensive simulations.  © 2001-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1304.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
