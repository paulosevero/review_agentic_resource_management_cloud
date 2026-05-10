---
id: paper-2552
title: 'On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey'
authors:
- Dawane, Anuja
venue: 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
venue_type: conference
year: 2026
doi: 10.1109/CCWC67433.2026.11393726
url: https://www.scopus.com/pages/publications/105035586204?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 669--675
keywords:
- edge AI
- on-device inference
- quantization
- real-time systems
- robotics
- Small language models
- vision-language-action
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
    my_justification: Review
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

# paper-2552 — On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Small language models (SLMs) and on-device large language model (LLM) deployments are rapidly becoming key enablers of natural language interaction, high-level decision making, and semantic perception in robotics. Unlike datacenter-scale models, robotic deployments must satisfy tight latency, energy, and memory constraints while operating on embedded platforms such as NVIDIA Jetson, mobile systems-on-chip (SoCs), or custom controllers, often without reliable network connectivity. This paper surveys inference acceleration methods for on-device SLMs with a focus on real-time robotic use cases. We organize techniques into four layers: (i) model-level approaches such as low-bit quantization, distillation, architecture optimization, and sparsity; (ii) algorithmic methods including efficient attention, KV-cache compression, and speculative and multi-token decoding; (iii) system-level runtimes and scheduling techniques for embedded and edge platforms; and (iv) hardware trends spanning mobile neural processing units (NPUs), Jetson-class GPUs, FPGAs, and vision-language-action (VLA) accelerators. We highlight representative state-of-the-art SLM families (e.g., Llama 3.2, Phi-3, Gemma, Qwen 2.5, MobileLLM, MobileLLMPro) and robotics-oriented models such as Gemini Robotics ondevice and edge LLMs for ground robots. We also summarize design trade-offs through a comparison of inference frameworks (ExecuTorch, MLC-LLM, NanoLLM, llama.cpp, MediaPipe LLM, TensorRT-based stacks) and discuss open challenges for deploying language models as real-time components in robotic systems. © 2026 IEEE.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2552.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
