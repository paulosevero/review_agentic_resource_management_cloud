---
id: paper-2848
title: Energy-efficient thermal management of air-liquid-cooled data centers via deep reinforcement learning
authors:
- Wu, Chengzhong
- Huang, Zhanhong
- Yu, Tao
- Pan, Zhenning
- Wang, Keying
- Wu, Yufeng
venue: Applied Thermal Engineering
venue_type: journal
year: 2026
doi: 10.1016/j.applthermaleng.2025.129626
url: https://www.scopus.com/pages/publications/105026596457?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Air-liquid-cooled system
- Data center
- Deep reinforcement learning
- Thermal management
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2848 — Energy-efficient thermal management of air-liquid-cooled data centers via deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data center cooling has become one of the primary contributors to overall energy consumption, especially under high-density computing scenarios. The improved thermal handling capability of the air-liquid-cooled system comes with the challenge of efficient management, due to interactions between heterogeneous equipment and dynamic workloads. To address this issue, this work proposes a deep reinforcement learning-based framework for energy-efficient thermal management of air-liquid-cooled data centers. First, this research employs a data-driven method to design a simulation model for the data center. A hierarchical heterogeneous network model is designed to capture the spatial distribution of the thermal field and the multi-variate time-series features, thereby enhancing the accuracy of thermal predictions. Then, a multi-agent reinforcement learning strategy jointly regulates air-cooling and liquid-cooling systems, while a counterfactual-based incentive mechanism enhances cooperation among agents. Comparative experiments conducted on the CINECA data center show that the proposed method reduces cooling energy consumption by 11.68%. This study provides a scalable control and optimization solution for large-scale data center thermal load management. Copyright © 2025. Published by Elsevier Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2848.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
