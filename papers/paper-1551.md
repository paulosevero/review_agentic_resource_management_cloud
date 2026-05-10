---
id: paper-1551
title: 'Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices'
authors:
- Duong, Viet Hung
- Truong, Van Duy
- Dinh, Duy Khanh
- Vu, Huan
- Luong, Thien Van
- Nguyen, Tien Cuong
venue: Proceedings - 2025 IEEE/CVF International Conference on Computer Vision Workshops, ICCV-W 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCVW69036.2025.00555
url: https://www.scopus.com/pages/publications/105035194200?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5322--5329
keywords:
- Road Object Detection in Fish-Eye Cameras
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1551 — Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying object detectors on fisheye cameras for smartcity surveillance requires coping with extreme lens distortion while meeting a strict real-time budget on resource-constrained edge GPUs. We present the first single-model pipeline that simultaneously exceeds the long-standing 60% F1 barrier and sustains 25 FPS on an NVIDIA Jetson AGX Orin. Our solution couples a data-centric augmentation strategy-barrel-transforming VisDrone imagery and harvesting high-quality pseudo-labels from Co-DETR-which lifts YOLO11m by +16.1 mAP over a COCO baseline, with large-scale pre-training on Objects365 that contributes a further +2 mAP. C++/TensorRT FP16 inference engine reduces end-to-end latency from 124.6 ms to 38.8 ms, ensuring stable real-time throughput. Under the AI City Challenge 2025 Track-4 metric, defined as the harmonic mean of F1 and FPS, the resulting model attains 63.42% F1 at 25 FPS, setting a new state of practice for real-time fisheye detection. These findings demonstrate that tightly integrating hardware-aware optimization, data augmentation and foundation-model distillation enables accurate and efficient fisheye object detection on edge devices. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1551.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
