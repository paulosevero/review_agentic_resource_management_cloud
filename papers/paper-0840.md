---
id: paper-0840
title: A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum
authors:
- Cai, Binlei
- Wang, Xiaoli
- Wang, Bin
- Yang, Meihong
- Guo, Ying
- Guo, Qin
venue: Computer Networks
venue_type: journal
year: 2024
doi: 10.1016/j.comnet.2024.110279
url: https://www.scopus.com/pages/publications/85186415484?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Edge-cloud continuum
- Microservice deployment
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

# paper-0840 — A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern user-facing services are progressively evolving from large monolithic applications to complex graphs of loosely-coupled microservices. While this shift provides opportunities to offload some microservices of a user-facing service to edge devices that are close to the end users, it also complicates the application deployment and resource provisioning in the edge-cloud continuum, due to complex relationships across microservices and unstable public networks. To reduce resource wastage and improve user experience, this paper presents SMO, a self-managed orchestration system for microservices. SMO leverages a self-stabilizing placement mechanism to optimally deploy microservices through perceiving both interferences and communication overheads. During runtime, it further tailors a multi-agent deep deterministic policy gradient (MADDPG)-based model in combination with attention and prioritized replay, which automatically provisions appropriate resources for each microservice subject to the differentiated tail latency Service Level Objectives (SLOs) of multiple user workloads. Experimental results demonstrate that SMO saves up to 39% of CPU cores and 47% of memory footprint while providing guarantees for heterogeneous tail latency SLOs. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0840.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
