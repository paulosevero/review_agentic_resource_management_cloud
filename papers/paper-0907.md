---
id: paper-0907
title: Multi-agent Deep Reinforcement Learning based Information-Energy Collaboration in Vehicle Edge Computing Networks
authors:
- Feng, Yaoyu
- Zhang, Biling
- Yu, Jung-Lang
venue: IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC
venue_type: conference
year: 2024
doi: 10.1109/PIMRC59610.2024.10817235
url: https://www.scopus.com/pages/publications/85215954907?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- computation offloading
- energy sharing
- Information-energy collaboration
- multi-agent DDPG
- vehicle edge computing network
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0907 — Multi-agent Deep Reinforcement Learning based Information-Energy Collaboration in Vehicle Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the vehicle edge computing network (VECN), how to deal with the computation resources and energy resources shortage problem the roadside units (RSUs) encounter when they are performing delay sensitive computation tasks is an important issue, especially during the peak hours and the situation of VECN is dynamic. To complete the computation tasks on time with the minimum expenditure, in this paper, we investigate the problem of information-energy collaboration among RSUs, where the spectrum management is also involved. For the considered scenario, the RSUs' strategies of spectrum selection, computation task offloading and energy sharing are derived from the formulated optimization problem. Since the proposed problem is a highly complex mixed-integer nonlinear programming problem and the strategies are coupled with each other, a multi-agent deep deterministic policy gradient (MADDPG) based algorithm is proposed to find the sub-optimal solutions quickly in a dynamic environment. The simulation results show that our approach is superior to the existing schemes in terms of total system expenditure and the spectral efficiency. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0907.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
