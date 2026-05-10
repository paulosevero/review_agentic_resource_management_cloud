---
id: paper-1799
title: GNN-based Inspection UAV-assisted Computing Task Scheduling Method for Power Networks
authors:
- Li, Hanyu
- Xie, Kun
- Huang, Xiaohong
- Zhao, Jialu
venue: 8th World Conference on Computing and Communication Technologies, WCCCT 2025
venue_type: conference
year: 2025
doi: 10.1109/WCCCT65447.2025.11027945
url: https://www.scopus.com/pages/publications/105009053325?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 498--504
keywords:
- Computing Task Scheduling
- Graph Neural Network
- Multi-Agent Reinforcement Learning
- Power Data Network
- UAV-Assisted Power Grid Inspection
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

# paper-1799 — GNN-based Inspection UAV-assisted Computing Task Scheduling Method for Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern power systems impose dual challenges on data networks: increasing computational tasks and stringent low-latency requirements. Traditional cloud computing struggles to meet these real-time demands in power IoT, whereas edge computing and UAV-assisted offloading offer promising alternatives. This paper proposes an inspection UAV-assisted task scheduling method to enhance grid terminal throughput and fairness while reducing system energy consumption via optimized resource allocation and path selection. We develop a scheduling architecture integrating multiple UAVs and grid terminals, and formulate a joint optimization problem balancing energy consumption, throughput, and fairness. To solve this, we introduce DGDCMM - a multi-agent reinforcement learning algorithm that combines a Double-layer Graph Attention Network with a Discrete Communication Model. UAVs process local observations through a Feature Extraction Network (FEN) and share information via a Discrete Communication Network (DCN) under centralized training with distributed execution. Simulation results show that DGDCMM outperforms baseline methods in overall throughput, resource uniformity, and energy efficiency.  © 2025 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1799.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
