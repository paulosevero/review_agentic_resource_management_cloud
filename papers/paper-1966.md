---
id: paper-1966
title: Reinforcement Learning-Based Adaptive Utilization of Resources in Cloud Networks
authors:
- Mondal, Sonali
- Lalnunthari
venue: 2025 International Conference on Intelligent Control, Computing and Communications, IC3 2025
venue_type: conference
year: 2025
doi: 10.1109/IC363308.2025.10957566
url: https://www.scopus.com/pages/publications/105003902364?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1013--1019
keywords:
- adaptive resource allocation
- cloud systems
- cost reduction
- deep reinforcement learning
- dynamic resource allocation
- multi-agent reinforcement learning
- Q-learning
- quality of service
- reinforcement learning
- resource management
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

# paper-1966 — Reinforcement Learning-Based Adaptive Utilization of Resources in Cloud Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The necessity of dynamic resource allocation in cloud systems has opened door for reinforcement learning based approaches in the domain. Cloud computing services provide users with on-demand resources for various workloads with distinct service performance requirements. However, dynamic workloads, varying resource requirements, and the tension between efficient performance and cost efficiency can place significant strain on the resource management within these types of platforms. Because cloud systems are inherently dynamic processes, traditional resource allocation approaches, like manual provisioning or using predefined optimization rules, are not likely to solve the problem satisfactorily which makes adaptive approaches (like those driven with RL) as appealing alternatives. A RL-based resource allocation framework includes an agent that interact with the cloud environment by trying different actions and learns the optimal policies as a result. This usually involves specifying a reward function, where the agent receives a signal indicating how well the system is performing, along with a number of criteria like minimizing latency, maximizing throughput or cutting operational costs. The RL agent works in a dynamical manner, meaning it adapts its resource allocation decision rules optimally based on previously made actions so as to improve efficiency in future decisions. This is fairly effective in managing cloud(such) environments which are extremely dynamic, i.e. resource requirement of these systems alters with time due varying user demands, system conditions and external dependencies. We propose the use of RL to provide dynamic resource allocation in cloud systems which brings us to discuss certain critical problems in this paper. The first part introduces the main elements of an RL framework for resource management agent: the environment, the state space, the action space, and the reward function. Cloud system state space may refer to cloud system present configuration abundance of resources, workload requirements, and performance metrics. The possible action space captures resource allocation decisions, such as adding or removing virtual machines, redistributing storage or modifying the network capacity. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1966.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
