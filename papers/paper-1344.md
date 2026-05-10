---
id: paper-1344
title: Federated deep reinforcement learning for task offloading and resource allocation in mobile edge computing-assisted vehicular networks
authors:
- Zhao, Xu
- Wu, Yichuan
- Zhao, Tianhao
- Wang, Feiyu
- Li, Maozhen
venue: Journal of Network and Computer Applications
venue_type: journal
year: 2024
doi: 10.1016/j.jnca.2024.103941
url: https://www.scopus.com/pages/publications/85197082632?origin=resultslist
publisher: Academic Press
pages: ''
keywords:
- Deep reinforcement learning
- Federated learning
- Internet of vehicles
- Mobile edge computing
- Resource allocation
- Task offloading
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

# paper-1344 — Federated deep reinforcement learning for task offloading and resource allocation in mobile edge computing-assisted vehicular networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) enables computation intensive applications in the Internet of Vehicles (IoV) to no longer be limited by device resources. However, the lack of an effective task scheduling strategy will seriously affect users’ quality of experience (QoE). In this paper, a task type-based task offloading and resource allocation strategy is proposed to reduce delay and energy consumption during task execution. First, we establish communication, computing, and system cost models based on task offloading schemes, and model the joint optimization problem of task offloading and resource allocation as a Markov decision process. The utility function is obtained based on the task completion rate and the system cost. Second, an algorithm framework based on multi-agent deep deterministic policy gradient (MADDPG) is designed to solve the difficulty that traditional single-agent reinforcement learning algorithms are difficult to converge in a dynamic environment. In distributed scenarios, the proposed framework can also reduce system costs while handling more tasks. Finally, federated learning is introduced in the training process to reduce the impact of non-IID data while protecting privacy. Simulation results show that the proposed algorithm can effectively improve system processing efficiency and reduce device energy consumption compared to the popular reinforcement learning algorithms. © 2024 Elsevier Ltd

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1344.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
