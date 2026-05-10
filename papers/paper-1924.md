---
id: paper-1924
title: 'DV365: Extremely Long User History Modeling at Instagram'
authors:
- Lyu, Wenhan
- Tyagi, Devashish
- Yang, Yihang
- Li, Ziwei
- Somani, Ajay
- Shanmugasundaram, Karthikeyan
- Andrejevic, Nikola
- Adeputra, Ferdi
- Zeng, Curtis
- Singh, Arun K.
- Ransan, Maxime
- Jain, Sagar
venue: Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining
venue_type: conference
year: 2025
doi: 10.1145/3711896.3737209
url: https://www.scopus.com/pages/publications/105014328940?origin=resultslist
publisher: Association for Computing Machinery
pages: 4717--4727
keywords:
- long user sequence modeling
- recommender system
- representation learning
- user embedding
- user modeling
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

# paper-1924 — DV365: Extremely Long User History Modeling at Instagram

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Long user history is highly valuable signal for recommendation systems, but effectively incorporating it often comes with high cost in terms of data center power consumption and GPU. In this work, we chose offline embedding over end-to-end sequence length optimization methods to enable extremely long user sequence modeling as a cost-effective solution, and propose a new user embedding learning strategy, multi-slicing and summarization, that generates highly generalizable user representation of user's long-term stable interest. History length we encoded in this embedding is up to 70,000 and on average 40,000. This embedding, named as DV365, is proven highly incremental on top of advanced attentive user sequence models deployed in Instagram. Produced by a single upstream foundational model, it is launched in 15 different models across Instagram and Threads with significant impact, and has been production battle-proven for >1 year since our first launch.  © 2025 Copyright held by the owner/author(s).

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1924.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
