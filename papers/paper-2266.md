---
id: paper-2266
title: 'Joint Task Offloading and Resource Allocation in Vehicular Platoon Networks: A Federated Reinforcement Learning Approach'
authors:
- Wang, Taomin
- Liu, Yiming
- Wang, Qiang
- Cao, Xuguang
- Chen, Jingyi
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2025
doi: 10.1109/VTC2025-Spring65109.2025.11174297
url: https://www.scopus.com/pages/publications/105019044432?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Federated learning
- MARL
- MEC
- NR-V2X
- Platoon communication
- Task offloading
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2266 — Joint Task Offloading and Resource Allocation in Vehicular Platoon Networks: A Federated Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the future, NR-V2X networks and platoon-based driving modes will become essential components of Intelligent Transportation Systems. However, with the advent of the Internet of Vehicles, the large-scale deployment of sensors and the explosive growth of data are driving the need for new solutions. Mobile edge computing has emerged as a key technology for addressing the distributed computing requirements. In this paper, we propose a Joint Optimization framework based on Federated multi-agent Reinforcement Learning (JOFRL) to solve the task offloading and resource allocation problems in a platoon-based NR-V2X network. Existing RL algorithms focus on either the communication link capacity or the completion rate of computing tasks. Differently, we consider the mutual influence between the allocation of computing and communication resources. We modify the reward function in the MARL framework so that each agent's communication performance on V2V links is aligned with its computing performance. Our experimental results demonstrate that JOFRL outperforms other baseline algorithms. Specificly, JOFRL achieves improvements of 10.87%, 22.43% and 23.02% in computing and communication respectively compared with MADDPG, SAC and DDPG algorithm. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2266.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
