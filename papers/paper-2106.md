---
id: paper-2106
title: Efficient Multi-Agent Optimized Reinforcement Learning Algorithm-Based Task Scheduling in Fog-Cloud Environment
authors:
- Sarumathi, S.
- Vijayalakshmi, K.
venue: IETE Journal of Research
venue_type: journal
year: 2025
doi: 10.1080/03772063.2025.2567597
url: https://www.scopus.com/pages/publications/105019233753?origin=resultslist
publisher: Taylor and Francis Ltd.
pages: ''
keywords:
- Fog-cloud computing
- IoT devices
- optimised reinforcement learning algorithm
- Q-learning, and enhanced pufferfish optimisation algorithm
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

# paper-2106 — Efficient Multi-Agent Optimized Reinforcement Learning Algorithm-Based Task Scheduling in Fog-Cloud Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog-cloud computing is crucial for Critical activities that can be integrated into smart (IoT) support by combining controlled resource heterogeneity cloud and mobile edge resources to optimise task scheduling. However, task scheduling in fog-cloud environments creates major obstacles, stochastic behaviour, network hierarchies, resource heterogeneity-controlled, device mobility and resource capabilities. Also, these challenges include optimising multiple conflicting objectives, such as minimising energy consumption, computational costs, makespan, and latency while ensuring dependability and scalability. Traditional task scheduling approaches often fail to address the dynamic nature of fog-cloud environments, leading to inefficiencies in resource utilisation and reduced system performance. Therefore, this paper proposes an efficient task-scheduling approach for fog-cloud environments. Initially, an IoT sensor collects user tasks and is given to the fog-cloud environment for scheduling. The task scheduler gathers data collected by the task manager and the resource manager about task and resource information. During the scheduling process, the tasks are scheduled to the resources using the Optimized Reinforcement Learning (ORL) algorithm, which combines the Q-learning and Enhanced Pufferfish optimisation (EPuO) algorithm. The EPuO algorithm improves Q-learning decision-making capabilities by selecting the best action sequences of Q-learning. To attain the best action state, the proposed EPuO algorithm considers two parameters as an objective function, namely, delay and energy consumption. The proposed ORL algorithm retains the Q-value associated with the state's appropriate action, hence saving storage space. Python is utilised to implement a proposed method. The effectiveness of the proposed approach is assessed using various metrics and compared with other approaches. © 2025 IETE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2106.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
