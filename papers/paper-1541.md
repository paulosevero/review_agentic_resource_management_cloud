---
id: paper-1541
title: Fairness-Guaranteed Joint Access Control, 3-D UAV Trajectory Planning, and Task Scheduling in AGINs
authors:
- Du, Jianbo
- Yan, Haobo
- Sun, Aijing
- Wang, Chong
- Gao, Yuan
- Liu, Zhiquan
- Chu, Xiaoli
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3569535
url: https://www.scopus.com/pages/publications/105005323448?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15978--15990
keywords:
- Air-ground integrated networks
- deep reinforcement learning
- multi-access edge computing
- unmanned aerial vehicle (UAV) path planning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1541 — Fairness-Guaranteed Joint Access Control, 3-D UAV Trajectory Planning, and Task Scheduling in AGINs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of Multi-access Edge Computing (MEC) with Air-Ground Integrated Networks (AGINs) enhances communication coverage and computational capabilities, especially for supporting critical tasks such as emergency responses and environmental monitoring. In this paper, we develop an MEC-enabled AGIN architecture to serve Internet-of-Things devices. Our objective is to minimize the total energy consumption of IoTDs and unmanned aerial vehicle (UAV) and the number of dropped tasks, while maximizing the fairness index through refined access control, UAV trajectory planning, and task scheduling. Given the complexity of the optimization problem, we reformulate the problem as a Markov decision process and define the state space, the action space, the immediate reward, and the state transfer. Considering the inclusion of discrete variables, we solve the problem by devising a novel Multi-Agent Deep Deterministic Policy Gradient (MADDPG) based algorithm, where the continuous action outputs of MADDPG are discretized to satisfy the coupling constraints between variables. The simulation results indicate that our algorithm outperforms baseline algorithms in both convergence speed and system energy consumption. Additionally, it demonstrates exceptional stability and robustness, leading to a substantial improvement in overall system performance. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1541.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
