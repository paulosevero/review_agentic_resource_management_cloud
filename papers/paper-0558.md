---
id: paper-0558
title: 'AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices'
authors:
- Cai, Binlei
- Wang, Bin
- Yang, Meihong
- Guo, Qin
venue: Future Generation Computer Systems
venue_type: journal
year: 2023
doi: 10.1016/j.future.2023.01.014
url: https://www.scopus.com/pages/publications/85147192698?origin=resultslist
publisher: Elsevier B.V.
pages: 61--75
keywords:
- Cloud computing
- Microservices
- Quality of service
- Reinforcement learning
- Resource management
- Tail latency
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0558 — AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern user-facing services are progressively evolving from large monolithic applications to complex graphs of loosely-coupled microservices. While microservice architecture greatly improves the efficiency of development and operation, it also complicates resource allocation and performance guarantee due to complex dependencies across different microservices. To prevent resource wastage and ensure user satisfaction, we present AutoMan, a learning-driven resource manager for microservices that enables much more efficient resource provisioning while guaranteeing the end-to-end tail latency Service Level Objective (SLO). AutoMan leverages a multi-agent deep deterministic policy gradient (MADDPG)-based method to capture the dependencies across different microservices and to allocate a proper amount of resources to each microservice subject to the target end-to-end tail latency SLO. During runtime, it further proactively identifies the critical microservices responsible for performance anomaly by deriving partial SLOs mathematically, and performs dynamic reprovisioning to mitigate the potential SLO violations. Testbed experiments show that AutoMan can save CPU and memory resources by up to 49.6% and 29.1% on average, while guaranteeing the same end-to-end tail latency objective. © 2023 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0558.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
