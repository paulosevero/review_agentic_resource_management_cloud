---
id: paper-1296
title: Energy Consumption Modeling and Optimization of UAV-Assisted MEC Networks Using Deep Reinforcement Learning
authors:
- Yan, Ming
- Zhang, Litong
- Jiang, Wei
- Chan, Chien Aun
- Gygax, Andre F.
- Nirmalathas, Ampalavanapillai
venue: IEEE Sensors Journal
venue_type: journal
year: 2024
doi: 10.1109/JSEN.2024.3370924
url: https://www.scopus.com/pages/publications/85187378754?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13629--13639
keywords:
- Cooperation strategy
- deep reinforcement learning (DRL)
- energy consumption
- multiaccess edge computing (MEC)
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
    my_justification: RL
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

# paper-1296 — Energy Consumption Modeling and Optimization of UAV-Assisted MEC Networks Using Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-assisted multiaccess edge computing (MEC) technology has garnered significant attention and has been successfully implemented in specific scenarios. The optimization of the network energy consumption in the relevant scenarios is essential for the whole system performance due to the constrained energy capacity of UAVs. However, the dynamic changes in MEC network resources make energy consumption optimization a challenge. In this article, a multi-UAV-multiuser MEC model is established to assess the system energy consumption, and the optimization problem of multi-UAV cooperation strategies is formulated based on the model. Then, a multiagent deep deterministic policy gradient (MADDPG) algorithm based on deep reinforcement learning (DRL) is employed to resolve the above optimization problem. Each UAV is equivalent to a single agent that cooperates with other agents to train actors and critic evaluation networks to accomplish collaborative decision-making. In addition, a prioritized experience replay (PER) scheme is used to improve the convergence of the training process. Simulation results show the impact of changes in different network resources on the network energy consumption by comparing the performance of different algorithms. The findings presented in this article serve as a valuable reference for future work on system performance optimization, specifically in terms of energy efficiency.  © 2001-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1296.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
