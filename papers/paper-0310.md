---
id: paper-0310
title: A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments
authors:
- Long, Saiqin
- Long, Weifan
- Li, Zhetao
- Li, Kenli
- Xia, Yuanqing
- Tang, Zhuo
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2021
doi: 10.1109/TPDS.2020.3041029
url: https://www.scopus.com/pages/publications/85097394725?origin=resultslist
publisher: IEEE Computer Society
pages: 1629--1640
keywords:
- Data centers
- game theory
- mutliple agent system
- QoS constraint
- queueing system
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Game theory
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

# paper-0310 — A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of the Internet of Things, the data that needs to be processed is increasing rapidly. Therefore, the collaboration of cloud and edge emerges as the times require. Edge nodes are mainly responsible for collecting data, and decide to process the data locally or offload to cloud data centers. Cloud data centers are suitable for data analysis, model training, and managing edge nodes. In this article, we focus on the task assignment problems in collaborative edge and cloud environments and study it in a distributed, non-cooperative environment. An M/M/1 queueing model is established to characterize the task transmission. Because of the multi-core processors, we set an M/M/C queueing model to characterize the task computation. We consider the problem from the perspective of game theory and formulate it into a non-cooperative game among multi-agents (multiple edge data centers) in which each agent is informed with incomplete information (allocation strategies) of others. For each agent, we define a function of the expected cost of tasks as the disutility function, and minimize it subject to the QoS constraint. We analyze the existence of Nash equilibrium and develop a Greedy Energy-aware Algorithm (GEA) to choose active servers using the Limit Searching Algorithm (LSA) to find the ceiling utilization. Then we propose the Best Response Algorithm (BRA) to optimize the utility function. The convergence of the BRA algorithm has been discussed. Finally, the results demonstrate that the BRA algorithm can get a solution close to Nash equilibrium and reach it quickly. © 1990-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Game theory"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0310.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
