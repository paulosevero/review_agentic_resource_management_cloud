---
id: paper-0988
title: Scaling Generative AI for E&P
authors:
- Koziol, T.
- Zamurovic, D.
- Dillen, M.
- Wellhausen, A.
- Pullig, M.
venue: 4th EAGE Digitalization Conference and Exhibition
venue_type: conference
year: 2024
doi: 10.3997/2214-4609.202439056
url: https://www.scopus.com/pages/publications/85217622975?origin=resultslist
publisher: European Association of Geoscientists and Engineers, EAGE
pages: ''
keywords:
- Generative adversarial networks
- AI Technologies
- Best practices
- Comprehension tasks
- Corporate environment
- Extended abstracts
- Language comprehensions
- Primary contribution
- Scalings
- Turning-points
- Web browsers
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-0988 — Scaling Generative AI for E&P

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The introduction of a new generation of models in early 2023 marked a profound and transformative turning point in the field of Artificial Intelligence, primarily owing to their versatility in applications related to information retrieval and language comprehension tasks. Despite the technology’s ease of access through a web browser (ChatGPT), the process of adapting it for enterprise-grade implementation poses several noteworthy challenges. In this extended abstract, we present a method for the effective integration of Generative AI technology into corporate environments, facilitating the deployment of various text-based applications. Our approach centers on the consolidation of best-practice components for Generative AI, drawn from individual use case implementations, into a collection of Python functions. These functions can subsequently be deployed as microservices to facilitate the execution of additional use cases. The primary contribution of our work is the emphasis on implementing Generative AI with scalability as a central focus. © 4th EAGE Digitalization Conference and Exhibition 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0988.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
