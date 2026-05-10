---
id: paper-2409
title: 'CoGroup: Cooperative Quality Offloading with Worker Grouping using Hierarchical Multi-Agent Deep Reinforcement Learning'
authors:
- Zaki, Amr M.
- Elsayed, Sara A.
- Elgazzar, Khalid
- Hassanein, Hossam S.
venue: 21st International Wireless Communications and Mobile Computing Conference, IWCMC 2025
venue_type: conference
year: 2025
doi: 10.1109/IWCMC65282.2025.11059498
url: https://www.scopus.com/pages/publications/105011352807?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1276--1281
keywords:
- Autonomous Vehicles
- Cooperative Perception
- Task Offloading
- Vehicular Edge Computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2409 — CoGroup: Cooperative Quality Offloading with Worker Grouping using Hierarchical Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task offloading in Vehicular Edge Computing (VEC) enhances cooperative perception (CP) for Autonomous Vehicles (AVs), improving traffic awareness. However, the high cost of Roadside Unit (RSU) and the underutilization of parked vehicles pose challenges. Leveraging Vehicle-to-Vehicle (V2V) communication, parked vehicles can form collaborative worker groups for efficient perception aggregation. We propose CoGroup, a two-tier framework integrating task offloading and dynamic worker grouping. Modeled as a double quadratic multiple knapsack problem, it employs Hierarchical Reinforcement Learning (HRL): QMIX for decentralized task allocation and DQN for optimized worker grouping. Experiments show that CoGroup improves traffic awareness by 21% over non-cooperative methods, reducing RSU dependence and offering a scalable, cost-effective solution for next-generation VEC systems.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2409.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
