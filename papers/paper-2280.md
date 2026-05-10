---
id: paper-2280
title: 'SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration'
authors:
- Wang, Huiyu
- Liu, Zhicheng
- Wang, Xiaofei
- Qiu, Chao
- Zhang, Cheng
- Wang, Wenyu
- Ye, Qianwen
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-2864-3_7
url: https://www.scopus.com/pages/publications/105002576903?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 75--87
keywords:
- Cloud-Edge Collaboration
- Diffusion Models
- Edge Intelligence
- Generative AI
- Model Inference
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

# paper-2280 — SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, the rapid rise of Artificial Intelligence Generated Content (AIGC) has been accompanied by a surge in demand for generative AI application services. This trend has not only driven the diversified deployment of large-scale models but also posed more significant challenges to the efficient inference of these models. Current computing solutions have struggled to solely keep pace with growing user demands, which results in insufferable latency and inefficient performance. Integrating cloud computing and edge computing for the inference process of large models is deemed a promising solution, while related resource scheduling issues are still pending. To address this challenge, we focus our research on diffusion models, a representative model in the field of generative artificial intelligence, and propose a cloud-edge collaborative framework to accelerate the inference pipeline of text-to-image diffusion models. Our optimization goal is to minimize the average completion time of inference tasks while maintaining image quality. Considering that the inference for each image is an iterative process, we propose a step clipping strategy to save and reuse intermediate results to reduce iterations, compressing the calculation amount of inference tasks. Above this, we design a task scheduling strategy using proximal policy optimization, which can make efficient resource decisions. Experiments demonstrate the superiority of our strategy over local execution, greedy task scheduling strategy, and learning-based task scheduling strategies. Compared with the three baselines, the average task completion time under different system configurations is reduced by 1.093 s, 1.024 s, and 0.481 s, respectively. © IFIP International Federation for Information Processing 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2280.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
