---
id: paper-0438
title: 'Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration'
authors:
- Jiang, Feibo
- Dong, Li
- Wang, Kezhi
- Yang, Kun
- Pan, Cunhua
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2021.3113872
url: https://www.scopus.com/pages/publications/85115674476?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6597--6610
keywords:
- Distributed deep reinforcement learning (DRL)
- Imitation learning
- Levy flight
- Multiagent reinforcement learning
- Resource scheduling
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

# paper-0438 — Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In large-scale mobile edge computing (MEC) systems, the task latency, and energy consumption are important for massive resource-consuming and delay-sensitive Internet of Things Devices (IoTDs). Against this background, we propose a distributed intelligent resource scheduling (DIRS) framework to minimize the sum of task latency and energy consumption for all IoTDs, which can be formulated as a mixed-integer nonlinear programming. The DIRS framework includes centralized training relying on the global information and distributed decision making by each agent deployed in each MEC server. Specifically, we first introduce a novel multiagent ensemble-assisted distributed deep reinforcement learning (DRL) architecture, which can simplify the overall neural network structure of each agent by partitioning the state space and also improve the performance of a single agent by combining decisions of all the agents. Second, we apply action refinement to enhance the exploration ability of the proposed DIRS framework, where the near-optimal state-action pairs are obtained by a novel Levy flight search. Finally, an imitation acceleration scheme is presented to pretrain all the agents, which can significantly accelerate the learning process of the proposed framework through learning the professional experience from a small amount of demonstration data. The simulation results in three typical scenarios demonstrate that the proposed DIRS framework is efficient and outperforms the existing benchmark schemes.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0438.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
