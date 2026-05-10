---
id: paper-0647
title: Joint Optimization on Trajectory, Computation and Communication Resources in Information Freshness Sensitive MEC System
authors:
- Li, Haozhe
- Zhang, Jiao
- Zhao, Haitao
- Ni, Yiyang
- Xiong, Jun
- Wei, Jibo
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2023.3326808
url: https://www.scopus.com/pages/publications/85177062705?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4162--4177
keywords:
- Age of information (AoI)
- multi-agent reinforcement learning
- multi-unmanned aerial vehicle (UAV) assisted mobile edge computing (MEC)
- stochastic task queue
- trajectory planning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0647 — Joint Optimization on Trajectory, Computation and Communication Resources in Information Freshness Sensitive MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV) assisted mobile edge computing (MEC) can provide flexible coverage and computation services. It is attractive for emergency search, traffic control, disaster response, as well as other applications with desperate requirements for information freshness. In this work, we investigate a three-layer multi-UAV assisted MEC system with stochastic task arrival. In order to minimize the age of information (AoI), we jointly optimize the computation offloading, UAV trajectory and communication resources. In particular, we propose a heterogeneous federated multi-agent reinforcement learning algorithm based on a heterogeneous actor-critic framework. All entities in the three-layer MEC system act as both the actor to interact with the environment and the critic to learn optimal policies. Since the training of each agent in the framework is independent, a novel federated updating method is further adopted to enable cooperation among entities and solve the problem of non-stationary environment. Extensive simulation results validate that the proposed scheme outperforms the baseline schemes in terms of both the convergence and resulted AoI in the multi-UAV assisted MEC system. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0647.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
