---
id: paper-1692
title: Resource Management and Security Challenges for Deploying and Adapting Large Language Models in Fog Computing
authors:
- Jebli, Achref
- Fourati, Rahma
- Drira, Fadoua
venue: 2025 IEEE 9th International Forum on Research and Technologies for Society and Industry, RTSI 2025 - Conference Proceedings
venue_type: conference
year: 2025
doi: 10.1109/RTSI64020.2025.11212497
url: https://www.scopus.com/pages/publications/105022295491?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 174--179
keywords:
- deep learning
- distributed computing
- Fog computing
- IoT security
- real-time systems
- resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-1692 — Resource Management and Security Challenges for Deploying and Adapting Large Language Models in Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing is an emerging distributed paradigm that extends cloud services to the network edge, enabling low-latency, context-aware processing for Internet of Things (IoT) applications. By decentralizing computation and storage to fog nodes near end devices, fog architectures significantly enhance real-time responsiveness compared to centralized clouds. As large language models (LLMs) gain prominence in AI-driven services, their deployment in fog environments introduces critical challenges due to their intensive computational and memory requirements. This paper provides a comprehensive analysis of resource management and security challenges associated with deploying and adapting LLMs in fog computing. We review state-of-the-art techniques in task scheduling, load balancing, and virtualization, and examine how these are impacted by the unique heterogeneity and resource constraints of fog infrastructures. Particular attention is given to model partitioning strategies, communication-computation tradeoffs, and adaptive deployment across diverse fog nodes. In addition, we explore key security risks posed by distributed LLM deployment, including data leakage, model theft, gradient inversion, and denial-of-service attacks. We evaluate emerging countermeasures such as differential privacy, homomorphic encryption, encrypted inference, and robust training techniques, assessing their suitability for fog-based learning frameworks. Finally, we highlight open research directions, including dynamic model partitioning, energy-efficient inference, security certification protocols, and the development of standardized benchmarks for evaluating LLM performance and privacy in fog environments. Our findings aim to support researchers and practitioners in addressing the trade-offs between efficiency, scalability, and security in deploying large-scale AI models at the network edge. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1692.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
