---
id: paper-0216
title: Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning
authors:
- Li, Shilu
- Li, Baogang
- Zhao, Wei
venue: IEEE Access
venue_type: journal
year: 2020
doi: 10.1109/ACCESS.2020.3002895
url: https://www.scopus.com/pages/publications/85087627827?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 112762--112771
keywords:
- caching
- Mobile edge computing (MEC)
- multi-agent Deep-Q-network (MADQN)
- non-orthogonal multiple access (NOMA)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0216 — Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of emerging applications such as augmented reality, more and more computing tasks are sensitive to delay. Caching popular task computation results on the mobile edge computing (MEC) server is an effective solution to meet the latency requirements. When multiple users request the same task, if the computation result is cached on the MEC server, it will return the computation result directly to the user to reduce the delay for repeated computation. In this paper, we use the caching to assist the calculation. Non-orthogonal multiple access (NOMA) is used to further reduce the delay for computation offloading. The optimization problem is formulated as how to make caching and offloading decision to minimize the delay of whole system. In the case of unknown popularity, we use Gated Recurrent Unit (GRU) algorithm to predict the task popularity in time-varying system, and place the computing results of tasks with high popularity on the corresponding server. Based on the predicted popularity, a multi-agent Deep-Q-network (MADQN) algorithm is used to solve the caching and offloading problem. The simulation results show that the prediction error of GRU algorithm can be reduced by increasing the learning rate. Meanwhile, the proposed MADQN can effectively reduce the delay compared with other methods. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0216.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
