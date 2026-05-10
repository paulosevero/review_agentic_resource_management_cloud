---
id: paper-1542
title: 'FI-NL2PY2SQL: Financial Industry NL2SQL Innovation Model Based on Python and Large Language Model'
authors:
- Du, Xiaozheng
- Hu, Shijing
- Zhou, Feng
- Wang, Cheng
- Nguyen, Binh Minh
venue: Future Internet
venue_type: journal
year: 2025
doi: 10.3390/fi17010012
url: https://www.scopus.com/pages/publications/85215960038?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- LLM
- NL2SQL
- pre-training
- prompt
- Python
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1542 — FI-NL2PY2SQL: Financial Industry NL2SQL Innovation Model Based on Python and Large Language Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of prominent models, NL2SQL has made many breakthroughs, but customers still hope that the accuracy of NL2SQL can be continuously improved through optimization. The method based on large models has brought revolutionary changes to NL2SQL. This paper innovatively proposes a new NL2SQL method based on a large language model (LLM), which could be adapted to an edge-cloud computing platform. First, natural language is converted into Python language, and then SQL is generated through Python. At the same time, considering the traceability characteristics of financial industry regulatory requirements, this paper uses the open-source big model DeepSeek. After testing on the BIRD dataset, compared with most NL2SQL models based on large language models, EX is at least 2.73% higher than the original method, F1 is at least 3.72 higher than the original method, and VES is 6.34% higher than the original method. Through this innovative algorithm, the accuracy of NL2SQL in the financial industry is greatly improved, which can provide business personnel with a robust database access mode. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1542.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
