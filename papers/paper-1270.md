---
id: paper-1270
title: Multi-UAV Collaborative Edge Computing Algorithm for Joint Task Offloading and Channel Resource Allocation
authors:
- Wei, Yuting
- Wu, Sheng
- Ji, Zhe
- Yu, Zhigang
- Jiang, Chunxiao
- Kuang, Linling
venue: Journal of Communications and Information Networks
venue_type: journal
year: 2024
doi: 10.23919/JCIN.2024.10582826
url: https://www.scopus.com/pages/publications/85199583498?origin=resultslist
publisher: Posts and Telecom Press Co Ltd
pages: 137--150
keywords:
- joint task offloading and wireless channel allocation
- multi-agent deep deterministic policy gradient (MADDPG)
- multi-UAV collaboration
- simulated annealing (SA) algorithm
- UAV-based edge computing
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

# paper-1270 — Multi-UAV Collaborative Edge Computing Algorithm for Joint Task Offloading and Channel Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-based edge computing is an emerging technology that provides fast task processing for a wider area. To address the issues of limited computation resource of a single UAV and finite communication resource in multi-UAV networks, this paper joints consideration of task offloading and wireless channel allocation on a collaborative multi-UAV computing network, where a high altitude platform station (HAPS) is adopted as the relay device for communication between UAV clusters consisting of UAV cluster heads (ch-UAVs) and mission UAVs (m-UAVs). We propose an algorithm, jointing task offloading and wireless channel allocation to maximize the average service success rate (ASSR) of a period time. In particular, the simulated annealing (SA) algorithm with random perturbations is used for optimal channel allocation, aiming to reduce interference and minimize transmission delay. A multi-agent deep deterministic policy gradient (MADDPG) is proposed to get the best task offloading strategy. Simulation results demonstrate the effectiveness of the SA algorithm in channel allocation. Meanwhile, when jointly considering computation and channel resources, the proposed scheme effectively enhances the ASSR in comparison to other benchmark algorithms. © 2024, Posts and Telecom Press Co Ltd. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1270.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
