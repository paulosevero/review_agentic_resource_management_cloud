---
id: paper-0824
title: Bi-objective cloud resource management for dependent tasks using Q-learning and NSGA-3
authors:
- Asghari, Ali
- Sohrabi, Mohammad Karim
venue: Journal of Ambient Intelligence and Humanized Computing
venue_type: journal
year: 2024
doi: 10.1007/s12652-022-03885-y
url: https://www.scopus.com/pages/publications/85131054509?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 197--217
keywords:
- Bi-objective
- Cloud computing
- NSGA-3
- Q-learning
- Resource management
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0824 — Bi-objective cloud resource management for dependent tasks using Q-learning and NSGA-3

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient management of cloud resources for more resource utilization on the one hand, and reducing the makespan on the other hand, has always been an important research issue in cloud environment. Since the proper allocation of cloud resources is an optimization problem, the learning-based and population-based meta-heuristic methods are used for this purpose. Most learning methods have scalability problem and may not converge to the optimal solution as the problem space becomes larger, and population-based optimization methods usually need a lot of iterations. The proposed method of this paper aims to overcome the limitations of these two techniques and uses their advantages to increase cloud resource utilization and improve the execution time. A Pareto-based algorithm is also exploited to solve this bi-objective problems. Since increasing the size of population leads to increase the convergence time, a proper learning-based selecting method of population is also utilized to reduce the number of iterations. The proposed method of this paper, called multi-agent bi-objective cloud resource management for dependent tasks using Q-learning and NSGA-3 (BCRN), employs an improved version of Q-learning to reduce the makespan and enhance resource utilization. To overcome the scalability problem of Q-learning, the number of states and actions are reduced in the BCRN, which reduces the complexity of the learning process and leads to better convergence time of the learning process. Two learning agents are also utilized in the BCRN, each of which seeks to improve the objectives of the problem. The NSGA-3 (non-deterministic sorting genetic algorithm-3) algorithm is used as to address the bi-objective problem. In the NSGA-3 algorithm, the initial population is often generated randomly, which leads to more convergence time of the learning process. Using a modified bi-objective Q-learning model, the initial population of the BCRN is generated considering the both objectives of the method to reduce the convergence time of the NSGA-3 algorithm. The long-term learning process attempts to find the best mapping between resources and tasks, and avoid local optima. The results of empirical experiments indicate that the proposed method reduces the makespan, and causes more efficient use of cloud resources. © The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2022.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0824.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
