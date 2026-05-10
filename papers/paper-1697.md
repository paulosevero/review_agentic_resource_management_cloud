---
id: paper-1697
title: Deep Multiagent Reinforcement Learning for Task Offloading and Resource Allocation in Satellite Edge Computing
authors:
- Jia, Min
- Zhang, Liang
- Wu, Jian
- Guo, Qing
- Zhang, Guowei
- Gu, Xuemai
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3482290
url: https://www.scopus.com/pages/publications/85207705452?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3832--3845
keywords:
- Deep reinforcement learning
- multiagent
- resource allocation
- satellite edge computing
- task offloading
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

# paper-1697 — Deep Multiagent Reinforcement Learning for Task Offloading and Resource Allocation in Satellite Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a supplement to terrestrial communication networks, satellite edge computing can break through geographical limitations and provide on-orbit computing services for people in some remote areas to achieve truly seamless global coverage. Considering time-varying channels, queue delays, and dynamic loads of edge computing satellites, we propose a multiagent task offloading and resource allocation (MATORA) algorithm with weighted latency as the optimization goal. It is a mixed integer nonlinear problem decoupled into task offloading and resource allocation subproblems. For the offloading subproblem, we propose a distributed multiagent deep reinforcement learning algorithm, and each agent generates its own offloading decision without knowing the prior knowledge of others. We show that the resource allocation problem is convex and can be solved using convex optimization methods. The experiment shows that the proposed algorithm can better adapt to the change of channel and the dynamic load of edge computing satellite, and it can effectively reduce task latency and task drop rate. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1697.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
