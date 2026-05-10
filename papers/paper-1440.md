---
id: paper-1440
title: Design and Optimization for AI/ML Acceleration on Resource-constrained and Edge Systems
authors:
- Boukhobza, Jalil
- Burrello, Alessio
- Chang, Yuan-Hao
- Li, Yawei
- Pagliari, Daniele Jahier
- Wu, Chun-Feng
- Yang, Ming-Chang
- Yang, Tsun-Yu
venue: Proceedings - 2025 International Conference on Compilers, Architecture, and Synthesis for Embedded Systems, CASES 2025
venue_type: conference
year: 2025
doi: 10.1145/3742872.3758334
url: https://www.scopus.com/pages/publications/105026929080?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1--10
keywords:
- ANN
- DNN
- Edge AI
- GMM
- graph processing
- heterogeneous computing
- I/O bottleneck
- K-means
- KV cache
- Memory
- RAG
- Storage
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from:
    - boukhobza2025special
    merge_reason: duplicate DOI
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1440 — Design and Optimization for AI/ML Acceleration on Resource-constrained and Edge Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of AI (from foundational machine learning to Large Language Models) and edge computing has placed unprecedented demands on computation, memory, and storage on resource-constrained edge devices. As AI models scale, the ability to efficiently manage computing resources, utilize memory and storage, and reduce energy consumption has become critical. This paper introduces contributions on 4 topics related to deploying AI on resource-constrained edge devices: 1) unlocking training of foundational machine learning algorithms on the edge, 2) exploring hardware-Aware DNN architecture and mapping co-optimization for inference on heterogeneous systems, 3) scaling RAG by leveraging advanced memory, storage, and energy-efficient designs, and 4) investigating cost-effective and high-performance large-scale graph processing.  © 2025 ACM.

**Dedup notes**

merged from: ['boukhobza2025special']

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1440.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
