---
id: paper-2794
title: Intelligent Cloud Resource Provisioning Using Multi-agent Reinforcement Learning and Deep Predictive Modelling
authors:
- Talhar, Nitin Rameshrao
- Gaikwad, D.P.
venue: International Journal of Intelligent Engineering and Systems
venue_type: journal
year: 2026
doi: 10.22266/ijies2026.0131.53
url: https://www.scopus.com/pages/publications/105027119883?origin=resultslist
publisher: Intelligent Network and Systems Society
pages: 880--895
keywords:
- Adaptive workload scheduling
- Cloud resource allocation
- Deep predictive modelling
- Distributed cloud environment
- Multi-agent reinforcement learning (MARL)
- Service level agreement (SLA)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2794 — Intelligent Cloud Resource Provisioning Using Multi-agent Reinforcement Learning and Deep Predictive Modelling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient cloud resource allocation is a critical challenge due to unpredictable workloads, fluctuating demand and energy constraints. Traditional heuristic and metaheuristic approaches like First Fit, Particle Swarm Optimization (PSO) and Ant Colony Optimization (ACO) are often struggle with adaptability, scalability and convergence in dynamic cloud environments. This paper proposes a hybrid Artificial Intelligence driven framework that combines Multi Agent Reinforcement Learning (MARL) optimization and deep predictive modelling. Each agent is representing a cloud node, learns allocation policies through reinforcement learning while a genetic algorithm evolves the agents’ neural network architectures and hyperparameters. Simultaneously Long Short-Term Memory (LSTM) based predictive modelling forecasts future workloads, enabling proactive resource scaling. A multi-objective reward function balances energy efficiency, Service Level Agreement (SLA) adherence and operational cost. Experiments using CloudSimPlus with real-world Google-Cluster traces demonstrate significant improvements in reduced SLA violations, enhanced load balancing, 23% higher resource utilization and 21% lower operational costs compared to conventional methods. This work highlights the potential of evolution-guided cooperative MARL integrated with predictive modelling for intelligent and sustainable cloud computing. © This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. https://creativecommons.org/licenses/by-sa/4.0/

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2794.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
