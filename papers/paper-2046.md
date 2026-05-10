---
id: paper-2046
title: Adaptive Cloud Resource Allocation Using Attention-Driven Deep Reinforcement Learning
authors:
- Prabha, Pandi S.
- Rengarajan, A.
venue: Engineering, Technology and Applied Science Research
venue_type: journal
year: 2025
doi: 10.48084/etasr.13443
url: https://www.scopus.com/pages/publications/105026906467?origin=resultslist
publisher: Dr D. Pylarinos
pages: 29334--29340
keywords:
- Cloud Computing (CC)
- Deep QNetwork (DQN)
- Deep Reinforcement Learning (DRL)
- multi-agent model
- resource allocation
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2046 — Adaptive Cloud Resource Allocation Using Attention-Driven Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient resource allocation remains a critical challenge in dynamic Cloud Computing (CC) environments, where maintaining Quality of Service (QoS), minimizing latency, and ensuring fairness are paramount. This study proposes a novel Deep Reinforcement Learning (DRL)-based framework that models resource allocation as a multi-agent Markov Decision Process (MDP), with each Virtual Machine (VM) link treated as an autonomous agent. Leveraging a Deep Q-Network (DQN) architecture enhanced by an attention mechanism, the framework enables agents to refine state observations and coordinate decisions adaptively. A custom reward function balancing throughput, latency, and resource cost guides the learning process, whereas experience replay and temporal annealing strategies promote optimal policy convergence. Experimental results demonstrate significant improvements in energy efficiency, execution time, waiting time, fairness, and throughput when benchmarked against existing Reinforcement Learning (RL)-based, Resource Management Framework–Deep Neural Network (RMF-DNN), and Federated Reinforcement Learning (F-RL) models. The proposed system introduces architectural innovations, including decentralized agent-based learning, attention-guided state refinement, and fairness-aware scheduling, establishing a scalable and intelligent solution for cloud resource management. © (c) by the authors

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2046.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
