---
id: paper-0411
title: 'Titan: A Scheduler for Foundation Model Fine-tuning Workloads'
authors:
- Gao, Wei
- Sun, Peng
- Wen, Yonggang
- Zhang, Tianwei
venue: SoCC 2022 - Proceedings of the 13th Symposium on Cloud Computing
venue_type: conference
year: 2022
doi: 10.1145/3542929.3563460
url: https://www.scopus.com/pages/publications/85143255760?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 348--354
keywords:
- cluster management system
- deep learning training
- foundation models
- GPU datacenter
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

# paper-0411 — Titan: A Scheduler for Foundation Model Fine-tuning Workloads

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The recent breakthrough of foundation model (FM) research raises a new trend to acquire efficient DL models by fine-tuning FMs with low-resource datasets. Current GPU clusters are mainly established to develop DL models by training from scratch. How to tailor a GPU cluster scheduler for FM fine-tuning workloads is still not explored. We propose Titan, a scheduler to improve the efficiency of FM fine-tuning workloads based on their three distinct features. (1) It takes full advantage of the fixed model structure to estimate the job duration accurately and configure the fine-tuning workload efficiently. (2) The multi-task adaptivity of FMs enables multiple fine-tuning workloads to share the same model parameters, which can significantly reduce the GPU resource consumption. (3) It considers the pipeline parallelism of FM fine-tuning workloads and concurrently executes the parameter transmission and gradient computation to hide the overhead of context switch. Preliminary simulation result validates the efficiency of Titan.  © 2022 Owner/Author.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0411.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
