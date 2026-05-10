---
id: paper-2751
title: Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting
authors:
- Qiu, Chen
venue: Proceedings of 2025 2nd Symposium on Big Data, Neural Networks, and Deep Learning, BDNNDL 2025
venue_type: conference
year: 2026
doi: 10.1145/3784013.3784082
url: https://www.scopus.com/pages/publications/105028823179?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 429--434
keywords:
- Cloud resource forecasting
- large language models
- multivariate time series
- cross-modal alignment
- expert routing
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
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
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Prompting temporal discreto para previsão de recursos cloud — forecasting, não loop fechado agentic (Boundary A/B).
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

# paper-2751 — Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud resource prediction is important for keeping flexibility and performance in large cloud systems. However, common time series models have problems with multimodal data, long-term patterns, and fast inference. This paper presents CloudLLaMA-TS, a Llama 3 text-backbone framework for multivariate time series forecasting. It connects continuous signals and discrete token spaces and supports two temporal modalities (metrics & logs), not visual/audio alignment, and expert decoding. It builds a discrete temporal codebook through learnable quantization and time prompts that include frequency features and position encodings. A sliding-window attention with adaptive stride lowers computation cost to with window size w, and a cross-modal time attention network aligns asynchronous logs and metrics. A hierarchical mixture-of-experts with knowledge-guided routing chooses experts for different workload types. The model also uses parameter-efficient tuning and inference improvements like caching, quantization, and Bloom filtering. CloudLLaMA-TS gives a practical and accurate solution for fast and reliable cloud resource forecasting.  © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Llama" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llama, matched_substring: "Llama" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_prompting, matched_substring: "Prompting" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_mixture_experts, matched_substring: "mixture-of-experts" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Prompting temporal discreto para previsão de recursos cloud — forecasting, não loop fechado agentic (Boundary A/B)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2751.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
