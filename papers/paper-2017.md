---
id: paper-2017
title: Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts
authors:
- Park, Eun Chan
- Baek, Kyeong Deok
- Ko, In-Young
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2025
doi: 10.1109/TSC.2025.3617074
url: https://www.scopus.com/pages/publications/105018316050?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3865--3877
keywords:
- autonomic services
- fog services
- Microservice autoscaling
- multi-agent reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2017 — Hierarchical Decentralized Autoscaling for Spatio-Temporal Load Bursts

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of fog computing has shown promising results for reducing network latency and congestion in the cloud. In this environment, effective autoscaling to handle spatio-temporal load bursts in geographically distributed and resource-constrained fog nodes has become a timely problem. A typical strategy for autoscaling is based on centralized monitoring of the fog nodes and the deployed service instances. However, centralized collection and analysis of the metrics for autoscaling can become infeasible with the increasing number of fog nodes. Moreover, the dynamic and fluctuating characteristics of the fog nodes make effective autoscaling challenging in fog computing environments. In this work, we propose HiDRA, a Hierarchical Decentralized Autoscaler that scales and places microservice instances based on multi-agent reinforcement learning. In HiDRA, agents are divided into scaling and placement agents that collaborate with each other to effectively handle spatio-temporal load bursts in fog computing. These Deep Q-Network-based autoscaling agents are trained solely based on their regional observations at runtime, eliminating the need for a centralized collection of metrics. We evaluated HiDRA in multiple simulated fog environments created using a real-world dataset. The environments were divided into three levels of sparsity, each consisting of 20, 15, and 10 initial instances and unstable nodes. The result shows that comparatively by ratio against the baseline, HiDRA increased the average request success rate by 10.7%, 16.4%, and 36.7% and reduced the number of created instances by 12.3%, 15.9%, and 16.8% in environments with 20, 15, and 10 initial instances and unstable nodes, respectively.  © 2008-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2017.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
