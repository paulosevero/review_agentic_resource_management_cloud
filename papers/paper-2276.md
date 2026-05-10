---
id: paper-2276
title: Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers
authors:
- Wang, Ting
- Cheng, Kai
- Du, Xiao
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2025
doi: 10.1109/INFOCOM55648.2025.11044699
url: https://www.scopus.com/pages/publications/105011040149?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Agents
- Collaborative learning
- Congestion control (communication)
- Distributed computer systems
- Learning algorithms
- Multi-task learning
- Optimization
- Robustness (control systems)
- Traffic congestion
- Collaborative network
- Data center networks
- Datacenter
- Multi tasks
- Network optimization
- Optimization strategy
- Performance
- Reinforcement learnings
- Sub-optimal performance
- Traffic scheduling
- Multi agent systems
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2276 — Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As data center networks increasingly grow in complexity and scale, efficiently managing traffic scheduling and congestion control becomes crucial for optimizing network performance. Traditional single-task optimization strategies often fall short, failing to adequately address the interplay between different tasks and resulting in suboptimal performance with inefficiencies and robustness issues. To tackle these challenges, this paper proposes a novel Multi-Task Reinforcement Learning (MTRL)-based collaborative Network Optimization scheme, termed MTRLNO, which establishes a structured framework with central and edge systems (i.e., hosts and switches). The SDN-enabled central system incorporates an MTRL agent that simultaneously optimizes traffic scheduling and congestion control tasks, leveraging global network state information to formulate instructive optimization policies for edge systems. Switches implement decentralized multi-agent RL agents to facilitate automatic ECN tuning for congestion control, with the ability to handle incast issues. Hosts feature an MTRL-guided Multiple Level Feedback Queue (MLFQ) demotion threshold adjustment scheme for adaptive traffic scheduling. We further develop a Prioritized Experience Replay-based Soft Actor-Critic (PERSAC) algorithm to enhance learning efficiency and a customized multi-task learning algorithm via improved parameter-sharing to effectively adapt across multiple tasks. Experimental results demonstrate that MTRLNO significantly outperforms state-of-the-art approaches in terms of FCT, latency, and robustness across diverse network conditions.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2276.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
