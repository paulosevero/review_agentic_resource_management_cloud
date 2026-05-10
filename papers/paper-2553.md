---
id: paper-2553
title: 'DACCA: Distributed Adaptive Cloud Continuum Architecture'
authors:
- Deligiannakis, Nektarios
- Papataxiarhis, Vassilis
- Loukeris, Michalis
- Hadjiefthymiades, Stathes
- Touloupou, Marios
- Ul Hassan, Syed Mafooq
- Herodotou, Herodotos
- Moustakas, Thanasis
- Bampis, Emmanouil
- Ioannidis, Konstantinos
- Michailidis, Iakovos T.
- Vrochidis, Stefanos
- Kosmatopoulos, Elias
- Romero Martínez, Francisco Javier
- Marín Pérez, Rafael
- Mousa, Amr
- Castellini, Jacopo
- Strasser, Pablo
venue: Future Internet
venue_type: journal
year: 2026
doi: 10.3390/fi18020074
url: https://www.scopus.com/pages/publications/105031099070?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- adaptive resource optimization
- cloud–edge–IoT continuum
- computing continuum
- distributed ledger technology
- distributed orchestration
- kubernetes-native architecture
- multi-agent reinforcement learning
- zero-trust security
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2553 — DACCA: Distributed Adaptive Cloud Continuum Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, the need for unified orchestration frameworks that can manage extremely heterogeneous, distributed, and resource-constrained environments has emerged due to the rapid development of cloud, edge, and IoT computing. Kubernetes and other traditional cloud-native orchestration systems are not built to facilitate autonomous, decentralized decision-making across the computing continuum or to seamlessly integrate non-container-native devices. This paper presents the Distributed Adaptive Cloud Continuum Architecture (DACCA), a Kubernetes-native architecture that extends orchestration beyond the data center to encompass edge and Internet of Things infrastructures. Decentralized self-awareness and swarm formation are supported for adaptive and resilient operation, a resource and application abstraction layer is established for uniform resource representation, and a Distributed and Adaptive Resource Optimization (DARO) framework based on multi-agent reinforcement learning is integrated for intelligent scheduling in the proposed architecture. Verifiable identity, access control, and tamper-proof data exchange across heterogeneous domains are further ensured by a zero-trust security framework based on distributed ledger technology. When combined, these elements enable increasingly autonomous workload orchestration, trading centralized control for adaptive, decentralized operation with enhanced interoperability, scalability, and trust. Thus, the proposed architecture enables self-managing and context-aware orchestration systems that support next-generation AI-driven distributed applications across the entire computing continuum. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2553.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
