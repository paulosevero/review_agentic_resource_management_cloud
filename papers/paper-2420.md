---
id: paper-2420
title: 'Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks'
authors:
- Zhang, Xinyuan
- Nie, Jiangtian
- Huang, Yudong
- Xie, Gaochang
- Xiong, Zehui
- Liu, Jiang
- Niyato, Dusit
- Shen, Xuemin
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2025
doi: 10.1109/TWC.2024.3497923
url: https://www.scopus.com/pages/publications/85210074556?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 643--658
keywords:
- edge inference
- Generative AI
- multiuser edge computing
- wireless networks
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

# paper-2420 — Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Generative Artificial Intelligenge (GAI) is revolutionizing the world with its unprecedented content creation ability. Large Language Model (LLM) is one of its most embraced branches. However, due to LLM's substantial size and resource-intensive nature, it is cloud-hosted, raising concerns about privacy, usage limitations, and latency. In this paper, we propose to utilize ubiquitous distributed wireless edge computing resources for real-time LLM inference. Specifically, we introduce a novel LLM edge inference framework, incorporating batching and model quantization to ensure high throughput inference on resource-limited edge devices. Then, based on the architecture of transformer decoder-based LLMs, we formulate an edge inference optimization problem which is NP-hard, considering batch scheduling and joint allocation of communication and computation resources. The solution is the optimal throughput under edge resource constraints and heterogeneous user requirements on latency and accuracy. To solve this NP-hard problem, we develop an OT-GAH (Optimal Tree-search with Generalized Assignment Heuristics) algorithm with reasonable complexity and $ {1}{2}$ -approximation ratio. We first design the OT algorithm with online tree-pruning for single-edge-node multi-user case, which navigates the inference request selection within the tree structure to miximize throughput. We then consider the multi-edge-node case and propose the GAH algorithm, which recrusively invokes the OT in each node's inference scheduling iteration. Simulation results demonstrate the superiority of OT-GAH batching over other benchmarks, revealing an over 45% time complexity reduction compared to brute-force searching. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2420.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
