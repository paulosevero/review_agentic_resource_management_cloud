---
id: paper-1591
title: 'Placing Computational Tasks Within Edge-Cloud Continuum: A DRL Delay Minimization Scheme'
authors:
- Giannopoulos, Anastasios
- Suárez-Cetrulo, Andrés L.
- Masip-Bruin, Xavi
- D’Andria, Francesco
- Trakadas, Panagiotis
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-3-031-90203-1_4
url: https://www.scopus.com/pages/publications/105008684579?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 36--45
keywords:
- IoT-edge-cloud continuum (IECC)
- Reinforcement learning
- Resource allocation
- Task offloading
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

# paper-1591 — Placing Computational Tasks Within Edge-Cloud Continuum: A DRL Delay Minimization Scheme

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the rapidly evolving landscape of IoT-Edge-Cloud continuum (IECC), effective management of computational tasks offloaded from mobile devices to edge nodes is crucial. This paper presents a Distributed Reinforcement Learning Delay Minimization (DRL-DeMi) scheme for IECC task offloading. DRL-DeMi is a distributed framework engineered to tackle the challenges arising from the unpredictable load dynamics at edge nodes. It empowers each edge node to independently make offloading decisions, optimizing for non-divisible, latency-sensitive tasks without reliance on prior knowledge of other nodes’ task models and decisions. By framing the problem as a multi-agent computation offloading scenario, DRL-DeMi aims to minimize expected long-term latency and task drop ratio. Adhering to IECC requirements for seamless task flow within the Edge layer and between Edge-Cloud layers, DRL-DeMi considers three computation decision avenues: local computation, horizontal offloading to another edge node, or vertical offloading to the Cloud. Integration of advanced techniques such as long short-term memory (LSTM), double deep Q-network (DQN), and dueling DQN enhances long-term cost estimation, thereby refining decision-making efficacy. Simulation results validate DRL-DeMi’s superiority over baseline offloading algorithms, showcasing reductions in both task drop ratio and average delay. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1591.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
