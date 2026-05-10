---
id: paper-0121
title: A Learning Algorithm for Real-Time Service in Vehicular Networks with Mobile-Edge Computing
authors:
- Dai, Penglin
- Liu, Kai
- Wu, Xiao
- Xing, Huanlai
- Yu, Zhaofei
- Lee, Victor C. S.
venue: IEEE International Conference on Communications
venue_type: conference
year: 2019
doi: 10.1109/ICC.2019.8761190
url: https://www.scopus.com/pages/publications/85070194788?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge computing
- Information services
- Multi agent systems
- Network architecture
- Optimal systems
- Real time systems
- Reinforcement learning
- Vehicles
- Cloud based computing
- Heterogeneous computing
- Multi-agent reinforcement learning
- Optimal solutions
- Real time service
- Vehicular mobilities
- Vehicular networks
- Wireless coverage
- Learning algorithms
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0121 — A Learning Algorithm for Real-Time Service in Vehicular Networks with Mobile-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is an emerging paradigm to offload the server-side resources closer to the mobile terminals compared with cloud-based computing. However, due to highly vehicular mobility and limited wireless coverage, it is challenging to apply off-the-shelf MEC-based architecture to support the real-time services in vehicular networks, especially when the vehicle density changes dynamically. Hence, this paper investigates a novel service scenario in an MEC-based architecture, where the local MEC server has to complete the real-time services of mobile vehicles in its service range. On this basis, we formulate a novel problem of distributed real-time service scheduling (DRSS) by comprehensively considering the delay requirements of real-time services, the heterogeneous computing capabilities of MEC servers and the mobility features of vehicles, which targets at maximizing the service ratio. To resolve such an issue, we propose a multi-agent reinforcement learning algorithm called Utility-based Learning (UL), in which each local MEC server selects the optimal solution by learning the global knowledge online. Specifically, a utility table is established to determine the optimal solution by estimating the pending delay of service request at each MEC server and it will be updated periodically based on the feedback signal from the assigned MEC server. Lastly, we build the simulation model and conduct an extensive performance evaluation, which demonstrates the superiority of the proposed algorithm. © 2019 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0121.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
