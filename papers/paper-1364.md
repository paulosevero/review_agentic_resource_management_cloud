---
id: paper-1364
title: Low Complexity and Mobility-Aware Robust Radio, Storage, Computing, and Cost Management for Cellular Vehicular Networks
authors:
- Abedi, Mohammad Reza
- Mokari, Nader
- Javan, Mohammad Reza
- Saeedi, Hamid
- Jorswieck, Eduard A.
- Zorba, Nizar
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2024.3480996
url: https://www.scopus.com/pages/publications/85207371893?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3327--3344
keywords:
- demand and channel uncertainties
- Mobile edge computing
- RSU activation/deactivation
- task migration
- task partitioning
- two-time scale task offloading/delivery
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1364 — Low Complexity and Mobility-Aware Robust Radio, Storage, Computing, and Cost Management for Cellular Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, a novel two-time scale task offloading/delivery framework is presented which dynamically manages radio, storage, computing, and cost aspects through multiple Mobile Edge Computing (MEC) servers distributed across Road Side Units (RSUs), Base Stations (BSs), vehicles, and pedestrians. To enhance flexibility, we introduce a smart dynamic task partitioning and cooperative offloading/delivery mechanism, enabling users to offload task partitions to various MEC servers. Uncertainties stemming from users' high mobility and traffic variations may lead to unpredictable task offloading demands and Imperfect Channel State Information (I-CSI), potentially causing unsuccessful task offloading/delivery. In response, we propose a robust and cooperative two-time-scale task offloading/delivery approach, adept at handling demand uncertainty and I-CSI. The problem formulation involves a two-time scale Markov decision process, aimed at minimizing task offloading/delivery costs while maximizing task completion rates. Large time-scale slots incorporate intelligent RSU activation/deactivation, while short time-scale slots focus on task offloading/delivery. To efficiently implement this framework, we propose Federated Reinforcement Learning (FRL) algorithm based on Deep Deterministic Policy Gradient (DDPG); namely Low overhead Multi-Agent DDPG (LoMADDPG) where at each slot, all agents tune their Actor and Critic neural network weights with the help of Global Software-defined Networking (SDN) Controller (GSC) which acts as a global weight tuner. Simulation results illustrate that our proposed task offloading/delivery scheme can result in significant improvement in task completion rate and cost reduction. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1364.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
