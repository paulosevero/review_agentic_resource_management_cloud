---
id: paper-0978
title: Snake swarm optimization-based deep reinforcement learning for resource allocation in edge computing environment
authors:
- Kaliraj, S.
- Sivakumar, V.
- Premkumar, N.
- Vatchala, S.
venue: 'Concurrency and Computation: Practice and Experience'
venue_type: journal
year: 2024
doi: 10.1002/cpe.8130
url: https://www.scopus.com/pages/publications/85192268687?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- internet of things
- mobile edge computing
- reinforcement learning
- resource allocation
- snake swarm optimization
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

# paper-0978 — Snake swarm optimization-based deep reinforcement learning for resource allocation in edge computing environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing has become popular in the past few years as a means of creating computing resources close to end-user nodes at the network edge. Nodes—end users—demand work offloading to improve service utilization. Furthermore, when the number of users in mobile edge computing increases, the minimal resources deployed at the edge become a problem. Develop the idea of reinforcement learning using a metaheuristic technique intended to achieve effective resource allocation and resolve offloading issues to handle this issue. The ideal way to manage the implementation of mobile edge computing with a cognitive agent's help is to request compensation for all client necessities. To complete the infrastructure type for the Internet of Things (IoT), the operator information is combined with its distinctive methodology. Neural caching during task execution is provided by reinforcement learning based on snake swarm optimization (SSO). Neural caching during task execution is provided by reinforcement learning based on SSO. In the process of creating the cost mapping table and incentive factor-based optimal resource allocation, this suggested method is applied to a contract with effective resource allocation among the end manipulators. Using performance metrics like delivery ratio, energy consumption, throughput, and delay, the suggested approach is put into practice and examined. It is also contrasted with traditional methods like Gray Wolf Optimization (GWO) ant colony optimization (ACO) and genetic algorithms (GA). © 2024 John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0978.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
