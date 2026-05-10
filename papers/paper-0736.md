---
id: paper-0736
title: Load Optimization Accessions, Ramification the QoS in Software Defined Networking
authors:
- Tiwna, Pardeep Singh
- Singh, Jaspreet
venue: 2023 International Conference on Artificial Intelligence and Smart Communication, AISC 2023
venue_type: conference
year: 2023
doi: 10.1109/AISC56616.2023.10085328
url: https://www.scopus.com/pages/publications/85153476863?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1013--1017
keywords:
- Controller
- Load Optimization
- Migration.
- QoS
- SDN
- Switch
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0736 — Load Optimization Accessions, Ramification the QoS in Software Defined Networking

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> It is difficult to manage traditional networks due to network growth, an increase in user numbers, and the emergence of new technologies like big data and cloud computing. Consequently, it is required to alter the current network design. SDN is a well-liked architecture because it offers customizable control and centralized management in data centers. To achieve scalability and dependability, it was necessary to propose the geographical dispersal of a logically centralized control plane due to the huge scale of networks. Software-defined networking (SDN) load-balancing optimization has been studied for a long time. Many approaches to the load-balancing conundrum have been put forth by researchers, but very few have taken the impact of transmission delay between controllers and switches under heavy network load into account. In this article we elaborate the various techniques of load balancing in SDN those working on different areas like multi-controller, switch migration, multi-agent, strategy, time sharing, prediction, reinforcement learning etc. We discuss the methods used along with the advantages and disadvantages of various costs, service quality, and network performance metrics.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0736.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
