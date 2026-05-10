---
id: paper-2431
title: Energy Efficient GPU Frequency Scaling Policy for Inference Serving using Queue Model
authors:
- Zhang, Yuhao
- Zhang, Wenqian
- Huang, Xiaowen
- Zhang, Guanglin
venue: 2025 International Conference on Sensor-Cloud and Edge Computing System, SCECS 2025
venue_type: conference
year: 2025
doi: 10.1109/SCECS65243.2025.11065043
url: https://www.scopus.com/pages/publications/105012241925?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 57--62
keywords:
- Dynamic Voltage and Frequency Scaling
- Edge Computing
- Energy Efficiency
- LLM Inference
- Queue Model
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2431 — Energy Efficient GPU Frequency Scaling Policy for Inference Serving using Queue Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of intelligent applications driven by large language models (LLMs) has significantly increased computational demands on cloud/edge computing infrastructures. These centers are commonly equipped with Graphics Processing Unit (GPU) to meet the high computational demands of LLMs. However, the substantial power consumption of GPUs poses a critical challenge in optimizing data center energy consumption without compromising task latency. In this paper, we propose QEEFS, a Queue-Theory-based Energy-Efficient Frequency Scaling policy to address the trade-off between latency and energy consumption in LLM inference processes. Specifically, we model the LLM inference server as a M/G(r, f)/1/N queue, capturing the stochastic nature of inference requests and predicting average service time under various server configurations. QEEFS optimizes GPU operating frequencies through offline profiling and online probing phases, making use of DVFS technology to dynamically control the energy consumption of individual GPUs. Evaluation on an NVIDIA RTX V100 Tesla GPU demonstrates the efficacy of our approach in reducing energy consumption while maintaining acceptable latency.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2431.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
