---
id: paper-0510
title: 'Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach'
authors:
- Waqar, Noor
- Hassan, Syed Ali
- Mahmood, Aamir
- Dev, Kapal
- Do, Dinh-Thuan
- Gidlund, Mikael
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2022
doi: 10.1109/TITS.2022.3179987
url: https://www.scopus.com/pages/publications/85132757893?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 21478--21491
keywords:
- integrated aerial-terrestrial networks
- mobile edge computing (MEC)
- multi-agent reinforcement learning
- Sixth generation (6G)
- vehicular communication
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0510 — Computation Offloading and Resource Allocation in MEC-Enabled Integrated Aerial-Terrestrial Vehicular Networks: A Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As important services of the future sixth-generation (6G) wireless networks, vehicular communication and mobile edge computing (MEC) have received considerable interest in recent years for their significant potential applications in intelligent transportation systems. However, MEC-enabled vehicular networks depend heavily on network access and communication infrastructure, often unavailable in remote areas, making computation offloading susceptible to breaking down. To address this issue, we propose an MEC-enabled vehicular network assisted through aerial-terrestrial connectivity to provide network access and high data-rate entertainment services to a vehicular network. We present a time-varying, dynamic system model where high altitude platforms (HAPs) equipped with MEC servers, connected to a backhaul system of low-earth orbit (LEO) satellites, are used to provide computation offloading capability to the vehicles, as well as to provide network access for vehicle-to-vehicle (V2V) communications. Our main objective is to minimize the total computation and communication overhead of the joint computation offloading and resource allocation strategies for the system of vehicles. Since our formulated optimization problem is a mixed-integer non-linear programming (MINLP) problem, which is NP-hard, we propose a decentralized value-iteration-based reinforcement learning (RL) approach as a solution. In our Q-learning-assisted analysis, each vehicle acts as an intelligent agent to form optimal strategies for offloading and resource allocation. We further extend our solution to deep Q-learning (DQL) and double deep Q-learning to overcome the issues of dimensionality and the over-estimation of the value functions, as in Q-learning. Simulation results prove the effectiveness of our solution in successfully reducing system costs compared to baseline schemes.  © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0510.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
