---
id: paper-0803
title: Time and Energy-Sensitive End-Edge-Cloud Resource Provisioning Optimization Method for Collaborative Vehicle-Road Systems; [时间和能量敏感的端—边—云车路协同系统资源调度优化方法]
authors:
- Zheng, Yingying
- Zhou, Junlong
- Shen, Yufan
- Cong, Peijin
- Wu, Zebin
venue: Jisuanji Yanjiu yu Fazhan/Computer Research and Development
venue_type: journal
year: 2023
doi: 10.7544/issn1000-1239.202220734
url: https://www.scopus.com/pages/publications/85169593169?origin=resultslist
publisher: Science Press
pages: 1037--1052
keywords:
- collaborative vehicle-road systems
- end-edge-cloud
- offloading
- reinforcement learning
- scheduling
language: Chinese
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

# paper-0803 — Time and Energy-Sensitive End-Edge-Cloud Resource Provisioning Optimization Method for Collaborative Vehicle-Road Systems; [时间和能量敏感的端—边—云车路协同系统资源调度优化方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous development of information technology, intelligent transportation system has gradually become the trend of future transportation. However, the increasing number of time-sensitive and computation-intensive applications in intelligent transportation systems has brought severe challenges to resource-limited vehicles. The end-edge-cloud hierarchical computing architecture is an effective means to cope with this challenge. In the collaborative end-edge-cloud vehicle-road system, vehicle users can offload time-sensitive tasks to nearby roadside units to ensure the timing requirement and offload computation-intensive tasks to the cloud to meet their needs of computing power. However, task offloading also leads to additional transmission latency and energy overhead. In addition, tasks may also suffer from errors during transmission, resulting in degraded reliability. Therefore, to ensure the user experience of vehicles in the collaborative end-edge-cloud vehicle-road system, a multi-agent reinforcement learning based resource scheduling scheme is proposed. The scheme makes full use of the end-edge-cloud architecture’s characteristics and adopts the centralized training-decentralized execution framework to construct a deep neural network which decides the optimal offloading and computing resource allocation for tasks and hence optimizes system latency and energy consumption under the reliability constraint. To verify the efficiency of the proposed scheme, a metric named utility value is adopted in the experiment to show the improvement on latency and energy efficiency. Experimental results show that compared with the existing approaches, the utility value increased by our scheme can be up to 221.9%. © 2023 Science Press. All rights reserved.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0803.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
