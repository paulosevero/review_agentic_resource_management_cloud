---
id: paper-2350
title: Reinforcement Learning for Dynamic Service Composition in Edge Networks
authors:
- Yalamati, Srinivasu
venue: 4th International Conference on Applied Artificial Intelligence and Computing, ICAAIC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICAAIC64647.2025.11330768
url: https://www.scopus.com/pages/publications/105034861522?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1158--1163
keywords:
- Adaptive Resource Allocation
- Distributed Systems
- Dynamic Service Composition
- Edge Computing
- Energy Efficiency
- Low-Latency Networks
- Q-learning
- Reinforcement Learning
- Service Orchestration
- SLA Optimization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2350 — Reinforcement Learning for Dynamic Service Composition in Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In distributed networks, edge computing has emerged as a fundamental paradigm for scalable and lowlatency service delivery on integrated hardware and software stacks. Unfortunately, the optimal service composition at the edge is heavily hindered by dynamic network conditions, resource diversity, and user demand evolution. This work present the Reinforcement Learning (RL) framework for dynamic service composition in edge networks with adaptive policies that intelligent agents can learn at run-time to map the constituent components to edge nodes. In the proposed paradigm, edge node selection for a service is one of the decision steps in an overall sequential decision-making process affecting latency, energy, and QoS conformance. The agent is designed to learn optimal mappings between these two sets of attributes (in terms of optimized SLA (%) - the proxy variable for total traffic - under energy and latency constraints) through a Q-learning algorithm. In order to reproduce heterogeneous edge nodes with various processing resources, bandwidth, and energy costs, an original simulation environment was implemented. Synthetic edge workloads were simulated to compare the RL-based approach with random allocation, greedy heuristic, and static weighted mapping (without online decisions on location targeting). The RL model significantly outperforms all baselines, as experimental results indicate that the average latency is reduced by 25-40%, the energy consumption by 15-25%, and more than 95% of SLAs are satisfied. The model is also responsive to node failures and bandwidth variations, showing robustness under workload bursts and environmental distortions. This agility underscores the potential of reinforcement learning in autonomously managing distributed edge infrastructures to enhance operational efficiency and reliability. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2350.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
