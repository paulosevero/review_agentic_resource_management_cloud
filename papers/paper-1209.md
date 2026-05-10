---
id: paper-1209
title: Accelerating Convergence of Federated Learning in MEC With Dynamic Community
authors:
- Sun, Wen
- Zhao, Yong
- Ma, Wenqiang
- Guo, Bin
- Xu, Lexi
- Duong, Trung Q.
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2023.3241770
url: https://www.scopus.com/pages/publications/85148413843?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1769--1784
keywords:
- Deep reinforcement learning
- edge intelligence
- federated learning
- resource allocation
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

# paper-1209 — Accelerating Convergence of Federated Learning in MEC With Dynamic Community

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) brings computational resources to the edge of network that triggers the paradigm shift of centralized machine learning towards federated learning. Federated learning enables edge nodes to collaboratively train a shared prediction model without sharing data. In MEC, heterogeneous edge nodes may join or leave the training phase during the federated learning process, resulting in slow convergence of dynamic communities and federated learning. In this paper, we propose a fine-grained training strategy for federated learning to accelerate its convergence rate in MEC with dynamic community. Based on multi-agent reinforcement learning, the proposed scheme enables each edge node to adaptively adjust its training strategy (aggregation timing and frequency) according to the network dynamics, while compromising with each other to improve the convergence of federated learning. To further adapt to the dynamic community in MEC, we propose a meta-learning-based scheme where new nodes can learn from other nodes and quickly perform scene migration to further accelerate the convergence of federated learning. Numerical results show that the proposed framework outperforms the benchmarks in terms of convergence speed, learning accuracy, and resource consumption.  © 2002-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1209.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
