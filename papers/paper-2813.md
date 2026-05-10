---
id: paper-2813
title: 'DP-Prox: A Robust and Differentially Private Framework for Federated Instruction Tuning of Small LLMs on 8 GB Edge Devices'
authors:
- Venkatesh, Vinay
- Liu, Yichen
venue: 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
venue_type: conference
year: 2026
doi: 10.1109/CCWC67433.2026.11393831
url: https://www.scopus.com/pages/publications/105035589499?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 620--626
keywords:
- Differential Privacy
- Edge Computing
- Fed-Prox
- Federated Learning
- Instruction Tuning
- IoT
- Phi-3
- QLoRA
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
    my_justification: Out of scope
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

# paper-2813 — DP-Prox: A Robust and Differentially Private Framework for Federated Instruction Tuning of Small LLMs on 8 GB Edge Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper introduces DP-Prox, an end-to-end framework for robust and differentially private federated instruction tuning of small Large Language Models (LLMs) on 8 GB edge devices. DP-Prox is instantiated using the 3.8 billionparameter Phi-3-mini model with 4-bit Quantized Low-Rank Adaptation (QLoRA), and combines (i) FedProx-style proximal regularization on low-rank adapters to stabilize optimization under highly Non-IID smart-home data, and (ii) Differentially Private SGD (DP-SGD) applied directly to adapter gradients to provide user-level (ϵ, δ) -differential privacy against an honest-but-curious server. In a realistic IoT instruction-following benchmark with Dirichlet-skewed clients (α=0.3), DP-Prox improves F1-score from 0.80 (Edge-FIT with FedAvg) to 0.82 while reducing convergence rounds from T=50 to T ≈ 40. Under a strict privacy budget (ϵ=5, δ=10<sup>-5</sup>), DP-Prox maintains an F1-score of 0.77 with only +15%-20% local overhead, and preserves the communication efficiency of QLoRA-based federated training. Qualitative analyses further show that DP-Prox yields more consistent instruction-following behavior across heterogeneous homes, especially on multi-device routines and privacy-sensitive queries. Together, these results position DP-Prox as a practical and regulation-ready blueprint for deploying small, edge-resident LLMs in smart-home IoT environments. © 2026 IEEE.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2813.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
