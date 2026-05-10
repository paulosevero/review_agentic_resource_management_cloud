---
id: paper-2610
title: MADQN-Enhanced Computation Offloading and Resource Allocation for 6G Low-Altitude Economy Vehicular Networks
authors:
- Hu, Bintao
- Liu, Hengyan
- Du, Jianbo
- López-Benitez, Miguel
- Wu, Celimuge
- Chu, Xiaoli
- Niyato, Dusit
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2025.3586868
url: https://www.scopus.com/pages/publications/105010323253?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2603--2617
keywords:
- deep reinforcement learning
- digital twins
- Low-altitude economy
- multi-agent deep Q-network
- UAV
- V2X communications
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2610 — MADQN-Enhanced Computation Offloading and Resource Allocation for 6G Low-Altitude Economy Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Air-to-ground communication networks in future sixth-generation (6G) networks are expected to leverage integrated sensing and communication (ISAC) to support the low-altitude economy (LAE). In such networks, a set of unmanned aerial vehicles (UAVs) acting as mobile edge computing (MEC) servers cooperatively process delay-sensitive tasks offloaded by multiple authorised vehicular user equipments (V-UEs). However, the diverse, stringent requirements of ISAC-enabled V-UE services require more intelligent and efficient resource allocation for the LAE-aided vehicle-to-everything (V2X) communications systems. To address this issue, we propose a digital twin (DT)-empowered multi-agent LAE MEC vehicular framework, where the DT technology enables real-time data collection, processing, monitoring, and optimisation in a virtual environment. Meanwhile, each V-UE may offload its delay-sensitive task to a UAV-assisted MEC server. We aim to minimise the long-term average total service delay (which may include the task processing delay and the transmission delay) of all V-UEs, the computation resource allocation at each UAV-assisted MEC server, the transmission power, and the allocation of resource blocks for all V-UEs. To solve the joint optimisation problem, we propose a Multi-agent deep Q-network-based Offloading and Resource allocation Optimisation (MORO) algorithm. Simulation results demonstrate that our proposed algorithm outperforms the benchmarks in terms of the convergence rate and the long-term average total service delay of all V-UEs. © 2015 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2610.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
