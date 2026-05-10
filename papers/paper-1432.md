---
id: paper-1432
title: 'PixelsDB: Serverless and NL-Aided Data Analytics with Flexible Service Levels and Prices'
authors:
- Bian, Haoqiong
- Geng, Dongyang
- Li, Haoyang
- Chai, Yunpeng
- Ailamaki, Anastasia
venue: Proceedings - International Conference on Data Engineering
venue_type: conference
year: 2025
doi: 10.1109/ICDE65448.2025.00365
url: https://www.scopus.com/pages/publications/105015515982?origin=resultslist
publisher: IEEE Computer Society
pages: 4612--4615
keywords:
- data analytics
- serverless
- service level
- SLA
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1432 — PixelsDB: Serverless and NL-Aided Data Analytics with Flexible Service Levels and Prices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless query processing has become increasingly popular due to its advantages, including automated resource management, high elasticity, and pay-as-you-go pricing. For users who are not system experts, serverless query processing greatly reduces the cost of owning a data analytic system. However, it is still a significant challenge for non-expert users to transform their complex and evolving data analytic needs into proper SQL queries and select a serverless query service that delivers satisfactory performance and price for each type of query. This paper presents PixelsDB, an open-source data analytic system that allows users who lack system or SQL expertise to explore data efficiently. It allows users to generate and debug SQL queries using a natural language interface powered by fine-tuned language models. The queries are then executed by a serverless query engine that offers varying prices for different performance service levels (SLAs). The performance SLAs are natively supported by dedicated architecture design and heterogeneous resource scheduling that can apply cost-efficient resources to process non-urgent queries. We demonstrate that the combination of a serverless paradigm, a natural-language-aided interface, and flexible SLAs and prices will substantially improve the usability of cloud data analytic systems.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1432.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
