---
id: paper-1773
title: A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing
authors:
- Li, Jialiuyuan
- Shi, You
- Dai, Chen
- Yi, Changyan
- Yang, Yuxiao
- Zhai, Xiangping
- Zhu, Kun
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3540964
url: https://www.scopus.com/pages/publications/85218714770?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9717--9733
keywords:
- energy efficiency
- game
- reinforcement learning
- space–air–ground integrated networks
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1773 — A Learning-Based Stochastic Game for Energy Efficient Optimization of UAV Trajectory and Task Offloading in Space/Aerial Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we study the energy-efficient unmanned aerial vehicle (UAV) and low earth orbital (LEO) satellite assisted mobile edge computing (MEC) in space–air–ground integrated networks (SAGINs). The key challenge involves how to efficiently execute tasks offloaded from IoT devices, given limited on-board computation capabilities of UAVs and delay constraints of tasks. To address it, UAVs are first allowed to adjust their trajectories to accommodate as many tasks as possible from IoT devices. Subsequently, UAVs compute a portion of these tasks while delegating the rest to LEO satellites for further execution. Accordingly, we formulate a joint optimization problem including UAV trajectory planning, task offloading, and bandwidth allocations, aiming to maximize the long-term energy efficiency of UAVs and LEO satellites (i.e., the total data size in computation offloading divided by energy consumption of UAVs and LEO satellites). Considering the interactions among intelligent UAVs, this problem is reformulated as a set of interconnected multi-agent stochastic games, and the existence of corresponding Nash Equilibrium (NE) is theoretically proved. To obtain the NE, a multi-agent reinforcement learning-based algorithm, namely UTPTR, is developed concerning system dynamics and uncertainties. Simulations evaluate the performance of the UTPTR and demonstrate its superiority compared to existing approaches. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1773.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
