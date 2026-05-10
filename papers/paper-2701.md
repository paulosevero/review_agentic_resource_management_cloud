---
id: paper-2701
title: 'TiPE-SAM: Tiny and Parameter-Efficient SAM for Edge Medical Image Segmentation with Mixture-of-Shape-Experts Priors'
authors:
- Lv, Xingguo
- Li, Ningshu
- Zhao, Lei
- Xu, Kai
- Lin, Qika
- Zhu, Yifan
- Zhang, Chuan
- Pu, Bin
venue: IEEE Transactions on Artificial Intelligence
venue_type: journal
year: 2026
doi: 10.1109/TAI.2026.3665493
url: https://www.scopus.com/pages/publications/105030703364?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge computing
- Medical image segmentation
- Parameter-efficient fine-tuning
- Vision Foundation Model
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

# paper-2701 — TiPE-SAM: Tiny and Parameter-Efficient SAM for Edge Medical Image Segmentation with Mixture-of-Shape-Experts Priors

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Medical image segmentation is a foundational component of numerous clinical measurement and quantitative analysis pipelines. However, deploying foundation models such as the Segment Anything Model (SAM) on clinical edge devices is hindered by stringent computational and memory constraints: their large model size renders full fine-tuning impractical, and existing efficient variants rarely incorporate anatomical priors or optimize for device-level resource budgets. We propose TiPESAM (Tiny, Parameter-Efficient SAM for Edge Devices), which augments a frozen SAM encoder with a shape-based mixture-of-experts prior, low-rank adaptation, and resource-aware execution. A learned dictionary of shape experts and a pixelwise gating network reconstruct a low-resolution shape map that is re-encoded as a dense structural prompt and fused with encoder tokens for the SAM decoder. To satisfy edge constraints, we define multiple execution profiles with device-specific costs and train a cost-aware routing network that trades off segmentation accuracy and expected computation. On multicenter echocardiographic segmentation benchmarks, TiPE-SAM matches or surpasses SAM-based baselines with only ~0.5M trainable parameters (less than 1% of the ViT-B) and provides explicit control over parameter and inference budgets, enabling resource-efficient deployment of medical foundation models. © 2020 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2701.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
