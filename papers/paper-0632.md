---
id: paper-0632
title: Cloud-Native Applications’ Workload Placement over the Edge-Cloud Continuum
authors:
- Kontos, Georgios
- Soumplis, Polyzois
- Kokkinos, Panagiotis
- Varvarigos, Emmanouel
venue: International Conference on Cloud Computing and Services Science, CLOSER - Proceedings
venue_type: conference
year: 2023
doi: 10.5220/0011850100003488
url: https://www.scopus.com/pages/publications/85160717107?origin=resultslist
publisher: Science and Technology Publications, Lda
pages: 57--66
keywords:
- Cloud-Native
- Edge-Cloud Continuum
- Multi-Agent Rollout
- Reinforcement Learning
- Resource Allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0632 — Cloud-Native Applications’ Workload Placement over the Edge-Cloud Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The evolution of virtualization technologies and of distributed computing architectures has inspired the so-called cloud native applications development approach. A cornerstone of this approach is the decomposition of a monolithic application into small and loosely coupled components (i.e., microservices). In this way, application’s performance, flexibility, and robustness can be improved. However, most orchestration algorithms assume generic application workloads that cannot serve efficiently the specific requirements posed by the applications, regarding latency and low communication delays between their dependent microservices. In this work, we develop advanced mechanisms for automating the allocation of computing resources, in order to optimize the service of cloud-native applications in a layered edge-cloud continuum. We initially present the Mixed Integer Linear Programming formulation of the problem. As the execution time can be prohibitively large for real-size problems, we develop a fast heuristic algorithm. To efficiently exploit the performance–execution time trade-off, we employ a novel multi-agent Rollout, the simplest and most reliable among the Reinforcement Learning methods, that leverages the heuristic’s decisions to further optimize the final solution. We evaluate the results through extensive simulations under various inputs that demonstrate the quality of the generated sub-optimal solutions. Copyright © 2023 by SCITEPRESS – Science and Technology Publications, Lda.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0632.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
