---
id: paper-2115
title: 'Beyond Decomposition: A LLM-Powered Automated Approach to Refactoring Monoliths Into Microservices'
authors:
- Sellami, Khaled
- Jebbar, Oussama
- Gannoun, Ayyoub
- Saied, Mohamed Aymen
venue: IEEE International Conference on Software Quality, Reliability and Security, QRS
venue_type: conference
year: 2025
doi: 10.1109/QRS65678.2025.00018
url: https://www.scopus.com/pages/publications/105018798967?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers
pages: 68--77
keywords:
- Decomposition
- Large Language Models
- Microservices Migration
- Refactoring
- Remote Procedural Calls
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2115 — Beyond Decomposition: A LLM-Powered Automated Approach to Refactoring Monoliths Into Microservices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Organizations migrating monolithic applications to microservice architectures often face significant challenges in both decomposition and refactoring phases. While the decomposition step has received considerable automation research, refactoring remains predominantly manual, creating bottlenecks in migration efforts and preventing runtime-based and a more realistic evaluation of decomposition techniques. We propose a fully automated refactoring methodology that complements existing decomposition approaches. Our technique implements an ID-based and DTO-based hybrid design for inter-service communication and leverages Large Language Models (LLMs) for decision making, code analysis and code generation. Taking a monolith's source code and decomposition plan as input, our approach identifies 'API classes' that cross service boundaries, selects their appropriate target design among the ID and DTO based methods and then automatically generates the necessary communication components - API contracts, server-side endpoints, and client-side proxies. This approach balances the preservation of the monolith's workflow consistency through the ID-based design and minimizing the overhead and complexity of the cross-service interactions through the DTO-based design. A qualitative evaluation using three benchmark applications demonstrates our approach's feasibility and advantages over related work.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2115.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
