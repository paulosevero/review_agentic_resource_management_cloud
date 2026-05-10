---
id: paper-1476
title: Mobile Edge Collaborative Caching Algorithm Based on Asynchronous Federation Popularity Prediction and Soft Multi-Agent Actor-Critic
authors:
- Chen, Junyan
- Chen, Jiahao
- Jiang, Ming
- Jin, Lei
- Yao, Rui
- Huang, Xuefeng
venue: 2025 IEEE 20th Conference on Industrial Electronics and Applications, ICIEA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICIEA65512.2025.11148452
url: https://www.scopus.com/pages/publications/105018126044?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Internet of Vehicles
- Mobile edge collaborative caching
- Multi-agent
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1476 — Mobile Edge Collaborative Caching Algorithm Based on Asynchronous Federation Popularity Prediction and Soft Multi-Agent Actor-Critic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge collaborative caching is a crucial technology for optimizing the performance of Internet of Vehicles (IoVs) network services. However, its application in IoVs environments faces several challenges, including limited resources, privacy concerns, and the need for algorithms adaptable to heterogeneous environments. Addressing the limitations of vehicle caching and computing power in IoVs, which prevent comprehensive content caching, we propose a mobile edge collaborative caching algorithm leveraging asynchronous federated popularity prediction and a soft multi-agent actor-critic method (AFPP-SMAAC). Firstly, we introduce an asynchronous federated learning algorithm to enhance the accuracy of the global model. Secondly, we develop a popularity-based content prediction algorithm, utilizing the global model to proactively identify the most popular content for vehicle edge calculations and cache it in a strategically selected Road Side Unit (RSU). And finally, we design a soft multi-agent actor-critic algorithm to optimize collaborative caching decisions, aiming to minimize content transmission delay and maximize cache hit rates. Simulation results demonstrate that the AFPP-SMAAC algorithm outperforms existing baseline caching algorithms. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1476.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
