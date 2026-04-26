---
id: "paper-2363"
title: "Communication-Efficient Speculative Decoding for Large Language Models Inference"
authors: ["Yang, Yong", "Yang, Ting Ting", "Gao, Shao Shuai"]
year: 2025
venue: "International Conference on Communication Technology Proceedings, ICCT"
venue_type: "conference"
doi: "10.1109/ICCT67417.2025.11374072"
url: "https://www.scopus.com/pages/publications/105034061246?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1--5"
keywords: ["Collaborative inference", "Communication optimization", "Cooperative Cache Sharing", "Distributed speculative decoding", "Incremental Synchronous Window"]
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

# paper-2363 — Communication-Efficient Speculative Decoding for Large Language Models Inference

## Metadata

- **Authors:** Yang, Yong and Yang, Ting Ting and Gao, Shao Shuai
- **Year:** 2025
- **Venue:** International Conference on Communication Technology Proceedings, ICCT
- **DOI:** 10.1109/ICCT67417.2025.11374072
- **URL:** https://www.scopus.com/pages/publications/105034061246?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1--5
- **Language:** English
- **Keywords:** Collaborative inference; Communication optimization; Cooperative Cache Sharing; Distributed speculative decoding; Incremental Synchronous Window

### Abstract

Large language models (LLMs) achieve state-of-the-art generation quality, but deploying them across device-edge-cloud hierarchies remains challenging due to constrained uplink bandwidth and tight latency budgets. Existing speculative decoding techniques reduce end-to-end delay by offloading candidate verification to an edge LLM, yet they still transmit large hidden-state updates at every decoding step. In this work, we introduce Fused Speculative Decoding with Cooperative Cache Sharing and Incremental Synchronous Window (FSD-CCS-ISW), a communication-optimized framework that combines two complementary innovations: (1)Cooperative Cache Sharing (CCS) leverages a Bloom filter-based cache to avoid retransmission of previously seen quantized hidden-state deltas, dramatically reducing redundant traffic; (2)Incremental Synchronous Window (ISW) batches unseen deltas within a sliding window of size W, amortizing per-step communication overhead and exploiting temporal locality. We validate our method on LLaMA-2-7B (main) and LLaMA-160M (draft) across Belle dialog prompts (1000 tokens each), demonstrating a 40-57% latency reduction under realistic PCIe latencies, while preserving generation fidelity. FSD-CCS-ISW offers a principled, low-overhead path toward scalable LLM inference in bandwidthlimited environments. © 2025 IEEE.

## 04 — Title Screening

**Title:** Communication-Efficient Speculative Decoding for Large Language Models Inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Communication-Efficient Speculative Decoding for Large Language Models Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Communication-Efficient Speculative Decoding for Large Language Models Inference
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
