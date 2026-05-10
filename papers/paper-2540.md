---
id: paper-2540
title: Survey on edge deployment and inference acceleration of multimodal large language models; [多模态大模型边缘部署与推理加速技术综述]
authors:
- Chen, Siru
- Shu, Yuanchao
venue: Zhejiang Daxue Xuebao (Gongxue Ban)/Journal of Zhejiang University (Engineering Science)
venue_type: journal
year: 2026
doi: 10.3785/j.issn.1008-973X.2026.04.005
url: https://www.scopus.com/pages/publications/105034025107?origin=resultslist
publisher: Zhejiang University
pages: 723--737
keywords:
- edge computing
- edge-cloud collaboration
- inference acceleration
- model architecture optimization
- multimodal large language models
- system-level optimization
language: Chinese
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2540 — Survey on edge deployment and inference acceleration of multimodal large language models; [多模态大模型边缘部署与推理加速技术综述]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Significant progress in multimodal large language models (MLLMs) has driven advances in visual question answering, visual understanding, and reasoning tasks, and their potential for deployment on resource-constrained edge devices is increasingly recognized. However, large model sizes and the substantial costs of deployment and inference remain major barriers to practical adoption. Optimizing MLLMs for edge devices has become a critical research direction in this field. A comprehensive survey of recent advances in optimizing MLLMs for edge deployment was presented, along with the associated challenges and development trends. The research evolution of MLLMs on edge devices was reviewed, with particular emphasis on model architecture optimization and inference scheduling strategies. In model architecture optimization, techniques including visual information compression, sparse attention, and mixture-of-experts models were specifically analyzed. System-level optimizations involving computation scheduling, hardware adaptation, compilation optimization, and cloud-edge collaboration were investigated to enhance inference efficiency and energy efficiency. Furthermore, the key challenges of these models in practical applications were discussed, and a variety of task scenarios ranging from assistive to collaborative and autonomous types were covered, categorized by the perspective of autonomy levels. Finally, current limitations were summarized and future research directions regarding standardized deployment, efficient computing and storage, and multi-modal fusion optimization were outlined. © 2026 Zhejiang University. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2540.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
