---
id: paper-2775
title: Prediction-based GPU sharing for distributed training
authors:
- Shin, Changyong
- Go, Younghun
- Yoo, Yeonho
- Jeong, Jinwoo
- Hwang, Jaehyun
- Yang, Gyeongsik
- Yoo, Chuck
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2026.108413
url: https://www.scopus.com/pages/publications/105034268374?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cloud computing
- GPU Scheduling
- GPU Sharing
- Performance prediction
- Service level agreement
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2775 — Prediction-based GPU sharing for distributed training

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AbstractGPU sharing aims to enhance the efficiency of GPU utilization by running distributed deep learning training jobs concurrently. However, GPU sharing poses a significant challenge: the increase in job completion time (JCT) caused by interference between jobs is inconsistent, complicating job scheduling. Our experiments reveal that the degree of JCT increase varies by as much as  ∼ 3.7 × . While previous studies have analyzed this JCT inconsistency problem, none of them have been able to minimize the inconsistency. We propose TensorShare, a proactive GPU sharing technique that leverages a deep learning model to predict the extent of JCT increase. This study defines a new metric, called GPU SLA, which represents the upper threshold of JCT increase. TensorShare then introduces a novel scheduler that proactively identifies which jobs meet GPU SLA while minimizing the JCT increase. Our evaluation shows that TensorShare improves GPU SLA satisfaction rates by 26.1 × –47.3 ×  and reduces the JCT increase by 37%–60%. Furthermore, we evaluate TensorShare with large language models that are not included in training TensorShare’s prediction model, achieving  ∼ 7 ×  and  ∼ 10.3 ×  improvements in GPU SLA satisfaction and JCT inconsistency, respectively. © 2026 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC license. http://creativecommons.org/licenses/by-nc/4.0/

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2775.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
