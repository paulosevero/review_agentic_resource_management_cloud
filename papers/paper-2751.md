---
id: "paper-2751"
title: "Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting"
authors: ["Qiu, Chen"]
year: 2026
venue: "Proceedings of 2025 2nd Symposium on Big Data, Neural Networks, and Deep Learning, BDNNDL 2025"
venue_type: "conference"
doi: "10.1145/3784013.3784082"
url: "https://www.scopus.com/pages/publications/105028823179?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "429--434"
keywords: ["Cloud resource forecasting", "large language models", "multivariate time series", "cross-modal alignment", "expert routing"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2751 — Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting

## Metadata

- **Authors:** Qiu, Chen
- **Year:** 2026
- **Venue:** Proceedings of 2025 2nd Symposium on Big Data, Neural Networks, and Deep Learning, BDNNDL 2025
- **DOI:** 10.1145/3784013.3784082
- **URL:** https://www.scopus.com/pages/publications/105028823179?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 429--434
- **Language:** English
- **Keywords:** Cloud resource forecasting; large language models; multivariate time series; cross-modal alignment; expert routing

### Abstract

Cloud resource prediction is important for keeping flexibility and performance in large cloud systems. However, common time series models have problems with multimodal data, long-term patterns, and fast inference. This paper presents CloudLLaMA-TS, a Llama 3 text-backbone framework for multivariate time series forecasting. It connects continuous signals and discrete token spaces and supports two temporal modalities (metrics & logs), not visual/audio alignment, and expert decoding. It builds a discrete temporal codebook through learnable quantization and time prompts that include frequency features and position encodings. A sliding-window attention with adaptive stride lowers computation cost to with window size w, and a cross-modal time attention network aligns asynchronous logs and metrics. A hierarchical mixture-of-experts with knowledge-guided routing chooses experts for different workload types. The model also uses parameter-efficient tuning and inference improvements like caching, quantization, and Bloom filtering. CloudLLaMA-TS gives a practical and accurate solution for fast and reliable cloud resource forecasting.  © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Discrete Temporal Prompting and Cross-Modal Alignment for Cloud Resource Forecasting
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
