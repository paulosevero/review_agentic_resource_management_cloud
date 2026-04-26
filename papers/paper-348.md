---
id: "paper-348"
title: "EdgeBERT: Sentence-level energy optimizations for latency-aware multi-task NLP inference"
authors: ["Tambe, Thierry", "Hooper, Coleman", "Pentecost, Lillian", "Jia, Tianyu", "Yang, En-Yu", "Donato, Marco", "Sanh, Victor", "Whatmough, Paul N.", "Rush, Alexander M.", "Brooks, David", "Wei, Gu-Yeon"]
year: 2021
venue: "Proceedings of the Annual International Symposium on Microarchitecture, MICRO"
venue_type: "conference"
doi: "10.1145/3466752.3480095"
url: "https://www.scopus.com/pages/publications/85118853820?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "830--844"
keywords: ["Embedded non-volatile memories", "Latency-aware", "Natural language processing", "Software and hardware co-Design"]
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
    human_decision: ""
    human_justification: ""

---

# paper-348 — EdgeBERT: Sentence-level energy optimizations for latency-aware multi-task NLP inference

## Metadata

- **Authors:** Tambe, Thierry and Hooper, Coleman and Pentecost, Lillian and Jia, Tianyu and Yang, En-Yu and Donato, Marco and Sanh, Victor and Whatmough, Paul N. and Rush, Alexander M. and Brooks, David and Wei, Gu-Yeon
- **Year:** 2021
- **Venue:** Proceedings of the Annual International Symposium on Microarchitecture, MICRO
- **DOI:** 10.1145/3466752.3480095
- **URL:** https://www.scopus.com/pages/publications/85118853820?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 830--844
- **Language:** English
- **Keywords:** Embedded non-volatile memories; Latency-aware; Natural language processing; Software and hardware co-Design

### Abstract

Transformer-based language models such as BERT provide significant accuracy improvement to a multitude of natural language processing (NLP) tasks. However, their hefty computational and memory demands make them challenging to deploy to resourceconstrained edge platforms with strict latency requirements. We present EdgeBERT, an in-depth algorithm-hardware codesign for latency-aware energy optimizations for multi-task NLP. EdgeBERT employs entropy-based early exit predication in order to perform dynamic voltage-frequency scaling (DVFS), at a sentence granularity, for minimal energy consumption while adhering to a prescribed target latency. Computation and memory footprint overheads are further alleviated by employing a calibrated combination of adaptive attention span, selective network pruning, and floating-point quantization. Furthermore, in order to maximize the synergistic benefits of these algorithms in always-on and intermediate edge computing settings, we specialize a 12nm scalable hardware accelerator system, integrating a fast-switching low-dropout voltage regulator (LDO), an all-digital phase-locked loop (ADPLL), as well as, highdensity embedded non-volatile memories (eNVMs) wherein the sparse floating-point bit encodings of the shared multi-task parameters are carefully stored. Altogether, latency-aware multi-task NLP inference acceleration on the EdgeBERT hardware system generates up to 7×, 2.5×, and 53× lower energy compared to the conventional inference without early stopping, the latency-unbounded early exit approach, and CUDA adaptations on an Nvidia Jetson Tegra X2 mobile GPU, respectively. © 2021 Association for Computing Machinery.

## 04 — Title Screening

**Title:** EdgeBERT: Sentence-level energy optimizations for latency-aware multi-task NLP inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeBERT: Sentence-level energy optimizations for latency-aware multi-task NLP inference
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeBERT: Sentence-level energy optimizations for latency-aware multi-task NLP inference
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
