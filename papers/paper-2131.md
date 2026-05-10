---
id: paper-2131
title: A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings
authors:
- Shi, Shanrui
- Miyata, Shohei
- Akashi, Yasunori
venue: Energy and Buildings
venue_type: journal
year: 2025
doi: 10.1016/j.enbuild.2025.116089
url: https://www.scopus.com/pages/publications/105009829755?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Distributed optimal control
- Energy efficiency
- Indoor environmental quality
- Multi-agent system
- Multizone VAV system
- Nash optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2131 — A hybrid multi-agent distributed optimal control strategy of multizone VAV systems for edge computing in smart buildings

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-agent-based distributed optimal control can effectively balance indoor environmental quality and energy consumption in multizone variable air volume (VAV) systems, while reducing computational load and enhancing scalability. However, existing methods often optimize airflow setpoints without fully addressing the coupled dynamics in multizone VAV systems and frequently rely on simplified models. To overcome these limitations, this study proposes a hybrid multiagent distributed control strategy that directly optimizes actuators by jointly considering indoor air temperature, CO<sub>2</sub> concentration, and energy use. The strategy decomposes the optimization problem into subproblems assigned to zone-level and system-level agents. Each zone agent employs a metaheuristic-based framework for damper control, coordinated through a Nash equilibrium-based scheme. Meanwhile, a model-free system agent dynamically adjusts the supply fan and the outdoor air damper. Two test cases with different occupancy patterns are evaluated in a virtual testbed. Results show that under normal occupancy conditions, the distributed strategy performs comparably to the centralized controller, whereas under unbalanced occupant distributions, it outperforms the centralized approach in both indoor climate management and energy efficiency. In both cases, the average computational load is reduced by more than 80 % relative to the centralized method. Additionally, the proposed strategy offers a tunable trade-off between computational complexity and control performance, making it suitable for resource-constrained edge devices. By leveraging advancing edge-computing capabilities, this hybrid multiagent approach provides an effective and decentralized solution for multizone VAV control in smart building systems. © 2025 The Author(s)

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2131.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
