---
id: paper-0922
title: 'MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC'
authors:
- Gao, Zhen
- Fu, Jiaming
- Jing, Zongming
- Dai, Yu
- Yang, Lei
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3362988
url: https://www.scopus.com/pages/publications/85184814018?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 18483--18502
keywords:
- Joint trajectory planning and task offloading (JTPTO)
- multiagent reinforcement learning (MARL)
- multiobjective reinforcement learning
- UAV-assisted mobile edge computing (MEC)
- unmanned aerial vehicle (UAV) cooperation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0922 — MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Existing joint trajectory planning and task offloading (JTPTO) methods provide ultralow latency services for mobile devices (MDs) in unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC). However, UAVs typically provide services to MDs under partial observation, leading to challenges in achieving optimal service performance due to information loss. Moreover, the JTPTO problem typically involves multiobjective optimization, which is challenging because the objectives may conflict with each other. In this article, we present a decentralized JTPTO method based on multiobjective and independently predicted communication multiagent actor-critic (MOIPC-MAAC). First, an IPC network is designed to facilitate UAV agents in learning a prior for communication between UAVs. UAV agents learn this prior through causal reasoning, which represents the mapping of UAV's observation to the level of confidence in choosing communication partners. The effect of one UAV on another UAV is predicted through the critic-network in multiagent reinforcement learning (MARL) and measured to indicate the necessity of UAV-UAV communication. Further, we regularize JTPTO policies to more effectively utilize exchanged messages. Second, a generalized variant of the Bellman optimality operator with multiple objectives is applied to address the JTPTO problem. We use it to learn a single parameterized expression that encompasses all the best JTPTO policies across the space of preferences. Experiments show that compared to existing solutions, MOIPC-MAAC reduces system costs by 14.23%-19.56% and the communication cost to approximately 11.23%. Moreover, compared to training from scratch, MOIPC-MAAC accelerates the adaptation of new JTPTO tasks with unknown preferences by 13.12%.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0922.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
