---
id: paper-1133
title: 'LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators'
authors:
- Prieto-Sibaja, Luis D.
- Leon-Vega, Luis G.
- Leon-Vega, Indra
- Castro-Godinez, Jorge
- Cozzini, Stefano
venue: Proceedings of the IEEE Central America and Panama Convention, CONCAPAN
venue_type: conference
year: 2024
doi: 10.1109/CONCAPAN63470.2024.10933896
url: https://www.scopus.com/pages/publications/105005866600?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud Computing
- Edge Computing
- Field Programmable Gate Arrays
- Hardware Acceleration
- High Performance Computing
- Large Language Models
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
    my_justification: LLM as workload
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

# paper-1133 — LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) have emerged as the leading technique in Natural Language Processing due to their remarkable capabilities. These models are exceptionally complex, often utilising billions of parameters and consuming tens of gigabytes of memory unless optimised. Typically, LLMs are trained and accelerated using general-purpose Graphics Processing Units (GPUs), with a single inference potentially occupying an entire GPU. Consequently, cloud services may require hundreds of GPUs to deliver high-quality AI assistant services. This demand for extensive hardware acceleration allows exploring alternative architectures that offer improved execution time and energy efficiency.This study evaluates Field-Programmable Gate Arrays (FP-GAs), renowned for their flexibility and efficiency, to accelerate LLMs. We specifically compare the resource consumption and latency of two distinct architectures: layer and spatial accelerators. Analysing the Llama 2-7B model, we identified potential optimisation opportunities within its composition and operational graphs. Our most successful implementations demonstrate a performance improvement ranging from 1.37× to 10.98× over two AMD EPYC processors with 64 cores each. Moreover, our results indicate that, with further refinement, FPGAs have the potential to surpass GPU performance for LLM inference, showcasing their feasibility as a viable alternative for this demanding application. © 2024 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1133.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
