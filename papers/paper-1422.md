---
id: paper-1422
title: 'Federated Synergy: Hierarchical Multi-Agent Learning for Sustainable Edge Computing in IIoT'
authors:
- Benila, S.
- Devi, K.
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3560781
url: https://www.scopus.com/pages/publications/105003766725?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 68311--68322
keywords:
- Deep Q-Network
- edge computing
- federated learning
- hierarchical multi-agent federated actor-critic (HMAFAC)
- Industrial Internet of Things
- task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
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

# paper-1422 — Federated Synergy: Hierarchical Multi-Agent Learning for Sustainable Edge Computing in IIoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Industrial Internet of Things (IIoT) presents significant challenges in task offloading, resource allocation, and energy efficiency, necessitating intelligent, scalable, and adaptive solutions. This paper introduces the Hierarchical Multi-Agent Federated Actor-Critic (HMAFAC) algorithm. This novel approach integrates hierarchical reinforcement learning with multi-agent federated learning to enhance decision-making in dynamic edge computing environments. It employs multi-agent reinforcement learning to optimize resource allocation and task offloading by leveraging local Actor-Critic models on IoT edge devices. A Deep Q-Network (DQN) agent manages task offloading decisions based on real-time system states, ensuring efficient task execution. To maintain data privacy and reduce communication overhead, federated learning aggregates model updates at the edge server, eliminating the need for raw data exchange. Additionally, a hierarchical framework enables adaptive scheduling, allowing flexible computational scaling from edge to cloud servers based on task complexity and network conditions. By effectively reducing latency and energy consumption, enhancing system adaptability, and maintaining computational efficiency, HMAFAC overcomes key limitations of existing IIoT frameworks. Simulation results validate its superior performance compared to baseline methods regarding resource utilization, energy conservation, and model convergence. These findings establish HMAFAC as a robust and scalable framework for optimizing IIoT applications in distributed and resource-constrained environments. Future work will further explore advanced federated learning techniques, enhanced privacy mechanisms, and real-world deployment in industrial systems to improve efficiency and scalability. © 2013 IEEE.

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
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "The Industrial Internet of Thi" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1422.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
