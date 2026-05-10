---
id: paper-1110
title: 'Eco-SLAM: Resource-Efficient Edge-Assisted Collaborative Visual SLAM System'
authors:
- Ou, Wenzhong
- Feng, Daipeng
- Luo, Ke
- Chen, Xu
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2024
doi: 10.1007/978-981-97-0859-8_19
url: https://www.scopus.com/pages/publications/85187792616?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 307--324
keywords:
- Collaborative SLAM
- Edge Computing
- Robotics Applications
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

# paper-1110 — Eco-SLAM: Resource-Efficient Edge-Assisted Collaborative Visual SLAM System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Collaboration among multiple smart agents such as robots and UAVs is critical for the key tasks of simultaneous localization and mapping (SLAM), which are essential for many robotics applications. Visual SLAM maps by multiple collaborative agents can be promptly generated with the assistance of edge servers in proximity as the computing infrastructures. However, as the number of agents connected to an edge server continues growing, the pressure on bandwidth consumption and resource utilization also climbs dramatically, which may trigger the failure of map generation. To tackle these challenges, this article proposes Eco-SLAM, a resource-efficient edge-assisted collaborative multi-agent visual SLAM system. Eco-SLAM has been designed to enable large-scale parallelism in SLAM framework and optimized for use in both edge servers and intelligent agents. The unique Core-tr and Co-Map library design ensures efficient utilization of resources and consistent data. Additionally, Eco-SLAM incorporates the ORB-based image compression algorithm, which optimizes data transmission with constrained networking resources. We implement and evaluate the Eco-SLAM system in a real environment and demonstrate its effectiveness through extensive experiments ranging from the public SLAM datasets to realistic deployment scenarios. Thorough evaluations show that Eco-SLAM can reduce the memory consumption of other multi-agent SLAM frameworks by up to 20.1% during runtime on the edge server, and save up to 25.1% wireless bandwidth consumption without compromising the accuracy of the map generation. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1110.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
