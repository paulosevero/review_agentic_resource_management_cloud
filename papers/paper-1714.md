---
id: paper-1714
title: Federated Data Modeling for LLM Deployment in Secure Cloud-Native Architectures
authors:
- Jonnalagadda, Anil Kumar
- Madupati, Bhanuprakash
- Vegesna, Rohith Varma
- Vududala, Santosh Kumar
venue: 2025 International Conference on Computing Technologies and Data Communication, ICCTDC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCTDC64446.2025.11158782
url: https://www.scopus.com/pages/publications/105019051830?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud-Native Architectures
- Confidential Computing
- Data Privacy
- Federated Learning
- Large Language Models (LLMs)
- Secure AI Deployment
- Zero Trust
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

# paper-1714 — Federated Data Modeling for LLM Deployment in Secure Cloud-Native Architectures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> LLMs have brought new, amazing abilities for understanding language, generating it and making decisions. Yet, there are serious concerns about data privacy, the ability to scale LLMs and how different components of a cloud-native system interact. The paper outlines a new Federated Data Modelling (FDM) framework specifically for making use of LLMs in secure and efficient distributed cloud settings. The framework achieves decentralized training, prevents data being leaked and meets the requirements of data residency laws by using federated learning and dynamic schema harmonization with container orchestration. Moreover, the proposed FDM technique relies on zero-trust security, confidential computing and Kubernetes-native operations to provide isolation, watching and traceability among the various tenants. On typical benchmark datasets, the approach shown here performs better in terms of privacy, how quickly the model learns and how quickly it may be used in practice compared to centralized training. By using this study, AI service providers can ensure their LLM service is trustworthy and safe for IAP use in healthcare, finance and government. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1714.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
