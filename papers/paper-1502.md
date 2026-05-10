---
id: paper-1502
title: Real-time Image Generation Utilizing ARM SBC Architecture
authors:
- Culafic, Igor
- Popovic, Tomo
- Jovovic, Ivan
- Cakic, Stevan
venue: ISAS 2025 - 9th International Symposium on Innovative Approaches in Smart Technologies, Proceedings
venue_type: conference
year: 2025
doi: 10.1109/ISAS66241.2025.11101730
url: https://www.scopus.com/pages/publications/105014946064?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- computer vision
- CUDA optimization
- edge computing
- real-time image generation
- stable diffusion
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

# paper-1502 — Real-time Image Generation Utilizing ARM SBC Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Real-time image generation using artificial intelligence has traditionally been constrained by computational limitations on edge devices. This paper presents a novel implementation of real-time image generation on the Jetson Orin Nano platform using Stable Diffusion models. We demonstrate the feasibility of running computationally intensive generative AI models on resource-constrained ARM-based systems while maintaining acceptable performance metrics. Our system processes live camera input and generates corresponding AIenhanced images in real-time. Unlike prior implementations focused on desktop systems, our work provides innovative solutions for ARM architecture, enabling practical applications in real-time environments while achieving frame rates of 2-6 FPS at 512 × 512 resolution. Through comprehensive performance analysis, we identify optimal operating parameters and critical thresholds for maintaining image quality while maximizing processing speed. The results demonstrate successful deployment of state-of-the-art generative models on edge devices, providing valuable insights for future edge AI applications in computer vision and real-time image processing. These results highlight the potential of low-power systems to contribute to decentralized highperformance computing frameworks. This opens new pathways for deploying advanced generative models in latency-sensitive, infrastructure-limited, or privacy-critical environments. © 2025 IEEE.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1502.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
