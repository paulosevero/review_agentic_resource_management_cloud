---
id: paper-0559
title: Migratory Perception in Edge-Assisted Internet of Vehicles
authors:
- Cai, Chao
- Chen, Bin
- Qiu, Jiahui
- Xu, Yanan
- Li, Mengfei
- Yang, Yujia
venue: Electronics (Switzerland)
venue_type: journal
year: 2023
doi: 10.3390/electronics12173662
url: https://www.scopus.com/pages/publications/85170558980?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge computing
- migratory perception
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0559 — Migratory Perception in Edge-Assisted Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Autonomous driving technology heavily relies on the accurate perception of traffic environments, mainly through roadside cameras and LiDARs. Although several popular and robust 2D and 3D object detection methods exist, including R-CNN, YOLO, SSD, PointPillar, and VoxelNet, the perception range and accuracy of an individual vehicle can be limited by blocking from other vehicles or buildings. A solution is to harness roadside perception infrastructures for vehicle–infrastructure cooperative perception, using edge computing for real-time intermediate features extraction and V2X networks for transmitting these features to vehicles. This emerging migratory perception paradigm requires deploying exclusive cooperative perception services on edge servers and involves the migration of perception services to reduce response time. In such a setup, competition among multiple cooperative perception services exists due to limited edge resources. This study proposes a multi-agent reinforcement learning (MADRL)-based service scheduling method for migratory perception in vehicle–infrastructure cooperative perception, utilizing a discrete time-varying graph to model the relationship between service nodes and edge server nodes. This MADRL-based approach can efficiently address the challenges of service placement and migration in resource-limited environments, minimize latency, and maximize resource utilization for migratory perception services on edge servers. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0559.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
