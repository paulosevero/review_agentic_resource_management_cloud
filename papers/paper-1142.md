---
id: paper-1142
title: Joint Task Allocation and Trajectory Optimization for Multi-UAV Collaborative Air-Ground Edge Computing
authors:
- Qin, Peng
- Li, Jinghan
- Zhang, Jing
- Fu, Yang
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2024
doi: 10.1109/TNSE.2024.3481061
url: https://www.scopus.com/pages/publications/85207462294?origin=resultslist
publisher: IEEE Computer Society
pages: 6231--6243
keywords:
- Lyapunov optimization
- Multi-Agent Deep Deterministic Policy Gradients (MADDPG)
- Multi-UAV collaborative air-ground edge computing
- resource allocation
- trajectory optimization
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

# paper-1142 — Joint Task Allocation and Trajectory Optimization for Multi-UAV Collaborative Air-Ground Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the proliferation of Internet of Things (IoT), compute-intensive and latency-critical applications continue to emerge. However, IoT devices in isolated locations have insufficient energy storage as well as computing resources and may fall outside the service range of ground communication networks. To overcome the constraints of communication coverage and terminal resource, this paper proposes a multiple Unmanned Aerial Vehicle (UAV)-assisted air-ground collaborative edge computing network model, which comprises associated UAVs, auxiliary UAVs, ground user devices (GDs), and base stations (BSs), intending to minimize the overall system energy consumption. It delves into task offloading, UAV trajectory planning and edge resource allocation, which thus is classified as a Mixed-Integer Nonlinear Programming (MINLP) problem. Worse still, the coupling of long-term task queuing delay and short-term offloading decision makes it challenging to address the original issue directly. Therefore, we employ Lyapunov optimization to transform it into two sub-problems. The first involves task offloading for GDs, trajectory optimization for associated UAVs as well as auxiliary UAVs, which is tackled using Deep Reinforcement Learning (DRL), while the second deals with task partitioning and computing resource allocation, which we address via convex optimization. Through numerical simulations, we verify that the proposed approach outperforms other benchmark methods regarding overall system energy consumption.  © 2024 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1142.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
