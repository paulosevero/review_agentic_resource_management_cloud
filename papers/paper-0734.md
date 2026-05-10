---
id: paper-0734
title: Knowledge Distillation with Source-free Unsupervised Domain Adaptation for BERT Model Compression
authors:
- Tian, Jing
- Chen, Juan
- Chen, Ning Jiang
- Bai, Lin
- Huang, Suqun
venue: Proceedings of the 2023 26th International Conference on Computer Supported Cooperative Work in Design, CSCWD 2023
venue_type: conference
year: 2023
doi: 10.1109/CSCWD57460.2023.10152760
url: https://www.scopus.com/pages/publications/85164711590?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1766--1771
keywords:
- BERT Model
- Knowledge Distillation
- Model Compression
- Unsupervised Domain Adaptation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0734 — Knowledge Distillation with Source-free Unsupervised Domain Adaptation for BERT Model Compression

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The pre-training language model BERT has brought significant performance improvements to a series of natural language processing tasks, but due to the large scale of the model, it is difficult to be applied in many practical application scenarios. With the continuous development of edge computing, deploying the models on resource-constrained edge devices has become a trend. Considering the distributed edge environment, how to take into account issues such as data distribution differences, labeling costs, and privacy while the model is shrinking is a critical task. The paper proposes a new BERT distillation method with source-free unsupervised domain adaptation. By combining source-free unsupervised domain adaptation and knowledge distillation for optimization and improvement, the performance of the BERT model is improved in the case of cross-domain data. Compared with other methods, our method can improve the average prediction accuracy by up to around 4% through the experimental evaluation of the cross-domain sentiment analysis task.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0734.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
