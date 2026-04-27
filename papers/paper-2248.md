---
id: "paper-2248"
title: "ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation"
authors: ["Wan, Zeyun", "Fan, Shichao", "Zhao, Huan", "Liu, Jiawei", "Chen, Ying"]
year: 2025
venue: "Neurocomputing"
venue_type: "journal"
doi: "10.1016/j.neucom.2025.130154"
url: "https://www.scopus.com/pages/publications/105002116396?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["CLIP", "GPT", "Text to 3D shape generation"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Out of scope"

---

# paper-2248 — ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation

## Metadata

- **Authors:** Wan, Zeyun and Fan, Shichao and Zhao, Huan and Liu, Jiawei and Chen, Ying
- **Year:** 2025
- **Venue:** Neurocomputing
- **DOI:** 10.1016/j.neucom.2025.130154
- **URL:** https://www.scopus.com/pages/publications/105002116396?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** CLIP; GPT; Text to 3D shape generation

### Abstract

Many recent works have attempted to generate 3D shapes from textual prompts. However, some of these methods are limited by high computational demands and slow optimization speeds, while others are constrained by the lack of sufficient detail, color, and texture in the generated results. This article proposes a method for rapidly generating high-fidelity 3D point clouds with color and texture based on textual prompts. The method consists of two stages: in the first stage, we generate voxels based on the textual prompts, and in the second stage, we refine the generated voxels into point clouds with enhanced geometric details and generate colors for them. During the voxel generation stage, we innovatively treat voxels as a form of “shape language” and propose ShapeGPT, a text-conditional voxel generative model based on GPT. It fully leverages the excellent generative capabilities of the language model, enabling the generation of high-fidelity and diverse voxels without the need for text-3D shape pairs as training data. Furthermore, we introduce PointPainter to upsample voxels into high-resolution dense point clouds and add colors and textures to the point clouds based on textual prompts. When generating color and texture, we use a newly proposed differentiable renderer to render the point clouds into images from multiple viewpoints and match the rendered images with the target text using the CLIP model. PointPainter not only generates intricate textures for point clouds but also achieves a fast optimization speed. Extensive experimental results demonstrate that our approach outperforms the state-of-the-art methods in terms of generative quality and consistency with the input text. © 2025 Elsevier B.V.

## 04 — Title Screening

**Title:** ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation
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
