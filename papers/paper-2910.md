---
id: paper-2910
title: 'EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices'
authors:
- Zhang, Yutao
- Zhong, Wentao
- Liu, Xuerui
- Huang, Fengyi
- Wang, Wenhua
- Wang, Tian
- Jia, Weijia
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-5012-8_34
url: https://www.scopus.com/pages/publications/105028311673?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 457--465
keywords:
- Edge LLM inference
- Heterogeneous
- KV cache
- Tensor parallelism
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2910 — EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Model (LLM) inference heavily relies on cloud systems, resulting in inherent limitations such as prolonged delays, escalated bandwidth expenditure, and potential data security risks. Edge computing emerges as a solution by enabling LLM execution on edge devices, closer to data sources. However, challenges such as device heterogeneity and limited memory capacity pose significant barriers to conventional tensor parallelism of LLM. Therefore, we propose EdgeInfer-TP, a resource-aware collaborative tensor parallelism inference system tailored for heterogeneous edge devices. It integrates MILP-based model allocation optimization and multi-level dynamic offloading of KV cache to enable efficient and stable collaborative inference on resource-constrained devices. The experimental results across multiple real-world heterogeneous devices and diverse network environments demonstrate that our approach achieves up to 22.23% latency reduction and 27.87% throughput improvement over baseline approaches. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2910.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
