---
id: paper-1024
title: 'Electric Vehicle Cluster Assisted Multi-Tier Vehicular Edge Computing System: Cross-System Framework Design and Optimization'
authors:
- Li, Yang
- Zhu, Li
- Liu, Shichao
- Wang, Hongwei
- Yu, F. Richard
- Cai, Baigen
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2024.3430507
url: https://www.scopus.com/pages/publications/85199076584?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17384--17399
keywords:
- Cooperative vehicle infrastructure
- cross-system two-level optimization
- electric vehicle cluster
- multi-tier VEC system
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

# paper-1024 — Electric Vehicle Cluster Assisted Multi-Tier Vehicular Edge Computing System: Cross-System Framework Design and Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cooperative vehicle infrastructure is critical for facilitating multi-tier vehicular edge computing (VEC) systems to collaboratively process latency-sensitive intelligent tasks. However, the dynamic topology and the scarcity of available computing resources on real traffic roads pose significant challenges. While previous works have explored using public transit and parked vehicles as cooperative vehicles, they often overlook the incentive mechanisms and the specific tasks of these vehicles, rendering these solutions impractical. Motivated by the achievements in smart electric vehicles (EVs), this paper presents an electric vehicle cluster (EVC) assisted multi-tier VEC system that leverages the capabilities of the vehicle-to-grid (V2G) technology to provide stable computing resources to traffic areas. The proposed EVC-assisted multi-tier VEC system employs a cross-system two-level optimization method that jointly considers offloading and resource allocation decisions for road task vehicles (RTVs) in the VEC system and charging power decisions for the EVs in the EVC. At the lower level, we minimize the task latency for RTVs by utilizing the computing resources of idle EVs. At the upper level, we build a multi-agent two-step game model and introduce a potential game-based strategy and a Nash equilibrium (NE) based EV-RSU mapping method to derive the optimal decision strategy for the EVC. Extensive simulation results demonstrate the efficient reduction in total-task latency of RTVs and lower cost for the EVC while meeting the essential requirements in the V2G. © 2024 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1024.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
