---
id: paper-1429
title: Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently
authors:
- Bhaurao, Phole Kamal
- Sawant, S.B.
- Umayal, A.R.
- Surekha, Swarna
- Beg, Mirza Samiulla
- Gupta, Umang
venue: Proceedings of 2025 10th International Conference on Science Technology, Engineering and Mathematics, ICONSTEM 2025
venue_type: conference
year: 2025
doi: 10.1109/ICONSTEM65670.2025.11374729
url: https://www.scopus.com/pages/publications/105034484607?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- GNN
- Horovod
- Kubernetes
- MAPPO
- RLlib
- TensorRT
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

# paper-1429 — Multi-Agent Reinforcement Learning Optimizing Cloud Resource Scheduling Efficiently

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this research, we present Proximal Policy Optimization (PPO) framework for Multi-Agent Systems (MAPPO) with Graph Neural Network (GNN) for online cloud resource allocation on heterogeneous infrastructure. We also use Ray RLlib distributed training environment for this (with every server represented as an intelligent agent acting in decentralized mode (Centralized Training with Decentralized Execution (CTDE) paradigm). Interagent dependencies are modelled using attention mechanisms and policy gradient calculation is done by the architecture using entropy regularized Stable-Baselines3. Custom operators provide real-time decisions from the scheduling point of view to Kubernetes orchestration with a maximum of 100 thousand task requests per hour. It utilizes time-series forecasting to model prediction workload and TensorRT optimization for below 10 ms inference latency. Deployed on Google Cloud Platform with multi-regional cluster structure, the framework reduces the resource wastage by 67 percent and improve the SLA compliance by 54 percent as compared to traditional heuristic scheduler. Horovod has the feature of making synchronization of weights scalable with 128 training nodes. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1429.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
