---
id: "paper-971"
title: "HEXGEN: Generative Inference of Large Language Model over Heterogeneous Environment"
authors: ["Jiang, Youhe", "Yan, Ran", "Yao, Xiaozhe", "Zhou, Yang", "Chen, Beidi", "Yuan, Binhang"]
year: 2024
venue: "Proceedings of Machine Learning Research"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/85203802677?origin=resultslist"
publisher: "ML Research Press"
pages: "21946--21961"
keywords: ["Budget control", "Generative adversarial networks", "Inference engines", "Tensors", "AI applications", "Centralised", "Datacenter", "Distributed inference", "Heterogeneous environments", "Language model", "Optimisations", "Pipeline parallelisms", "State of the art", "Tensor model", "Constrained optimization"]
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

# paper-971 — HEXGEN: Generative Inference of Large Language Model over Heterogeneous Environment

## Metadata

- **Authors:** Jiang, Youhe and Yan, Ran and Yao, Xiaozhe and Zhou, Yang and Chen, Beidi and Yuan, Binhang
- **Year:** 2024
- **Venue:** Proceedings of Machine Learning Research
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/85203802677?origin=resultslist
- **Publisher:** ML Research Press
- **Pages:** 21946--21961
- **Language:** English
- **Keywords:** Budget control; Generative adversarial networks; Inference engines; Tensors; AI applications; Centralised; Datacenter; Distributed inference; Heterogeneous environments; Language model; Optimisations; Pipeline parallelisms; State of the art; Tensor model; Constrained optimization

### Abstract

Serving generative inference of the large language model is a crucial component of contemporary AI applications. This paper focuses on deploying such services in a heterogeneous and cross-datacenter setting to mitigate the substantial inference costs typically associated with a single centralized datacenter. Towards this end, we propose HEXGEN, a flexible distributed inference engine that uniquely supports the asymmetric partition of generative inference computations over both tensor model parallelism and pipeline parallelism and allows for effective deployment across diverse GPUs interconnected by a fully heterogeneous network. We further propose a sophisticated scheduling algorithm grounded in constrained optimization that can adaptively assign asymmetric inference computation across the GPUs to fulfill inference requests while maintaining acceptable latency levels. We conduct an extensive evaluation to verify the efficiency of HEXGEN by serving the state-of-the-art LLAMA-2 (70B) model. The results suggest that HEXGEN can choose to achieve up to 2.3× lower latency deadlines or tolerate up to 4× more request rates compared with the homogeneous baseline given the same budget. Our implementation is available at https://github.com/Relaxed-System-Lab/HexGen. Copyright 2024 by the author(s)

## 04 — Title Screening

**Title:** HEXGEN: Generative Inference of Large Language Model over Heterogeneous Environment

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** HEXGEN: Generative Inference of Large Language Model over Heterogeneous Environment
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** HEXGEN: Generative Inference of Large Language Model over Heterogeneous Environment
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
