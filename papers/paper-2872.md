---
id: paper-2872
title: Optimizing LLMs Using Quantization for Mobile Execution
authors:
- Yadav, Agatsya
- Bhargavi, Renta Chintala
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-06697-8_33
url: https://www.scopus.com/pages/publications/105023192428?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 330--339
keywords:
- BitsAndBytes
- Edge Computing
- GGUF
- Large Language Models (LLMs)
- Llama 3
- llama.cpp
- Mobile AI
- Model Compression
- Post-Training Quantization (PTQ)
- Quantization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLMs é o workload não o tomador de decisões
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

# paper-2872 — Optimizing LLMs Using Quantization for Mobile Execution

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) offer powerful capabilities but their significant size and computational requirements hinder deployment on resource-constrained mobile devices. This paper investigates Post-Training Quantization (PTQ) for compressing LLMs for mobile execution. We specifically apply 4-bit PTQ using the BitsAndBytes library via the Hugging Face Transformers framework to Meta’s Llama 3.2 3B model. The quantized model is further converted to the GGUF format using llama.cpp tools for optimized mobile inference. The proposed PTQ workflow achieved a 68.66% reduction in model size through 4-bit post-training quantization, enabling the Llama 3.2 3B model to run efficiently on a standard Android device. Qualitative validation confirmed the 4-bit quantized model’s ability to perform inference tasks successfully. We demonstrate the feasibility of running the final quantized GGUF model on an Android device using the Termux environment and the Ollama framework. PTQ, particularly down to 4-bit precision combined with mobile-optimized formats like GGUF, presents a viable pathway for deploying capable LLMs directly on mobile devices, balancing model size and functional performance. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLMs é o workload não o tomador de decisões"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2872.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
