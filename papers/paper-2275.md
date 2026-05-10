---
id: paper-2275
title: Multi-agent reinforcement learning for task offloading with hybrid decision space in multi-access edge computing
authors:
- Wang, Ji
- Zhang, Miao
- Yin, Quanjun
- Yin, Lujia
- Peng, Yong
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2024.103671
url: https://www.scopus.com/pages/publications/85204939127?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Hybrid action space
- Multi-access edge computing
- Multiagent proximal policy optimization (MAPPO)
- Reward design
- Task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2275 — Multi-agent reinforcement learning for task offloading with hybrid decision space in multi-access edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access Edge Computing (MEC) has become a significant technology for supporting the computation-intensive and time-sensitive applications on the Internet of Things (IoT) devices. However, it is challenging to jointly optimize task offloading and resource allocation in the dynamic wireless environment with constrained edge resource. In this paper, we investigate a multi-user and multi-MEC servers system with varying task request and stochastic channel condition. Our purpose is to minimize the total energy consumption and time delay by optimizing the offloading decision, offloading ratio and computing resource allocation simultaneously. As the users are geographically distributed within an area, we formulate the problem of task offloading and resource allocation in MEC system as a partially observable Markov decision process (POMDP) and propose a novel multi-agent deep reinforcement learning (MADRL) -based algorithm to solve it. In particular, two aspects have been modified for performance enhancement: (1) To make fine-grained control, we design a novel neural network structure to effectively handle the hybrid action space arisen by the heterogeneous variables. (2) An adaptive reward mechanism is proposed to reasonably evaluate the infeasible actions and to mitigate the instability caused by manual configuration. Simulation results show the proposed method can achieve 7.12%−20.97% performance enhancements compared with the existing approaches. © 2024 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2275.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
