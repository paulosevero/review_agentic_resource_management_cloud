---
id: paper-2307
title: 'Optimizing inventory management: a causal inference-driven Bayesian network with transfer learning adaptation'
authors:
- Xi, Zhu
- Guan, Wei
- Savasan, Ahmet
venue: PeerJ Computer Science
venue_type: journal
year: 2025
doi: 10.7717/peerj-cs.3262
url: https://www.scopus.com/pages/publications/105024845089?origin=resultslist
publisher: PeerJ Inc.
pages: ''
keywords:
- Adaptive and Self-Organizing Systems
- Agents and Multi-Agent Systems
- Computer Aided Design
- Data Science
- Data science
- Databases
- Edge computing
- Inventory optimization
- IoT
- Machine learning
- Supply chain management
- Transfer learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2307 — Optimizing inventory management: a causal inference-driven Bayesian network with transfer learning adaptation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Inventory management faces increasing challenges, including data limitations and demand uncertainty. To enhance inventory forecasting and optimization in supply chain management, this study proposes a Transfer-learning Bayesian Network (TBN) framework that integrates causal inference and transfer learning. Unlike traditional inventory forecasting models that rely on historical data patterns, the proposed framework introduces a causal inference-based Bayesian network to establish explicit causal relationships between sales volume, sales revenue, and inventory levels. To address data scarcity and improve generalization, a novel transfer learning mechanism is incorporated, leveraging a balanced weight coefficient method to optimize model adaptation from a source domain to a target domain. The results indicate that the proposd approach ensures effective knowledge transfer and maintains prediction accuracy with limited training data. The TBN model consistently outperforms traditional machine learning methods and other Bayesian-based models. On the self-constructed dataset, the TBN framework achieved a mean squared error (MSE) of 4.97 and a mean absolute error (MAE) of 2.78, demonstrating superior predictive accuracy. Additionally, an analysis of the balance weight coefficient further validated its role in enhancing transfer learning efficiency and model robustness, which provides a scalable and adaptable solution for intelligent inventory management in supply chain systems. © Copyright 2025 Xi et al. Distributed under Creative Commons CC-BY 4.0. http://www.creativecommons.org/licenses/by/4.0/

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2307.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
