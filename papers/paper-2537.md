---
id: paper-2537
title: Mobility-Aware Cooperative Optimization for Task Offloading and Resource Allocation in Multi-Edge Computing
authors:
- Chen, Dong
- Zhang, Ximing
- Lin, Kequan
- Mei, Chunhua
- Huo, Ru
venue: Algorithms
venue_type: journal
year: 2026
doi: 10.3390/a19030221
url: https://www.scopus.com/pages/publications/105034257151?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- mobile edge computing
- mobility modeling
- multi-agent deep reinforcement learning (MADRL)
- resource allocation
- task offloading
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

# paper-2537 — Mobility-Aware Cooperative Optimization for Task Offloading and Resource Allocation in Multi-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of mobile Internet of Things (IoT) devices has introduced significant resource scheduling challenges in multi-edge computing networks, where device mobility leads to dynamic network connectivity and load imbalance, complicating task offloading and resource management. To address these issues, this paper presents a mobility-driven hierarchical optimization framework for task offloading and computation resource allocation in multi-region edge computing environments, a functionally coupled hierarchical framework that integrates mobility-aware heuristic offloading with multi-agent deep deterministic policy gradient (MADDPG)-based resource allocation. Devices are first clustered according to their mobility patterns, and offloading decisions are dynamically made based on trajectory and dwell-time characteristics. Each edge server is modeled as an autonomous agent, and an MADDPG framework is adopted to collaboratively optimize resource allocation, with the joint objective of minimizing task processing delay and system energy consumption. Experimental evaluations under diverse mobility and workload conditions show that the proposed approach achieves a 19.0% reduction in task delay compared to the Multi-Objective Gray Wolf Optimization (MOGWO) method at the largest device scale (60 devices) and maintains comparable energy efficiency. Furthermore, it exhibits stronger adaptability and scheduling performance across varying mobility group distributions. These results confirm the effectiveness of the proposed method in enhancing system performance within dynamic mobile edge computing scenarios. © 2026 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2537.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
