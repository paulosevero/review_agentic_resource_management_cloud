---
id: paper-1337
title: Optimization of Edge-Cloud Collaborative Computing Resource Management for Internet of Vehicles Based on Multiagent Deep Reinforcement Learning
authors:
- Zhang, Tianrong
- Wu, Fan
- Chen, Zeyu
- Chen, Senyang
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3439603
url: https://www.scopus.com/pages/publications/105002090152?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 36114--36126
keywords:
- Augmented Intelligence of Things (AIoT)
- deep reinforcement learning
- edge computing
- edge-cloud collaboration
- Internet of Vehicles (IoV)
- multiagent
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

# paper-1337 — Optimization of Edge-Cloud Collaborative Computing Resource Management for Internet of Vehicles Based on Multiagent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the current Augmented Intelligence of Things (AIoT) vehicular road collaborative edge offloading application scenario, considering the limited computing resources of edge servers and the unpredictability of vehicle user offloading requests, this article fully utilizes the computing resources in the Internet of Vehicles (IoV). During the offloading task execution phase, the caching system is applied to the task execution process to solve the problem of resource waste caused by redundant computing. At the same time, in order to alleviate the problem of low cache hit rate of task calculation results, the task is decomposed into several sub tasks, including vehicle self-execution, edge offloading, cloud offloading, etc. Considering the high dependency between tasks and application services in edge offloading scenarios, as well as the limited storage space of edge servers, this article adopts a cluster edge server application layout strategy. Through the cooperation of various nodes, the offloading services are provided to vehicles as a whole, giving the cluster the ability to handle various tasks. On this basis, in order to reduce the additional system costs caused by task and application misalignment within the cluster, a multiagent deep reinforcement learning algorithm (MADRL) for edge-cloud collaboration is further proposed to obtain the corresponding placement relationship between in vehicle applications and edge servers, and optimize in vehicle computing resources. The simulation results show that the algorithm proposed in this article can improve the success rate of edge offloading, effectively reduce task offloading latency, and improve system resource utilization. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1337.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
