---
id: paper-2764
title: 'Onboard Deployment of Remote Sensing Foundation Models: A Comprehensive Review of Architecture, Optimization, and Hardware'
authors:
- Sang, Hanbo
- Zhang, Limeng
- Chen, Tianrui
- Guo, Weiwei
- Zhang, Zenghui
venue: Remote Sensing
venue_type: journal
year: 2026
doi: 10.3390/rs18020298
url: https://www.scopus.com/pages/publications/105028667906?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge computing
- foundation model
- hardware accelerator
- model compression
- onboard deployment
- remote sensing
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
    agrees_with_regex: false
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

# paper-2764 — Onboard Deployment of Remote Sensing Foundation Models: A Comprehensive Review of Architecture, Optimization, and Hardware

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Highlights: What are the main findings? This review presents the first comprehensive survey on the deployment of remote sensing foundation models (RSFMs) on resource-constrained satellites for onboard computing. This review systematically covers a unified deployment pipeline, including RSFMs development, model optimization, and hardware analysis. What are the implications of the main findings? The onboard deployment of RSFMs is feasible and promising from the perspectives of memory, energy, and computation. This review serves as a practical roadmap for future research on the deployment of large-scale models on edge devices. With the rapid growth of multimodal remote sensing (RS) data, there is an increasing demand for intelligent onboard computing to alleviate the transmission and latency bottlenecks of traditional orbit-to-ground downlinking workflows. While many lightweight AI algorithms have been widely developed and deployed for onboard inference, their limited generalization capability restricts performance under the diverse and dynamic conditions of advanced Earth observation. Recent advances in remote sensing foundation models (RSFMs) offer a promising solution by providing pretrained representations with strong adaptability across diverse tasks and modalities. However, the deployment of RSFMs onboard resource-constrained devices such as nano satellites remains a significant challenge due to strict limitations in memory, energy, computation, and radiation tolerance. To this end, this review proposes the first comprehensive survey of onboard RSFMs deployment, where a unified deployment pipeline including RSFMs development, model compression techniques, and hardware optimization is introduced and surveyed in detail. Available hardware platforms are also discussed and compared, based on which some typical case studies for low Earth orbit (LEO) CubeSats are presented to analyze the feasibility of onboard RSFMs’ deployment. To conclude, this review aims to serve as a practical roadmap for future research on the deployment of RSFMs on edge devices, bridging the gap between the large-scale RSFMs and the resource constraints of spaceborne platforms for onboard computing. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2764.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
