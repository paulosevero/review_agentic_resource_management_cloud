---
id: paper-1398
title: 'Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5'
authors:
- Arora, Saarang
- Kachari, Kishor Kumar
- Gupta, Suyash
- Saarthi, Parth
- Yadav, Arpit Kumar
- Patnaik, Salur Srikant
venue: 2025 IEEE International Conference on Computer Vision and Machine Intelligence, CVMI 2025
venue_type: conference
year: 2025
doi: 10.1109/CVMI66673.2025.11337918
url: https://www.scopus.com/pages/publications/105033525475?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- ASR
- conversational AI
- edge devices
- LLM
- quantization
- Raspberry Pi 5
- single-board computers
- TTS
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1398 — Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying conversational AI systems on resource-constrained edge computing devices requires sophisticated optimization techniques to ensure computational efficiency without compromising performance quality. This paper presents a comprehensive study on the optimization and deployment of an end-to-end conversational AI pipeline - comprising Whisper automatic speech recognition (ASR), a 3-billion parameter Llama-3 large language model (LLM) and lightweight text-to-speech (TTS) - running entirely on a Raspberry Pi module. Multiple quantization levels are benchmarked across two inference stacks, Ollama and the lower-overhead llama.cpp. The evaluation is conducted in two phases: first, by analyzing the metrics for individual components and second, by assessing the overall pipeline. The results show that implementing a lower bit quantized version of llama.cpp within the pipeline yields significant improvements in latency and energy consumption compared to the higher bit baseline, with only a marginal reduction in coherence. Similar results are observed for the Ollama deployment. These findings demonstrate that strategic quantization and runtime optimizations facilitate the practical deployment of conversational AI systems on edge devices, maintaining high conversational quality while paving the way for locally executed, privacy-preserving AI applications. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "conversational AI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1398.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
