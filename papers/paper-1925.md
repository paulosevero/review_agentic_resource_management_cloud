---
id: paper-1925
title: Task Offloading and Resource Allocation for Satellite-Terrestrial Integrated Networks
authors:
- Lyu, Ting
- Xu, Yueqiang
- Liu, Feifei
- Xu, Haitao
- Han, Zhu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3465656
url: https://www.scopus.com/pages/publications/86000378544?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 262--275
keywords:
- Computing offloading
- deep reinforcement learning (DRL)
- multiagent
- resource allocation
- satellite-terrestrial integrated network (STIN)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1925 — Task Offloading and Resource Allocation for Satellite-Terrestrial Integrated Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —Low-Earth orbit (LEO) satellite networks can achieve global network coverage without geographical restrictions and are essential to the future communication network. In this article, we study the computing offloading problem in a satellite-terrestrial integrated network for the Internet of Remote Things (IoRT), which aims to reduce the total cost (weighted sum of energy consumption and delay), and jointly offload node selection, offloading ratio, and computational resource allocation to achieve the dynamic management of network resources. First, we propose a hybrid cloud and satellite multilayer multiaccess edge computing (MEC) network architecture that can provide heterogeneous computing resources to terrestrial users. Subsequently, since the problem under consideration is a mixed-integer nonlinear programming problem, we propose a computing offloading algorithm for multiagent reinforcement learning, which is an integration of double deep Q learning (DDQN) and deep deterministic policy gradient (DDPG). The algorithm can learn the optimal policy for actions containing a mixture of discrete and continuous variables. Finally, an optimal computational resource allocation scheme is proposed to improve the task computation efficiency. Simulation results show that the proposed task offloading and resource allocation scheme can achieve reasonable scheduling of computational tasks and optimal allocation of computational resources, reducing the cost of task computation. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1925.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
