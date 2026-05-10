---
id: paper-2925
title: 'AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training'
authors:
- Zhao, Boran
- Liu, Hetian
- Yuan, Zihang
- Zhu, Li
- Yang, Fan
- Xie, Lina
- Xia, Tian
- Zhao, Wenzhe
- Ren, Pengju
venue: 'IEEE Transactions on Circuits and Systems I: Regular Papers'
venue_type: journal
year: 2026
doi: 10.1109/TCSI.2026.3667183
url: https://www.scopus.com/pages/publications/105032857105?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Dataset sampling
- DNN training
- edge computing
- hardware/software co-design
- parallel circuits
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2925 — AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Training deep neural networks (DNNs) on edge devices faces challenges due to the large-scale datasets required, which are costly for edge devices, especially in large language model (LLM) tasks. To address this, a DNN-free method called Near-Memory Sampling (NMS) has been introduced. NMS reduces dimensionality and performs exemplar sampling in the reduced space, avoiding architectural bias and improving generalization. However, NMS has two limitations: 1) The mismatch between the search method and the non-monotonic property of the perplexity error function leads to the emergence of outliers; 2) Key parameter (i.e., target perplexity) is selected empirically, introducing arbitrariness and leading to uneven sampling. These two issues lead to representative bias of exemplars, resulting in degraded accuracy. To overcome these, we propose AdapSNE, which integrates the Fireworks Algorithm (FWA) for efficient non-monotonic search to avoid outliers and uses entropy-guided optimization for uniform sampling, ensuring representative training samples. To reduce the cost of iterative computations, we design an accelerator with custom dataflow and time-multiplexing mechanisms. Experimental results show that AdapSNE outperforms state-of-the-art methods, including both DNN-based (DQAS) and DNN-free (NMS) approaches, across small-scale image datasets, large-scale datasets, and the MMLU benchmark for LLM tasks. © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2925.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
