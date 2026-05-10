---
id: paper-1886
title: 'GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum'
authors:
- Liu, Peini
- Santos, José
- De Turck, Filip
- Guitart, Jordi
venue: Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025
venue_type: conference
year: 2025
doi: 10.1145/3773274.3774275
url: https://www.scopus.com/pages/publications/105027132697?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: ''
keywords:
- Computing Continuum
- Intelligent Service Migration
- Kubernetes
- Power-Performance Aware
- Reinforcement Learning
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1886 — GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Machine Learning (ML) services require both responsiveness and efficiency. In the dynamic Computing Continuum (CC), service migration has emerged as an important strategy to optimize service performance, improve power efficiency, or reduce operational costs. A basis enabler of the service migration in the CC is containerization and container orchestration, however, dynamically moving the service among Cloud and Edge servers based on several uncertainties is still challenging. In this paper, we present GreenWise, a framework for intelligent service migration for containerized ML services in the heterogeneous CC. GreenWise extends the monitoring agents to continuously monitor power consumption and performance metrics across diverse layers and sources in real-time, providing a holistic view of states. Leveraging Reinforcement Learning (RL), it enables Power-Performance aware strategies to achieve near-optimal online migration decisions under dynamic conditions. We perform GreenWise on top of a Kubernetes-based CC platform, implementing agents for intelligent migration for containerized ML services. Experimental results demonstrate that GreenWise achieves effective trade-offs between performance and power efficiency. Our proposed Power-Latency-Aware (MaskPPO) migration strategy outperforms Random and Round-Robin baselines 159.2% and 13.8% in a real cluster. These results highlight GreenWise's potential for sustainable and intelligent ML service migration in the dynamic CC. © 2025 Copyright held by the owner/author(s).

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1886.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
