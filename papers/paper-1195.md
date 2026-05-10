---
id: paper-1195
title: 'DeepMRA: An Efficient Microservices Resource Allocation Framework with Deep Reinforcement Learning in the Cloud'
authors:
- Si, Qi
- Shi, Jilin
- Li, Weiyi
- Lu, Xuesong
- Pu, Peng
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2024
doi: 10.1007/978-981-97-5581-3_37
url: https://www.scopus.com/pages/publications/85201087067?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 455--466
keywords:
- Cloud Computing
- Deep Reinforcement Learning
- Microservice
- Resource Allocation
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
    my_justification: RL
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

# paper-1195 — DeepMRA: An Efficient Microservices Resource Allocation Framework with Deep Reinforcement Learning in the Cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of cloud computing has precipitated a paradigm shift in application service deployment, transitioning predominantly from monolithic to microservices architectures. This shift to microservices brings new, complex challenges in managing cloud resources. Traditional cloud resource allocation methods struggle with microservices’ unique challenges, like complex inter-service dependencies and the need to balance Quality of Service (QoS) with cost efficiency. Recognizing these challenges in cloud resource management, our study proposes an innovative approach to dynamically allocate resources for cloud microservices with Deep Reinforcement Learning (DRL). Specifically, we introduce DeepMRA, an efficient microservices resource allocation framework with Deep Reinforcement Learning in the Cloud, with multiple agents navigating the complexities arising from varying workloads. We propose a performance predictor to forecast application performance, guiding the training of agents in DRL. Due to the shortcomings of traditional performance data collection methods in the context of microservices, we developed the Parallel and Asynchronous Uncertainty-Directed Sampling (PAUDS) algorithm. This algorithm is specifically designed to optimize data collection processes, ensuring a robust dataset for building a reliable performance predictor. Extensive experiments conducted with microservice-based applications indicate that the proposed method reduces resource consumption while upholding QoS requirements under varying workloads. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2024.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1195.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
