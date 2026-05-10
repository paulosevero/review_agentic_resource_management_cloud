---
id: paper-1772
title: 'A deep reinforcement learning-based task offloading algorithm for cell-free architecture CFMADRL: co-optimization of delay-energy-sensitive tasks'
authors:
- Li, Keke
- Wu, Xiaochun
- Liu, Jiali
- Lou, Yichao
- Qi, Mingjun
venue: Journal of Supercomputing
venue_type: journal
year: 2025
doi: 10.1007/s11227-025-08040-w
url: https://www.scopus.com/pages/publications/105021529276?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Cell-free architecture
- Deep reinforcement learning
- Delay-sensitive tasks
- Energy-sensitive tasks
- Task offloading
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1772 — A deep reinforcement learning-based task offloading algorithm for cell-free architecture CFMADRL: co-optimization of delay-energy-sensitive tasks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous proliferation of wireless devices, the growing pressure on wireless channels has resulted in degraded network quality for edge users and increased energy consumption of mobile devices. To enhance user experience and extend devices’ battery life, this paper proposes a multi-agent deep reinforcement learning-based task-offloading algorithm, referred to as cell-free multi-agent deep reinforcement learning (CFMADRL). Under a cell-free architecture, the proposed model introduces two representative task types, namely, delay-sensitive tasks and energy-sensitive tasks. The model also designs a multidimensional task classification mechanism that integrates task complexity, device status, and delay-energy pressure metrics. To effectively handle heterogeneous tasks, a dual-agent collaborative framework is constructed, where each agent is dedicated to a specific optimization objective: minimizing task completion delay or reducing energy consumption. Both objectives are achieved through global task offloading and resource scheduling. Furthermore, CFMADRL incorporates a user-driven access point (AP) cooperative offloading mechanism and a hierarchical optimization strategy. The system optimization problem is decomposed into two subproblems: computational resource allocation and task offloading/power control, which are addressed using convex optimization and multi-agent deep reinforcement learning, respectively. Simulation results demonstrate that the proposed algorithm significantly outperforms existing benchmark methods in terms of reducing system delay and energy consumption, and the method also shows strong robustness and adaptability in dynamic edge computing environments. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1772.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
