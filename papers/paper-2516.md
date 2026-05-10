---
id: paper-2516
title: 'SQ-LoRA: Memory-Efficient Language Model Compression Through Stable-Rank-Guided Quantization for Edge Computing Applications'
authors:
- Bayat Toksöz, Seda
- Işik, Gültekin
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2026
doi: 10.3390/app16042113
url: https://www.scopus.com/pages/publications/105031528587?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge computing
- low-rank adaptation
- natural language processing
- neural network quantization
- structured sparsity
- transformer models
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2516 — SQ-LoRA: Memory-Efficient Language Model Compression Through Stable-Rank-Guided Quantization for Edge Computing Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deployment of transformer-based language models on resource-constrained edge devices presents fundamental challenges in computational efficiency and memory utilization. We introduce SQ-LoRA (Stable-rank Quantized Low-Rank Adaptation), a theoretically grounded compression framework that achieves unprecedented efficiency through the synergistic integration of adaptive low-rank decomposition, hardware-accelerated structured sparsity, and intelligent hybrid quantization. Our primary contribution establishes the first rigorous mathematical connection between the matrix stable rank and optimal LoRA rank selection, formalized in Theorem I, which provides bounded approximation guarantees. SQ-LoRA implements: (1) adaptive rank allocation via stable-rank analysis to automatically determine layer-wise compression ratios; (2) 4:8 structured sparsity patterns, enabling 2× hardware acceleration on modern edge processors; and (3) a three-tier quantization scheme that combines 4-bit NormalFloat storage with selective 3-bit/8-bit precision to preserve outliers. A comprehensive evaluation on four diverse natural language processing (NLP) benchmarks demonstrates that SQ-LoRA achieves a 320 MB memory footprint (96.7% reduction) and a 10 ms inference latency (91.7% improvement), and maintains 82.0% average accuracy (within 0.15% of the full model). Statistical significance testing (p < 0.001) confirms its superiority over state-of-the-art methods. This framework enables the deployment of sophisticated language models on devices with 2 GB of RAM, advancing practical edge-AI applications. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2516.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
