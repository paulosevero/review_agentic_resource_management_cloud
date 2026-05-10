---
id: paper-1027
title: 'Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference'
authors:
- Li, Cong
- Xu, Yutao
venue: Proceedings of the 17th ACM International Systems and Storage Conference, SYSTOR 2024
venue_type: conference
year: 2024
doi: 10.1145/3688351.3689153
url: https://www.scopus.com/pages/publications/85206848613?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 53--67
keywords:
- knowledge-driven optimization
- language model inference
- matrix multiplication
- memory-bound
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

# paper-1027 — Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The majority of the latency in large language model inference lies in a few memory-bound matrix multiplication kernels. Traditionally, those kernels are optimized by extensive offline experiments of different tiling, striding, and slicing parameter choices on the target hardware. Scaling to different models, inference settings, and GPU hardware then becomes difficult. In this paper, we propose Foreseer, a new policy to generate the high-performing parameters for different kernels on the fly without offline experiments on the hardware. Foreseer leverages the specific characteristics of memory-bound matrix multiplication kernels, and synthesizes various prior knowledge such as keeping the adequate memory access pressure, avoiding the potential tail effect from load imbalance in dispatching, etc., into a simple penalty function. For a given parameter choice, Foreseer provides an analytical estimation of the impacting factors such as the memory access pressure, the potential tail effect, etc., to score the choice. A high-performing parameter choice is then discriminated from the penalty function. Micro-benchmarks of matrix multiplication kernels from popular language models on two different high-end Intel Data Center GPUs demonstrate that Foreseer outperforms different baselines including the vendor libraries, achieving >90% of the best-known performance obtained from the exhaustive offline parameter search experiments. End-to-end inference experiments on those language models with different settings also show that Foreseer accelerates the baseline by 20% on average, being competitive with and quite often exceeding the performance of the comprehensively-optimized vendor inference engine. © 2024 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1027.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
