---
id: paper-0744
title: Bandwidth Allocation and Trajectory Control in UAV-Assisted IoV Edge Computing Using Multiagent Reinforcement Learning
authors:
- Wang, Juzhen
- Zhang, Xiaoli
- He, Xingshi
- Sun, Yongqiang
venue: IEEE Transactions on Reliability
venue_type: journal
year: 2023
doi: 10.1109/TR.2022.3192020
url: https://www.scopus.com/pages/publications/85135753872?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 599--608
keywords:
- Attention mechanism
- bandwidth assignment
- location deployment
- multiagent deep reinforcement learning (DRL)
- value decomposition network (VDN)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0744 — Bandwidth Allocation and Trajectory Control in UAV-Assisted IoV Edge Computing Using Multiagent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid development of an unmanned aerial vehicle (UAV) has brought new opportunities for wireless communication and edge computing. In this article, we investigate the scenario where multiple UAVs serve as edge computing devices for the Internet of Vehicles (IoV). Regardless of the allocation of computing resources, we focus on bandwidth allocation and trajectory control to maximize the communication capacity of the system so that the UAV edge computing network can process more data. With this intent, a UAV-assisted IoV edge computing system model is constructed as a nonconvex optimization problem, aiming to maximize the achievable channel capacity of the network. To solve this problem, two 'quasi-distributed' multiagent algorithms, i.e., actor-critic mixing network (AC-Mix) and multi-attentive agent deep deterministic policy gradient (MA2DDPG), are proposed based on deep deterministic policy gradient. Specifically, AC-Mix utilizes a mixing network to obtain a global Q-value for better evaluation of joint action, while MA2DDPG employs a multihead attention mechanism to achieve multiagent collaboration. Using multi-agents deep deterministic policy gradient (MADDPG) as benchmark, several experiments are carried out to verify the performance of the proposed algorithms. Simulation results show that the convergence velocity of AC-Mix and MA2DDPG is improved by 30.0% and 63.3%, respectively, compared with MADDPG.  © 1963-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0744.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
