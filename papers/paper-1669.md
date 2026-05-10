---
id: paper-1669
title: 'HyperJet: Joint Communication and Computation Scheduling for Hypergraph Tasks in Distributed Edge Computing'
authors:
- Huang, Kang
- Qiu, Chao
- Hou, Chenxuan
- Li, Xiuhua
- Wang, Xiaofei
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2025
doi: 10.1109/INFOCOM55648.2025.11044587
url: https://www.scopus.com/pages/publications/105011035831?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computational efficiency
- Edge computing
- Energy efficiency
- Energy utilization
- Green computing
- Multitasking
- Neural networks
- Parallel processing systems
- Scheduling algorithms
- Communication latency
- Communication scheduling
- Computation scheduling
- Edge computing
- Energy-consumption
- Hyper graph
- Multiple tasks
- Parallel computing efficiency
- Parallel efficiency
- Performance
- Decision making
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

# paper-1669 — HyperJet: Joint Communication and Computation Scheduling for Hypergraph Tasks in Distributed Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Distributed Edge Computing (DEC) has emerged as a novel paradigm, owing to its superior performance in communication latency, parallel computing efficiency, and energy consumption. With the surge of tasks in generative artificial intelligence, DEC faces higher demands for parallel computing efficiency. Scheduling multiple tasks for simultaneous processing, rather than one-by-one handling, could enhance parallel efficiency. Multiple tasks have multi-dependencies, i.e., sequence dependency, attribute similarity, and attribute correlation. Utilizing the bidirectional edges of traditional graphs to represent multi-dependencies can lead to an explosion in quantity. A hypergraph, with its hyperedges capable of connecting any number of vertices, can significantly solve the above problem. However, the multi-dependencies are rarely studied in the current research, posing the challenges, including incapable representing and unable capturing of multi-dependency hypergraph. In this work, we introduce a Joint communication and computation scheduling for hypErgraph Tasks in DEC, namely HypeJet, To effectively represent multi-dependencies, we employ hypergraph construction to represent task attributes and utilize hypergraph partitioning to clarify and refine task attribute correlations, enhancing parallel efficiency. In response to the challenge of capturing multi-dependencies, we employ a scheduling mechanism with the hypergraph neural network that efficiently acquires higher-order attribute correlated information among convolution matrices, providing enriched contextual information on multi-dependencies that supports decision-making in scheduling tasks. The evaluations using real-world traces demonstrate an 18.07% improvement in parallel efficiency of task scheduling.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1669.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
