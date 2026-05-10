---
id: paper-2903
title: Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge
authors:
- Zhai, Yu
- Wei, Lili
venue: Electronics (Switzerland)
venue_type: journal
year: 2026
doi: 10.3390/electronics15010230
url: https://www.scopus.com/pages/publications/105027026575?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge computing
- lightweight semantic segmentation
- point machine inspection
- quantization and deployment
- vision-language model
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2903 — Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Existing inspection systems for railway point machines often suffer from high latency and poor interpretability, which impedes the real-time detection of critical mechanical anomalies, thereby increasing the risks of derailment and leading to cascading schedule delays. Addressing these challenges, this study proposes a lightweight computer vision-based detection framework deployed on the RK3588S edge platform. First, to overcome the accuracy degradation of segmentation networks on constrained edge NPUs, a Sensitivity-Aware Mixed-Precision Quantization and Heterogeneous Scheduling (SMPQ-HS) strategy is proposed. Second, a Multimodal Semantic Diagnostic Framework is constructed. By integrating geometric engagement depths—calculated via perspective rectification—with visual features, a Hard-Constrained Knowledge Embedding Paradigm is designed for the Qwen2.5-VL model. This approach constrains the stochastic reasoning of the Qwen2.5-VL model into standardized diagnostic conclusions. Experimental results demonstrate that the optimized model achieves an inference speed of 38.5 FPS and an mIoU of 0.849 on the RK3588S, significantly outperforming standard segmentation models in inference speed while maintaining high precision. Furthermore, the average depth-estimation error remains approximately 3%, and the VLM-based fault identification accuracy reaches 88%. Overall, this work provides a low-cost, deployable, and interpretable solution for intelligent point machine maintenance under edge-computing constraints. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2903.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
