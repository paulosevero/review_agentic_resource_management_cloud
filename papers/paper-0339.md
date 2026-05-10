---
id: paper-0339
title: 'Energy Efficient Edge Computing: When Lyapunov Meets Distributed Reinforcement Learning'
authors:
- Sana, Mohamed
- Merluzzi, Mattia
- Pietro, Nicola Di
- Calvanese Strinati, Emilio
venue: 2021 IEEE International Conference on Communications Workshops, ICC Workshops 2021 - Proceedings
venue_type: conference
year: 2021
doi: 10.1109/ICCWorkshops50388.2021.9473797
url: https://www.scopus.com/pages/publications/85112854389?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge computing
- Energy efficiency
- Energy utilization
- Green computing
- Heuristic methods
- Iterative methods
- Low power electronics
- Multi agent systems
- NP-hard
- Optimization
- Resource allocation
- Computing resource
- Distributed reinforcement learning
- Formulated problems
- Inter and intra-cell interference
- Iterative algorithm
- Multi-agent reinforcement learning
- Radio resource allocation
- Stochastic optimizations
- Reinforcement learning
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
    my_justification: RL
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

# paper-0339 — Energy Efficient Edge Computing: When Lyapunov Meets Distributed Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this work, we study the problem of energy-efficient computation offloading enabled by edge computing. In the considered scenario, multiple users simultaneously compete for limited radio and edge computing resources to get offloaded tasks processed under a delay constraint, with the possibility of exploiting low power sleep modes at all network nodes. The radio resource allocation takes into account inter- and intra-cell interference, and the duty cycles of the radio and computing equipment have to be jointly optimized to minimize the overall energy consumption. To address this issue, we formulate the underlying problem as a dynamic long-term optimization. Then, based on Lyapunov stochastic optimization tools, we decouple the formulated problem into a CPU scheduling problem and a radio resource allocation problem to be solved in a per-slot basis. Whereas the first one can be optimally and efficiently solved using a fast iterative algorithm, the second one is solved using distributed multi-agent reinforcement learning due to its non-convexity and NP-hardness. The resulting framework achieves up to 96.5% performance of the optimal strategy based on exhaustive search, while drastically reducing complexity. The proposed solution also allows to increase the network's energy efficiency compared to a benchmark heuristic approach. © 2021 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0339.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
