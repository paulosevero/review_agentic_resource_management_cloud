---
id: paper-2569
title: Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems
authors:
- Fang, Juan
- Wang, Xinghao
- Liu, Yaqi
- Tang, Heng
- Li, Xiaolin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3674519
url: https://www.scopus.com/pages/publications/105033241203?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Collaborative Inference
- Edge Computing
- Large-Scale Models
- Multi-Agent
- Proximal Policy Optimization
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
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

# paper-2569 — Multi-Agent Collaborative Inference Optimization for Large-Scale DNNs in IoT Edge Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying large deep neural networks (DNNs) on resource-constrained Internet of Things (IoT) devices is often limited by high inference latency and energy consumption. This paper studies collaborative inference between user devices and edge servers, where a DNN is partitioned and executed across both sides under shared wireless resources. We jointly optimize the partition point across layers, uplink channel allocation, and transmission power control, and formulate the coupled decisions as a markov decision process (MDP). Under centralized training with decentralized execution (CTDE), we develop a multi-agent proximal policy optimization (MAPPO) framework with a multi-head critic and profiling-aware state design to stabilize learning under large hybrid action spaces. To validate practicality, we implement a containerized experimental platform that emulates resource-limited IoT devices and GPU enabled edge servers, enabling repeatable measurements of end-to-end latency and energy. Experiments with representative DNNs show that the proposed method consistently improves the latency–energy trade-off over baseline algorithms, achieving lower end-to-end latency and comparable or lower energy consumption across diverse model structures and computation patterns. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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
  - `{ category: rl, pattern_id: rl_mappo, matched_substring: "MAPPO" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2569.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
