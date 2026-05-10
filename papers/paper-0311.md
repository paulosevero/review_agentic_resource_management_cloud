---
id: paper-0311
title: 'Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach'
authors:
- Lorido-Botran, Tania
- Bhatti, Muhammad Khurram
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2021
doi: 10.1007/978-3-030-75078-7_57
url: https://www.scopus.com/pages/publications/85106414131?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 572--581
keywords:
- Cloud computing
- Container scheduling
- Deep reinforcement learning
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

# paper-0311 — Adaptive Container Scheduling in Cloud Data Centers: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud data centers rely on virtualization to run a diverse set of applications. Container technology allows for a more lightweight execution, in comparison with popular Virtual Machines. Efficient scheduling of containers is still challenging due to varying request arrival patterns, application-specific resource consumption and resource heterogeneity in physical servers. Besides, containers are also more prone to resource contention and performance interference. Cloud providers need to overcome these challenges with a goal in mind: maximize resource utilization to satisfy as many requests as possible. This paper introduces RLSched, a deep reinforcement learning-based (DRL) scheduler that is self-adaptive and automatically captures the resource usage dynamics in the data center. The scheduler is based on a decentralized actor-critic multi-agent architecture that enables for parallel execution and faster convergence. RLSched relies on an enhanced network model with action shaping, which filters invalid actions and prevents the agent to fall into a sub-optimal policy. The proposed scheduler is compared against other state-of-the-art DRL methods on a simulated data center environment based on real traces from Microsoft Azure. The results show faster convergence and higher number of containers placed per session. © 2021, The Author(s), under exclusive license to Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0311.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
