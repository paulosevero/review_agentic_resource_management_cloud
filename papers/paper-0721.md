---
id: paper-0721
title: Everyone-Centric Heterogeneous Multi-Server Computation Offloading in ITS with Pervasive AI
authors:
- Song, Xiaoqin
- Xu, Bowen
- Zhang, Xinting
- Wang, Shumo
- Song, Tiecheng
- Xing, Guoliang
- Liu, Fang
venue: IEEE Network
venue_type: journal
year: 2023
doi: 10.1109/MNET.131.2200394
url: https://www.scopus.com/pages/publications/85149812102?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 62--68
keywords:
- Client server computer systems
- Computation offloading
- Computation theory
- Computer architecture
- Deep learning
- Game theory
- Intelligent systems
- Job analysis
- Resource allocation
- Cloud-computing
- Computation offloading
- Computational modelling
- Edge computing
- Intelligent transportation systems
- Multiaccess
- Multiservers
- Resource management
- Service experience
- Task analysis
- Reinforcement learning
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
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

# paper-0721 — Everyone-Centric Heterogeneous Multi-Server Computation Offloading in ITS with Pervasive AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The challenges of everyone-centric customized end-To-end (E2E) service experience are spurring the worldwide interests on the sixth-generation (6G) networks. Nevertheless, in current intelligent transportation systems (ITS), fixed roadside units (RSUs) based multi-Access edge computing (MEC) has the defects of poor flexibility, unbalanced utilization and high deployment cost, which cannot meet the diverse requirements for computation-intensive and latency-sensitive Internet of vehicles (IoV) services. In this article, we propose a novel MEC architecture with multiple heterogeneous servers and pervasive intelligence to provide computation offloading cooperatively for customized requirements of task vehicle users (TVUs). A potential game theory and federated deep reinforcement learning based approach, namely GT-FDRL, is proposed to decouple the offloading decision and resource allocation. First, a binary offloading model based on game theory is utilized to make offloading decisions. Secondly, horizontal federated learning is introduced to multi-Agent double deep Q-network (DDQN) to optimize the channel assignment and power allocation. Furthermore, the client-server architecture and federated aggregation are used to maintain the global model. A case study is presented and the simulation results demonstrate the effectiveness and robustness of our proposed approach. © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "The challenges of everyone-cen" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_pervasive_ai, matched_substring: "Pervasive AI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0721.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
