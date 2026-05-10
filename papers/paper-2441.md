---
id: paper-2441
title: Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks
authors:
- Zhang, Zhenyu
- Lu, Lu
- Li, Qin
- Chai, Yuhao
- Wu, Di
- Zhang, Yong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3587979
url: https://www.scopus.com/pages/publications/105010344392?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 39042--39060
keywords:
- artificial intelligence (AI) service placement
- digital twin
- Internet of Things (IoT)
- mean-field multiagent reinforcement learning (MARL)
- task scheduling
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2441 — Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As Internet of Things (IoT)-based artificial intelligence (AI) applications grow, the surge in computational and communication demands has raised concerns about energy consumption, making it critical for 6G networks to address this challenge. This article examines the joint optimization of AI service placement, task scheduling, and computing resource allocation in an edge-network-cloud system to minimize long-term energy consumption. These problems are interdependent: AI service placement determines service locations, influencing task scheduling, which in turn dictates computing resource allocation. The key challenge lies in the coupling of these variables and the two time-scale nature of the problem, involving long-term (AI service placement) and short-term (task scheduling and computing resource allocation) strategies. To address this, a hierarchical Markov decision process (HMDP) framework is proposed for efficient and coordinated optimization across time scales. A hierarchical mean-field dueling double deep Q-network (HMFD3QN) algorithm is developed within this framework, where the upper layer optimizes AI service placement, and the lower layer manages task scheduling and computing resource allocation. By integrating mean-field theory, the algorithm reduces the complexity of multiagent interactions. The computing resource allocation problem is shown to be convex when other variables are fixed, and an optimal strategy is derived using Karush–Kuhn–Tucker (KKT) conditions to simplify the action space for reinforcement learning. Experimental results demonstrate that the proposed method can reduce energy consumption by up to 34% compared to baseline methods, significantly improve queue stability, and increase the proportion of tasks meeting QoS requirements. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2441.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
