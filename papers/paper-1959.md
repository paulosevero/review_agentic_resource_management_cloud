---
id: paper-1959
title: Achieving Cost Efficiency in Cloud Data Centers Through Model-Free Q-Learning
authors:
- Mohammadi, Parisa
- Nasiri, Aliakbar
- Darshi, Razieh
- Shirzad, Arman
- Abdollahipour, Razieh
venue: Lecture Notes in Electrical Engineering
venue_type: conference
year: 2025
doi: 10.1007/978-981-97-9112-5_27
url: https://www.scopus.com/pages/publications/85219206791?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 457--468
keywords:
- Cloud data center
- Energy management
- Q-learning
- Renewable energy
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

# paper-1959 — Achieving Cost Efficiency in Cloud Data Centers Through Model-Free Q-Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing data centers play a critical role in storing, processing, and accessing vast amounts of digital information. They are essential infrastructures that support modern businesses, scientific research, communication networks, and various online services relying on reliable and efficient data management. However, their substantial energy consumption poses challenges in terms of operational costs and environmental sustainability. As a result, this paper investigates the utilization of distributed energy resources such as photovoltaics and wind turbines to reduce reliance on fossil fuels and achieve sustainability goals. Due to the intermittent and stochastic nature of these energy resources, traditional model-based methods are insufficient. Therefore, we propose a novel model-free Q-learning approach to address the challenges and ensure reliable and consistent power supply within data center operations. In the proposed structure, producers and consumers are modeled as autonomous agents within a multi-agent framework, making decisions to maximize their rewards. This paper addresses the hour-ahead energy scheduling problem using this approach, aiming to effectively manage the data center’s load demand and optimize distributed energy resources. By formulating the problem as a Markov Decision Process (MDP) and employing Q-learning, our study demonstrates increased energy producer profits and reduced data center costs. Finally, the proposed method is validated through simulation using real-world power datasets. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1959.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
