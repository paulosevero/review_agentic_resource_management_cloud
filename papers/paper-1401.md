---
id: paper-1401
title: 'Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability'
authors:
- Asadi, Navidreza
- Ursu, Rǎzvan-Mihai
- Wong, Leon
- Kellerer, Wolfgang
venue: NGNO 2025 - Proceedings of the 2025 1st Workshop on Next-Generation Network Observability, Part of SIGCOMM 2025
venue_type: conference
year: 2025
doi: 10.1145/3748496.3748991
url: https://www.scopus.com/pages/publications/105019924497?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 21--28
keywords:
- Adversarial Benchmarking
- Adversarial Patterns
- Autonomous Networks
- Bayesian Optimization
- Chaos Engineering
- Cost Optimization
- Fault Tolerance
- Microservice Autoscaling
- Multi-Agent Systems
- Parallel Environments
- Proactive Observability
- Reinforcement Learning
- System Dependability
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
    proposed_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    winning_category: classical_agents
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

# paper-1401 — Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Microservices autoscaling is essential for dynamically adjusting resources to meet fluctuating workload demands and maintain service-level objectives (SLOs), such as latency, while minimizing resource usage. However, the control logic of modern autoscalers is susceptible to exploitation. Assessing its performance requires more than passive monitoring; the rapid evolution of application development has outpaced the availability of observability tools to benchmark and identify corner cases in autoscaling configurations relative to an application's behavior. In this work, we aim to address a critical yet underexplored question: Can we systematically identify adversarial inputs, i.e., traffic anti-patterns that disproportionately increase SLO violations or operational costs - -or both? We propose Simurgh, an adversarial benchmarking framework designed to generate traffic patterns tailored for finding autoscaling anti-patterns. It evolves strategies based on real-time observability signals from both the application and infrastructure layers. This problem is inherently complex due to its large solution space. To address this, we introduce heuristics that relax the problem while leveraging multiple parallel systems, each paired with a local controller and optimizer. These controllers act as individual agents being managed by a global controller, asynchronously generating diverse traffic patterns while collectively optimizing toward a shared adversarial objective. We evaluate our framework on two applications and three optimization methods, including Bayesian optimization, chaos engineering, and a distributed reinforcement learning approach. Our preliminary empirical results illustrate Simurgh's effectiveness in identifying anti-patterns with respect to different objectives, such as SLO violations and operational costs, and demonstrate generalizability across different applications and cluster sizes of 10× larger. © 2025 Owner/Author.

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
- **regex_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **winning_category:** 'classical_agents'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1401.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
