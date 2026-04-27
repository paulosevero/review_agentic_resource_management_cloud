---
id: "paper-1551"
title: "Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices"
authors: ["Duong, Viet Hung", "Truong, Van Duy", "Dinh, Duy Khanh", "Vu, Huan", "Luong, Thien Van", "Nguyen, Tien Cuong"]
year: 2025
venue: "Proceedings - 2025 IEEE/CVF International Conference on Computer Vision Workshops, ICCV-W 2025"
venue_type: "conference"
doi: "10.1109/ICCVW69036.2025.00555"
url: "https://www.scopus.com/pages/publications/105035194200?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5322--5329"
keywords: ["Road Object Detection in Fish-Eye Cameras"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1551 — Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices

## Metadata

- **Authors:** Duong, Viet Hung and Truong, Van Duy and Dinh, Duy Khanh and Vu, Huan and Luong, Thien Van and Nguyen, Tien Cuong
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE/CVF International Conference on Computer Vision Workshops, ICCV-W 2025
- **DOI:** 10.1109/ICCVW69036.2025.00555
- **URL:** https://www.scopus.com/pages/publications/105035194200?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5322--5329
- **Language:** English
- **Keywords:** Road Object Detection in Fish-Eye Cameras

### Abstract

Deploying object detectors on fisheye cameras for smartcity surveillance requires coping with extreme lens distortion while meeting a strict real-time budget on resource-constrained edge GPUs. We present the first single-model pipeline that simultaneously exceeds the long-standing 60% F1 barrier and sustains 25 FPS on an NVIDIA Jetson AGX Orin. Our solution couples a data-centric augmentation strategy-barrel-transforming VisDrone imagery and harvesting high-quality pseudo-labels from Co-DETR-which lifts YOLO11m by +16.1 mAP over a COCO baseline, with large-scale pre-training on Objects365 that contributes a further +2 mAP. C++/TensorRT FP16 inference engine reduces end-to-end latency from 124.6 ms to 38.8 ms, ensuring stable real-time throughput. Under the AI City Challenge 2025 Track-4 metric, defined as the harmonic mean of F1 and FPS, the resulting model attains 63.42% F1 at 25 FPS, setting a new state of practice for real-time fisheye detection. These findings demonstrate that tightly integrating hardware-aware optimization, data augmentation and foundation-model distillation enables accurate and efficient fisheye object detection on edge devices. © 2025 IEEE.

## 04 — Title Screening

**Title:** Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Augmentation, Distillation and Optimization: A Practical Pipeline for Fisheye Object Detection on Edge Devices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
