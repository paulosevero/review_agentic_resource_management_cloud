---
id: paper-2602
title: 'An End-to-End Intelligent Control Architecture for 6G Networks: A Dual-SDN Approach With DRL, QNN and Cognitive Interface'
authors:
- Hechmi, Mohamed Amine
- Ben Rejeb, Sonia
- Tabbane, Sami
venue: IEEE Networking Letters
venue_type: journal
year: 2026
doi: 10.1109/LNET.2026.3652911
url: https://www.scopus.com/pages/publications/105028184214?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 110--114
keywords:
- 6G
- load balancing
- network slicing
- quantum neural networks
- reinforcement learning
- software-defined networking
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2602 — An End-to-End Intelligent Control Architecture for 6G Networks: A Dual-SDN Approach With DRL, QNN and Cognitive Interface

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> 6G networks require ultra-reliable, low-latency, and context-aware orchestration of heterogeneous resources spanning radio access and core domains. This letter proposes an end-to-end (E2E) intelligent architecture leveraging two cooperative SDN-based control planes: one at the Radio Access Network (SDN-RAN) and one at the Core Network (SDN-CN), interconnected via a cognitive East–West interface. The SDN-RAN integrates a DRL agent based on Proximal Policy Optimization (PPO) and Graph Neural Networks (GNN) for dynamic resource allocation and access mode switching (NOMA/RSMA). The SDN-CN, embedded within a Quantum-empowered RIC (Q-RIC), orchestrates virtualized core functions using DRL and Quantum Neural Networks (QNN). A digital twin supervises and simulates decisions in real time. Experimental scenarios show the model’s ability to ensure latency-sensitive service continuity, proactive load balancing, and coordinated migration toward MEC resources. © 2019 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2602.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
