---
id: paper-1889
title: Microservice-Aware Deployment and Swarm Intelligence Cooperative Routing in Vehicle Edge Computing
authors:
- Liu, Chunhong
- Wang, Huaichen
- Zhou, Rui
- Liu, Jialei
- Yuan, Peiyan
- Cheng, Bo
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3590152
url: https://www.scopus.com/pages/publications/105011701952?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 21215--21231
keywords:
- microservices
- request routing
- service deployment
- swarm intelligence
- Vehicle edge computing
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

# paper-1889 — Microservice-Aware Deployment and Swarm Intelligence Cooperative Routing in Vehicle Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of vehicle edge computing (VEC) and microservice architectures improves real-time data processing and computational optimization in the Internet of Vehicles. Specifically, in high-traffic areas, the dynamic deployment and request routing of microservices with complex data dependencies within vehicle clusters can effectively reduce the computational load on edge devices. However, existing research has primarily focused on efficiently utilizing vehicular resources, overlooking the dynamic nature of vehicular cluster networks and the additional communication costs arising from data dependencies between microservices. Therefore, we propose a joint service deployment and request routing problem for vehicle collaboration. We first design a vehicle-road collaborative service framework assisted by temporary vehicle workers, expanding available resources and coverage by deploying microservice instances on selected temporary vehicle nodes. Second, recognizing the dependency between service deployment and request routing, we propose a dual-timescale service-deployment and request-routing policy. On a long timescale, a microservice-aware deployment method optimizes request selection and response time. On a short timescale, we propose a decentralized, swarm intelligence-based collaborative request routing method that constructs a response threshold model through agent interaction, thereby enhancing the collaborative optimization capability of the system. Finally, experimental results using real datasets show that our method outperforms other approaches in reducing request response time when communication costs are taken into account. © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1889.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
