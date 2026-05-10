---
id: paper-2259
title: Dynamic Trajectory Design for Multi-UAV-Assisted Mobile Edge Computing
authors:
- Wang, Zhuwei
- Wang, Haowei
- Liu, Lihan
- Sun, Enchang
- Zhang, Haijun
- Li, Zhidu
- Fang, Chao
- Li, Meng
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2024.3485182
url: https://www.scopus.com/pages/publications/105001067554?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4684--4697
keywords:
- Dynamic trajectory
- flight dynamics
- intelligent design
- unpiloted aerial vehicle (UAV)-assisted MEC
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2259 — Dynamic Trajectory Design for Multi-UAV-Assisted Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The trajectory design for unpiloted aerial vehicle (UAV)-assisted mobile edge computing (MEC) networks has become a hot research topic. In the UAV-assisted MEC scenario, the UAV is required to frequently adjust its flight trajectory due to dynamic factors such as time-varying task offloading requirements, user mobility, and transmission environment variation. In this paper, with consideration of the constraint induced by the UAV flight dynamics, the dynamic trajectory design challenge within the blockchain-based multi-UAV-assisted MEC framework is investigated. An intelligent algorithm that integrates multi-agent deep deterministic policy gradient (MADDPG), linear quadratic regulator (LQR), and CVXPY solver, named MADDPG-LC, is proposed to achieve real-time joint optimization of dynamic trajectory control and resource allocation with respect to minimizing weighted energy consumption and delays. Numerical simulation results demonstrate the efficacy of the proposed MADDPG-LC algorithm in addressing the UAV flight dynamics constraint, which has generally overlooked in existing works. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2259.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
