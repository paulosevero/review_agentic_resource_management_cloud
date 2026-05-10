---
id: paper-0347
title: Adaptive Resource Optimized Edge Federated Learning in Real-Time Image Sensing Classifications
authors:
- Tam, Prohim
- Math, Sa
- Nam, Chaebeen
- Kim, Seokhoon
venue: IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing
venue_type: journal
year: 2021
doi: 10.1109/JSTARS.2021.3120724
url: https://www.scopus.com/pages/publications/85118254838?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10929--10940
keywords:
- Convolutional neural networks (CNN)
- deep q-learning (DQL)
- federated learning (FL)
- quality of service (QoS)
- real-time image classifications
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0347 — Adaptive Resource Optimized Edge Federated Learning in Real-Time Image Sensing Classifications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the exponential growth of the Internet of things (IoT) in remote sensing image applications, network resource orchestration and data privacy are significant aspects to handle in bigdata cellular networks. The image data sharing procedure toward central cloud servers in order to perform real-time classifications has leaked client personalization and heavily burdened the communication networks. Thus, the deployment of IoT image sensors in privacy-constrained sectors requires an optimized federated learning (FL) scheme to efficiently consider both aspects of securing data privacy and maximizing the model accuracy with sufficient communication and computation resources. In this article, an adaptive model communication scheme with virtual resource optimization for edge FL is proposed by converging a deep q-learning algorithm to enforce a self-learning agent interacting with network functions virtualization orchestrator and software-defined networking based architecture. The agent targets to optimize the resource control policy of virtual multi-access edge computing entities in virtualized infrastructure manager. The proposed scheme trains the learning model and weighs the optimal actions for particular network states by using an epsilon-greedy strategy. In the exploitation phase, the scheme considers multiple spatial-resolution sensing conditions and allocates computation offloading resources for global multiconvolutional neural networks model aggregation based on the congestion states. In the simulation results, the quality of service and global collaborative model performance metrics were evaluated in terms of delay, packet drop ratios, packet delivery ratios, loss values, and overall accuracy.  © 2008-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0347.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
