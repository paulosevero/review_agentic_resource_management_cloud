---
id: paper-2387
title: Comparative Study on Energy Consumption of Neural Networks by Scaling of Weight-Memory Energy Versus Computing Energy for Implementing Low-Power Edge Intelligence
authors:
- Yoon, Ilpyung
- Mun, Jihwan
- Min, Kyeong-Sik
venue: Electronics (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/electronics14132718
url: https://www.scopus.com/pages/publications/105010566896?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge intelligence
- energy consumption of neural networks
- MAC computing energy
- weight-memory energy
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2387 — Comparative Study on Energy Consumption of Neural Networks by Scaling of Weight-Memory Energy Versus Computing Energy for Implementing Low-Power Edge Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Energy consumption has emerged as a critical design constraint in deploying high-performance neural networks, especially on edge devices with limited power resources. In this paper, a comparative study is conducted for two prevalent deep learning paradigms—convolutional neural networks (CNNs), exemplified by ResNet18, and transformer-based large language models (LLMs), represented by GPT3-small, Llama-7B, and GPT3-175B. By analyzing how the scaling of memory energy versus computing energy affects the energy consumption of neural networks with different batch sizes (1, 4, 8, 16), it is shown that ResNet18 transitions from a memory energy-limited regime at low batch sizes to a computing energy-limited regime at higher batch sizes due to its extensive convolution operations. On the other hand, GPT-like models remain predominantly memory-bound, with large parameter tensors and frequent key–value (KV) cache lookups accounting for most of the total energy usage. Our results reveal that reducing weight-memory energy is particularly effective in transformer architectures, while improving multiply–accumulate (MAC) efficiency significantly benefits CNNs at higher workloads. We further highlight near-memory and in-memory computing approaches as promising strategies to lower data-transfer costs and enhance power efficiency in large-scale deployments. These findings offer actionable insights for architects and system designers aiming to optimize artificial intelligence (AI) performance under stringent energy budgets on battery-powered edge devices. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2387.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
