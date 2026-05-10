---
id: paper-1632
title: 'Blockchain-Empowered Resource Allocation in HAPS-Assisted IoV Digital Twin Networks: A Federated DRL Approach'
authors:
- Hayla, Nahom Abishu
- Seid, Abegaz Mohammed
- Jhaveri, Rutvij H.
- Gadekallu, Thippa Reddy
- Erbad, Aiman
- Guizani, Mohsen
venue: IEEE Transactions on Intelligent Vehicles
venue_type: journal
year: 2025
doi: 10.1109/TIV.2024.3492015
url: https://www.scopus.com/pages/publications/105021578769?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4710--4726
keywords:
- Blockchain
- deep reinforcement learning
- digital twin
- double auction
- federated learning
- resource allocation
- smart vehicles
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1632 — Blockchain-Empowered Resource Allocation in HAPS-Assisted IoV Digital Twin Networks: A Federated DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is a new paradigm in smart cities with the potential to provide and manage resources such as computing and storage closer to resource-constrained smart vehicles (SV) to support ultra-reliable low-latency communications and knowledge sharing. However, it is challenging to make optimal resource allocation and offloading decisions due to the mobility, ubiquitous communications, and diverse resource demands of SVs and the dynamic nature of the vehicular network topology. In this paper, we propose an adaptive resource allocation and task offloading scheme for HAPS-assisted Internet of Vehicle networks by exploiting the potential of digital twins (DT), blockchain, and federated multi-agent deep reinforcement learning (FMADRL) technologies to address these issues. The DT network is utilized to intelligently monitor and control the demand and supply of resources in the digital representation of the physical operating environment. We adopt a dynamic pricing-based double auction to model the supplies and demands of resource providers and requesters. This enables resource providers and SVs to make adaptive and optimal resource allocation and task offloading decisions. In addition, we deploy a consortium blockchain to enable distributed and secure resource allocation. The resource allocation and task offloading multi-objective optimization problem is formulated as a multi-agent extension of the Markov decision process and solved using an FMADRL-based multi-agent deep deterministic policy gradient (FMADDPG) algorithm. The numerical results show that the proposed scheme archives efficient resource allocation and maximizes the utility function while minimizing costs compared to the baseline schemes.  © 2016 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1632.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
