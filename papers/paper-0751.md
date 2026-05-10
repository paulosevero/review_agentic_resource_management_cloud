---
id: paper-0751
title: 'SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems'
authors:
- Wang, Ziwei
- Zhao, Yunfeng
- Qiu, Chao
- He, Qiang
- Wang, Xin
- Wang, Xiaofei
- Hu, Qinghua
venue: Proceedings - International Conference on Distributed Computing Systems
venue_type: conference
year: 2023
doi: 10.1109/ICDCS57875.2023.00066
url: https://www.scopus.com/pages/publications/85175073095?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 853--863
keywords:
- cloud-edge collaboration
- deep reinforcement learning
- edge computing
- Request dispatch
- service orchestration
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez a ideia de socialização indique Agents.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: RL
    winning_category: rl
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-0751 — SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The ability for cloud data centres and edge data centres to collaborate unleashes the potential of the edge-cloud system. However, its sophistication causes unexpected issues in request scheduling, such as Insufficient intelligence, complicated hierarchy and limited cooperation. Traditional resource optimization methods for the edge-cloud system struggle to accommodate such intricate situations. In this paper, inspired by the behaviors and regulations in human society, we propose a socialized learning-based scheduling approach for the edge-cloud system, namely SocialEdge. In order to adapt to time-varying requests and dynamic service prevalence, we propose a learning-based approach, multi-agent advantage actor-critic (MAA2C) and graph convolutional networks-based MAA2C for two phases, respectively, which can improve individual intelligence to achieve optimal dispatch and orchestration decisions. Then, to make use of hierarchy correlation, we develop the socialized refining inter the layers, where inference results from one layer guide the training process of the other layer so that optimization-critical knowledge can be abstracted. Besides, we apply socialized cooperation to each layer, where federated averaging with MAA2C is implemented to ensure cooperation over private data for achieving optimal global solutions. Experimental evaluations on a proof-of-concept testbed along with two real traces demonstrate that baselines have 105% more delay than SocialEdge while being 76.6% less time efficiency and 21.6% less throughput. © 2023 IEEE.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez a ideia de socialização indique Agents."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "The ability for cloud data cen" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0751.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
