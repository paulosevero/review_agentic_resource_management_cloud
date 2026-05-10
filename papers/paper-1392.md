---
id: paper-1392
title: Energy-efficient edge deployment of generative AI models using federated learning
authors:
- Alzu’bi, Shadi
- Kanan, Tarek
- Elbes, Mohammed
- Kanaan, Ghassan
- Trrad, Issam
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-025-05263-7
url: https://www.scopus.com/pages/publications/105003795803?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Decentralized Data Processing
- Distributed Machine Learning
- Edge Computing
- Energy-Efficient Computing
- Federated Learning
- Generative AI
- Resource Management
- Scalability in AI Deployment
- Sustainable IoT
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

# paper-1392 — Energy-efficient edge deployment of generative AI models using federated learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid expansion of Internet of Things (IoT) applications has underscored the critical role of edge computing in enhancing real-time data processing and responsiveness. Although deploying advanced generative AI models such as GANs and VAEs at the edge holds immense potential, the inherent constraints in computational power, memory, and energy resources pose significant challenges. This work introduces a novel framework that integrates distributed machine learning techniques, including federated learning (FL), to optimize the deployment of generative AI models in resource-constrained edge environments. Importantly, FL is utilized here not for data privacy, but for its ability to improve efficiency and scalability by minimizing data transfers and leveraging decentralized data processing. The proposed framework incorporates strategies for power-aware orchestration, dynamic resource allocation, thermal management, and robust failure recovery. Case studies across various domains, such as healthcare, agriculture, and intelligent transportation systems, demonstrate the practical advantages of this approach, including energy savings and improved model performance. This work contributes to the advancement of sustainable AI-driven edge computing, highlighting the scalability and adaptability of our framework in diverse IoT settings. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1392.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
