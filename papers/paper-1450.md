---
id: paper-1450
title: Neural Network Architectures for Enhancing Data Center Intelligence through Deep Learning
authors:
- Castillo, Antonio Cortés
venue: ISMSIT 2025 - 9th International Symposium on Multidisciplinary Studies and Innovative Technologies, Proceedings
venue_type: conference
year: 2025
doi: 10.1109/ISMSIT67332.2025.11268124
url: https://www.scopus.com/pages/publications/105031123524?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- artificial intelligence
- data centers
- deep learning
- generative artificial intelligence
- metrics
- neural networks
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

# paper-1450 — Neural Network Architectures for Enhancing Data Center Intelligence through Deep Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Artificial Intelligence (AI) is one of those new paradigms that are transforming daily work into various aspects related to network infrastructure, medicine, cybersecurity, data analysis, etc. In the context of data networks, it observing how traditional networks consisting of analog and digital copper communication media transforming into networks that integrate Artificial Intelligence components with optical fiber whose purpose is to optimize communication protocols, for example: InfiniBand (IB) that helps to manage large volumes of information better, as well as obtain better bandwidth performance, with average speeds of 800 G / 1.5 T, low latency, and a reduction in energy consumption. In this article, we begin with an analysis of traditional Fat Tree Spine-Leaf network architecture, its optimization, and the integration of Generative Artificial Intelligence (GenAI) into Data Centers. In turn, a series of metrics identifying at the Data Center level (latency, throughput, packet_loss, bandwidth, jitter, error_rate, network_utilization, uptime, average_response_time and peak_response_time) that are part of the general metric that we have called Server_links_performance and that help us through the analysis of Neural Networks (NN) to identify which of these metrics, once normalized, are the most relevant for the correct operation of the Data Centers. To train the architecture model for GenIA's data centers, in addition to using neural networks, we also use linear equations and regression analysis for predictive and residual values, respectively. Determining these metrics can help improve the performance of our network infrastructure and the services provided to our customers.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1450.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
