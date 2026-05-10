---
id: paper-0835
title: Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks
authors:
- Betalo, Mesfin Leranso
- Leng, Supeng
- Abishu, Hayla Nahom
- Seid, Abegaz Mohammed
- Fakirah, Maged
- Erbad, Aiman
- Guizani, Mohsen
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2024
doi: 10.1109/TNSM.2024.3454217
url: https://www.scopus.com/pages/publications/85203645296?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6527--6541
keywords:
- Deep reinforcement learning
- energy harvesting
- laser technology
- mobile edge computing
- unmanned aerial vehicles
- wireless sensor networks
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0835 — Multi-Agent DRL-Based Energy Harvesting for Freshness of Data in UAV-Assisted Wireless Sensor Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In sixth-generation (6G) networks, unmanned aerial vehicles (UAVs) are expected to be widely used as aerial base stations (ABS) due to their adaptability, low deployment costs, and ultra-low latency responses. However, UAVs consume large amounts of power to collect data from multiple sensor nodes (SNs). This can limit their flight time and transmission efficiency, resulting in delays and low information freshness. In this paper, we present a multi-access edge computing (MEC)-integrated UAV-assisted wireless sensor network (WSN) with a laser technology-based energy harvesting (EH) system that makes the UAV act as a flying energy charger to address these issues. This work aims to minimize the age of information (AoI) and improve energy efficiency by jointly optimizing the UAV trajectories, EH, task scheduling, and data offloading. The joint optimization problem is formulated as a Markov decision process (MDP) and then transformed into a stochastic game model to handle the complexity and dynamics of the environment. We adopt a multi-agent deep Q-network (MADQN) algorithm to solve the formulated optimization problem. With the MADQN algorithm, UAVs can determine the best data collection and EH decisions to minimize their energy consumption and efficiently collect data from multiple SNs, leading to reduced AoI and improved energy efficiency. Compared to the benchmark algorithms such as deep deterministic policy gradient (DDPG), Dueling DQN, asynchronous advantage actor-critic (A3C) and Greedy, the MADQN algorithm has a lower average AoI and improves energy efficiency by 95.5%, 89.9%, 78.02% and 65.52% respectively.  © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0835.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
