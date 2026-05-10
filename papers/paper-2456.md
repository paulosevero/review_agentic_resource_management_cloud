---
id: paper-2456
title: Split Fine-Tuning for Large Language Models in Wireless Networks
authors:
- Zhang, Songge
- Cheng, Guoliang
- Wu, Wen
- Huang, Xinyu
- Song, Lingyang
- Shen, Xuemin
venue: IEEE Journal on Selected Topics in Signal Processing
venue_type: journal
year: 2025
doi: 10.1109/JSTSP.2025.3581484
url: https://www.scopus.com/pages/publications/105008922887?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1376--1391
keywords:
- fine-tuning
- Large language models
- resource management
- split learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2456 — Split Fine-Tuning for Large Language Models in Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fine-tuning is the process of adapting the pre-trained large language models (LLMs) for downstream tasks. Due to substantial model parameters, fine-tuning LLM on mobile devices demands considerable memory resources, and suffers from high communication overhead and fine-tuning delay. In this paper, we propose an efficient LLM fine-tuning scheme in wireless networks, named Split Fine-Tuning (SFT), which can accommodate LLM fine-tuning on mobile devices. Specifically, an LLM is split into a server-side part on the edge server and a device-side part on the mobile device to satisfy the device-side memory constraint. All devices share a server-side model and perform parallel fine-tuning to reduce fine-tuning delay. In addition, to reduce communication overhead incurred by data exchange between devices and the edge server, we propose an activation data compression scheme by jointly leveraging sparsification, stochastic quantization, and lossless encoding methods. Furthermore, we formulate a fine-tuning delay minimization problem under model accuracy and device-side memory constraints, taking device heterogeneity and channel dynamics into account. To solve the problem, the nonlinear mixed-integer problem is decoupled into two subproblems in different timescales. A two-timescale resource management algorithm is proposed to jointly optimize the compression rate and transformer block allocation in the large timescale using the augmented Lagrangian method, and determine spectrum resource allocation in the small timescale via sequential quadratic programming. Extensive simulation results demonstrate that the proposed scheme can reduce the fine-tuning delay by up to 66.4% and communication overhead by 93.6% compared to state-of-the-art benchmarks, while satisfying device-side memory and model accuracy constraints. © 2007-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2456.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
