---
id: paper-0356
title: An intelligent offloading system based on multiagent reinforcement learning
authors:
- Weng, Yu
- Chu, Haozhen
- Shi, Zhaoyi
venue: Security and Communication Networks
venue_type: journal
year: 2021
doi: 10.1155/2021/8830879
url: https://www.scopus.com/pages/publications/85104442979?origin=resultslist
publisher: Hindawi Limited
pages: ''
keywords:
- Edge computing
- Intelligent vehicle highway systems
- Learning systems
- Multi agent systems
- Quality of service
- Scheduling
- User experience
- Vehicles
- Autonomous exploration
- Complex services
- Computing resource
- Mobile core network
- Multi-agent reinforcement learning
- Offloading system
- Quality of experience (QoE)
- Resource requirements
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0356 — An intelligent offloading system based on multiagent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent vehicles have provided a variety of services; there is still a great challenge to execute some computing-intensive applications. Edge computing can provide plenty of computing resources for intelligent vehicles, because it offloads complex services from the base station (BS) to the edge computing nodes. Before the selection of the computing node for services, it is necessary to clarify the resource requirement of vehicles, the user mobility, and the situation of the mobile core network; they will affect the users' quality of experience (QoE). To maximize the QoE, we use multiagent reinforcement learning to build an intelligent offloading system; we divide this goal into two suboptimization problems; they include global node scheduling and independent exploration of agents. We apply the improved Kuhn-Munkres (KM) algorithm to node scheduling and make full use of existing edge computing nodes; meanwhile, we guide intelligent vehicles to the potential areas of idle computing nodes; it can encourage their autonomous exploration. Finally, we make some performance evaluations to illustrate the effectiveness of our constructed system on the simulated dataset. Copyright © 2021 Yu Weng et al. This is an open access article distributed under the Creative Commons Attribution License

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0356.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
