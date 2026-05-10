---
id: paper-0340
title: 'Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach'
authors:
- Seid, Abegaz Mohammed
- Boateng, Gordon Owusu
- Anokye, Stephen
- Kwantwi, Thomas
- Sun, Guolin
- Liu, Guisong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2021
doi: 10.1109/JIOT.2021.3063188
url: https://www.scopus.com/pages/publications/85102274239?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12203--12218
keywords:
- Collaborative computation offloading
- deep reinforcement learning (DRL)
- Edge Internet of Things (EIoT)
- IoT network
- multi-UAV network
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0340 — Collaborative Computation Offloading and Resource Allocation in Multi-UAV-Assisted IoT Networks: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the fifth-generation (5G) wireless networks, Edge-Internet-of-Things (EIoT) devices are envisioned to generate huge amounts of data. Due to the limitation of computation capacity and battery life of devices, all tasks cannot be processed by these devices. However, mobile-edge computing (MEC) is a very promising solution enabling offloading of tasks to nearby MEC servers to improve quality of service. Also, during emergency situations in areas where network failure exists, unmanned aerial vehicles (UAVs) can be deployed to restore the network by acting as Aerial Base Stations and computational nodes for the edge network. In this article, we consider a central network controller who trains observations and broadcasts the trained data to a multi-UAV cluster network. Each UAV cluster head acts as an agent and autonomously allocates resources to EIoT devices in a decentralized fashion. We propose model-free deep reinforcement learning (DRL)-based collaborative computation offloading and resource allocation (CCORA-DRL) scheme in an aerial to ground (A2G) network for emergency situations, which can control the continuous action space. Each agent learns efficient computation offloading policies independently in the network and checks the statuses of the UAVs through Jain's Fairness index. The objective is minimizing task execution delay and energy consumption and acquiring an efficient solution by adaptive learning from the dynamic A2G network. Simulation results reveal that our scheme through deep deterministic policy gradient, effectively learns the optimal policy, outperforming A3C, deep $Q$ -network and greedy-based offloading for local computation in stochastic dynamic environments. © 2014 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0340.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
