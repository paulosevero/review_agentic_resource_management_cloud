---
id: paper-2817
title: Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence
authors:
- Wang, Peng
- Huang, Long
- Sun, Wen
- Yang, Yi
- Niyato, Dusit
- Wu, Dapeng Oliver
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3675369
url: https://www.scopus.com/pages/publications/105033388354?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge intelligence
- energy efficiency
- inference offloading
- multi-agent reinforcement learning
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

# paper-2817 — Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge intelligence deploys artificial intelligence models on edge nodes proximal to data sources, and delivers real-time inference support for resource-constrained devices. To realize this vision, inference offloading differs from conventional computation offloading by tailoring offloading strategies to the intrinsic characteristics of AI inference tasks. In this field, existing researchs generally lack fine-grained model partitioning capabilities and long-term resource adaptability, failing to optimize resource utilization and sustain stable performance in mobile environments. To address these issues, we propose an adaptive inference acceleration framework that dynamically partitions inference models into hierarchical subtasks and offloads these subtasks to heterogeneous edge servers. We formulate a joint optimization problem for task partitioning, offloading and resource allocation, which takes queue stability as the constraint and aims to minimize the long-term average task completion time. To realize the optimal trade-off between latency and stability without future state prediction, we adopt Lyapunov optimization to decompose the long-term stochastic optimization into slot-by-slot solvable deterministic subproblems. For these slot-by-slot subproblems, we design a Q-network Mixing (QMIX)-based multi-agent reinforcement learning method to enable collaborative strategy selection across edge servers. Experimental simulations show that, compared with baseline algorithms including the greedy, genetic and MAD2RL methods, our proposed framework achieves a substantial reduction in task completion time while preserving inference accuracy and queue stability. © 2002-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2817.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
