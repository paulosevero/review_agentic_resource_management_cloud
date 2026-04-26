---
id: "paper-1027"
title: "Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference"
authors: ["Li, Cong", "Xu, Yutao"]
year: 2024
venue: "Proceedings of the 17th ACM International Systems and Storage Conference, SYSTOR 2024"
venue_type: "conference"
doi: "10.1145/3688351.3689153"
url: "https://www.scopus.com/pages/publications/85206848613?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "53--67"
keywords: ["knowledge-driven optimization", "language model inference", "matrix multiplication", "memory-bound"]
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

# paper-1027 — Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference

## Metadata

- **Authors:** Li, Cong and Xu, Yutao
- **Year:** 2024
- **Venue:** Proceedings of the 17th ACM International Systems and Storage Conference, SYSTOR 2024
- **DOI:** 10.1145/3688351.3689153
- **URL:** https://www.scopus.com/pages/publications/85206848613?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 53--67
- **Language:** English
- **Keywords:** knowledge-driven optimization; language model inference; matrix multiplication; memory-bound

### Abstract

The majority of the latency in large language model inference lies in a few memory-bound matrix multiplication kernels. Traditionally, those kernels are optimized by extensive offline experiments of different tiling, striding, and slicing parameter choices on the target hardware. Scaling to different models, inference settings, and GPU hardware then becomes difficult. In this paper, we propose Foreseer, a new policy to generate the high-performing parameters for different kernels on the fly without offline experiments on the hardware. Foreseer leverages the specific characteristics of memory-bound matrix multiplication kernels, and synthesizes various prior knowledge such as keeping the adequate memory access pressure, avoiding the potential tail effect from load imbalance in dispatching, etc., into a simple penalty function. For a given parameter choice, Foreseer provides an analytical estimation of the impacting factors such as the memory access pressure, the potential tail effect, etc., to score the choice. A high-performing parameter choice is then discriminated from the penalty function. Micro-benchmarks of matrix multiplication kernels from popular language models on two different high-end Intel Data Center GPUs demonstrate that Foreseer outperforms different baselines including the vendor libraries, achieving >90% of the best-known performance obtained from the exhaustive offline parameter search experiments. End-to-end inference experiments on those language models with different settings also show that Foreseer accelerates the baseline by 20% on average, being competitive with and quite often exceeding the performance of the comprehensively-optimized vendor inference engine. © 2024 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Foreseer: Knowledge-Driven Acceleration of Memory-Bound Matrix Multiplications for Large Language Model Inference
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
