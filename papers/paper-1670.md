---
id: paper-1670
title: Inference method for power large-scale model operation based on distributed computing resource scheduling
authors:
- Huang, Xiaoguang
- Qin, Yu
- Liu, Yaqing
- Cui, Yingbao
- Guo, Ting
- Gu, Qingtong
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2025
doi: 10.1117/12.3059877
url: https://www.scopus.com/pages/publications/105000499205?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- distributed computing power resources
- large-scale power models
- model inference
- resource scheduling
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1670 — Inference method for power large-scale model operation based on distributed computing resource scheduling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Electric power computing resources are distributed in the respective regions of provincial data centers and transmission and transformation equipment, and the scheduling efficiency of computing resources is limited by conditions such as long distribution locations. Composite data model inference has been widely used in power equipment maintenance analysis, and large-scale model inference requires the use of distributed computing resources. In order to improve the scheduling and fusion efficiency of distributed computing power resources, this paper adopts a lightweight language model to infer and calculate the scheduling parameters of computing power resources in different regions. At the same time, in order to make more rational use of computing power resources, the intelligent models and algorithms used for power equipment maintenance are optimized. Configure the adaptation parameters of the model according to different application scenarios, and adjust the fusion method of input data for the fault diagnosis model and the classification strategy for the fault prediction model separately. Using a fine-tuning language model to map the predicted results to the semantics of power business, and then enhancing the rationality and interoperability of the answer results based on historical knowledge memory, ultimately pushing the reasoning results of the reasons and the classification results of the equipment defect diagnosis classifier to the equipment diagnosis designer. © 2025 SPIE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1670.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
