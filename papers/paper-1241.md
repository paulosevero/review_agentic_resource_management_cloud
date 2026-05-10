---
id: paper-1241
title: Cooperative End-Edge-Cloud Computing and Resource Allocation for Digital Twin Enabled 6G Industrial IoT
authors:
- Wang, Yuao
- Fang, Jingjing
- Cheng, Yao
- She, Hao
- Guo, Yongan
- Zheng, Gan
venue: IEEE Journal on Selected Topics in Signal Processing
venue_type: journal
year: 2024
doi: 10.1109/JSTSP.2023.3345154
url: https://www.scopus.com/pages/publications/85181819203?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 124--137
keywords:
- Collaborative computing
- digital twin
- industrial Internet of Things
- resource allocation
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

# paper-1241 — Cooperative End-Edge-Cloud Computing and Resource Allocation for Digital Twin Enabled 6G Industrial IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> End-edge-cloud (EEC) collaborative computing is regarded as one of the most promising technologies for the Industrial Internet of Things (IIoT). It offers effective solutions for managing computationally intensive and delay-sensitive tasks efficiently. Indeed, achieving intelligent manufacturing in the context of 6G networks requires the development of efficient resource scheduling schemes. However, improving the quality of service and resource management in the face of challenges like time-varying physical operating environments of IIoT, task heterogeneity, and the coupling of different resource types is undoubtedly a complex task. In this work, we propose a digital twin (DT) assisted EEC collaborative computing scheme, where DT is utilized to monitor the physical operating environment in real-time and determine the optimal strategy, and the potential deviation between the real values and DT estimates is also considered. We aim to minimize the system cost by optimizing device association, offloading mode, bandwidth allocation, and task split ratio. Our optimization is constrained by the maximum tolerable latency of the task while considering both latency and energy consumption. To solve the collaborative computation and resource allocation (CCRA) problem in the EEC, we propose an algorithm with DT based on Multi-Agent Deep Deterministic Policy Gradient (MADDPG), where each user end (UE) in DT operates as an independent agent to determine the optimum offloading decision autonomously. Simulation results demonstrate the effectiveness of the proposed scheme, which can significantly improve the task success rate compared to benchmark schemes, while reducing the latency and energy consumption of task offloading with the assistance of DT.  © 2007-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1241.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
