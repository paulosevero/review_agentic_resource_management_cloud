---
id: paper-0123
title: 'Autonomic decentralized microservices: The Gru approach and its evaluation'
authors:
- Di Nitto, Elisabetta
- Florio, Luca
- Tamburri, Damian A.
venue: 'Microservices: Science and Engineering'
venue_type: book-chapter
year: 2019
doi: 10.1007/978-3-030-31646-4_9
url: https://www.scopus.com/pages/publications/85092693855?origin=resultslist
publisher: Springer International Publishing
pages: 209--248
keywords: []
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
    my_justification: GRU
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

# paper-0123 — Autonomic decentralized microservices: The Gru approach and its evaluation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud applications are more and more featuring microservices as a design pattern, using related technologies (containerization, orchestration, continuous deployment, integration, and more) to speed up design, development, and operation. However, microservices are not bullet-proof: they increase design and management issues in the cloud adding to the mix all the intrinsic complexities of highly distributed systems. This addition can render ineffective all centralized management technologies like Docker or clustering systems like Swarm and Kubernetes. Conversely, autonomic and decentralized microservices management is still largely unexplored. We address this problem with Gru, an approach based on multiagent systems that adds an autonomic adaptation layer for microservice applications focusing on Docker, the de facto market leader in container technology. Gru is designed to support fully decentralized microservices management, and can be integrated with ease in dockerized applications, managing them with autonomic actions to satisfy application quality requirements. We evaluate Gru with a concrete case study showing autoscaling dockerized microservices matching variating and bursty workloads. Evaluation shows encouraging results for Gru autonomic management. © Springer Nature Switzerland AG 2020.

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
- **my_justification:** "GRU"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0123.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
