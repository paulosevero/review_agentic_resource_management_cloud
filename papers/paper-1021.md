---
id: paper-1021
title: Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing
authors:
- Li, Mingchu
- Li, Shuai
- Qi, Wanying
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2024
doi: 10.1007/978-3-031-54521-4_23
url: https://www.scopus.com/pages/publications/85187709342?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 421--439
keywords:
- Dynamic trade-off
- Edge computing
- Meta deep reinforcement learning
- Smart homes
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

# paper-1021 — Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the edge computing enabled smart home scenario. Various smart home devices generate a large number of computing tasks, and users can offload these tasks to servers or perform them locally. Offloading to the server will result in lower delay, but it will also require paying the corresponding offloading cost. Therefore, users need to consider the low delay and additional costs caused by offloading. Different users have different trade-offs between latency and offload costs at different times. If the trade-off is set as a fixed hyperparameter, it will give users a poor experience. In the case of dynamic trade-offs, the model may have difficulty adapting to arrive at an optimal offloading decision. By jointly optimizing the task delay and offloading cost, We model it as a long-term cost minimization problem under dynamic trade-off (DT-LCMP). To solve the problem, we propose an offloading algorithm based on multi-agent meta deep reinforcement learning and load prediction (MAMRL-L). Combined with the idea of meta-learning, the DDQN method is used to train the network. By training the sampling data in different environments, the agent can adapt to the dynamic environment quickly. In order to improve the performance of the model, LSTNet is used to predict the load level of the next slot server in real time. The simulation results show that our algorithm has higher performance than the existing algorithms and benchmark algorithms. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1021.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
