---
id: paper-1865
title: Accelerating LLM Inference on RISC-V Edge Devices via Vector Extension Optimization
authors:
- Liu, Zhilong
- Peng, Long
- Wang, Wenzhu
- Li, Ke
- Zeng, Binrui
- Yu, Jie
- Liu, Xiaodong
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-9869-1_43
url: https://www.scopus.com/pages/publications/105013060244?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 515--526
keywords:
- Inference Acceleration
- Large Language Models
- Operator Optimization
- RISC-V Vector
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
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

# paper-1865 — Accelerating LLM Inference on RISC-V Edge Devices via Vector Extension Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deployment of large language models (LLMs) on edge devices faces significant challenges due to limited computational resources, memory bandwidth, and strict power constraints. While RISC-V architecture offers advantages in edge computing through its modularity, scalability, and open-source ecosystem, the LLM inference framework llama.cpp struggle to leverage the full potential of the RISC-V Vector Extension (RVV), leading to suboptimal performance. This study has achieved efficient LLM deployment in resource-constrained environments by optimizing critical operators in the llama.cpp framework using RVV instructions. We first identify performance bottlenecks, such as the f16 vector dot product and layer normalization, through runtime profiling. These operators are then redesigned with RVV’s SIMD capabilities, including half-precision floating-point support via the "zvfh" extension, to maximize parallel computation. Experimental results on a RISC-V-based BananaPi BPI-F3 platform demonstrate substantial improvements: the Gemma-2-2B model achieves a 1.7 × speedup in prefill prompt processing and a 53% acceleration in token generation during decoding, while the larger Llama-3.1-8B model shows 36% and 19% improvements in prefill and decode phases, respectively. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1865.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
