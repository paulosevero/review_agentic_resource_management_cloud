---
id: paper-2929
title: HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network
authors:
- Zhao, Haitao
- Zhang, Taiming
- Tang, Guijin
- Liu, Miao
- Chen, Shuaifei
- Wang, Chengxiang
venue: IEEE Transactions on Communications
venue_type: journal
year: 2026
doi: 10.1109/TCOMM.2026.3681581
url: https://www.scopus.com/pages/publications/105035405351?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AoI
- data offloading
- digital twin channel
- heterogeneous GNN
- layered UAVs
- MARL
- trajectory control
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2929 — HG-MARL Based Scheduling of Trajectory and Offloading for Layered UAVs-enabled Digital Twin Channel Modeling in Integrated Communication-Computing-Intelligence-Controlling Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a key paradigm in sixth-generation (6G) systems for enabling physical–virtual mapping and intelligent network management, Digital Twin (DT) networks demand high-precision, low-latency modeling and continuous updates of wireless environments. However, in dynamic urban scenarios, channel conditions are highly non-stationary, and traditional sensing schemes suffer from limitations in coverage, information timeliness, and scheduling efficiency. To address these challenges, this paper proposes an Integrated Communication-Computing-Intelligence-Controlling (ICCIC) network based on layered unmanned aerial vehicles (UAVs). The system comprises mobile edge servers (ESs) with trajectory control and scheduling capabilities, and statically deployed working UAVs responsible for wireless channel measurements. The collected data is offloaded to ESs for edge computing and local model construction, which supports subsequent DT channel modeling. A multi-objective optimization problem is formulated to jointly schedule UAV trajectories and data offloading, with Age of Information (AoI) and service delay as performance metrics. The optimization is subject to constraints including maximum task execution time and service fairness. To capture multi-type interactions among UAVs during sensing and coordination, we build a multi-relational heterogeneous graph and encode it with a graph neural network (GNN) to obtain structured system states. On this basis, we adopt a QMIX-based multi-agent reinforcement learning (MARL) framework under centralized training and decentralized execution (CTDE) is developed to learn cooperative scheduling policies. Simulation results demonstrate that the proposed method achieves superior performance in sensing timeliness, scheduling responsiveness, and policy convergence, providing robust support for efficient and reliable DT channel modeling. © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2929.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
