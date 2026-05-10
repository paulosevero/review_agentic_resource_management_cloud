---
id: paper-1441
title: 'Trustworthy computation offloading in digital twin edge networks: A hierarchical game-based approach'
authors:
- Bounaira, Soumaya
- Alioua, Ahmed
- Vegni, Anna Maria
- Shayea, Ibraheem
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2025.104008
url: https://www.scopus.com/pages/publications/105017970426?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Blockchain
- Digital twin
- Game theory
- Mobile edge computing
- Task offloading
- Trust
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

# paper-1441 — Trustworthy computation offloading in digital twin edge networks: A hierarchical game-based approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid adoption of artificial intelligence (AI) across Internet of things (IoT) applications has intensified the demand for substantial computational resources. Due to the inherent resource limitations of IoT mobile devices, they are often unable to run most resource-intensive applications locally. Mobile edge computing (MEC) emerges as a promising solution, enabling task offloading to powerful edge servers. Although the technical aspects of task offloading are well-investigated in literature, the critical dimensions of security and trust concerns often remain under-explored. To address this gap, we introduce a blockchain-based trust management mechanism for digital Twin (DT) empowered MEC, facilitating informed offloading decision-making in task delegation and processing. The proposed trust management mechanism uses DT to enhance dynamic real-time task offloading. DT provides insights into the physical MEC environment and shares AI agent training data deployed on IoT devices, optimizing workload distribution. Our proposed trust management mechanism is based on an incentive cooperation model based on a hierarchical game model. Initially, we model cooperation among reliable servers as a hedonic coalition formation game, capturing edge servers’ selfish behavior and aiming to maximize utilities. Subsequently, we model interactions between service-seeking devices and the coalition as a two-stage Stackelberg game, encouraging devices to delegate tasks to the most reliable coalition. The simulation results validate the effectiveness of our trustworthy approaches, demonstrating significant improvements in energy efficiency compared to existing related works. Our study shows up to a 60% increase in energy consumption fairness, while ensuring trust among nodes. © 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1441.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
