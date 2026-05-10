---
id: paper-1202
title: UAV-Assisted Heterogeneous Multi-Server Computation Offloading With Enhanced Deep Reinforcement Learning in Vehicular Networks
authors:
- Song, Xiaoqin
- Zhang, Wenjing
- Lei, Lei
- Zhang, Xinting
- Zhang, Lijuan
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2024
doi: 10.1109/TNSE.2024.3446667
url: https://www.scopus.com/pages/publications/85201789212?origin=resultslist
publisher: IEEE Computer Society
pages: 5323--5335
keywords:
- Computation offloading
- deep reinforcement learning
- Internet of Vehicles
- multi-access edge computing (MEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1202 — UAV-Assisted Heterogeneous Multi-Server Computation Offloading With Enhanced Deep Reinforcement Learning in Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of intelligent transportation systems (ITS), computation-intensive and latency-sensitive applications are flourishing, posing significant challenges to resource-constrained task vehicles (TVEs). Multi-access edge computing (MEC) is recognized as a paradigm that addresses these issues by deploying hybrid servers at the edge and seamlessly integrating computing capabilities. Additionally, flexible unmanned aerial vehicles (UAVs) serve as relays to overcome the problem of non-line-of-sight (NLoS) propagation in vehicle-to-vehicle (V2V) communications. In this paper, we propose a UAV-assisted heterogeneous multi-server computation offloading (HMSCO) scheme. Specifically, our optimization objective to minimize the cost, measured by a weighted sum of delay and energy consumption, under the constraints of reliability requirements, tolerable delay, and computing resource limits, among others. Since the problem is non-convex, it is further decomposed into two sub-problems. First, a game-based binary offloading decision (BOD) is employed to determine whether to offload based on the parameters of computing tasks and networks. Then, a multi-agent enhanced dueling double deep Q-network (ED3QN) with centralized training and distributed execution is introduced to optimize server offloading decision and resource allocation. Simulation results demonstrate the good convergence and robustness of the proposed algorithm in a highly dynamic vehicular environment. © 2024 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1202.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
