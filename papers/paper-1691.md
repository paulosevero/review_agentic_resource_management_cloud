---
id: paper-1691
title: Analyzing quantized small language models for efficient edge deployment
authors:
- Jangw, Sooyoung
- Yang, Seungho
- Choi, Changbeom
venue: Journal of Korean Institute of Communications and Information Sciences
venue_type: journal
year: 2025
doi: 10.7840/kics.2025.50.9.1364
url: https://www.scopus.com/pages/publications/105019188399?origin=resultslist
publisher: Korean Institute of Communications and Information Sciences
pages: 1364--1380
keywords:
- Edge AI Deployment
- Edge Computing
- MMLU-Pro
- Quantization
- Small Language Models
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-1691 — Analyzing quantized small language models for efficient edge deployment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Quantized small language models (SLMs) offer a promising approach for deploying advanced natural language process- ing (NLP) services on resource-constrained edge devices. However, an in-depth examination of how different quantization configurations influence accuracy and efficiency remains underexplored. This paper systematically evaluates 72 quantized variants of Llama 3.2 (1B and 3B parameters) and Qwen 2.5 (1.5B and 3B parameters) across 13 quantization configura- tions, ranging from q2_K to q6_K. We use the MMLU-Pro benchmark to measure the accuracy (including and excluding random guesses), inference time, resource utilization, and power consumption on an NVIDIA Jetson Orin Nano. Our findings reveal that low-bit quantized models often rely heavily on random guessing, with modest accuracy improvements observed when these are excluded. Furthermore, Qwen 2.5 models generally yield superior accuracy and lower latency than Llama 3.2, albeit with higher sensitivity to quantization, whereas Llama 3.2 exhibits more consistent performance across quantization configurations. CPU utilization remains low (approximately 1-4%), with GPU utilization peaking up to 90% and power consumption ranging from 9.2 W to 11.5 W. Variability across different domains (computer science, engineering, and math) underscores the importance of selecting the appropriate model family, parameter size, and quantization configuration for specific applications. We conclude by outlining future directions for improving on-device NLP, including mixed-precision quantization, hardware-specific optimizations, and broader assessments covering multilingual or multimodal tasks. © 2025, Korean Institute of Communications and Information Sciences. All rights reserved.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "small language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "small language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NLP" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1691.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
