---
id: paper-1491
title: 'Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL'
authors:
- Chinta, Pratima
- Naidu, Gokul
- Manjunatha, B.
- Ponnath, Anand
venue: 2025 IEEE International Conference on Omni-Layer Intelligent Systems, COINS 2025
venue_type: conference
year: 2025
doi: 10.1109/COINS65080.2025.11125795
url: https://www.scopus.com/pages/publications/105016145843?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud Cost Data insights
- Generative AI
- Large Language Models
- Natural language processing
- Text-to-SQL
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-1491 — Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern enterprises increasingly leverage public cloud services to host application workloads with underlying cloud components, service tiers, and associated costs. These usage-based charging models introduce complexity. This necessitates the analysis of substantial data volumes to derive valuable insights. In this paper, we aim to address the challenge of enabling business and financial stakeholders to efficiently interpret cloud cost data and its trends without SQL expertise. We present an AI-powered system built on the DSPy framework that translates natural language questions into SQL queries using an enterprise-grade Large Language Model (LLM), delivering context-aware and desired responses. Existing dashboards and NLP approaches rely on rule-based parsing, requiring predefined data schemas and manual configuration. DSPy also uses these schemas but enhances flexibility by adapting them through structured pipelines and multi-step reasoning to improve accuracy. To train and evaluate our model, we augment a small dataset of question-SQL pairs through LLM-based generation and manual refinement. Additionally, we develop a custom recommendation engine using search-based techniques in Python to identify and disambiguate field names and values for both users and the LLM. Our system achieves 90% execution accuracy on our dataset, which indicates that the generated SQL queries return correct results when executed on the target database. These results demonstrate the effectiveness of prompt-tuned LLMs and in-context learning in providing a scalable, accessible solution for enterprise data analysis, ultimately enhancing decision-making in financial management.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1491.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
