---
id: paper-0848
title: Pareto Approximation Empirical Results of Energy-Aware Optimization for Precedence-Constrained Task Scheduling Considering Switching Off Completely Idle Machines
authors:
- Castán Rocha, José Antonio
- Santiago, Alejandro
- García-Ruiz, Alejandro H.
- Terán-Villanueva, Jesús David
- Martínez, Salvador Ibarra
- Treviño Berrones, Mayra Guadalupe
venue: Mathematics
venue_type: journal
year: 2024
doi: 10.3390/math12233733
url: https://www.scopus.com/pages/publications/85211808071?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- directed acyclic graph
- energy aware
- energy idle
- evolutionary algorithms
- heterogeneous computing
- makespan
- multi-objective optimization
- parallel applications
- precedence–constraint
- task scheduling
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0848 — Pareto Approximation Empirical Results of Energy-Aware Optimization for Precedence-Constrained Task Scheduling Considering Switching Off Completely Idle Machines

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent advances in cloud computing, large language models, and deep learning have started a race to create massive High-Performance Computing (HPC) centers worldwide. These centers increase in energy consumption proportionally to their computing capabilities; for example, according to the top 500 organization, the HPC centers Frontier, Aurora, and Super Computer Fugaku report energy consumptions of 22,786 kW, 38,698 kW, and 29,899 kW, respectively. Currently, energy-aware scheduling is a topic of interest to many researchers. However, as far as we know, this work is the first approach considering the idle energy consumption by the HPC units and the possibility of turning off unused units entirely, driven by a quantitative objective function. We found that even when turning off unused machines, the objectives of makespan and energy consumption still conflict and, therefore, their multi-objective optimization nature. This work presents empirical results for AGEMOEA, AGEMOEA2, GWASFGA, MOCell, MOMBI, MOMBI2, NSGA2, and SMS-EMOA. The best-performing algorithm is MOCell for the 400 real scheduling problem tests. In contrast, the best-performing algorithm is GWASFGA for a small-instance synthetic testbed. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0848.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
