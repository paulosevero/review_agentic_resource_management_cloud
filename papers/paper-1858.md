---
id: paper-1858
title: Multi-Domain Computation-Aware Resource Slicing and Orchestration for 6G Programmable Converged Wireless-Optical Networks
authors:
- Lin, Shih-Chun
- Lin, Chia-Hung
- Subramaniam, Suresh
- Matsuura, Motoharu
- Hasegawa, Hiroshi
venue: Proceedings of IEEE/IFIP Network Operations and Management Symposium 2025, NOMS 2025
venue_type: conference
year: 2025
doi: 10.1109/NOMS57970.2025.11073629
url: https://www.scopus.com/pages/publications/105012221136?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Benchmarking
- Edge computing
- Fiber optic networks
- Mobile telecommunication systems
- Profitability
- Quality of service
- Reinforcement learning
- Telecommunication services
- Transparent optical networks
- Virtual reality
- Wireless networks
- End-to-end service
- In networks
- Mobile systems
- Multi-domains
- Network caching
- Network communications
- Network computations
- Servicelevel agreement (SLA)
- Stringents
- Wireless optical networks
- Augmented reality
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1858 — Multi-Domain Computation-Aware Resource Slicing and Orchestration for 6G Programmable Converged Wireless-Optical Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Six-generation mobile systems aim to support stringent end-to-end service-level agreements for diverse user applications simultaneously. This paper introduces novel multi-domain computation-aware resource slicing orchestration that jointly manages in-network communications, computation, and caching storage resources for multi-domain networking. It automatically programs wireless access, edge cloud, and regional/central cloud infrastructure to enable wireless-optical network virtualization. Specifically, a mobile virtual network operator's long-term profit maximization problem and two subproblems are formulated to slice wired and wireless infrastructure resources and assign user requests and contents to slices. Accordingly, a reinforcement learning-based slicing with greedy pre-caching is proposed, which automatically allocates in-network resources for dynamic wireless connectivity and supports real-time inferring with minimal user request signaling. Numerical results show that our solutions provide superior performance from both user and infrastructure perspectives, with 20% improved operator profits, 17% enhanced service provisioning rates, and 80% reduced delay when simultaneously serving augmented reality and large language model's quality demands. This innovation exploits a generalized rein-forcement learning approach to minimize the signaling overheads and computation complexity while agilely adapting to practical converged networks, thus benchmarking AI-driven multi-domain network slicing development.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1858.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
