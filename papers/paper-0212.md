---
id: paper-0212
title: Dynamic provisioning of resources based on load balancing and service broker policy in cloud computing
authors:
- Jyoti, Amrita
- Shrimali, Manish
venue: Cluster Computing
venue_type: journal
year: 2020
doi: 10.1007/s10586-019-02928-y
url: https://www.scopus.com/pages/publications/85064347105?origin=resultslist
publisher: Springer
pages: 377--395
keywords:
- Cloud computing
- Dynamic optimal load-aware service broker
- Dynamic resource allocation
- Mixed Integer Programming
- Multi-agent deep reinforcement learning
- Service Measurement Index
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

# paper-0212 — Dynamic provisioning of resources based on load balancing and service broker policy in cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic resource allocation is the key objective of the paper motivated due to a large number of user’s service request and increasing network infrastructure complexity. Load balancing and Service Broker Policy are taken as two main key areas for the dynamic provision of resources to the cloud user in order to meet the QoS requirement. While provisioning the resources, the conventional approaches degrade due to QoS performance limits such as time delay, energy, etc. To overcome those problems, we proposed a new approach to provide dynamic provisioning of resources based on load balancing and service brokering. Initially, the Multi-agent Deep Reinforcement Learning-Dynamic Resource Allocation (MADRL-DRA) is used in the Local User Agent (LUA) to predict the environmental activities of user task and allocate the task to the Virtual Machine (VM) based on priority. Next, a Load balancing (LB) is performed in the VM, which increases the throughput and reduces the response time in the resource allocation task. Secondly, the Dynamic Optimal Load-Aware Service Broker (DOLASB) is used in the Global User Agent (GUA) for scheduling the task and provide the services to the users based on the available cloud brokers (CBs). In the global agent, cloud brokers are the mediators between users and providers. The optimization problem in Global Agent (GA) is formulated by the programming of mixed integers, and Bender decomposition algorithm. The result of our proposed method is better as compared with the conventional techniques in terms of Execution Time, Waiting Time, Energy Efficiency, Throughput, Resource Usage, and Makespan. © 2019, Springer Science+Business Media, LLC, part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0212.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
