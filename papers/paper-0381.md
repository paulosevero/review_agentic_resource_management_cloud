---
id: paper-0381
title: Smart and fuzzy approach based on CSP for cloud resources allocation
authors:
- Almutawakel, Abdallah
- Kazar, Okba
- Bali, Mouadh
- Belouaar, Houcine
- Barkat, Abdelbasset
venue: International Journal of Computers and Applications
venue_type: journal
year: 2022
doi: 10.1080/1206212X.2019.1701241
url: https://www.scopus.com/pages/publications/85076445827?origin=resultslist
publisher: Taylor and Francis Ltd.
pages: 117--129
keywords:
- Cloud computing
- distributed constraints satisfaction problems
- fuzzy logic
- multiagent system
- resources allocation
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0381 — Smart and fuzzy approach based on CSP for cloud resources allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this study, we proposed a resource allocation approach that aims at fulfilling two main objectives. First, it equilibrates between the different cloud infrastructure particularities including load balancing, so it enhances the performance of infrastructure. Second, our approach provides a solution for the customer needs through shortening the execution time and reducing payments of the requested resources that have a dynamic nature. This paper suggests a new hybrid resources allocation approach based on three methods: multiagent system (MAS), distributed constraints satisfaction problems (DCSP), and the fuzzy logic (FL). The MAS represents the physical infrastructure. It provides an efficient management of the resources in the distribution and the heterogeneity of this infrastructure. DCSP, on the other hand, works side by side with MAS to maintain resources allocation policies in datacenters, while the FL is used to facilitate the representation of the dynamic resource values into linguistic terms (low, medium, high …) and helps the system to determine the best solution according to the criteria of customer requests. The experimental results show the efficiency of our approach in terms of load balancing, energy consumption cost, execution time, and the rate payment gain of customers. © 2019 Informa UK Limited, trading as Taylor & Francis Group.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0381.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
