---
id: paper-0851
title: Distributed Multi-Agent Reinforcement Learning for Collaborative Path Planning and Scheduling in Blockchain-Based Cognitive Internet of Vehicles
authors:
- Chang, Huigang
- Liu, Yiming
- Sheng, Zhengguo
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2023.3344934
url: https://www.scopus.com/pages/publications/85182350261?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6301--6317
keywords:
- Cognitive Internet of Vehicles (CIoVs)
- load balancing
- mobile edge computing (MEC)
- multi-agent reinforcement learning
- path planning and scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0851 — Distributed Multi-Agent Reinforcement Learning for Collaborative Path Planning and Scheduling in Blockchain-Based Cognitive Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The collaborative path planning and scheduling can overcome the limitations of single vehicle intelligence to obtain a globally optimal decision strategy in cognitive Internet of Vehicles (CIoVs). The collaboration of vehicles necessitates the exchange of environmental and decision information, generating massive collaborative computing tasks with strict latency requirements. Leveraging mobile edge computing (MEC) technology, computing tasks can be processed near the vehicles to reduce latency. However, traffic congestion and computational load imbalance seriously affect traffic efficiency and computational latency. In hybrid driving scenarios, it is challenging to fulfill the diverse service requirements of vehicles with different intelligence levels. Moreover, non-collaborative tend to result in traffic congestion due to vehicle aggregation effects, while centralized solutions lack flexibility and have high computational complexity. To address these concerns, a distributed multi-agent reinforcement learning (DMARL) algorithm is proposed for collaborative path planning and scheduling in a blockchain-based collaboration framework. In this framework, we model the communication, traffic situation and task processing of the system and formulate a joint optimization problem to minimize both travel time and computation latency. Last, we convert the scheduling problem for different types of vehicles into Markov decision processes (MDPs) and propose Q-learning-based DMARL algorithm to achieve proactive load balancing of both road infrastructures and MEC nodes (MECNs). Simulation results demonstrate that the proposed approach outperforms the comparison schemes in terms of load balance indexes of roads and MECNs, travel time, and computation latency.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0851.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
