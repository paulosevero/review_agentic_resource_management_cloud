---
id: paper-0179
title: Online scheduling of dependent tasks of cloud’s workflows to enhance resource utilization and reduce the makespan using multiple reinforcement learning-based agents
authors:
- Asghari, Ali
- Sohrabi, Mohammad Karim
- Yaghmaee, Farzin
venue: Soft Computing
venue_type: journal
year: 2020
doi: 10.1007/s00500-020-04931-7
url: https://www.scopus.com/pages/publications/85084138737?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 16177--16199
keywords:
- Cloud computing
- Multi-agent systems
- Reinforcement learning
- Resource provisioning
- Task scheduling
- Workflow
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

# paper-0179 — Online scheduling of dependent tasks of cloud’s workflows to enhance resource utilization and reduce the makespan using multiple reinforcement learning-based agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to different heterogeneous cloud resources and diverse and complex applications of the users, an optimal task scheduling, which can satisfy users and cloud service providers with energy-saving and cost-effective use of resources, is a major issue in cloud computing. On the one hand, network users are demanding the quality assurance of their requested services, minimizing their costs, and their own data security, and on the other hand, the service providers consider less power consumption, more efficient use of resources, and optimal utilization. In dependent tasks dealing with massive data, resource scheduling is considered as an important challenge. Due to the time limitation of online scheduling process of dependent tasks, many existing methods of the literature are not able to guarantee the best resource utilization. In this paper, a reinforcement learning approach is exploited in a multi-agent system for task scheduling and resource provisioning, in order to reduce the makespan, minimize the required power, optimize the cost of using the resources, and maximize the utilization of the resources (considering their expiration time), simultaneously. The proposed algorithm has two phases. In the first phase, the tasks are scheduled using reinforcement learning techniques, and in the second one, considering the information obtained from the scheduling phase, resources are allocated in a multi-agent environment. The results of experiments show that this method improves the efficiency of the use of resources and reduces their costs. Moreover, the expiration time of the tasks is observed and the total execution time and energy consumption will be significantly reduced. © 2020, Springer-Verlag GmbH Germany, part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0179.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
