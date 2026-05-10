---
id: paper-0439
title: Stable Resource Allocation Based on Multi-agent Reinforcement Learning for Edge Computing
authors:
- Jiang, Song
- Zhang, Xuejie
venue: Proceedings - 2022 2nd International Conference on Frontiers of Electronics, Information and Computation Technologies, ICFEICT 2022
venue_type: conference
year: 2022
doi: 10.1109/ICFEICT57213.2022.00083
url: https://www.scopus.com/pages/publications/85143803396?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 432--438
keywords:
- computation offloading
- edge computing
- Lyapunov optimization
- multi-agent deep reinforcement learning
- resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0439 — Stable Resource Allocation Based on Multi-agent Reinforcement Learning for Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the needs of distributed decision making and maintaining long-term system stability in edge computing resource allocation, we propose a distributed resource allocation framework DLMAO, and multi-agent deep reinforcement learning-based allocation algorithms QSLSQP and IDSAC deployed for cooperative and non-cooperative scenarios, respectively. Considering the stochastic nature of the environment and the mobility of terminals, the resource allocation problem is modeled as a mixed-integer nonlinear programming (MINLP) problem on sequential time series. The DLMAO framework is based on Lyapunov optimization, which decouples the programming into multiple independent MINLPs and ensures the system's long-term stability, and then QSLSQP and IDSAC are used to solve binary offloading and resource allocation problems in the hybrid action space to maximize the system's weighted data processing rate with limited resource constraints. Both algorithms allow every agent to make autonomous decisions. Experimental results demonstrate that the QSLSQP algorithm, which utilizes global information in a cooperative scenario, has the best performance, and the fully autonomous IDSAC algorithm outperforms the single-agent global optimization approach. The extremely short decision latency of both algorithms makes them appropriate to be applied in edge computing environments. © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0439.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
