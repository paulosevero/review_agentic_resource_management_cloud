---
id: paper-0723
title: Security-Aware Resource Allocation in the Edge-Cloud Continuum
authors:
- Soumplis, Polyzois
- Kontos, Georgios
- Kretsis, Aristotelis
- Kokkinos, Panagiotis
- Nanos, Anastassios
- Varvarigos, Emmanouel
venue: 2023 IEEE 12th International Conference on Cloud Networking, CloudNet 2023
venue_type: conference
year: 2023
doi: 10.1109/CloudNet59005.2023.10490073
url: https://www.scopus.com/pages/publications/85191254330?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 161--169
keywords:
- cloud edge continuum
- cloud-native applications
- resource allocation
- security
- workload isolation
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

# paper-0723 — Security-Aware Resource Allocation in the Edge-Cloud Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-native applications, comprised of multiple services, optimize their execution on the edge cloud continuum, by leveraging both edge for time-critical computations and the more distant (but abundant) cloud resources for time-driven computations. The infrastructure is controlled by a hierarchical orchestrator logic, with sub-modules at each level managing a specific set of resources. A crucial challenge in deploying applications over such a distributed infrastructure is the allocation of resources, considering jointly application-specific security requirements and computing and networking constraints, that increase significantly the complexity of the decision-making process. In this work, we assume varying levels of workload isolation achievable through lightweight virtualization mechanisms, establishing distinct tiers of security and trustworthiness, each with its own quantified computational and storage requirements. We model the respective resource allocation problem, i.e., of provisioning edge-cloud continuum resources for cloud-native applications subject to applications' performance and security requirements, as a Mixed Integer Linear Program. Additionally, a best-fit heuristic is introduced to reduce the execution time for real-size scenarios, performing a fast allocation of resources for the applications while maintaining a tolerable optimality gap. Finally, a Multi-agent Rollout Mechanism is proposed that trades off execution time with performance, leveraging the greedy heuristic for the approximation of future decisions in a Reinforcement Learning manner. Several simulation experiments were performed to showcase the effectiveness of the developed mechanisms, while simultaneously addressing the needs of conflicting objectives. © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0723.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
