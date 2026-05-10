---
id: paper-1203
title: 'Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement'
authors:
- Soumplis, Polyzois
- Kontos, Georgios
- Kokkinos, Panagiotis
- Kretsis, Aristotelis
- Barrachina-Muñoz, Sergio
- Nikbakht, Rasoul
- Baranda, Jorge
- Payaró, Miquel
- Mangues-Bafalluy, Josep
- Varvarigos, Emmanuel
venue: SN Computer Science
venue_type: journal
year: 2024
doi: 10.1007/s42979-024-02630-w
url: https://www.scopus.com/pages/publications/85187721285?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Cloud edge continuum
- Cloud native applications
- Multi-agent rollout
- Reinforcement learning
- Resource allocation
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

# paper-1203 — Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advancements in virtualization technologies and distributed computing infrastructures have sparked the development of cloud-native applications. This is grounded in the breakdown of a monolithic application into smaller, loosely connected components, often referred to as microservices, enabling enhancements in the application’s performance, flexibility, and resilience, along with better resource utilization. When optimizing the performance of cloud-native applications, specific demands arise in terms of application latency and communication delays between microservices that are not taken into consideration by generic orchestration algorithms. In this work, we propose mechanisms for automating the allocation of computing resources to optimize the service delivery of cloud-native applications over the edge-cloud continuum. We initially introduce the problem’s Mixed Integer Linear Programming (MILP) formulation. Given the potentially overwhelming execution time for real-sized problems, we propose a greedy algorithm, which allocates resources sequentially in a best-fit manner. To further improve the performance, we introduce a multi-agent rollout mechanism that evaluates the immediate effect of decisions but also leverages the underlying greedy heuristic to simulate the decisions anticipated from other agents, encapsulating this in a Reinforcement Learning framework. This approach allows us to effectively manage the performance–execution time trade-off and enhance performance by controlling the exploration of the Rollout mechanism. This flexibility ensures that the system remains adaptive to varied scenarios, making the most of the available computational resources while still ensuring high-quality decisions. © The Author(s) 2024.

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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "The advancements in virtualiza" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1203.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
