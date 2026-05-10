---
id: paper-1444
title: 'Intelligent Edge Computing and Machine Learning: A Survey of Optimization and Applications'
authors:
- Cajas Ordóñez, Sebastián A.
- Samanta, Jaydeep
- Suárez-Cetrulo, Andrés L.
- Carbajo, Ricardo Simón
venue: Future Internet
venue_type: journal
year: 2025
doi: 10.3390/fi17090417
url: https://www.scopus.com/pages/publications/105017432952?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- data drift
- edge AI
- edge machine learning
- ethical AI
- federated learning
- IoT
- knowledge distillation
- large language models
- low-rank adaptation
- MLOps
- model optimization
- multimodal fusion
- quantization
- resource-constrained devices
- system resilience
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-1444 — Intelligent Edge Computing and Machine Learning: A Survey of Optimization and Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent edge machine learning has emerged as a paradigm for deploying smart applications across resource-constrained devices in next-generation network infrastructures. This survey addresses the critical challenges of implementing machine learning models on edge devices within distributed network environments, including computational limitations, memory constraints, and energy-efficiency requirements for real-time intelligent inference. We provide comprehensive analysis of soft computing optimization strategies essential for intelligent edge deployment, systematically examining model compression techniques including pruning, quantization methods, knowledge distillation, and low-rank decomposition approaches. The survey explores intelligent MLOps frameworks tailored for network edge environments, addressing continuous model adaptation, monitoring under data drift, and federated learning for distributed intelligence while preserving privacy in next-generation networks. Our work covers practical applications across intelligent smart agriculture, energy management, healthcare, and industrial monitoring within network infrastructures, highlighting domain-specific challenges and emerging solutions. We analyze specialized hardware architectures, cloud offloading strategies, and distributed learning approaches that enable intelligent edge computing in heterogeneous network environments. The survey identifies critical research gaps in multimodal model deployment, streaming learning under concept drift, and integration of soft computing techniques with intelligent edge orchestration frameworks for network applications. These gaps directly manifest as open challenges in balancing computational efficiency with model robustness due to limited multimodal optimization techniques, developing sustainable intelligent edge AI systems arising from inadequate streaming learning adaptation, and creating adaptive network applications for dynamic environments resulting from insufficient soft computing integration. This comprehensive roadmap synthesizes current intelligent edge machine learning solutions with emerging soft computing approaches, providing researchers and practitioners with insights for developing next-generation intelligent edge computing systems that leverage machine learning capabilities in distributed network infrastructures. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1444.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
