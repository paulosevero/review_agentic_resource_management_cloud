---
id: paper-0818
title: Heterogeneous Computational Scheduling Using Adaptive Neural Hyper-Heuristic
authors:
- Allahverdyan, A.
- Zhadan, A.
- Kondratov, I.
- Petrosian, O.
- Romanovskii, A.
- Kharin, V.
- Li, Yin
venue: Doklady Mathematics
venue_type: journal
year: 2024
doi: 10.1134/S106456242460221X
url: https://www.scopus.com/pages/publications/105000697801?origin=resultslist
publisher: Pleiades Publishing
pages: S151 - S161
keywords:
- Directed Acyclic Graph
- genetic algorithm
- Neural networks
- scheduling
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

# paper-0818 — Heterogeneous Computational Scheduling Using Adaptive Neural Hyper-Heuristic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Abstract: In heterogeneous computing environments, efficiently scheduling tasks, especially those forming Directed Acyclic Graphs (DAGs), is critical. This is particularly true for various Cloud and Edge computing tasks, as well as training Large Language Models (LLMs). This paper introduces a new scheduling approach using an Adaptive Neural Hyper-heuristic. By integrating a neural network trained with genetic algorithms, our method aims to minimize makespan. The approach uses a two-level algorithm: the first level prioritizes tasks using adaptive heuristic and the second level assigns resources based on the Earliest Finish Time (EFT) algorithm. Our tests show that this method significantly improves over traditional scheduling heuristics and other machine learning-based approaches. It reduces the makespan by 6.7% for small-scale DAGs and 28.49% for large-scale DAGs compared to the leading DONF algorithm. Additionally, it achieves a proximity of 84.08% to 96.43% to the optimal solutions found using Mixed-Integer Linear Programming (MILP), demonstrating its effectiveness in diverse computational settings. © The Author(s) 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0818.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
