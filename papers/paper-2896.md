---
id: paper-2896
title: 'Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach'
authors:
- Yu, Zihang
- Zhang, Zhenjiang
- Zeadally, Sherali
venue: Journal of Industrial Information Integration
venue_type: journal
year: 2026
doi: 10.1016/j.jii.2025.101037
url: https://www.scopus.com/pages/publications/105024310480?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Edge computing
- Industrial Internet of Things
- Lyapunov optimization
- Reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2896 — Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access Edge Computing (MEC) integrated with the Industrial Internet of Things (IIoT) is vital for intelligent manufacturing and industrial automation because it enables low-latency and high-efficiency task offloading from resource-limited devices to an edge server. However, dynamic wireless channels and stochastic task arrivals introduce significant uncertainties, leading to queuing delays, inefficient resource utilization, and high energy consumption. Moreover, the lack of future system information makes real-time offloading decisions particularly challenging. To address these issues, we construct both task queues and delay-aware virtual queues, and we formulate a stochastic optimization problem for joint task offloading and resource allocation. The objective is to minimize long-term energy consumption while ensuring queue stability and satisfying task deadline constraints. To solve this problem, we propose a novel Lyapunov-guided multi-agent deep reinforcement learning framework (LYMADDPG), which integrates Lyapunov optimization with Multi-Agent Deep Deterministic Policy Gradient (MADDPG). Specifically, we use Lyapunov optimization to transform delay constraints into a virtual queue stability control problem, converting the original long-term problem into a series of per-slot optimizations. Next, we use MADDPG to learn optimal offloading and resource allocation policies in a distributed and adaptive manner. Extensive simulation results demonstrate that our method significantly outperforms baseline algorithms in reducing energy consumption, ensuring queue stability, and meeting task deadlines. These results confirm the practical effectiveness of our approach and highlight its strong potential for real-world deployment in MEC-enabled IIoT systems. © 2025 Elsevier Inc.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2896.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
