---
id: paper-0631
title: Secure Distributed Storage Orchestration on Heterogeneous Cloud-Edge Infrastructures
authors:
- Kontodimas, Konstantinos
- Soumplis, Polyzois
- Kretsis, Aristotelis
- Kokkinos, Panagiotis
- Feher, Marcell
- Lucani, Daniel E.
- Varvarigos, Emmanouel
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2023
doi: 10.1109/TCC.2023.3287653
url: https://www.scopus.com/pages/publications/85162926320?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3407--3425
keywords:
- cloud-edge continuum
- data availability
- data security
- Distributed storage
- erasure coding
- resource allocation
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

# paper-0631 — Secure Distributed Storage Orchestration on Heterogeneous Cloud-Edge Infrastructures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Distributed storage systems spanning across different cloud data centers have substantially improved availability and flexibility for data storage and retrieval operations. However, stringent latency requirements of emerging applications necessitate optimized selection of storage resources that exhibit smaller delay. Introducing edge resources into distributed storage systems enables data placement closer to its source, but simultaneously increases the complexity of decision-making and orchestration processes for optimal data placement. In this work, we develop mechanisms for storing data across an infrastructure that includes both edge and cloud resources. Our approach focuses on optimizing data integrity, longevity, security, and cost, while leveraging erasure coding when performing the resource allocation. We first present a comprehensive mixed integer linear programming formulation of the storage resource orchestration problem. As the search space for the optimal solution can be vast and the execution time prohibitively large for real size problems, we also propose an innovative multi-Agent heuristic approach that uses the rollout, a reinforcement based policy, to balance performance and execution time efficiently. Through various simulation experiments, we evaluate the developed mechanisms and trade-offs involved in our approach. By incorporating data from a multi-cloud provider, we further enhance the validity of the simulations and the conclusions drawn.  © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0631.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
