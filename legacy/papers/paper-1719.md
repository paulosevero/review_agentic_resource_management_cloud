---
id: "paper-1719"
title: "Large Language Model Partitioning for Low-Latency Inference at the Edge"
authors: ["Kafetzis, Dimitrios", "Khalili, Ramin", "Koutsopoulos, Iordanis"]
year: 2025
venue: "Proceedings of the International Symposium on Modeling and Optimization in Mobile, Ad Hoc, and Wireless Networks, WiOpt"
venue_type: "conference"
doi: "10.23919/WiOpt66569.2025.11123401"
url: "https://www.scopus.com/pages/publications/105015948390?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge computing", "Large Language Models (LLMs)", "Low-latency inference", "Multi-head attention", "Resource allocation", "Transformer partitioning"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1719 — Large Language Model Partitioning for Low-Latency Inference at the Edge

## Metadata

- **Authors:** Kafetzis, Dimitrios and Khalili, Ramin and Koutsopoulos, Iordanis
- **Year:** 2025
- **Venue:** Proceedings of the International Symposium on Modeling and Optimization in Mobile, Ad Hoc, and Wireless Networks, WiOpt
- **DOI:** 10.23919/WiOpt66569.2025.11123401
- **URL:** https://www.scopus.com/pages/publications/105015948390?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge computing; Large Language Models (LLMs); Low-latency inference; Multi-head attention; Resource allocation; Transformer partitioning

### Abstract

Large Language Models (LLMs) based on autoregressive, decoder-only Transformers generate text one token at a time, where a token represents a discrete unit of text. As each newly produced token is appended to the partial output sequence, the length grows and so does the memory and compute load, due to the expanding key-value (K/V) caches—which store intermediate representations of all previously generated tokens—in the multi-head attention (MHA) layer. As this iterative process steadily increases memory and compute demands, layer-based partitioning in resource-constrained edge environments often results in memory overload or high inference latency. To address this, aiming to reduce inference latency, we propose a resource-aware Transformer architecture partitioning algorithm, where the partitioning decision is updated at regular intervals during token generation. The approach is a myopic algorithm in the sense that it is based on instantaneously available information about device resources availability and network link bandwidths. When the algorithm is first executed, it generates a placement of blocks on devices, and in each consecutive time it is executed, it migrates these blocks among devices so that the sum of migration delay and inference delay remains low. Our approach partitions the decoder at the attention head-level, co-locating each attention head with its K/V cache and allowing dynamic migrations whenever resources become tight. By allocating different attention heads to different devices, we exploit parallel execution of attention heads and thus allow for substantial reductions in inference delays. Our experiments show that in small-scale settings (3–5 devices), the proposed method achieves within 15–20% of an exact optimal solver’s latency, while in larger-scale tests it achieves notable improvements in inference speed and memory usage compared to state-of-the-art layer-based partitioning approaches. © 2025 IFIP.

## 04 — Title Screening

**Title:** Large Language Model Partitioning for Low-Latency Inference at the Edge

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Large Language Model Partitioning for Low-Latency Inference at the Edge
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Large Language Model Partitioning for Low-Latency Inference at the Edge
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
