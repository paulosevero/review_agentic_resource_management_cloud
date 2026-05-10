---
id: paper-2016
title: Energy-Efficient Task Computation at the Edge for Vehicular Services
authors:
- Parastar, Paniz
- Caso, Giuseppe
- Iglesias, Jesus Alberto Omana
- Lutu, Andra
- Alay, Ozgu
venue: Proceedings of IEEE/IFIP Network Operations and Management Symposium 2025, NOMS 2025
venue_type: conference
year: 2025
doi: 10.1109/NOMS57970.2025.11073636
url: https://www.scopus.com/pages/publications/105012206789?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computation offloading
- Computational efficiency
- Energy efficiency
- Energy utilization
- Green computing
- Intelligent agents
- Mobile telecommunication systems
- Autonomous driving
- Car mobility
- Computational resources
- Computing sites
- Edge computing
- Energy efficient
- Low latency
- Multiaccess
- Optimal performance
- Static scenarios
- Multi agent systems
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

# paper-2016 — Energy-Efficient Task Computation at the Edge for Vehicular Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-Access Edge Computing (MEC) is a promising solution for providing the computational resources and low latency required by vehicular services, such as autonomous driving. It enables cars to offload computationally intensive tasks to nearby servers. Effective offloading involves determining when to offload tasks, selecting the appropriate MEC site, and efficiently allocating resources to ensure optimal performance. While car mobility poses significant challenges to guaranteeing reliable task completion, today we lack energy-efficient solutions to solve this problem, especially when considering real-world car mobility traces. In this paper, we begin by examining the mobility patterns of cars using data obtained from a leading mobile network operator in Europe. Based on the insights from this analysis, we design an optimization problem for task computation/offloading, considering both static and mobility scenarios. Our objective is to minimize the total energy consumption - both at the cars and the MEC nodes - while satisfying the latency requirements of various tasks. We evaluate our solution, based on multi-agent reinforcement learning, both in simulations as well as in a realistic setup that relies on datasets from the operator. Our solution shows a significant reduction of user dissatisfaction and task interruptions in both static and mobile scenarios, while achieving energy savings of 47% (static) and 14% (mobile) compared to state-of-the-art schemes.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2016.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
