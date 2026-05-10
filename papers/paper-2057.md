---
id: paper-2057
title: 'Tri-AFLLM: Resource-Efficient Adaptive Asynchronous Accelerated Federated LLMs'
authors:
- Qiao, Dewen
- Ao, Xiang
- Liu, Yu
- Chen, Xuetao
- Song, Fuyuan
- Qin, Zheng
- Jin, Wenqiang
venue: IEEE Transactions on Circuits and Systems for Video Technology
venue_type: journal
year: 2025
doi: 10.1109/TCSVT.2024.3519790
url: https://www.scopus.com/pages/publications/85212758037?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4198--4211
keywords:
- edge intelligence
- Federated learning
- large language models
- momentum gradient descent
- resource efficiency
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-2057 — Tri-AFLLM: Resource-Efficient Adaptive Asynchronous Accelerated Federated LLMs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The local deployment of federated large language models (FLLM) has further advanced the development of edge intelligence. However, the resource constraints of end devices, device heterogeneity, and the non-independent and identically distributed (Non-IID) nature of data pose significant challenges to the application of FLLM. To address this issue, we propose an Adaptive Asynchronous Accelerated FLLM (Tri-AFLLM) algorithm to achieve the efficient utilization of limited resources and improve model accuracy in the edge computing (EC) scenarios. Specifically, Tri-AFLLM first ships an off-the-shelf LLM, i.e., CLIP, to each end device, keeping the backbone parameters frozen and updating only the parameters of the adapter containing two linear transformation layers by using momentum gradient descent (MGD). Next, a toy example is provided to illustrate the necessity of using different numbers of local iterations for heterogeneous devices in resource-constrained environments. Subsequently, the convergence bound of the Tri-AFLLM under a given resource budget is discussed. Then, we formulated the bound into a resource consumption minimization problem with the number of local iterations as the optimization variable under a given model accuracy to mitigate the contribution disparity of local models to the global aggregation. Finally, extensive experiments are conducted to validate the superiority of Tri-AFLLM in terms of resource consumption, model accuracy, and addressing the Non-IID problem. © 1991-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs

The local deployment" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of federated large" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2057.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
