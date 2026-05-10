---
id: paper-1095
title: 'FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network'
authors:
- Nagabushnam, Ganesan
- Choi, Yundo
- Kim, Kyong Hoon
venue: 2024 9th International Conference on Fog and Mobile Edge Computing, FMEC 2024
venue_type: conference
year: 2024
doi: 10.1109/FMEC62297.2024.10710250
url: https://www.scopus.com/pages/publications/85208137483?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 46--53
keywords:
- Aperiodic task
- Cloud Computing
- Deadline
- Fog computing
- Heterogeneous
- Multi-Agent Reinforcement Learning
- Proximal Policy Optimization
- Recurrent Neural Network
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

# paper-1095 — FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In heterogeneous fog-cloud computing networks, efficiently scheduling aperiodic tasks is an NP-hard problem, particularly when aiming to minimize makespan, adhere to deadlines, and conserve energy. This paper introduces a novel scheduling algorithm, Fog-Optimized Deadline-Adaptive Scheduling (FODAS), which combines Earliest Deadline First (EDF) principles with Deep Multi-Agent Reinforcement Learning, incorporating Proximal Policy Optimization (PPO) and Recurrent Neural Networks (RNN). FODAS is specifically designed to manage aperiodic tasks in heterogeneous fog-cloud environments, prioritizing deadline adherence and energy efficiency. The proposed algorithm begins by collecting tasks into a global scheduling queue, and sorting them by their deadlines. It incorporates three homogeneous schedulers within a heterogeneous framework, ensuring tasks meet their deadlines and achieve notable energy savings. Key performance metrics such as deadline meeting rate, makespan, and energy savings are evaluated, comparing FODAS against single-Agent reinforcement learning algorithms such as PPO and Asynchronous Advantage Actor-Critic (A3C). Our findings reveal that FODAS significantly improves the rate of meeting deadlines by up to 18% compared to the conventional algorithms. Additionally, it delivers substantial energy savings, with improvements of up to 80% in certain setups, and markedly decreases makespan, achieving reductions of up to 57.3% compared to traditional algorithms. The proposed algorithm also demonstrates exceptional operational efficiency, reducing the time required for scheduling tasks, particularly in high-density node networks. These results underscore the effectiveness of FODAS in managing complex task scheduling within fog-cloud computing environments. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1095.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
