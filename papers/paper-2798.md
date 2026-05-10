---
id: paper-2798
title: Strategies for computational efficiency in small language models
authors:
- Taylar, Jonathan
venue: Autonomous Intelligent Systems
venue_type: journal
year: 2026
doi: 10.1007/s43684-026-00130-7
url: https://www.scopus.com/pages/publications/105036043172?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Generative AI
- Large Language Models (LLMs)
- Natural Language Processing (NLP)
- Small Language Models (SLMs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
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

# paper-2798 — Strategies for computational efficiency in small language models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The proliferation of Large Language Models (LLMs) is often constrained by their significant computational and memory requirements, limiting their deployment to large data centers. Small Language Models (SLMs) offer a feasible solution for on-device applications; yet their efficiency requires optimization to operate well on resource-constrained hardware. This study looks at ways to make SLMs more efficient at using computers. The effects of two primary methods were compared: post-training optimization and architectural innovation through quantitative and observational study. Using a standardized suite of benchmarks measuring accuracy, reasoning, and inference performance, a baseline is established with state-of-the-art SLMs like Phi-3 and Llama 3. Post-training techniques were evaluated, including 4-bit quantization (GPTQ) and knowledge distillation from a superior teacher model. Finally, these optimized Transformers were compared against a custom-trained, non-Transformer model based on the Mamba (State-Space Model) architecture. Results show that 4-bit quantization is the most effective compression strategy among those evaluated. It reduces peak inference memory footprint by 71%, increases throughput by 83%, and does so with minimal accuracy degradation. Within the controlled experimental space evaluated in this study, the 4-bit quantized Phi-3-mini model occupies a Pareto-optimal position in memory-normalized accuracy. Focused skill growth works best with knowledge distillation. However, new designs like Mamba offer a different trade-off by being the best at streaming jobs’ raw output. It was found that improving current Transformer-based SLMs through quantization is the best way to use them for general purposes. However, customized designs and distillation work better for specific, high-performance uses. This research offers a definitive framework and pragmatic recommendations for advancing the next generation of robust, efficient, and accessible language models. © The Author(s) 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "small language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Small Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLMs" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2798.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
