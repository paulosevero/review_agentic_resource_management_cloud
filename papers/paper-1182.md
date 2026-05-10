---
id: paper-1182
title: Mean-field reinforcement learning for decentralized task offloading in vehicular edge computing
authors:
- Shen, Si
- Shen, Guojiang
- Yang, Xiaoxue
- Xia, Feng
- Du, Hao
- Kong, Xiangjie
venue: Journal of Systems Architecture
venue_type: journal
year: 2024
doi: 10.1016/j.sysarc.2023.103048
url: https://www.scopus.com/pages/publications/85179127778?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Digital twin
- Mean-field reinforcement learning
- Task offloading
- Vehicular edge computing
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

# paper-1182 — Mean-field reinforcement learning for decentralized task offloading in vehicular edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular Edge Computing (VEC) is a promising paradigm for providing low-latency and high-reliability services in the Internet of Vehicles (IoV). The increasing number of mobile devices and the diverse resource requirements of the growing IoV have resulted in a shift from centralized resource management to a decentralized approach. This shift offers improved fault tolerance, scalability, and privacy preservation. However, constructing collaborative awareness and coordination mechanisms between multiple vehicles and edge nodes in a decentralized manner is a challenge. To address this issue, we propose a decentralized many-to-many task offloading method that aims to minimize the average task completion latency of vehicles. In this study, we propose a data-sharing mechanism between vehicles and edge servers using the digital twin service, which provides global environmental perceptions to the vehicles by a low-cost approach. Additionally, we develop a mean-field multi-agent reinforcement learning algorithm to generate coordinated task offloading schemes. Instead of interacting with multiple agents, the vehicle only needs to respond to the mean action of the environment. Based on this transition, the agent generates coordinated task offloading decisions in complex scenarios. We evaluate the performance of our method using real urban traffic data. Experiment results verify the efficiency of our proposed method. © 2023 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1182.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
