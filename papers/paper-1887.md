---
id: paper-1887
title: Joint Task Coding and Transfer Optimization for Edge Computing Power Networks
authors:
- Liu, Jiajia
- Lu, Yunlong
- Wu, Hao
- Ai, Bo
- Jamalipour, Abbas
- Zhang, Yan
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2025
doi: 10.1109/TNSE.2025.3554100
url: https://www.scopus.com/pages/publications/105001307317?origin=resultslist
publisher: IEEE Computer Society
pages: 2783--2796
keywords:
- computing power networks
- Edge intelligence
- multi-agent deep reinforcement learning
- task coding
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1887 — Joint Task Coding and Transfer Optimization for Edge Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the exponential growth of the Internet of Everything (IoE) and substantial advancements in artificial intelligence, services based on deep learning have seen a significant increase in demand for computing resources. The existing edge computing paradigms struggle to handle the explosive growth in computing demands. They also face challenges in jointly optimizing the high transmission load and privacy concerns of task collaboration while failing to utilize computing resources efficiently in complex and dynamic computing power networks. In this paper, we investigate an edge computing power network framework that integrates heterogeneous computing resources from both horizontal and vertical dimensions. We formulate a collaborative task transfer problem to minimize the total execution time of multiple tasks by joint optimization task coding, computing-task association, and collaborative transfer computing strategies among nodes. To solve the formulated problem, we conduct in-depth theoretical analyses and design a two-layer multi-agent optimization algorithm. Specifically, the task coding problem is reformulated in the inner layer into a solvable form, and a closed-form expression for the task coding ratio is derived. Subsequently, we design an adaptive hybrid reward-based multi-agent deep reinforcement learning algorithm to address the sparsity challenges of single-layer rewards while ensuring efficient and stable training convergence. Numerical results show the superiority of our proposed algorithm. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1887.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
