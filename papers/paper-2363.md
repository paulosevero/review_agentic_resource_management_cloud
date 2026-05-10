---
id: paper-2363
title: Communication-Efficient Speculative Decoding for Large Language Models Inference
authors:
- Yang, Yong
- Yang, Ting Ting
- Gao, Shao Shuai
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2025
doi: 10.1109/ICCT67417.2025.11374072
url: https://www.scopus.com/pages/publications/105034061246?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1--5
keywords:
- Collaborative inference
- Communication optimization
- Cooperative Cache Sharing
- Distributed speculative decoding
- Incremental Synchronous Window
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2363 — Communication-Efficient Speculative Decoding for Large Language Models Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) achieve state-of-the-art generation quality, but deploying them across device-edge-cloud hierarchies remains challenging due to constrained uplink bandwidth and tight latency budgets. Existing speculative decoding techniques reduce end-to-end delay by offloading candidate verification to an edge LLM, yet they still transmit large hidden-state updates at every decoding step. In this work, we introduce Fused Speculative Decoding with Cooperative Cache Sharing and Incremental Synchronous Window (FSD-CCS-ISW), a communication-optimized framework that combines two complementary innovations: (1)Cooperative Cache Sharing (CCS) leverages a Bloom filter-based cache to avoid retransmission of previously seen quantized hidden-state deltas, dramatically reducing redundant traffic; (2)Incremental Synchronous Window (ISW) batches unseen deltas within a sliding window of size W, amortizing per-step communication overhead and exploiting temporal locality. We validate our method on LLaMA-2-7B (main) and LLaMA-160M (draft) across Belle dialog prompts (1000 tokens each), demonstrating a 40-57% latency reduction under realistic PCIe latencies, while preserving generation fidelity. FSD-CCS-ISW offers a principled, low-overhead path toward scalable LLM inference in bandwidthlimited environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2363.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
