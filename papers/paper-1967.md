---
id: paper-1967
title: Experimental Evaluation of Quantization Methods in Facial Recognition
authors:
- Monteiro, Carlos Henrique
- Raphaloski, Evandro
- Matsubara, Edson Takashi
venue: Proceedings - 2025 IEEE/SBC 37th International Symposium on Computer Architecture and High Performance Computing Workshops, SBAC-PADW 2025
venue_type: conference
year: 2025
doi: 10.1109/SBAC-PADW69789.2025.00023
url: https://www.scopus.com/pages/publications/105030542935?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 108--115
keywords:
- CelebA
- FaceNet
- LFW
- ONNX
- Quantization
- Torch
- TransFace
- VGGFace2
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1967 — Experimental Evaluation of Quantization Methods in Facial Recognition

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Quantization techniques are recognized for their effective in optimizing large language models. However, their application in smaller language models, such as those used for face recognition, is uncommon. In the field of facial recognition, these techniques can be utilized across a diverse range of settings, from API services in data centers to mobile application deployment. Smaller quantized models can reduce costs while maintaining a strong performance. However, their combination with facial recognition is uncommon. This study tested the impact of 8-bit quantization on embedding generation models for facial recognition. We compared two models: FaceNet (Inception-ResNet) and TransFace (Vision Transformer). We analyzed different precision formats (FP32 and INT8) and inference backends (Torch and ONNX) using datasets such as LFW, VGGFace2, and CelebA to evaluate the top-1 accuracy and cosine distance for similarity. The results show that FaceNet performs well under quantization, maintaining accuracy while reducing precision. In contrast, TransFace exhibited a significant decrease in performance. Quantizing embedding vectors can also reduce storage needs by up to 80% without much loss in performance. These findings support quantization as an effective strategy for optimizing models in resource-limited environments and enhancing facial recognition technology. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1967.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
