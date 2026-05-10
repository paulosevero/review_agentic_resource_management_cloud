---
id: paper-2802
title: Exploring the Systematic Use of LLMs for Micro services Generation
authors:
- Trabelsi, Imen
- Naouel, Moha
- Yann-Gaël, Guéhéneuc
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-96-7238-7_10
url: https://www.scopus.com/pages/publications/105021000165?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 121--128
keywords:
- Automation
- Generative
- LLMs
- Microservices
- Migration
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

# paper-2802 — Exploring the Systematic Use of LLMs for Micro services Generation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The inflexibility of monolithic architectures results in a low software systems scalability and agility, compared to the modular systems based on microservices that can be independently developed and deployed. To facilitate the migration from monolithic to microservices architecture (MSA), researchers and practitioners have proposed various approaches. However, most of these works focus on automating the identification of microservices, and few have addressed the practical aspects of generating and deploying them. This gap leaves the migration process costly and complex, relying on expert intervention and manual labour to transform monolith systems into micro services. In this paper, we suggest that LLMs constitute an exciting but ill-studied means to automate key steps of the generation of micro services, including source code restructuring, API implementation, and integration of micro service patterns. We introduce (1) a systematic approach for generating LLM prompts to guide the migration process and (2) insights drawn from applying this approach to a real-world system. Our position challenges the current reliance on manual labour for MSA migration and supports LLM-assisted automation, encouraging discussions on the feasibility, benefits and wider impact of incorporating LLMs into the migration process. We introduce (1) a systematic approach for generating LLM prompts to guide the migration process and (2) insights drawn from applying this approach to a real-world system. Our position challenges the current reliance on manual labour for MSA migration and supports LLM-assisted automation, driving the discussion on the practicality, advantages and impact of including LLMs in the migration process. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2802.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
