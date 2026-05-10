---
id: paper-2291
title: A Cooperative Computation Offloading Strategy for Reusable Tasks in the Multi-UAV-Assisted MEC System
authors:
- Wu, Wenqing
- Wu, Shie
- Mu, Hanchao
- Chen, Jiahui
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2025
doi: 10.1109/ICCT67417.2025.11374258
url: https://www.scopus.com/pages/publications/105034106115?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1080--1085
keywords:
- cooperative task offloading
- mobile edge computing (MEC)
- reusable tasks
- trajectory optimization
- Unmanned aerial vehicles (UAVs)
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

# paper-2291 — A Cooperative Computation Offloading Strategy for Reusable Tasks in the Multi-UAV-Assisted MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> By integrating unmanned aerial vehicles (UAVs) with mobile edge computing (MEC) servers, the multi-UAV-assisted MEC system has become a potential paradigm for task offloading due to its flexibility and mobility. However, the performance of the system is constrained by the limited energy of the UAVs and the dynamic environment brings challenges for task offloading among multiple UAVs. In this paper, taking into consideration the diversity and similarity of the tasks, we investigate the energy consumption minimization problem under the multi-UAV-assisted MEC system with reusable tasks. To address the issue, a joint optimization of cooperative task offloading and UAV flight trajectories (JOCOT) algorithm is proposed. Firstly, UEs are clustered based on the graph coloring method. Then, based on the multi-agent deep deterministic policy gradient (MADDPG) method, the cooperative task offloading and UAV flight trajectories are jointly optimized. Simulation results show that the proposed JOCOT scheme outperforms other benchmark methods, consuming the least energy under different scenarios. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2291.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
