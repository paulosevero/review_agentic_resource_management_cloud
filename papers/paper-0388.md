---
id: paper-0388
title: Anomaly Detection in Industrial IoT Applications Using Deep Learning Approach
authors:
- Bulla, Chetan
- Birje, Mahantesh N.
venue: Learning and Analytics in Intelligent Systems
venue_type: book-chapter
year: 2022
doi: 10.1007/978-3-030-85383-9_9
url: https://www.scopus.com/pages/publications/85135848628?origin=resultslist
publisher: Springer Nature
pages: 127--147
keywords:
- And fog computing
- Anomaly detection
- Cloud computing
- GRU
- Hyperparameter optimization
- Multi-step prediction
- Prediction
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0388 — Anomaly Detection in Industrial IoT Applications Using Deep Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet of Things (IoT) becomes popular in last two decade as it provides many advantages such as flexibility, autonomous, cost effective and productivity. Many industries adopted IoT to improve the efficiency, security and predictive maintenance. To improve the quality of service (QoS), it is essential to identify various types of anomalies in productive maintenance. An anomaly is a value, a status of resources or outcome that deviates from expected or normal values and it affects QoS of production. In this paper, a multi-agent based anomaly detection scheme is introduced to improve the QoS. The fog computing infrastructure is used to reduce the latency of communication. Multiple agents are deployed in fog node to perform the various operations of detecting anomalies. The proposed anomaly detection scheme uses a multi-step prediction technique and applies an anomaly detection algorithm to detect anomalies. The Gated Recurrent Unit (GRU) model is used for Multi-step time series prediction and a bio-inspired Artificial Bee Colony algorithm is used for tuning the GRU model hyperparameters to improve the accuracy. The proposed model detects various types of anomalies in the fog computing environment. The Google Colab using TensorFlow library Keras is used for experimental evaluation. The proposed model increases accuracy over existing approaches, according to the experiment evaluation. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0388.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
