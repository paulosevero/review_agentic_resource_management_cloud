---
id: "paper-2173"
title: "Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference"
authors: ["Stoyanov, Radostin", "Spi\u0161akov\u00e1, Vikt\u00f3ria", "Reber, Adrian", "Armour, Wesley", "Copik, Marcin", "Bruno, Rodrigo"]
year: 2025
venue: "Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops"
venue_type: "conference"
doi: "10.1145/3731599.3767354"
url: "https://www.scopus.com/pages/publications/105023407201?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "114--125"
keywords: ["Cloud Computing", "Containers", "GPU Checkpointing", "LLM Inference"]
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
    human_justification: "LLM as workload"

---

# paper-2173 — Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference

## Metadata

- **Authors:** Stoyanov, Radostin and Spišaková, Viktória and Reber, Adrian and Armour, Wesley and Copik, Marcin and Bruno, Rodrigo
- **Year:** 2025
- **Venue:** Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops
- **DOI:** 10.1145/3731599.3767354
- **URL:** https://www.scopus.com/pages/publications/105023407201?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 114--125
- **Language:** English
- **Keywords:** Cloud Computing; Containers; GPU Checkpointing; LLM Inference

### Abstract

The widespread adoption of Large Language Models (LLMs) has led to an increased demand for large-scale inference services, presenting a unique set of challenges for the HPC community. These services are characterized by moderate-scale models that require dedicating expensive GPUs to handle bursty inference requests, leading to high costs and resource underutilization. In this paper, we propose SwapServeLLM - a novel engine-agnostic hot-swapping method for cost-effective inference. This model hot-swapping approach is enabled by recent driver capabilities for transparent GPU checkpointing. SwapServeLLM optimizes resource utilization by dynamically allocating GPU resources with two key mechanisms: (1) a demand-aware preemption leveraging information about concurrent requests, and (2) efficient request routing with memory reservation minimizing inference latency. Our evaluation demonstrates that SwapServeLLM optimizes model loading for state-ofthe-art inference engines by 31× compared to vLLM and up to 29% compared to Ollama, enabling cost-effective inference. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference
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
