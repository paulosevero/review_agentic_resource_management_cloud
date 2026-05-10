---
id: paper-0903
title: Multi-agent deep reinforcement learning for trajectory planning in UAVs-assisted mobile edge computing with heterogeneous requirements
authors:
- Fan, Chenchen
- Xu, Hongyu
- Wang, Qingling
venue: Computer Networks
venue_type: journal
year: 2024
doi: 10.1016/j.comnet.2024.110469
url: https://www.scopus.com/pages/publications/85192316615?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Counterfactual inference
- Deep reinforcement learning
- Mobile edge computing
- Unmanned aerial vehicle
- Whale optimization algorithm
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

# paper-0903 — Multi-agent deep reinforcement learning for trajectory planning in UAVs-assisted mobile edge computing with heterogeneous requirements

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In heterogeneous wireless networks, massive user equipments (UEs) generate computing tasks with time-varying heterogeneous requirements. To improve the service quality, this paper formulates a unmanned aerial vehicles (UAVs)-assisted mobile edge computing (MEC) framework for time-varying heterogeneous task requirements. In the framework, the task delay and the number of successfully executed tasks are optimized by jointly controlling the trajectories of multiple UAVs. To address the considered trajectory planning optimization problem, a collaborative multi-agent deep reinforcement learning (MADRL) algorithm is proposed, where each UAV is regarded as a learning agent. First, a counterfactual inference based personalized policy update mechanism is proposed to evaluate the independent policy of agents by comparing the policy with a designed counterfactual policy. Based on this idea, each agent updates a personalized policy from both group and individual interests to improve its cooperation ability in dynamic and complex environments. Then, a diversified experience sampling mechanism is proposed to enhance the efficiency of policy evaluation and update with rich experiences provided by the environment interaction and the modified whale optimization algorithm. Finally, evaluation results demonstrate the superiority and effectiveness of the proposed MADRL algorithm. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0903.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
