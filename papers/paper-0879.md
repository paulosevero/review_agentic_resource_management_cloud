---
id: paper-0879
title: Delay-Aware and Energy-Efficient Task Scheduling Using Strength Pareto Evolutionary Algorithm II in Fog-Cloud Computing Paradigm
authors:
- Daghayeghi, Atousa
- Nickray, Mohsen
venue: Wireless Personal Communications
venue_type: journal
year: 2024
doi: 10.1007/s11277-024-11510-8
url: https://www.scopus.com/pages/publications/85202074763?origin=resultslist
publisher: Springer
pages: 409--457
keywords:
- Energy consumption
- Fog computing
- Multi-objective optimization
- Service response time
- SPEAII
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0879 — Delay-Aware and Energy-Efficient Task Scheduling Using Strength Pareto Evolutionary Algorithm II in Fog-Cloud Computing Paradigm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The exponential growth of technology and advent of the Internet of Things (IoT) paradigm have caused large volumes of data to be continuously generated from the intelligent devices. One common feature of these devices is their limited capabilities, hence, they are not able to process large volumes of generated data. However, the processing of these data in the cloud leads to high latency and high power consumption. Hence, providing services to the latency-sensitive IoT applications in the cloud is a challenging issue. Fog computing as a complement to the cloud, allows data to be processed near IoT devices. However, the resources in the fog layer are heterogeneous. Thus, the proper distribution of tasks among heterogeneous nodes while serving the task within the intended deadline is of great importance. In this paper, we have presented a task scheduling model in the fog-cloud paradigm, which formulates the task scheduling problem as a multi-objective optimization problem with the aim of minimizing service response time and the total energy consumption of the system, while considers deadline and load balancing constraints. Since the problem of task scheduling is np-hard, we have proposed a modified version of Strength Pareto Evolutionary Algorithm II (SPEA-II) with customized operators to achieve the optimal scheduling strategy. The experimental results reveal that the proposed scheme outperforms some benchmarking algorithms in terms of service response time and energy consumption. Furthermore, by optimal distribution of tasks among heterogeneous computing nodes, it leads to better resource utilization and improvement in the percentage of missed-deadline tasks. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0879.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
