---
id: paper-0999
title: 'Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach'
authors:
- Lang, Junyi
- Zheng, Xiaokang
- Sun, Yimeng
- Ding, Zhaohao
venue: 2024 IEEE IAS Industrial and Commercial Power System Asia, I and CPS Asia 2024
venue_type: conference
year: 2024
doi: 10.1109/ICPSAsia61913.2024.10761284
url: https://www.scopus.com/pages/publications/85214487717?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 748--753
keywords:
- data locality
- Geo-distributed data centers
- job scheduling
- power consumption
- reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0999 — Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid growth of cloud computing, geo-distributed data centers are becoming more energy-intensive. Given the unique characteristics of computing jobs, they can be executed across data centers in different geographic locations to better utilize lower electricity prices. However, data locality is a crucial factor to be considered in this process, as it is a precondition for the execution of jobs. In this paper, we propose a multi-agent deep reinforcement learning-based job scheduling algorithm that addresses constraints such as data locality and job deadlines to achieve real-time scheduling of jobs and data across data centers to optimize energy costs. First, we formulate the data locality-aware job scheduling problem across geo-distributed data centers as a Partially Observable Markov Decision Process (POMDP). Then, we develop a multi-agent system where agents handle job scheduling and data transfer respectively. The job scheduling agent needs to consider data transfer conditions when taking actions, as the necessary data for job execution must be available before executing. These agents collaborate by sharing the reward function to optimize the scheduling strategy, reducing the overall energy costs of job execution and data transfer. Finally, we conduct numerical experiments to validate the effectiveness of our proposed scheduling method in reducing data center energy costs while maintaining high service quality. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0999.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
