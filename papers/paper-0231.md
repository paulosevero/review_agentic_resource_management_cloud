---
id: paper-0231
title: Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation
authors:
- Obermeier, Sandra
- Berrendorf, Max
- Kroger, Peer
venue: Proceedings - 2020 IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent Agent Technology, WI-IAT 2020
venue_type: conference
year: 2020
doi: 10.1109/WIIAT50758.2020.00056
url: https://www.scopus.com/pages/publications/85114440496?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 387--390
keywords:
- Edge computing
- Index compression
- Reverse k-nearest neighbor
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: kNN
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

# paper-0231 — Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The reverse k-nearest neighbor (RkNN) query is an established query type with various applications reaching from identifying highly influential objects over incrementally updating kNN graphs to optimizing sensor communication and outlier detection. State-of-the-art solutions exploit that the k-distances in real-world datasets often follow the power-law distribution, and bound them with linear lines in log-log space. In this work, we investigate this assumption and uncover that it is violated in regions of changing density, which we show are typical for real-life datasets. Towards a generic solution, we pose the estimation of k-distances as a regression problem. Thereby, we enable harnessing the power of the abundance of available Machine Learning models and profiting from their advancement. We propose a flexible approach which allows steering the performance-memory consumption trade-off, and in particular to find good solutions with a fixed memory budget crucial in the context of edge computing. Moreover, we show how to obtain and improve guaranteed bounds essential to exact query processing. In experiments on real-world datasets, we demonstrate how this framework can significantly reduce the index memory consumption, and strongly reduce the candidate set size. We publish our code at https://github.com/sobermeier/nonlinear-kdist, and a detailed technical report at https://arxiv.org/abs/2011.01773. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "kNN"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0231.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
