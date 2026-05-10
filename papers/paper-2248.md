---
id: paper-2248
title: ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation
authors:
- Wan, Zeyun
- Fan, Shichao
- Zhao, Huan
- Liu, Jiawei
- Chen, Ying
venue: Neurocomputing
venue_type: journal
year: 2025
doi: 10.1016/j.neucom.2025.130154
url: https://www.scopus.com/pages/publications/105002116396?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- CLIP
- GPT
- Text to 3D shape generation
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
    my_justification: Out of scope
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

# paper-2248 — ShapeGPT and PointPainter for fast zero shot text-to-3d point cloud generation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Many recent works have attempted to generate 3D shapes from textual prompts. However, some of these methods are limited by high computational demands and slow optimization speeds, while others are constrained by the lack of sufficient detail, color, and texture in the generated results. This article proposes a method for rapidly generating high-fidelity 3D point clouds with color and texture based on textual prompts. The method consists of two stages: in the first stage, we generate voxels based on the textual prompts, and in the second stage, we refine the generated voxels into point clouds with enhanced geometric details and generate colors for them. During the voxel generation stage, we innovatively treat voxels as a form of “shape language” and propose ShapeGPT, a text-conditional voxel generative model based on GPT. It fully leverages the excellent generative capabilities of the language model, enabling the generation of high-fidelity and diverse voxels without the need for text-3D shape pairs as training data. Furthermore, we introduce PointPainter to upsample voxels into high-resolution dense point clouds and add colors and textures to the point clouds based on textual prompts. When generating color and texture, we use a newly proposed differentiable renderer to render the point clouds into images from multiple viewpoints and match the rendered images with the target text using the CLIP model. PointPainter not only generates intricate textures for point clouds but also achieves a fast optimization speed. Extensive experimental results demonstrate that our approach outperforms the state-of-the-art methods in terms of generative quality and consistency with the input text. © 2025 Elsevier B.V.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2248.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
