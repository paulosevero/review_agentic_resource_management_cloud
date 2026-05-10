---
id: paper-1410
title: 'SWARM: Reimagining scientific workflow management systems in a distributed world'
authors:
- Balaprakash, Prasanna
- Raghavan, Krishnan
- Cappello, Franck
- Deelman, Ewa
- Mandal, Anirban
- Jin, Hongwei
- Mahmud, Imtiaz
- Thareja, Komal
- Wu, Shixun
- Zuk, Pawel
- Kiran, Mariam
- Chen, Zizhong
- Di, Sheng
- Wu, Kesheng
venue: International Journal of High Performance Computing Applications
venue_type: journal
year: 2025
doi: 10.1177/10943420251339317
url: https://www.scopus.com/pages/publications/105005578173?origin=resultslist
publisher: SAGE Publications Inc.
pages: 692--712
keywords:
- agentic AI
- consensus algorithms
- large language models
- network overlays
- resilience
- Swarm intelligence
- workflow systems
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1410 — SWARM: Reimagining scientific workflow management systems in a distributed world

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern scientific workflows process massive amounts of data from diverse instruments and sensors, leveraging geographically distributed, heterogeneous compute and storage resources—from leadership-class systems to edge devices—connected by high-performance networks. The diversity of resources introduces challenges in harnessing their full potential, with resilience issues arising across applications, system software, networks, storage, and hardware. Today, workflow management systems (WMS) coordinate the execution of computation and data management tasks across target resources. However, WMS’s centralized nature makes them vulnerable to faults and scalability issues that may result in failures of entire computational campaigns. This paper introduces a novel agentic framework for workflow management, fully distributing and decentralizing the WMS functions and modeling them as swarm intelligence agents infused with advanced artificial intelligence solutions and traditional distributed computing algorithms that can make coordinated decisions in the presence of failures of the underlying cyberinfrastructure. © The Author(s) 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1410.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
