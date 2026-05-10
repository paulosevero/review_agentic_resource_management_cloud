---
id: paper-1980
title: 'FAMASO: fog-adaptive multi-agent scheduling optimization'
authors:
- Nagabushnam, Ganesan
- Kim, Kyong Hoon
- Choi, Yundo
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-025-05588-3
url: https://www.scopus.com/pages/publications/105013677031?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Aperiodic task
- Cloud computing
- Deadline task
- Deep multi-agent reinforcement learning
- Heterogeneous Fog computing
- IoT
- Proximal policy optimization
- Recurrent neural network
- Task scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1980 — FAMASO: fog-adaptive multi-agent scheduling optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient scheduling of aperiodic tasks in fog-cloud environments poses significant challenges due to dynamic workloads, heterogeneous resources, and the need to simultaneously optimize for deadline adherence, energy efficiency, scalability, and Quality of Service (QoS). Traditional scheduling approaches, including heuristic methods such as Earliest Deadline First, and metaheuristic techniques such as Genetic Algorithm and Particle Swarm Optimization, are often limited by inflexible prioritization and poor adaptability to workload variation. Similarly, single-agent reinforcement learning models such as Proximal Policy Optimization and Asynchronous Advantage Actor-Critic exhibit limited scalability and delayed convergence in distributed settings. To address these limitations, this paper proposes fog-adaptive multi-agent scheduling optimization (FAMASO), a deep multi-agent reinforcement learning framework that integrates Earliest Deadline First-based task prioritization with Proximal Policy Optimization and Recurrent Neural Networks for real-time, decentralized scheduling in fog-cloud infrastructures. FAMASO dynamically adapts to system conditions, learns temporal task patterns, and supports distributed decision-making to optimize key objectives. Experimental evaluations across workloads of 100 to 900 aperiodic tasks and fog networks ranging from 10 to 100 nodes show that FAMASO consistently outperforms baseline algorithms, including Earliest Deadline First, Genetic Algorithm, Particle Swarm Optimization, Multi-Agent Deep Deterministic Policy Gradient, Asynchronous Advantage Actor-Critic, and Proximal Policy Optimization. FAMASO achieves up to 95.66% deadline adherence, 38% energy savings, 56% makespan reduction, 7.8% improvement in resource utilization, 70% reduction in scheduler time, and notably higher throughput, completing more tasks per unit time than all compared methods. Additionally, it achieves SLA violation rate reductions of up to 80%, demonstrating strong compliance with real-time constraints. These results validate FAMASO’s effectiveness, scalability, and practical potential for deploying efficient, SLA-aware task scheduling in next-generation fog-cloud computing environments supporting time-sensitive IoT applications. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Efficient scheduling of aperio" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1980.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
