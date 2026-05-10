---
id: paper-1557
title: 'ELLIE: Energy-Efficient LLM Inference at the Edge Via Prefill-Decode Splitting'
authors:
- Fan, Haoyang
- Lin, Yi-Chien
- Prasanna, Viktor
venue: Proceedings of the International Conference on Application-Specific Systems, Architectures and Processors
venue_type: conference
year: 2025
doi: 10.1109/ASAP65064.2025.00031
url: https://www.scopus.com/pages/publications/105015603487?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 139--146
keywords:
- Edge inference
- Heterogeneous computing
- LLM
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1557 — ELLIE: Energy-Efficient LLM Inference at the Edge Via Prefill-Decode Splitting

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As Large Language Models (LLMs) are increasingly deployed for on-device applications, optimizing inference on edge platforms becomes critical. In real-world scenarios, LLM inference must satisfy diverse constraints and user requirements, such as low latency, high energy efficiency, or low Energy-Delay Product (EDP). Most state-of-the-art edge platforms, such as AI PCs and mobile SoCs, integrate heterogeneous processing units, including CPUs, GPUs, and Neural Processing Units (NPUs), each with distinct performance and power characteristics. However, existing approaches often adopt static mapping to a single processing unit (e.g., CPU, GPU, or NPU) and perform optimizations for either latency or energy consumption. This limits their effectiveness in meeting the requirements of diverse application scenarios. Moreover, LLM inference consists of two distinct phases: a highly parallel, compute-intensive Prefill phase, and a sequential, memory-intensive Decode phase. These phases have different computational characteristics, and splitting them across suitable processing units can potentially yield better energy efficiency and EDP than static mapping. However, such improvements may not be realized in all cases, as the actual benefit depends on many factors, including prompt characteristics, the models used, and features of the target hardware. To address these challenges, we propose ellie, a lightweight inference framework for edge heterogeneous platforms that dynamically selects the optimal execution plan based on the usage scenario, LLM, hardware feature, and input prompt. ELLIE builds performance models by regressing latency and power from offline profiling data, and integrates it with a lightweight output token length predictor. At runtime, it estimates the latency and energy of candidate execution plans using the predicted output length and selects an optimized device mapping accordingly. We implement ellie on an Intel AI PC platform with integrated CPU, GPU, and NPU. On average, when optimizing for EDP, ELLIE reduces energy consumption by 1.8×, improves EDP by 1.5×, and achieves latency comparable to GPU-only inference, across diverse LLMs and prompt types. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1557.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
