---
id: paper-0868
title: Two-Timescale Joint Optimization of Task Scheduling and Resource Scaling in Multi-Data Center System Based on Multi-Agent Deep Reinforcement Learning
authors:
- Chen, Shuangwu
- Li, Jiangming
- Yuan, Qifeng
- He, Huasen
- Li, Sen
- Yang, Jian
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2024
doi: 10.1109/TPDS.2024.3467212
url: https://www.scopus.com/pages/publications/85205428454?origin=resultslist
publisher: IEEE Computer Society
pages: 2331--2346
keywords:
- deep reinforcement learning
- graph convolution network
- Multi-data center system
- resource scaling
- task scheduling
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

# paper-0868 — Two-Timescale Joint Optimization of Task Scheduling and Resource Scaling in Multi-Data Center System Based on Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —As a new computing paradigm, multi-data center computing enables service providers to deploy their applications close to the users. However, due to the spatio-temporal changes in workloads, it is challenging to coordinate multiple distributed data centers to provide high-quality services while reducing service operation costs. To address this challenge, this article studies the joint optimization problem of task scheduling and resource scaling in multi-data center systems. Since the task scheduling and the resource scaling are usually performed in different timescales, we decompose the joint optimization problem into two sub-problems and propose a two-timescale optimization framework. The short-timescale task scheduling can promptly relieve the bursty arrivals of computing tasks, and the long-timescale resource scaling can adapt well to the long-term changes in workloads. To address the distributed optimization problem, we propose a two-timescale multi-agent deep reinforcement learning algorithm. In order to characterize the graph-structured states of connected data centers, we develop a directed graph convolutional network based global state representation model. The evaluation indicates that the proposed algorithm is able to reduce both the task makespan and the task timeout while maintaining a reasonable cost. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0868.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
