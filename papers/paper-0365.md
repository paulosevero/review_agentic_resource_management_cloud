---
id: paper-0365
title: A new task offloading algorithm in edge computing
authors:
- Zhang, Zhenjiang
- Li, Chen
- Peng, ShengLung
- Pei, Xintong
venue: Eurasip Journal on Wireless Communications and Networking
venue_type: journal
year: 2021
doi: 10.1186/s13638-021-01895-6
url: https://www.scopus.com/pages/publications/85099775936?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Deep reinforcement learning
- Edge computing
- Internet of things
- Load balancing
- Task offload
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0365 — A new task offloading algorithm in edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the last few years, the Internet of Things (IOT), as a new disruptive technology, has gradually changed the world. With the prosperous development of the mobile Internet and the rapid growth of the Internet of Things, various new applications continue to emerge, such as mobile payment, face recognition, wearable devices, driverless, VR/AR, etc. Although the computing power of mobile terminals is getting higher and the traditional cloud computing model has higher computing power, it is often accompanied by higher latency and cannot meet the needs of users. In order to reduce user delay to improve user experience, and at the same time reduce network load to a certain extent, edge computing, as an application of IOT, came into being. In view of the new architecture after dating edge computing, this paper focuses on the task offloading in edge computing, from task migration in multi-user scenarios and edge server resource management expansion, and proposes a multi-agent load balancing distribution based on deep reinforcement learning DTOMALB, a distributed task allocation algorithm, can perform a reasonable offload method for this scenario to improve user experience and balance resource utilization. Simulations show that the algorithm has a certain adaptability compared to the traditional algorithm in the scenario of multi-user single cell, and reduces the complexity of the algorithm compared to the centralized algorithm, and reduces the average response delay of the overall user. And balance the load of each edge computing server, improve the robustness and scalability of the system. © 2021, The Author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0365.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
