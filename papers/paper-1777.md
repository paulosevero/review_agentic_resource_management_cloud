---
id: paper-1777
title: A Reinforcement Learning-Based Stochastic Game for Energy-Efficient UAV Swarm-Assisted MEC With Dynamic Clustering and Scheduling
authors:
- Li, Jialiuyuan
- Yi, Changyan
- Chen, Jiayuan
- Shi, You
- Zhang, Tong
- Li, Xiaolong
- Wang, Ran
- Zhu, Kun
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TGCN.2024.3424449
url: https://www.scopus.com/pages/publications/85197477722?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 255--270
keywords:
- long-term energy efficiency
- MEC
- reinforcement learning
- stochastic game
- UAV swarm
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

# paper-1777 — A Reinforcement Learning-Based Stochastic Game for Energy-Efficient UAV Swarm-Assisted MEC With Dynamic Clustering and Scheduling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we study the energy-efficient unmanned aerial vehicle (UAV) swarm assisted mobile edge computing (MEC) with dynamic clustering and scheduling. In the considered system model, UAVs are divided into multiple swarms, with each swarm consisting of a leader UAV and several follower UAVs. These UAVs serve as mobile edge servers, providing computing services to their covered ground end-users. Unlike existing works, we allow UAVs to dynamically cluster into different swarms, in other words, each follower UAV can change its leader based on the time-varying spatial positions, updated application placement, etc. in a dynamic manner. With the objective of maximizing the long-term energy efficiency of the UAV swarm assisted MEC system, a joint optimization problem of UAV swarm dynamic clustering and scheduling is formulated. Considering the inherent cooperation and competition among intelligent UAVs, we further reformulate this problem as a combination of a series of strongly interconnected multi-agent stochastic games, and theoretically prove the existence of the corresponding Nash Equilibrium (NE). Then, we propose a novel reinforcement learning based UAV swarm dynamic coordination (RLDC) algorithm for obtaining such an equilibrium. Furthermore, the convergence and complexity of the RLDC algorithm are analyzed. Simulations are performed to evaluate the performance of RLDC and illustrate its superiority compared to existing approaches.  © 2017 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1777.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
