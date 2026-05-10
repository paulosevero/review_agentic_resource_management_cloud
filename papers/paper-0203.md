---
id: paper-0203
title: Fog computing architecture for personalized recommendation of banking products
authors:
- Hernández-Nieves, E.
- Hernández, Guillermo
- Gil-González, Ana-Belén
- Rodríguez-González, Sara
- Corchado, Juan M.
venue: Expert Systems with Applications
venue_type: journal
year: 2020
doi: 10.1016/j.eswa.2019.112900
url: https://www.scopus.com/pages/publications/85071848820?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Architecture
- Commercial banking
- Fintech
- Fog computing
- Recommendation system
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

# paper-0203 — Fog computing architecture for personalized recommendation of banking products

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this article, a novel Fog Computing solution is proposed, developed in the area of fintech. It integrates predictive systems in the process of delivery of personalized customer services for the recommendation of the products of a banking entity. The motivation behind this research is to improve aspects of customer support services, especially, achieve greater security, increased transparency and agility of processes as well as reduce entity management costs. The presented architecture includes fog nodes where data are processed by light intelligent agents allowing for the implementation of contextual recommendation systems together with the configuration of a Case Based Reasoning in the Cloud layer to improve the efficiency of the whole system over the time. The recommendation system is the cornerstone of architecture operating on banking products, such as mortgages, loans, retirement plans, etc., and it is developed by a hybrid method of recommendation: collaborative filtering combined with content-based filtering. The article analyzes the presented architecture while performing a verification and simulation of the data in the context of commercial banking. For this purpose, it shows the use of the proposed system of recommendations that represent the different communication channels as well as the possible devices. The proposed architecture offers the opportunity to improve the customer service in the bank's physical channels and at the same time generate technological support to improve the resolution capacity of office managers, allowing employees to adopt a more versatile and flexible role. It also allows the evolution of the banking services model in offices while the processes that support it to follow a one-stop shop approach. © 2019 Elsevier Ltd

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0203.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
