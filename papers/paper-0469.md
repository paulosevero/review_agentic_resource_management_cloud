---
id: paper-0469
title: Multi-UAV Joint Observation, Communication, and Policy in MEC
authors:
- Liu, Shuai
- Bai, Yuebin
venue: Proceedings - 2022 18th International Conference on Mobility, Sensing and Networking, MSN 2022
venue_type: conference
year: 2022
doi: 10.1109/MSN57253.2022.00144
url: https://www.scopus.com/pages/publications/85152267533?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 891--896
keywords:
- Communication
- Deep reinforcement learning
- Mobile edge computing
- Multi-UAV
- Sensing
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

# paper-0469 — Multi-UAV Joint Observation, Communication, and Policy in MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The use of multi-agent reinforcement learning methods (MARL) in mobile edge computing (MEC) environments enables multiple unmanned aerial vehicles (multi-UAV) to intelligently provide relay or computational offloading services to mission targets. UAV's observation range and communication methods between UAVs have a significant impact on multi-UAV collaboration strategy. For this purpose, we study the multi-UAV observation range dynamic control method and the optimal inter-UAV communication method. Our approach is to design a multi-UAV joint observation, communication, policy, and service collaboration protocol and study the optimization method of the protocol. We propose an expert-guided deep reinforcement learning framework to optimize this protocol. Each UAV's optimal radar observation range and inter-UAV communication method are learned using an information entropy value decomposition method. Through our observation and communication method, multi-UAV are able to obtain the most valuable information. Experiments demonstrate that our method can improve MEC's service coverage by 9.38%-21.88% compared to the classical MARL algorithm. Our method improves the radar observation efficiency and communication efficiency by 3.05%-38.9% and 8.55%-22.03%, respectively. The results show that this method improves multi-UAV energy utilization. © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0469.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
