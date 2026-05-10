---
id: paper-0264
title: Task scheduling, resource provisioning, and load balancing on scientific workflows using parallel SARSA reinforcement learning agents and genetic algorithm
authors:
- Asghari, Ali
- Sohrabi, Mohammad Karim
- Yaghmaee, Farzin
venue: Journal of Supercomputing
venue_type: journal
year: 2021
doi: 10.1007/s11227-020-03364-1
url: https://www.scopus.com/pages/publications/85087562957?origin=resultslist
publisher: Springer
pages: 2800--2828
keywords:
- Cloud computing
- Genetic algorithm
- Load balancing
- Reinforcement learning
- Resource management
- Task scheduling
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

# paper-0264 — Task scheduling, resource provisioning, and load balancing on scientific workflows using parallel SARSA reinforcement learning agents and genetic algorithm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is one of the most popular distributed environments, in which, multiple powerful and heterogeneous resources are used by different user applications. Task scheduling and resource provisioning are two important challenges of cloud environment, called cloud resource management. Resource management is a major problem especially for scientific workflows due to their heavy calculations and dependency between their operations. Several algorithms and methods have been developed to manage cloud resources. In this paper, the combination of state-action-reward-state-action learning and genetic algorithm is used to manage cloud resources. At the first step, the intelligent agents schedule the tasks during the learning process by exploring the workflow. Then, in the resource provisioning step, each resource is assigned to an agent, and its utilization is attempted to be maximized in the learning process of its corresponding agent. This is conducted by selecting the most appropriate set of the tasks that maximizes the utilization of the resource. Genetic algorithm is utilized for convergence of the agents of the proposed method, and to achieve global optimization. The fitness function that has been exploited by this genetic algorithm seeks to achieve more efficient resource utilization and better load balancing by observing the deadlines of the tasks. The experimental results show that the proposed algorithm reduces makespan, enhances resource utilization, and improves load balancing, compared to MOHEFT and MCP, the well-known workflow scheduling algorithms of the literature. © 2020, Springer Science+Business Media, LLC, part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0264.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
