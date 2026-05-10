---
id: paper-1824
title: 'SimpleScale: Simplifying the Training of an LLM Model Using 1024 GPUs'
authors:
- Li, Tianfa
- Pan, Jingshan
- Ma, Siwei
- Raikov, Aleksandr
- Arkhipov, Alexander
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/app15158265
url: https://www.scopus.com/pages/publications/105013195766?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- dynamic hybrid shared strategy
- flash attention
- FSDP
- Slurm
- training
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

# paper-1824 — SimpleScale: Simplifying the Training of an LLM Model Using 1024 GPUs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> LLMs are trained using many thousands of GPUs in well-known conventional models. It is necessary to address numerous issues in the training process, such as manual data collection organization, data parallel, model parallel, evaluation, testing, deployment, transferring large data streams, detecting errors, ongoing maintenance, and project management. A team of dozens of engineers is required to handle system problems in the training process. Therefore, it is time-consuming and expensive to build an efficient and fault-tolerant system based on Kubernetes. This paper develops SimpleScale for building LLMs based on FSDP and Slurm, which is a simple and efficient training system that includes the training agent, the efficient parallel strategy, the optimal step of checkpoint, and so on. Using the proposed system enables us to significantly accelerate the process of building the LLM without incurring substantial time spent on various manual issues. The proposed 1024-GPU cluster was tested on TinyLlama, which has 1.1 billion parameters and 300 billion tokens. For example, utilizing a 16-H100 GPU cluster accelerated the traditional TinyLlama training time costs from 89.05 days to 39.05 days. In the future, the project team plans to integrate Flash-Attention3, aiming for an MFU of more than 60% while maintaining the acceleration achieved in the present work. © 2025 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1824.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
