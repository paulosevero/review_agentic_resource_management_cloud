---
id: paper-0400
title: Multi-agent Reinforcement Learning for Task Allocation in Cooperative Edge Cloud Computing
authors:
- Ding, Shiyao
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2022
doi: 10.1007/978-3-031-14135-5_24
url: https://www.scopus.com/pages/publications/85137051634?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 283--297
keywords:
- Edge cloud computing
- Internet of Things (IoT)
- Multiagent systems
- Reinforcement learning
- Task allocation
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

# paper-0400 — Multi-agent Reinforcement Learning for Task Allocation in Cooperative Edge Cloud Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge cloud computing has become a fundamental computation infrastructure supporting the resource-limited devices of Internet of Things (IoT). An important problem in edge cloud computing is how to allocate tasks to the servers while minimizing various costs and satisfying task requirements. Studies to date usually assume a self-interested setting where each edge/cloud server is owned by one user who tries to maximize own interests. However, with the strong development of smart communities like smart factory, the servers are usually owned by an organization like an IT corporation. This triggers the necessity for edge/cloud server cooperation to maximize team interests. Thus, in this paper, we consider a new problem called cooperative edge cloud computing where edge/cloud servers cooperate with each other to perform tasks to optimize the interests of the whole system. This problem is difficult due to some features such as 1) the tasks usually have high workloads which cannot be well performed by only one server; 2) the tasks usually have a dependency relationship; 3) edge servers are usually distributed where each server only has a partial observation. Our idea is to formulate the problem as a multiagent system, where each server is regarded as an agent who can learn to execute decision-making for task allocation based on its observation (e.g., current server status and arriving task). Then, we employee multiagent reinforcement learning methods to make agents learn from the environment by themselves without previously designed rules. Our expected impact is that our algorithm can offer significantly better attributes such as low latency and low energy consumption in the cooperative edge cloud computing. © 2022, Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0400.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
