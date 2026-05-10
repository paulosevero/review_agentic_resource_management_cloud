---
id: paper-1759
title: An Empirical Study of Industry Awareness and Adoption of Green Practices in Modern Software Architectures
authors:
- Lal, Supriya
- Narasannagari, Lakshmithejaswi
- Andalam, Sowmyanka
- Shastri, Shilpa
venue: Proceedings - 19th IEEE International Conference on Service-Oriented System Engineering, SOSE 2025
venue_type: conference
year: 2025
doi: 10.1109/SOSE67019.2025.00016
url: https://www.scopus.com/pages/publications/105016121871?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 97--107
keywords:
- Event-Driven
- Generative AI
- Green Software
- Machine Learning
- Microservices
- Serverless
- Sustainable Architectures
- Sustainable Architectures Awareness
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

# paper-1759 — An Empirical Study of Industry Awareness and Adoption of Green Practices in Modern Software Architectures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This empirical study investigates industry awareness about the adoption of green practices across five modern software architectures: Microservices, Event-Driven, Serverless, Machine Learning, and Generative AI. Using an approach that combined surveys (109 responses) and interviews (19 professionals) from the industry, we gathered data to understand awareness of green practices throughout the design, development and maintenance of software architectures. Our findings reveal that while software professionals understand green software concepts, practical implementation lags due to higher priority given to performance, cost, accuracy, and reliability. Each architecture has specific energy challenges: Microservices struggles with resource allocation and excessive communication; Serverless faces over-invocation and cold-start issues; Event-Driven systems struggle with excessive triggering; Machine Learning systems have challenges with inadequate maintenance of model health and lack of awareness in compute requirements between training and inference phases; and Generative AI consumes high energy due to model size and algorithmic complexity. We identify both architecture-specific and common operational strategies for reducing energy consumption, establishing a foundation for future work in sustainable development in resource-intensive architectures.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1759.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
