---
id: paper-1351
title: Scheduling Generative-AI Job DAGs with Model Serving in Data Centers
authors:
- Zheng, Ying
- Jiao, Lei
- Xu, Yuedong
- An, Bo
- Wang, Xin
- Li, Zongpeng
venue: IEEE International Workshop on Quality of Service, IWQoS
venue_type: conference
year: 2024
doi: 10.1109/IWQoS61813.2024.10682885
url: https://www.scopus.com/pages/publications/85206383798?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge computing
- Generative adversarial networks
- Integer programming
- Job shop scheduling
- Mixed-integer linear programming
- Profitability
- Acyclic graphs
- Computing environments
- Datacenter
- Edge computing
- Model Selection
- Non linear
- Non-trivial
- Scheduling selection
- Task modelling
- Tasks scheduling
- Integer linear programming
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

# paper-1351 — Scheduling Generative-AI Job DAGs with Model Serving in Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Scheduling generative-AI jobs in the edge computing environment faces multiple non-trivial challenges, including the Directed Acyclic Graph (DAG) dependency among tasks, the intrinsic intertwinement between task scheduling and model selection, and the dynamic unpredictable arrival of job DAGs. In this work, we capture all such challenges and formulate a non-linear integer program to optimize the long-term profit of the generative-AI service provider, i.e., service revenue of the admitted jobs minus system costs of executing the tasks contained in such job DAGs. This problem is NP-hard even in the offline setting. To solve it, we first reformulate it into an equivalent schedule selection problem using generated schedules to tackle complex constraints. Then, we design a new online scheduling method through the online primal-dual technique. Experimental results confirm that our approach can increase the total service profit by up to 41.2% compared to existing algorithms. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1351.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
