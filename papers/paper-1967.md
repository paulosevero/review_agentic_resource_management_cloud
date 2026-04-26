---
id: "paper-1967"
title: "Experimental Evaluation of Quantization Methods in Facial Recognition"
authors: ["Monteiro, Carlos Henrique", "Raphaloski, Evandro", "Matsubara, Edson Takashi"]
year: 2025
venue: "Proceedings - 2025 IEEE/SBC 37th International Symposium on Computer Architecture and High Performance Computing Workshops, SBAC-PADW 2025"
venue_type: "conference"
doi: "10.1109/SBAC-PADW69789.2025.00023"
url: "https://www.scopus.com/pages/publications/105030542935?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "108--115"
keywords: ["CelebA", "FaceNet", "LFW", "ONNX", "Quantization", "Torch", "TransFace", "VGGFace2"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1967 — Experimental Evaluation of Quantization Methods in Facial Recognition

## Metadata

- **Authors:** Monteiro, Carlos Henrique and Raphaloski, Evandro and Matsubara, Edson Takashi
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE/SBC 37th International Symposium on Computer Architecture and High Performance Computing Workshops, SBAC-PADW 2025
- **DOI:** 10.1109/SBAC-PADW69789.2025.00023
- **URL:** https://www.scopus.com/pages/publications/105030542935?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 108--115
- **Language:** English
- **Keywords:** CelebA; FaceNet; LFW; ONNX; Quantization; Torch; TransFace; VGGFace2

### Abstract

Quantization techniques are recognized for their effective in optimizing large language models. However, their application in smaller language models, such as those used for face recognition, is uncommon. In the field of facial recognition, these techniques can be utilized across a diverse range of settings, from API services in data centers to mobile application deployment. Smaller quantized models can reduce costs while maintaining a strong performance. However, their combination with facial recognition is uncommon. This study tested the impact of 8-bit quantization on embedding generation models for facial recognition. We compared two models: FaceNet (Inception-ResNet) and TransFace (Vision Transformer). We analyzed different precision formats (FP32 and INT8) and inference backends (Torch and ONNX) using datasets such as LFW, VGGFace2, and CelebA to evaluate the top-1 accuracy and cosine distance for similarity. The results show that FaceNet performs well under quantization, maintaining accuracy while reducing precision. In contrast, TransFace exhibited a significant decrease in performance. Quantizing embedding vectors can also reduce storage needs by up to 80% without much loss in performance. These findings support quantization as an effective strategy for optimizing models in resource-limited environments and enhancing facial recognition technology. ©2025 IEEE.

## 04 — Title Screening

**Title:** Experimental Evaluation of Quantization Methods in Facial Recognition

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Experimental Evaluation of Quantization Methods in Facial Recognition
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Experimental Evaluation of Quantization Methods in Facial Recognition
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
