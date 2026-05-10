---
id: paper-2419
title: Architecture and Application Path for On-Device Deployment of Aviation Large Vision Models
authors:
- Zhang, Xilin
- Liu, Bo
- Du, Ziliang
- Shao, Yang
venue: 8th International Conference on Pattern Recognition and Artificial Intelligence, PRAI 2025
venue_type: conference
year: 2025
doi: 10.1109/PRAI67447.2025.11412453
url: https://www.scopus.com/pages/publications/105034060952?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 368--372
keywords:
- artificial intelligence
- aviation
- large vision models
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
    my_justification: LLM as workload
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

# paper-2419 — Architecture and Application Path for On-Device Deployment of Aviation Large Vision Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advancement of edge computing technology, aviation vision tasks demand higher real-time performance, privacy, and resource adaptability. This paper addresses the on-device deployment challenges of aviation large vision models by designing a task-oriented architecture and optimization path. The architecture introduces a data flow-model flow separation mechanism combined with modular design principles, significantly enhancing the flexibility of model updates and system maintenance. For model optimization, structured pruning, mixed-precision quantization, and knowledge distillation are comprehensively employed to enable efficient operation of large vision models such as Vision Transformer (ViT), Segment Anything Model (SAM), and Contrastive Language-Image Pre-Training(CLIP) on resource-constrained edge devices. Through analysis of typical application scenarios, the proposed system demonstrates advantages in real-time performance, accuracy, and energy efficiency. Additionally, this paper presents an intelligent Agent-based deployment strategy, providing a unified framework for rapid adaptation and evolution of multi-task aviation vision systems. The research offers a systematic solution for edge intelligence deployment of large vision models in the aviation domain, with significant engineering and academic value. © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2419.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
