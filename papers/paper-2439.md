---
id: paper-2439
title: Intelligent Offloading, Phase-Shift and Trajectory Design in Priority-Aware IRS- and UAV-Assisted MEC Systems
authors:
- Zhang, Sinong
- Wang, Haowei
- Zhao, Liang
- Li, Wencai
- Leung, Victor C. M.
venue: S3 2025 - Proceedings of the 2025 16th ACM Workshop on Wireless of the Students, by the Students, for the Students
venue_type: conference
year: 2025
doi: 10.1145/3737898.3769038
url: https://www.scopus.com/pages/publications/105025550348?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 1--3
keywords:
- intelligent reflecting surface (IRS)
- MEC
- multi-agent deep reinforcement learning (MADRL)
- task priority
- UAV
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: false
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

# paper-2439 — Intelligent Offloading, Phase-Shift and Trajectory Design in Priority-Aware IRS- and UAV-Assisted MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has become increasingly popular due to its flexibility. However, the task priority of ground users (GUs) is often neglected and the wireless communications between UAVs and GUs are usually unreliable, leading to poor quality of service (QoS). To address this issue, we propose a priority-aware intelligent reflecting surface (IRS) and UAV-aided MEC network. Subsequently, we formulate a system utility maximization problem by jointly optimizing task offloading, IRS phase shift, UAV trajectory and resource allocation. Then, we decouple the original problem into three subproblems, and design a Dynamic Dual-Weighting (DDW)-based optimization framework (DOF) to effectively solve them. Numerical results show that DOF is superior to other baselines in terms of system utility.  © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2439.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
