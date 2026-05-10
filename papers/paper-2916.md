---
id: paper-2916
title: Multi-Objective Decomposition Evolutionary DRL for UAV-Assisted MEC in Internet of Vehicles
authors:
- Zhang, Lei
- Tian, Can
- Liu, Tingting
- Li, Xingwang
- Mumtaz, Shahid
- Khan, Wali Ullah
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2025.3602933
url: https://www.scopus.com/pages/publications/105014479480?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3133--3148
keywords:
- deep reinforcement learning
- Internet of Vehicles
- mobile edge computing
- multi-objective optimization
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

# paper-2916 — Multi-Objective Decomposition Evolutionary DRL for UAV-Assisted MEC in Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic multi-objective optimization in Uncrewed Aerial Vehicle (UAV)-assisted Mobile Edge Computing (MEC) for Internet of Vehicles (IoV) faces significant challenges, due to complex operational environments and conflicting objectives. While Deep Reinforcement Learning (DRL) enables real-time optimization, conventional weighted-sum approaches fail to balance these objectives effectively. To address this, we propose a Multi-Objective Decomposition Evolutionary DRL (MODE-DRL) framework, which include the following three innovative aspects. Firstly, a multi-objective optimization model is developed, aiming to minimize delay and energy consumption while maximizing the number of completed tasks, thus ensuring overall network performance. Secondly, a novel MODE strategy that dynamically associates weight vectors with learning agents to optimize policy distribution and enhance population diversity. Lastly, two integrated algorithms, called MODE with Proximal Policy Optimization (MODE-PPO) and MODE with Deep Deterministic Policy Gradient (MODE-DDPG), are developed to combine DRL's dynamic decision-making with MODE's global optimization capabilities, enabling agents to rapidly adapt strategies based on different weights. Experimental results demonstrate that the MODE-DRL achieves a 33.2% improvement in hypervolume, along with a 16.3% reduction in average delay, a 15.5% decrease in average energy consumption, and a 34.4% increase in average number of completed tasks. These results confirm that MODE-DRL exhibits significant advantages in both convergence and diversity, while enhancing overall network performance. This work provides a scalable paradigm for real-time multi-objective decision-making in UAV-assisted MEC for IoV systems.  © 1967-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2916.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
