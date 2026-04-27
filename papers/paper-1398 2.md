---
id: "paper-1398"
title: "Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5"
authors: ["Arora, Saarang", "Kachari, Kishor Kumar", "Gupta, Suyash", "Saarthi, Parth", "Yadav, Arpit Kumar", "Patnaik, Salur Srikant"]
year: 2025
venue: "2025 IEEE International Conference on Computer Vision and Machine Intelligence, CVMI 2025"
venue_type: "conference"
doi: "10.1109/CVMI66673.2025.11337918"
url: "https://www.scopus.com/pages/publications/105033525475?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["ASR", "conversational AI", "edge devices", "LLM", "quantization", "Raspberry Pi 5", "single-board computers", "TTS"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1398 — Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5

## Metadata

- **Authors:** Arora, Saarang and Kachari, Kishor Kumar and Gupta, Suyash and Saarthi, Parth and Yadav, Arpit Kumar and Patnaik, Salur Srikant
- **Year:** 2025
- **Venue:** 2025 IEEE International Conference on Computer Vision and Machine Intelligence, CVMI 2025
- **DOI:** 10.1109/CVMI66673.2025.11337918
- **URL:** https://www.scopus.com/pages/publications/105033525475?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** ASR; conversational AI; edge devices; LLM; quantization; Raspberry Pi 5; single-board computers; TTS

### Abstract

Deploying conversational AI systems on resource-constrained edge computing devices requires sophisticated optimization techniques to ensure computational efficiency without compromising performance quality. This paper presents a comprehensive study on the optimization and deployment of an end-to-end conversational AI pipeline - comprising Whisper automatic speech recognition (ASR), a 3-billion parameter Llama-3 large language model (LLM) and lightweight text-to-speech (TTS) - running entirely on a Raspberry Pi module. Multiple quantization levels are benchmarked across two inference stacks, Ollama and the lower-overhead llama.cpp. The evaluation is conducted in two phases: first, by analyzing the metrics for individual components and second, by assessing the overall pipeline. The results show that implementing a lower bit quantized version of llama.cpp within the pipeline yields significant improvements in latency and energy consumption compared to the higher bit baseline, with only a marginal reduction in coherence. Similar results are observed for the Ollama deployment. These findings demonstrate that strategic quantization and runtime optimizations facilitate the practical deployment of conversational AI systems on edge devices, maintaining high conversational quality while paving the way for locally executed, privacy-preserving AI applications. © 2025 IEEE.

## 04 — Title Screening

**Title:** Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Bringing Llama-3 to the Edge: End-to-End Quantized Conversational AI on Raspberry Pi 5
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
