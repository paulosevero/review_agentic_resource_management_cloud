---
id: paper-2483
title: 'EdgeDriver: optimising autonomous driving assistance with multi-LLM framework in cloud-edge computing environments'
authors:
- Zhu, Yitian
venue: International Journal of Vehicle Information and Communication Systems
venue_type: journal
year: 2025
doi: 10.1504/IJVICS.2025.147511
url: https://www.scopus.com/pages/publications/105011244049?origin=resultslist
publisher: Inderscience Publishers
pages: 285--298
keywords:
- AIGC
- autonomous driving
- large language models
- mobile edge network
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2483 — EdgeDriver: optimising autonomous driving assistance with multi-LLM framework in cloud-edge computing environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Autonomous driving technology has recently made significant strides, laying the groundwork for the future of transportation systems. This advancement is increasingly powered by the emergence of Large Language Models (LLMs), which have become a focal point of research due to their remarkable common sense and reasoning ability. However, the deployment of LLMs is challenged by their computationally intensive nature, making direct implementation on mobile devices impractical. In this paper, we introduce EdgeDriver, an autonomous driving assistance framework leveraging multiple Large Language Models (LLMs) within cloud-edge computing environments to optimise computational efficiency and service quality. The framework comprises three modules: Perception, Planning and Evaluation, which process real-world driving scenarios to generate driving suggestions. Experiments were conducted using the BBD-100K data set, evaluating the impact of model parameters and input lengths on service quality. Results indicate that a 14B parameter model with 150-word input texts achieves optimal performance, balancing accuracy and computational efficiency. The study concludes that the quality of driving assistance services depends on matching input lengths and model capabilities to real-world conditions, providing valuable insights for future smart transportation systems. Copyright © 2025 Inderscience Enterprises Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2483.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
