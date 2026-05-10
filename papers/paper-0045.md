---
id: paper-0045
title: A real-world inspired multi-strategy based negotiating system for cloud service market
authors:
- Adabi, Sepideh
- Mosadeghi, Mozhgan
- Yazdani, Samaneh
venue: Journal of Cloud Computing
venue_type: journal
year: 2018
doi: 10.1186/s13677-018-0116-5
url: https://www.scopus.com/pages/publications/85053542935?origin=resultslist
publisher: Springer Verlag
pages: ''
keywords:
- Cloud computing
- E-market
- Fuzzy decision controller
- Multi-agent system
- Negotiation model
- Pricing
- Resource allocation
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
    my_justification: Game theory
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

# paper-0045 — A real-world inspired multi-strategy based negotiating system for cloud service market

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Designing negotiator agents who adopt real-world inspired negotiation strategies in front of different types of negotiation scenario increases the chance of having better utility and success rate in negotiation-based cloud resource allocation. To realize real-world inspired multi-strategy based negotiating system for cloud marketplace, three following issues are focused in this paper: 1) Designing a new negotiation_strategy_basket with the aim of approaching the strategies of the real-world negotiation markets, 2) Modeling the critical condition of the cloud trading market, and 3) Adopting a new fuzzy decision system (i.e., Fuzzy Negotiation Strategy Selection System (FNSSDS)) for conducting negotiator agents of type resource providers and resource customers in how to select a suitable negotiation strategy from negotiation_strategy_basket according to the critical condition of the cloud trading market. We perform extensive simulation experiments to compare the performance of the proposed negotiator agents with the well known negotiator agents in name MDA (Market Driven Agent). The results show that the proposed negotiation agents outperform the MDAs. © 2018, The Author(s).

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
- **my_justification:** "Game theory"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0045.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
