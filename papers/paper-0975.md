---
id: paper-0975
title: Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native
authors:
- Joshi, Suyash
- Hasan, Basit
- Brindha, R.
venue: Proceedings of the 3rd International Conference on Applied Artificial Intelligence and Computing, ICAAIC 2024
venue_type: conference
year: 2024
doi: 10.1109/ICAAIC60222.2024.10575306
url: https://www.scopus.com/pages/publications/85198731134?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 578--582
keywords:
- API
- Kubernetes
- Operator
- Orchestration
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

# paper-0975 — Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The widespread use of Large Language Models (LLMs) in natural language processing tasks has become increasingly common. LLMs have the ability to produce content that is both coherent and contextually relevant. Notwithstanding, there exist notable obstacles in effectively implementing and overseeing these models within operational settings, especially in infrastructures that are cloud native. A cloud-native system for optimizing and delivering live learning modules on Kubernetes clusters is presented in this study. There are many obstacles in the way of effectively deploying inference services on the cloud. After obtaining a trained model, cloud operators need to specify hardware configurations for every model-serving container. These settings cover a wide range of topics, including CPU core counts, GPU specs, GPU RAM, possible setups for GPU sharing, and runtime parameters like batch size. When combined, these factors provide a vast and intricate configuration space. By utilizing the declarative resource management that Kubernetes provides, the suggested approach leverages declarative resource management capabilities of Kubernetes and allows users to easily train and serve LLMs on those clusters. Kubernetes clusters from a variety of cloud providers, including KIND (provisioned on bare metal), Google Kubernetes Engine (GKE), and Amazon Elastic Kubernetes Service (EKS), are specifically supported by the framework. This Kubernetes custom resource enables users to maximize the performance and cost-effectiveness of LLM deployments by utilizing Kubernetes' scalability, flexibility, and resource allocation properties and allows to maintain the stable state with use of operators and watch pattern. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0975.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
