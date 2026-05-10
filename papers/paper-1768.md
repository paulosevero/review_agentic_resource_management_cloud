---
id: paper-1768
title: Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters
authors:
- Lehmann, Noah
- Groth, Christian
venue: 2025 3rd International Conference on Federated Learning Technologies and Applications, FLTA 2025
venue_type: conference
year: 2025
doi: 10.1109/FLTA67013.2025.11336462
url: https://www.scopus.com/pages/publications/105033519665?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 463--470
keywords:
- availability
- eviction
- kubernetes
- maintenance
- migration
- scheduling
- singleton
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

# paper-1768 — Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Maintaining service availability in heterogeneous, resource-constrained edge clusters remains a significant challenge, particularly when workloads depend on specialized hardware or cannot be interrupted without user impact. Existing Kubernetes scheduling and maintenance solutions often assume workload replication or statelessness, leaving a gap in handling singleton, hardware-bound, and user-interactive pods typical of many edge AI deployments. This paper identifies these gaps by surveying current approaches to node maintenance scheduling, pod eviction, and rescheduling, highlighting their limitations in heterogeneous and low-redundancy environments. To address these challenges, we propose a system that integrates a custom Kubernetes operator for defining maintenance windows with a controller responsible for patient, eviction-aware restarts and workload rescheduling. Our design introduces soft time constraints, respects hardware affinity, and minimizes disruption to critical workloads such as long-running ML training or interactive LLM services. By building on standard Kubernetes mechanisms with custom logic, the approach improves resilience and operational predictability. A prototype implementation accompanies this paper, and we conclude by outlining future directions including automation, adaptive scheduling, and maintenance strategies tailored to edge AI clusters. © 2025 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1768.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
