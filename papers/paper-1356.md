---
id: paper-1356
title: Decomposition-based learning in drone-assisted wireless-powered mobile edge computing networks
authors:
- Zhou, Xiaoyi
- Huang, Liang
- Ye, Tong
- Sun, Weiqiang
venue: Digital Communications and Networks
venue_type: journal
year: 2024
doi: 10.1016/j.dcan.2023.11.010
url: https://www.scopus.com/pages/publications/85208762624?origin=resultslist
publisher: KeAi Communications Co.
pages: 1769--1781
keywords:
- Mobile-edge computing
- Multi-agent reinforcement learning
- Offloading decision
- Trajectory planning
- Unmanned aerial vehicle
- Wireless power transfer
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

# paper-1356 — Decomposition-based learning in drone-assisted wireless-powered mobile edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates the multi-Unmanned Aerial Vehicle (UAV)-assisted wireless-powered Mobile Edge Computing (MEC) system, where UAVs provide computation and powering services to mobile terminals. We aim to maximize the number of completed computation tasks by jointly optimizing the offloading decisions of all terminals and the trajectory planning of all UAVs. The action space of the system is extremely large and grows exponentially with the number of UAVs. In this case, single-agent learning will require an overlarge neural network, resulting in insufficient exploration. However, the offloading decisions and trajectory planning are two subproblems performed by different executants, providing an opportunity for problem-solving. We thus adopt the idea of decomposition and propose a 2-Tiered Multi-agent Soft Actor-Critic (2T-MSAC) algorithm, decomposing a single neural network into multiple small-scale networks. In the first tier, a single agent is used for offloading decisions, and an online pretrained model based on imitation learning is specially designed to accelerate the training process of this agent. In the second tier, UAVs utilize multiple agents to plan their trajectories. Each agent exerts its influence on the parameter update of other agents through actions and rewards, thereby achieving joint optimization. Simulation results demonstrate that the proposed algorithm can be applied to scenarios with various location distributions of terminals, outperforming existing benchmarks that perform well only in specific scenarios. In particular, 2T-MSAC increases the number of completed tasks by 45.5% in the scenario with uneven terminal distributions. Moreover, the pretrained model based on imitation learning reduces the convergence time of 2T-MSAC by 58.2%. © 2023 Chongqing University of Posts and Telecommunications

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1356.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
