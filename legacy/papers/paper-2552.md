---
id: "paper-2552"
title: "On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey"
authors: ["Dawane, Anuja"]
year: 2026
venue: "2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026"
venue_type: "conference"
doi: "10.1109/CCWC67433.2026.11393726"
url: "https://www.scopus.com/pages/publications/105035586204?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "669--675"
keywords: ["edge AI", "on-device inference", "quantization", "real-time systems", "robotics", "Small language models", "vision-language-action"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Review"

---

# paper-2552 — On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey

## Metadata

- **Authors:** Dawane, Anuja
- **Year:** 2026
- **Venue:** 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
- **DOI:** 10.1109/CCWC67433.2026.11393726
- **URL:** https://www.scopus.com/pages/publications/105035586204?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 669--675
- **Language:** English
- **Keywords:** edge AI; on-device inference; quantization; real-time systems; robotics; Small language models; vision-language-action

### Abstract

Small language models (SLMs) and on-device large language model (LLM) deployments are rapidly becoming key enablers of natural language interaction, high-level decision making, and semantic perception in robotics. Unlike datacenter-scale models, robotic deployments must satisfy tight latency, energy, and memory constraints while operating on embedded platforms such as NVIDIA Jetson, mobile systems-on-chip (SoCs), or custom controllers, often without reliable network connectivity. This paper surveys inference acceleration methods for on-device SLMs with a focus on real-time robotic use cases. We organize techniques into four layers: (i) model-level approaches such as low-bit quantization, distillation, architecture optimization, and sparsity; (ii) algorithmic methods including efficient attention, KV-cache compression, and speculative and multi-token decoding; (iii) system-level runtimes and scheduling techniques for embedded and edge platforms; and (iv) hardware trends spanning mobile neural processing units (NPUs), Jetson-class GPUs, FPGAs, and vision-language-action (VLA) accelerators. We highlight representative state-of-the-art SLM families (e.g., Llama 3.2, Phi-3, Gemma, Qwen 2.5, MobileLLM, MobileLLMPro) and robotics-oriented models such as Gemini Robotics ondevice and edge LLMs for ground robots. We also summarize design trade-offs through a comparison of inference frameworks (ExecuTorch, MLC-LLM, NanoLLM, llama.cpp, MediaPipe LLM, TensorRT-based stacks) and discuss open challenges for deploying language models as real-time components in robotic systems. © 2026 IEEE.

## 04 — Title Screening

**Title:** On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** On-Device Small Language Model Inference Acceleration for Real-Time Robotics: A Survey
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
