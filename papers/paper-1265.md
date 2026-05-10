---
id: paper-1265
title: 'Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach'
authors:
- Wang, Yupeng
- He, Jinbo
- Shi, Haiyong
- Han, Weizhen
- Liu, Bingyi
venue: 2024 International Conference on Information and Communication Technologies for Disaster Management, ICT-DM 2024
venue_type: conference
year: 2024
doi: 10.1109/ICT-DM62768.2024.10798952
url: https://www.scopus.com/pages/publications/85216536499?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 5G
- constrained reinforcement learning
- Disaster management
- multi-access edge computing
- task offloading
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1265 — Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the boom in fifth-generation (5G) communication technology, task offloading using multi-access edge computing (MEC) technologies has become an effective approach to satisfy the computation demand of various types of users. Nevertheless, most of the existing task offloading schemes overlook the unavailability of computational resources in disaster areas, failing to guarantee the quality of service (QoS) requirements of task computation in such scenarios. Therefore, this paper treats each edge node as an agent and designs a cooperative multi-agent constrained reinforcement learning (CMACRL) framework for learning the adaptive task offloading policy for each agent, ensuring the performance of emergency services and enhancing the utilization of available computational resources in disaster areas. Specifically, to satisfy the QoS requirements of applications, we formulate the constraints of applications' performance requirements and then adopt the reward constrained policy optimization algorithm to meet the target constraints. Moreover, to mitigate the resource imbalance between disaster and safe areas, we leverage the heterogeneous-agent proximal policy optimization algorithm to generate cooperative resource use strategies for edge nodes. To evaluate the performance of CMACRL, we develop a simulator based on a real-world urban scenario. Extensive experiments are conducted, and experimental results demonstrate that CMACRL significantly improves the task offloading success rate by up to 22.49% and reduces the average service latency by up to 22.69% compared to all the baselines.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1265.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
