---
id: paper-1960
title: Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures
authors:
- Mohan, Jaya Preethi
- Ranganathan, Prakash
venue: Proceedings - 2025 IEEE Cloud Summit, Cloud-Summit 2025
venue_type: conference
year: 2025
doi: 10.1109/Cloud-Summit64795.2025.00027
url: https://www.scopus.com/pages/publications/105015510221?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 130--136
keywords:
- API endpoints
- containers
- deployment
- large language models
- multi-cloud
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
    my_justification: LLM as workload
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

# paper-1960 — Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a secure and scalable framework for deploying Large Language Models (LLMs) across multi-cloud platforms using containerization technologies. The framework implements a dual-container architecture comprising a data_service container for Distributed Energy Resource (DER) data processing, aggregation, and the llm_service container that orchestrates multiple LLM providers, including GPT, Claude, Gemini and Llama. Leveraging tools such as Docker, Kubernetes, FASTAPI, and multi-cloud authentication, the framework addresses the key challenges related to security, interoperability and performance in distributed environments. The data_service container processes DER data at a configurable interval and integrates GPT models for energy pattern analysis and optimization recommendations. The llm_service container provides multi-model AI gateway functionality with dynamic load balancing and comprehensive performance monitoring across cloud providers. Security implementation includes container security scan, API security testing, network, and runtime security. Performance results show the GPT model for the analysis achieving 14.21% CPU usage and 1302.16MB memory consumption. Google Cloud Platform provides optimal cost efficiency up to 16.4% per analysis, compared to Amazon Web Services (AWS) and Microsoft Azure. The framework validates successful multi-cloud deployment across AWS, GCP, and Azure while maintaining enterprise-grade security. ©2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1960.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
