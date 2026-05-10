---
id: "paper-2872"
title: "Optimizing LLMs Using Quantization for Mobile Execution"
authors: ["Yadav, Agatsya", "Bhargavi, Renta Chintala"]
year: 2026
venue: "Lecture Notes in Networks and Systems"
venue_type: "conference"
doi: "10.1007/978-3-032-06697-8_33"
url: "https://www.scopus.com/pages/publications/105023192428?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "330--339"
keywords: ["BitsAndBytes", "Edge Computing", "GGUF", "Large Language Models (LLMs)", "Llama 3", "llama.cpp", "Mobile AI", "Model Compression", "Post-Training Quantization (PTQ)", "Quantization"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "LLMs é o workload não o tomador de decisões"

---

# paper-2872 — Optimizing LLMs Using Quantization for Mobile Execution

## Metadata

- **Authors:** Yadav, Agatsya and Bhargavi, Renta Chintala
- **Year:** 2026
- **Venue:** Lecture Notes in Networks and Systems
- **DOI:** 10.1007/978-3-032-06697-8_33
- **URL:** https://www.scopus.com/pages/publications/105023192428?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 330--339
- **Language:** English
- **Keywords:** BitsAndBytes; Edge Computing; GGUF; Large Language Models (LLMs); Llama 3; llama.cpp; Mobile AI; Model Compression; Post-Training Quantization (PTQ); Quantization

### Abstract

Large Language Models (LLMs) offer powerful capabilities but their significant size and computational requirements hinder deployment on resource-constrained mobile devices. This paper investigates Post-Training Quantization (PTQ) for compressing LLMs for mobile execution. We specifically apply 4-bit PTQ using the BitsAndBytes library via the Hugging Face Transformers framework to Meta’s Llama 3.2 3B model. The quantized model is further converted to the GGUF format using llama.cpp tools for optimized mobile inference. The proposed PTQ workflow achieved a 68.66% reduction in model size through 4-bit post-training quantization, enabling the Llama 3.2 3B model to run efficiently on a standard Android device. Qualitative validation confirmed the 4-bit quantized model’s ability to perform inference tasks successfully. We demonstrate the feasibility of running the final quantized GGUF model on an Android device using the Termux environment and the Ollama framework. PTQ, particularly down to 4-bit precision combined with mobile-optimized formats like GGUF, presents a viable pathway for deploying capable LLMs directly on mobile devices, balancing model size and functional performance. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

## 04 — Title Screening

**Title:** Optimizing LLMs Using Quantization for Mobile Execution

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.5
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimizing LLMs Using Quantization for Mobile Execution
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Optimizing LLMs Using Quantization for Mobile Execution
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
