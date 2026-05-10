---
id: paper-1929
title: 'Optimizing Profit and Delay in Computing Power Network via Deep Deterministic Policy Gradient: A Task Decomposition and Computing Path Optimization Approach'
authors:
- Ma, Bo
- Hu, Xiaosen
- Pan, Yexin
- Lu, Qin
- Li, Chuanhuang
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2025
doi: 10.1109/TSC.2025.3570862
url: https://www.scopus.com/pages/publications/105005439173?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2295--2309
keywords:
- Computing power architecture
- computing power network (CPN)
- convex optimization theory
- deep reinforcement learning
- scheduling strategy
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1929 — Optimizing Profit and Delay in Computing Power Network via Deep Deterministic Policy Gradient: A Task Decomposition and Computing Path Optimization Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the contemporary landscape of computationally intensive applications, Computing Power Network (CPN) offers a solution to enhance computational efficiency and cost-effectiveness by integrating and sharing computing resources. However, with the surge in task volume within multi-user environments, effectively scheduling these tasks to optimize system profit and delay presents a significant challenge. This article introduces an optimization approach leveraging Deep Deterministic Policy Gradient (DDPG) to enhance CPN performance through task decomposition and computing path optimization. We initially construct a multi-layer CPN system model encompassing cloud computing, edge computing, and terminal device layers. Subsequently, we integrate a novel mechanism for convex optimization-based task decomposition, enabling intelligent subdivision of tasks into sub-tasks and dynamic allocation to suitable nodes within the network. Furthermore, we devise a Convex Optimization Task Decomposition-based Multi-Agent Deep Deterministic Policy Gradient (CO-MADDPG) algorithm, empowering multiple computing tasks as independent agents to learn and identify optimal offloading paths and computing nodes, thereby minimizing delay and maximizing system profit. A series of simulation experiments validate the effectiveness of the CO-MADDPG algorithm in handling concurrent tasks, demonstrating its capability to reduce task completion times, enhance system revenue, and maintain adaptability and stability across varying task demands. © 2008-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1929.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
