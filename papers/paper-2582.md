---
id: paper-2582
title: 'MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems'
authors:
- Ghosh, Aswini
- Sharma, Nelson
- Mishra, Shivendu
- Misra, Rajiv
- Das, Sajal K.
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2025.3632862
url: https://www.scopus.com/pages/publications/105021668238?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 477--490
keywords:
- Internet of Things
- mobility aware edge computing
- offloading
- sequence to sequence deep Q-learning
- transformer
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

# paper-2582 — MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobility introduces significant challenges for optimal computation offloading, latency minimization, and efficient resource utilization in multi-access edge computing (MEC) systems. A key difficulty lies in leveraging real user trajectories to jointly optimize horizontal (inter-edge) and vertical (edge-to-cloud) task offloading decisions. This paper proposes a two-dimensional offloading scheme for a multi-layer edge–cloud architecture that enables collaborative task execution among resource-constrained edge nodes under mobility conditions. We present MGCO (Mobility-Aware Generative Computation Offloading), a generative AI–driven Transformer-based sequence-to-sequence Deep Q-Network (s2s-DQN) framework that learns from real-time trajectory data to anticipate user movement and optimize task placement dynamically. The Transformer architecture is adopted because its multi-head self-attention effectively captures long-range dependencies in mobility and task-demand patterns while avoiding vanishing gradients and sequential bottlenecks inherent to LSTM/GRU models. This design enables parallel contextual reasoning and stable autoregressive action generation, supporting real-time offloading decisions within strict operational latency constraints. Experimental results demonstrate that MGCO consistently outperforms existing methods, achieving up to 41.61% reduction in turnaround time compared to GASTO, and substantial improvements over DMQTO and HMAOA, reaching up to 645.40% and 751.90%, respectively, for longer prediction horizons (48 time slots of 5 seconds each). These results highlight MGCO’s robustness, scalability, and effectiveness in managing complex mobility scenarios in dynamic edge–cloud environments. © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2582.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
