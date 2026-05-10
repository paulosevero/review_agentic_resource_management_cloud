---
id: paper-0312
title: Comparison of Efficient Planning and Optimization Methods of Last Mile Delivery Resources
authors:
- Maestro, J.A.
- Rodriguez, S.
- Casado, R.
- Prieto, J.
- Corchado, J.M.
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2021
doi: 10.1007/978-3-030-68737-3_11
url: https://www.scopus.com/pages/publications/85101514321?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 163--173
keywords:
- Cloud computing
- Last mile delivery
- Multi-Agent Systems
- Planning optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-0312 — Comparison of Efficient Planning and Optimization Methods of Last Mile Delivery Resources

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A review of recent Last Mile Delivery optimization proposals is presented. The proposals are classified according to the criteria of collaboration, ranging from optimization of a single route to the integration of multiple carriers. An alternative proposal is presented, based also on collaboration, but which does not involve either integration into a single organization or sharing of its resources. Each carrier is represented as a Virtual Organization of Agents (VO). A global optimizer, also a VO, oversees the search for deliveries that can be better delivered by another carrier and new routes are calculated based on a win-win approach. This approach has the advantages of being easily configurable by integrating or removing the VO of each carrier, highly distributable using a cloud infrastructure, easily scalable both for physical areas and computational resources using the cloud infrastructure in case more computational power is needed. It also allows the sharing of the least amount of information possible among carriers, so that they only know about the deliveries that they are losing or gaining. © 2021, ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0312.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
