---
id: paper-0366
title: Cooperative multi-agent actor–critic control of traffic network flow based on edge computing
authors:
- Zhang, Yongnan
- Zhou, Yonghua
- Lu, Huapu
- Fujita, Hamido
venue: Future Generation Computer Systems
venue_type: journal
year: 2021
doi: 10.1016/j.future.2021.04.018
url: https://www.scopus.com/pages/publications/85105361041?origin=resultslist
publisher: Elsevier B.V.
pages: 128--141
keywords:
- Cooperative multi-agent actor–critic framework
- Distributed deep reinforcement learning
- Edge computing
- Traffic network flow control
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0366 — Cooperative multi-agent actor–critic control of traffic network flow based on edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Most of the existing traffic signal control strategies are hard to satisfy the real-time requirements of traffic big data analysis, knowledge reasoning and decision making for sophisticated traffic dynamics and heterogeneous intersection structures in the context of Internet of Vehicles (IoV). In this paper, we attempt to propose a cooperative multi-agent actor–critic (CMAC) deep reinforcement learning (DRL) approach with value decomposition based on edge computing architecture. The intuition behind CMAC is to decompose the global actor–critic learning tasks into several local actor–critic​ sub-problems with respect to each intersection. Each agent searches the local optimal decision by actor–critic network that takes the discrete state encoding about several consecutive frames of image-like traffic states as the inputs of the network. Among them, the green ratio output strategy considering multiple constraints is formulated in the output layer of the actor network, so that the continuous control of traffic signals using multi-agent DRL (MADRL) can be realized. Furthermore, a cooperative mechanism that considers contribution weight distributions of local agents to the global traffic pattern is proposed to coordinate multiple local agents to evolve toward global optimization. Especially, some parallel training tasks of CMAC with a large number of computing loads are deployed on the cloud side in the edge computing architecture to accelerate learning and reconstructing knowledge. The well-trained multi-agent model is downloaded from the cloud side into the edge side for real-time decision making of traffic network flow adaptive control. Simulation results with regard to a realistic traffic network demonstrate that the proposed CMAC approach under edge computing architecture outperforms the value-decomposition based multi-agent actor–critic (VMAC), independent multi-agent actor–critic (IMAC), and the fixed timing control (FTC) in terms of alleviating traffic congestion. © 2021

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0366.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
