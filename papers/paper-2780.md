---
id: paper-2780
title: 'Optimizing Renewable Energy Distribution Networks with AI Techniques: The A-IsolE Project'
authors:
- Soma, Gian Giuseppe
- Pasquarelli, Maria Giulia
- Pentolini, Massimo
- Dore, Cristina
- Martini, Francesco
- Bagnasco, Andrea
- Vinci, Andrea
- Valfrè, Giulio
- Bessone, Enrico
- Mosaico, Gabriele
- Saviozzi, Matteo
venue: Energies
venue_type: journal
year: 2026
doi: 10.3390/en19071718
url: https://www.scopus.com/pages/publications/105035652722?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- artificial intelligence
- distribution management system
- distribution network
- edge computing
- renewable energy sources
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2780 — Optimizing Renewable Energy Distribution Networks with AI Techniques: The A-IsolE Project

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The large-scale penetration of Distributed Energy Resources (DERs), the proliferation of Energy Communities, and the increasing provision of flexibility services are fundamentally transforming distribution network operation, rendering traditional Distribution Management Systems (DMSs) structurally inadequate. This paper addresses this structural gap by proposing and experimentally validating A-ISolE, a novel hybrid Artificial Intelligence (AI) architecture that natively integrates centralized and distributed intelligence within a unified DMS framework. The core scientific contribution of this work lies in the formulation and deployment of a coordinated, hierarchical AI paradigm in which cloud-level predictive and optimization modules dynamically interact with edge-level autonomous control agents. Specifically, the paper introduces: (1) an integrated forecasting state estimation pipeline with AI-enhanced grid observability; (2) intelligent fault location and optimal feeder reconfiguration algorithms embedded into operational control loops; and (3) distributed edge control strategies enabling autonomous yet coordinated microgrid stabilization. The architecture is validated on a real pilot microgrid in Sanremo (Italy). Experimental results demonstrate quantifiable gains in many parameters, substantiating the feasibility of hybrid centralized/distributed AI as a foundational paradigm for future resilient and decarbonized distribution networks. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2780.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
