---
id: paper-0691
title: Multiagent Meta-Reinforcement Learning for Optimized Task Scheduling in Heterogeneous Edge Computing Systems
authors:
- Niu, Liwen
- Chen, Xianfu
- Zhang, Ning
- Zhu, Yongdong
- Yin, Rui
- Wu, Celimuge
- Cao, Yangjie
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3241222
url: https://www.scopus.com/pages/publications/85148434444?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10519--10531
keywords:
- Computation task scheduling
- heterogeneous edge computing systems
- Markov decision process (MDP)
- meta-learning
- multiagent proximal policy optimization (PPO)
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

# paper-0691 — Multiagent Meta-Reinforcement Learning for Optimized Task Scheduling in Heterogeneous Edge Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile-edge computing (MEC) brings the potential to address the ever increasing computation demands from the mobile users (MUs). In addition to local processing, the resource-constrained MUs in an MEC system can also offload computation to the nearby servers for remote execution. With the explosive growth of mobile devices, computation offloading faces the challenge of spectrum congestion, which, in turn, deteriorates the overall quality of computation experience. This article, hence, investigates computation task scheduling in a heterogeneous cellular and WiFi MEC system. Such a system provides both licensed and unlicensed spectrum opportunities. Due to the sharing of communication and computation resources as well as the uncertainties, we formulate the problem of computation task scheduling among the competing MUs in a stationary heterogeneous edge computing system as a noncooperative stochastic game. We propose an approximation-based multiagent Markov decision process without the global system state observations, under which a multiagent proximal policy optimization (PPO) algorithm is derived to solve the corresponding Nash equilibrium. When expanding to a nonstationary heterogeneous edge computing system, the obtained algorithm suffers from the slow convergence due to constrained adaptability. Accordingly, we explore meta-learning and propose a multiagent meta-PPO algorithm, which rapidly adapts the control policy learning to the nonstationarity. Numerical experiments demonstrate performance gains from our proposed algorithms. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0691.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
