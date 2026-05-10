---
id: paper-2829
title: Joint Energy-Efficient Task Scheduling and Trajectory Optimization for Multi-UAV MEC Networks in Low-Altitude Economy
authors:
- Wang, Zhiying
- Chen, Jinghui
- Sun, Gang
- Yu, Hongfang
- Guizani, Mohsen
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2025.3627914
url: https://www.scopus.com/pages/publications/105020942683?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3058--3072
keywords:
- deep reinforcement learning
- Mobile edge computing
- task offloading
- trajectory optimization
- uncrewed aerial vehicle (UAV)
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

# paper-2829 — Joint Energy-Efficient Task Scheduling and Trajectory Optimization for Multi-UAV MEC Networks in Low-Altitude Economy

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the increasing deployment of Internet of Things (IoT) devices and significant progress in Uncrewed Aerial Vehicle (UAV) technologies, UAV-assisted Mobile Edge Computing (UMEC) has emerged as an effective approach to address the challenges of constrained ground network coverage and insufficient computational resources. Leveraging their mobility, flexible deployment, and low cost, UAVs can dynamically support edge networks by providing computation and communication services for latency and energy sensitive tasks. Nevertheless, task scheduling and UAV trajectory optimization in UMEC systems still face significant challenges. To address the task scheduling problem for energy-sensitive tasks in the UMEC system, this paper first formulates a mathematical model of the system's energy consumption and establishes an optimization objective aimed to optimize the energy cost of UMEC system. Building upon this, we propose a task scheduling algorithm that integrates Multi-Agent Proximal Policy Optimization (MAPPO) with a bargaining game-based resource coordination mechanism. The proposed algorithm reduces the overall energy consumption and enhances the system performance through a bargaining-based resource allocation and matching strategy, alongside MAPPO-driven trajectory optimization. Simulation results show that our method outperforms the baseline algorithms in terms of system utility, achieving up to a 7.4% improvement.  © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2829.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
