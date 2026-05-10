---
id: paper-1135
title: Reconfigurable Intelligent Surface Assisted VEC Based on Multi-Agent Reinforcement Learning
authors:
- Qi, Kangwei
- Wu, Qiong
- Fan, Pingyi
- Cheng, Nan
- Fan, Qiang
- Wang, Jiangzhou
venue: IEEE Communications Letters
venue_type: journal
year: 2024
doi: 10.1109/LCOMM.2024.3451182
url: https://www.scopus.com/pages/publications/85202733431?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2427--2431
keywords:
- multi-agents deep reinforcement learning (MA-DRL)
- Reconfigurable intelligent surface (RIS)
- vehicular edge computing (VEC)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1135 — Reconfigurable Intelligent Surface Assisted VEC Based on Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is an emerging technology that enables vehicles to perform high-intensity tasks by executing tasks locally or offloading them to nearby edge devices. However, obstacles may degrade the communications and incur communication interruptions, and thus the vehicle may not meet the requirement for task offloading. Reconfigurable intelligent surfaces (RIS) is introduced to support vehicle communication and provide an alternative communication path. The system performance can be improved by flexibly adjusting the phase-shift of the RIS. For RIS-assisted VEC system where tasks arrive randomly, we design a control scheme that considers offloading power, local power allocation and phase-shift optimization. To solve this non-convex problem, we propose a new deep reinforcement learning (DRL) framework that employs modified multi-agent deep deterministic policy gradient (MADDPG) approach to optimize the power allocation for vehicle users (VUs) and block coordinate descent (BCD) algorithm to optimize the phase-shift of the RIS. Simulation results show that our proposed scheme outperforms the centralized deep deterministic policy gradient (DDPG) scheme and random scheme.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1135.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
