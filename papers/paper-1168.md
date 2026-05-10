---
id: paper-1168
title: Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios
authors:
- Sang, Ziyi
- Cai, Mingjun
- Shen, Shihao
- Zhang, Cheng
- Wang, Xiaofei
- Qiu, Chao
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901331
url: https://www.scopus.com/pages/publications/105000819313?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4618--4623
keywords:
- diffusion model
- imitation learning
- Kubernetes
- Service migration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1168 — Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid increase in user scale and the explosive rise of emerging applications, the contradiction between heavy load pressure and excellent network performance is becoming increasingly prominent, and task processing is gradually shifting towards the edge of the network. However, the resources of edge networks are limited, making it difficult to meet the huge computing and storage needs, and managing and allocating edge nodes is also a huge challenge. The Kubernetes (K8S) framework for deploying and orchestrating containerized applications provides a solution for this. How to improve the adaptability of K8S in edge networks, meet the demand of services for heterogeneous resources, and train decision models with better performance using limited datasets has become an urgent problem to be solved. Based on the above issues, we propose a distributed service migration architecture for multi-user access, and design a service migration algorithm based on imitation learning to achieve resource combination optimization and reduce the impact of insufficient data on model training. Design agent models based on diffusion models to accelerate model convergence and avoid the increase in training costs caused by constantly updating agent models. Our results show that the efficiency of the expert model is 92.0%, and the learning process of the agent model can converge within 100 training cycles with an accuracy of 97.89%. The service processing delay, throughput rate, and model convergence are all significantly better than those of classical algorithms. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1168.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
