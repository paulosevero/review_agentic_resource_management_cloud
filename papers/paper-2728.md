---
id: paper-2728
title: Privacy preserving hierarchical graph federated learning for intelligent task scheduling in edge cloud networks
authors:
- Neerukonda, RatnaKumari
- Hariharan, B.
venue: Discover Computing
venue_type: journal
year: 2026
doi: 10.1007/s10791-026-10081-5
url: https://www.scopus.com/pages/publications/105034805385?origin=resultslist
publisher: Springer Science and Business Media B.V.
pages: ''
keywords:
- Federated learning
- Heterogeneous differential privacy
- Local-edge-cloud computing
- Multi-agent reinforcement learning
- Task offloading
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2728 — Privacy preserving hierarchical graph federated learning for intelligent task scheduling in edge cloud networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing reliance on latency-sensitive and privacy-critical applications in modern computing has highlighted the limitations of conventional task offloading methods in hierarchical Local-Edge-Cloud (LEC) environments. Key challenges include managing dynamic resource availability, minimizing execution latency, and ensuring strong data privacy without centralized data sharing. To address these issues, this research proposes a novel framework named Multi-agent Graph-based Reinforcement Federated learning with Improved Builder Optimization Algorithm (MGRF-IBOA). The framework starts by defining task offloading as a constrained optimization problem that reduces execution time, increases energy efficiency, and ensures privacy. MGRF-IBOA combines several intelligent mechanisms, including graph-based task-resource mapping for spatial allocation, multi-agent reinforcement learning for adaptive scheduling, federated learning for decentralized model updates, and heterogeneous differential privacy to meet varying user privacy needs. The optimization process is further enhanced using the Improved Builder Optimization Algorithm (IBOA) for faster and more accurate convergence. Experimental results demonstrate that MGRF-HDP is superior to previous benchmark solutions, reaching a Dice Similarity Coefficient of 98.21%, a Jaccard index of 93.41%, a sensitivity rate of 98.50% and a specificity rate of 96.10%, confirming MGRF-HDP as a practical means of scaling, securing and managing latency in a distributed intelligent system. © The Author(s) 2026.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2728.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
