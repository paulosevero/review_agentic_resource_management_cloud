---
id: paper-0534
title: Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems
authors:
- Zhang, Yi
- Zhu, Haihua
- Tang, Dunbing
- Zhou, Tong
- Gui, Yong
venue: Robotics and Computer-Integrated Manufacturing
venue_type: journal
year: 2022
doi: 10.1016/j.rcim.2022.102412
url: https://www.scopus.com/pages/publications/85133429544?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Flexible job-shop scheduling problem
- Multi-agent manufacturing system
- Proximal policy optimization
- Reinforcement learning
- Smart manufacturing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0534 — Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Personalized orders bring challenges to the production paradigm, and there is an urgent need for the dynamic responsiveness and self-adjustment ability of the workshop. Traditional dispatching rules and heuristic algorithms solve the production planning and control problems by making schedules. However, the previous methods cannot work well in a changeable workshop environment when encountering a large number of stochastic disturbances of orders and resources. Recently, the potential of artificial intelligence (AI) algorithms in solving the dynamic scheduling problem has attracted researchers' attention. Therefore, this paper presents a multi-agent manufacturing system based on deep reinforcement learning (DRL), which integrates the self-organization mechanism and self-learning strategy. Firstly, the manufacturing equipment in the workshop is constructed as an equipment agent with the support of edge computing node, and an improved contract network protocol (CNP) is applied to guide the cooperation and competition among multiple agents, so as to complete personalized orders efficiently. Secondly, a multi-layer perceptron is employed to establish the decision-making module called AI scheduler inside the equipment agent. According to the perceived workshop state information, AI scheduler intelligently generates an optimal production strategy to perform task allocation. Then, based on the collected sample trajectories of scheduling process, AI scheduler is periodically trained and updated through the proximal policy optimization (PPO) algorithm to improve its decision-making performance. Finally, in the multi-agent manufacturing system testbed, dynamic events such as stochastic job insertions and unpredictable machine failures are considered in the verification experiments. The experimental results show that the proposed method is capable of obtaining the scheduling solutions that meet various performance metrics, as well as dealing with resource or task disturbances efficiently and autonomously. © 2022 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0534.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
