---
id: paper-0508
title: Multi-Layer Computation Offloading in Distributed Heterogeneous Mobile Edge Computing Networks
authors:
- Wang, Pengfei
- Di, Boya
- Song, Lingyang
- Jennings, Nicholas R.
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2022
doi: 10.1109/TCCN.2022.3161955
url: https://www.scopus.com/pages/publications/85132004792?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1301--1315
keywords:
- distributed computing
- Minimum energy control
- resource management
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

# paper-0508 — Multi-Layer Computation Offloading in Distributed Heterogeneous Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we consider distributed heterogeneous multi-layer mobile edge computing (HetMEC) networks, where resource-poor edge devices (EDs) upload computing tasks for processing to the mobile edge computing (MEC) servers and a cloud center (CC). To reduce total energy consumption, computation offloading and resource allocation are independently performed by each device and each server. However, due to the partial information available at each device and server, the offloading strategies may overwhelm the layers above. This may lead to network congestion, i.e., so many tasks are offloaded to the same node that this node is overloaded. To address this problem, we develop a smart pricing mechanism to coordinate the computation offloading of multi-layer devices, where the CC charges the MEC servers and EDs for computing services and network congestion. In particular, to satisfy the latency constraints of each task, we construct a Lagrangian framework where multi-agent reinforcement learning is utilized by each MEC server to determine its offloading strategies and resource allocation, so that the total energy consumption is reduced. Simulation results show that our algorithm achieves an energy consumption reduction of 28% and a decrease in congestion probability of between 28% and 100% compared to the state of the art.  © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0508.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
