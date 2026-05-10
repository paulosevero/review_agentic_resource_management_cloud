---
id: paper-1765
title: 'Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System'
authors:
- Latif, Imran
- Newkirk, Alex C.
- Carbone, Matthew R.
- Munir, Arslan
- Lin, Yuewei
- Koomey, Jonathan
- Yu, Xi
- Dong, Zhihua
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3554728
url: https://www.scopus.com/pages/publications/105003088186?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 61740--61747
keywords:
- AI training
- GPU power measurements
- large language models
- sustainable computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1765 — Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The expansion of artificial intelligence (AI) applications has driven substantial investment in computational infrastructure, especially by cloud computing providers. Quantifying the energy footprint of this infrastructure requires models parameterized by the power demand of AI hardware during training. In this work, we measured the instantaneous power draw of an 8-GPU NVIDIA H100 HGX node during the training of open-source image classifier (ResNet) and large-language models (Llama2-13b). We characterize power demand for a single node configuration, providing foundational data for future multi-node studies. The maximum observed power draw was approximately 8.4 kW, 18% lower than the manufacturer-rated 10.2 kW, even with GPUs near full utilization. Holding model architecture constant, increasing batch size from 512 to 4096 images for ResNet reduced total training energy consumption by a factor of 4. These findings can inform capacity planning for data center operators and energy use estimates by researchers. Future work will investigate the impact of cooling technology and carbon-aware scheduling on AI workload energy consumption. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1765.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
