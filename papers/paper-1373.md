---
id: paper-1373
title: 'Divide and Compute: Distributed Model Offloading for Computation'
authors:
- Akhilesh, M.K.
- Bharadwaj, Abhinav R
- Prabhu, Nandan N
- Abhiram, H.K.
- Auradkar, Prafullata K
venue: 2025 10th International Conference on Big Data Analytics, ICBDA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICBDA65366.2025.11211291
url: https://www.scopus.com/pages/publications/105023836576?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 263--268
keywords:
- distributed computing
- fault tolerance
- IoT
- machine learning
- model offloading
- pipeline parallelism
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

# paper-1373 — Divide and Compute: Distributed Model Offloading for Computation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) and deep learning models generally demand high computational resources, particularly GPUs, which are expensive and energy-intensive. This reliance on specialized hardware restricts the availability and scalability of these models for real-Time applications, especially in resource constrained environments. In this paper, we present a novel approach that distributes the inference of LLMs and deep learning models across a cluster of heterogeneous edge devices. By partitioning and deploying models onto edge devices, it utilizes the aggregate computing power to do inference in an efficient manner. Pipeline parallelism is utilized to split the models layerwise, hence ensuring optimal assignment of computational tasks among the edge devices. It thereby enables inference of complex models in locations where conventional hardware configurations cannot be afforded, thereby reducing cost expenditure without sacrificing the inference accuracy. This approach shows how edge computing can democratize access to powerful models in real time, on demand AI inference at any location. which allows for the deployment of powerful models at any place with minimum infrastructures. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1373.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
