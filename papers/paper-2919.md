---
id: paper-2919
title: Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled Mobile Edge Computing
authors:
- Zhang, Xiuling
- Jia, Riheng
- Yin, Quanjun
- Zheng, Zhonglong
- Li, Minglu
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3632884
url: https://www.scopus.com/pages/publications/105021858874?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5648--5665
keywords:
- cooperative trajectory planning
- job scheduling
- Mobile edge computing
- multi-UAV system
- resource allocation
- safe reinforcement learning
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

# paper-2919 — Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) has recently gained significant attention as a promising solution for processing delay-sensitive and resource-intensive computational jobs. Existing system schedulers in MEC networks typically assume homogeneous service providers, uniformly distributed user equipment (UE), and identical service requirements, making them unsuitable for practical MEC scenarios where jobs are randomly generated with varying service and completion time requirements. Thus, in this work, we jointly optimize job scheduling and resource allocation in a heterogeneous multi-unmanned aerial vehicle (UAV) enabled MEC network, considering practical factors such as diverse service requirements of jobs, unknown distribution of UEs, and spatial-temporal job arrivals. We aim to reduce the overall job miss rate and the average energy consumption of both UAVs and UEs by jointly planning safe UAV trajectories and onboard resource allocation. To learn uncertain and dynamic UE-side states (e.g., job arrivals and mobility patterns) and ensure the UAV's safety during the flight, we propose a multi-agent safe reinforcement learning algorithm that combines a Shared Soft Actor-Critic architecture for extracting features of heterogeneous UAVs and a two-agent Markov Game of Intervention mechanism for collision avoidance, named SSAC-MGI. In particular, SSAC-MGI further incorporates a fine-grained resource allocation scheme to improve onboard resource utilization and reduce job miss rate. Extensive real trace-driven simulations based on Alibaba cluster data validate the effectiveness and superiority of SSAC-MGI, compared with several state-of-the-art algorithms. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2919.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
