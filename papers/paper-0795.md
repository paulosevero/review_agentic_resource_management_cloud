---
id: paper-0795
title: Research on resource allocation technology in highly trusted environment of edge computing
authors:
- Zhang, Yang
- Zhu, Kaige
- Zhao, Xuan
- Zhao, Quancheng
- Zhang, Zhenjiang
- Bashir, Ali Kashif
venue: Journal of Parallel and Distributed Computing
venue_type: journal
year: 2023
doi: 10.1016/j.jpdc.2023.03.011
url: https://www.scopus.com/pages/publications/85152128555?origin=resultslist
publisher: Academic Press Inc.
pages: 29--42
keywords:
- Edge computing
- Resource allocation
- Task offloading
- Trust model
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

# paper-0795 — Research on resource allocation technology in highly trusted environment of edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing can use many edge devices to provide users with real-time computing and storage functions. With the development of the Internet of Things (IOT), edge computing is becoming more and more prevalent currently. However, the consequent challenges in search efficiency, reliability requirements and resource allocation appear followed. Therefore, this article focuses on resource allocation and security performance issues. A lightweight trust evaluation mechanism was constructed and time-varying trust coefficients were introduced as incentives to address the problem of distrust between user terminals and edge server entities in multi-cell and multi-user scenarios. This enables the user terminal to immediately distinguish malicious servers. Considering the limited and dynamic changes of computing resources, the problem of complete migration of multi-user tasks was transformed into an issue of computing resource distribution to reduce the total system energy consumption. As a Markov game model, a system was developed to address the problems of centralized single-agent algorithms, including the explosion of action space and difficulty in convergence with increasing the number of users. Besides, a resource allocation algorithm was proposed based on a trust model and multi-agents that follows a centralized training and distributed implementation architecture. The simulated consequences indicated that the proposed algorithm resists malicious attacks, and can quickly make reasonable task migration decisions based on different system states, thereby efficiently decreasing the consumption of the total system energy, and providing a better user experience. © 2023 Elsevier Inc.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0795.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
