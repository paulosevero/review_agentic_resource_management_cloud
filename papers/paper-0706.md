---
id: paper-0706
title: Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning
authors:
- Rossi, Fabiana
- Cardellini, Valeria
- Lo Presti, Francesco
- Nardelli, Matteo
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2023
doi: 10.1109/TCC.2022.3163357
url: https://www.scopus.com/pages/publications/85127477181?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1807--1821
keywords:
- deep Q-learning
- Elasticity
- microservice architecture
- reinforcement learning
- self-adaptation
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0706 — Dynamic Multi-Metric Thresholds for Scaling Applications Using Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —Cloud-native applications increasingly adopt the microservices architecture, which favors elasticity to satisfy the application performance requirements in face of variable workloads. To simplify the elasticity management, the trend is to create an auto-scaler instance per microservice, which controls its horizontal scalability by using the classic threshold-based policy. Although easy to implement, setting manually the scaling thresholds, which are usually statically-defined on a single metric, may lead to poor scaling decisions when applications are heterogeneous in terms of resource consumption. In this article, we study dynamic multi-metric threshold-based scaling policies, that exploit Reinforcement Learning (RL) to autonomously update the scaling thresholds, one per controlled resource (CPU and memory). The proposed RL approaches (i.e., QL, MB, and DQL Threshold) use different degrees of knowledge about the system dynamics. To model the thresholds’ adaptation actions, we consider two RL-based architectures. In the single-agent architecture, one agent drives the updates of both scaling thresholds. To speed-up the learning, the multi-agent architecture adopts a distinct agent per threshold. Simulation- and prototype-based results show the benefits of the proposed solutions when compared to the state-of-the-art policies and highlight the advantages of multi-agent MB Threshold and DQL Threshold approaches, in terms of deployment objectives and execution times. © 2023 Institute of Electrical and Electronics Engineers Inc.. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0706.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
