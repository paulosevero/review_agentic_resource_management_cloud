---
id: paper-2530
title: 'DR4SV: A Digital Twin-Enhanced Resource Allocation Mechanism for Satellite-Terrestrial Integrated Vehicular Networks'
authors:
- Chen, Yining
- Peng, Kai
- Zhao, Bohai
- Xu, Xiaolong
- Leung, Victor C. M.
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3665833
url: https://www.scopus.com/pages/publications/105030673502?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1148--1161
keywords:
- DRL
- DT
- IoV
- MEC
- satellite computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2530 — DR4SV: A Digital Twin-Enhanced Resource Allocation Mechanism for Satellite-Terrestrial Integrated Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Mobile Edge Computing (MEC)-Empowered Internet of Vehicles (IoVs), a transformative paradigm characterized by real-time decision-making and distributed processing via data offloading to the network edge, has garnered substantial research interest. Nonetheless, emerging applications such as autonomous driving pose dual challenges of computational bottlenecks and inadequate wide-area coverage in resource scheduling. To this end, we propose a Digital Twin (DT)-enhanced, satellite-assisted resource allocation framework that synergistically coordinates MEC and satellite networks while leveraging DTs for network virtualization and collaborative training, thereby fully exploiting the low-latency capabilities of edge computing, the high-capacity processing of satellite computing, and the cost-efficient simulation advantages of DT technology. During the training phase, we develop DR4SV, a Deep Reinforcement Learning (DRL)-based online optimization method that constructs specialized intelligent agents tailored for satellite-collaborative IoV scenarios. By incorporating depthwise over-parameterized convolutional layers, DR4SV enables multi-channel synergistic processing across heterogeneous communication channels while establishing robust policy alignment between physical agents and their DT counterparts. This architecture facilitates real-time state mapping and multi-dimensional parallel simulation within the digital space, enhancing resource allocation efficiency while dynamically balancing latency and energy consumption with accelerated convergence. Extensive experiments are conducted based on real-world datasets, encompassing hyperparameter configurations and rigorous performance evaluations. The numerical results demonstrate that DR4SV achieves reductions in both time and energy consumption, with optimization rates reaching up to 6.8% and 19.1%, respectively. Meanwhile, the correlation between DTs and physical entities reaches up to 97%, thereby validating the effectiveness and feasibility of DT technology in satellite-terrestrial integrated vehicular networks. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2530.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
