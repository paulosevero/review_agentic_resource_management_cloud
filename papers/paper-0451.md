---
id: paper-0451
title: Route Optimization using Hybrid GRU Learning Model for SDN and Edge-Based VANET Topology
authors:
- Kumar, Savitha
- Chinnasamy, Chandrasekar
venue: Journal of Computer Science
venue_type: journal
year: 2022
doi: 10.3844/jcssp.2022.743.756
url: https://www.scopus.com/pages/publications/85136637598?origin=resultslist
publisher: Science Publications
pages: 743--756
keywords:
- Edge computing
- Gru
- Ml
- Reinforcement learning
- Sdn
- Vanet
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0451 — Route Optimization using Hybrid GRU Learning Model for SDN and Edge-Based VANET Topology

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent Transportation System (ITS) offers outstanding features, including security applications and emergency alerts. Unfortunately, ITS limits traffic control services, adaptability, and adjustability due to the traffic volume. Hence, expanding the standard Vehicular Ad hoc Networks (VANET) framework is a requirement. As a result, in the latest days, the concept of Software-Defined Networking based Vehicular Ad hoc Networks (SDN-VANETs) has drawn considerable attention, creating VANETs smarter. The SDN-VANETs design is capable of addressing the aforementioned VANET issues. The integrated (analytically) SDN architecture is customizable and it also contains domain knowledge about the VANET architecture. Packet forwarding is a fundamental challenge in VANET wherein a router, as in the form of an RSU, determines the next hop of every signal in the pipeline to provide it to its recipient as fast as possible. Reinforcement Learning (RL) is used to develop autonomous routing protocol rules; however, the limitation of RL's depth prevents it from representing more comprehensively dynamic network conditions, restricting its true value. In this research, we present a VANET infrastructure based on SDN + EDGE with a new Deep Reinforcement Learning (DRL) route optimization framework, "Gated Recurrent Reinforcement Learning (GRRL)" neural network, whereby each router has its hybrid GRU + Feed Forward Neural Network (NN) for learning and making decisions in an entirely distributed environment. The GRRL collects routing characteristics from valuable information about huge backlog packets and previous operations, substantially approximating the weighting scheme of Q-learning. We also enable every route to connect with its immediate neighbors regularly such that a more comprehensive view of network topology may be integrated. Trial findings demonstrated that the multi-agent GRRL strategy could achieve a delicate balance between congestion awareness and the fastest routes, considerably reducing packet transmission time in general network topologies compared to its competitors. © 2022. Savitha Kumar and Chandrasekar Chinnasamy. This open-access article is distributed under a Creative Commons Attribution (CC-BY) 4.0 license.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0451.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
