---
id: paper-2423
title: Computation Offloading Optimization for Digital Twin Assisted 5G-Enabled Edge Computing Network in Urban Rail Transit
authors:
- Zhang, Qingmiao
- Liu, Minghao
- Zhao, Junhui
- Zhang, Chenxi
- Zhang, Ming
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3621533
url: https://www.scopus.com/pages/publications/105021065414?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 21574--21587
keywords:
- 5G
- digital twin
- edge computing
- Urban rail transit
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

# paper-2423 — Computation Offloading Optimization for Digital Twin Assisted 5G-Enabled Edge Computing Network in Urban Rail Transit

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As urban rail transit evolves, the convergence of digitalization, networking and intelligence has emerged as a pivotal trend, accompanied by the surge of intensive computing tasks and real-time demand. Edge computing is a promising solution to address the local resource constraints of various application devices covered by various subsystems within Urban Rail Transit Systems (URTS). In this paper, a Digital Twin (DT) assisted 5G-enabled edge computing network in URTS is established. We consider the heterogeneous service requirements of Ultra-Reliable Low-Latency Communication (URLLC) and Enhanced Mobile Broadband (eMBB) in different intelligent applications, and accordingly, we develop a task execution queue model. Additionally, to improve the task processing performance of the system, a task offloading and resource allocation scheme based on the Multi-Agent Twin Delayed Deep Deterministic policy gradient (MATD3) algorithm is proposed. User Equipment (UEs) and Edge Servers (ESs) are treated as distinct agents, accounting for their collaborative computation capabilities and differences in decision-making. A framework is established for centralized training in a DT assisted system with decentralized execution by each agent. Simulation results demonstrate that the proposed approach ensures the stringent latency requirement for URLLC tasks, enhances the Transaction Per Time Slot (TPTS) for eMBB tasks, and significantly reduces processing delays across all tasks. In addition, the proposed scheme also achieves load balance between UEs and ESs. © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2423.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
