---
id: paper-0272
title: Coded stochastic admm for decentralized consensus optimization with edge computing
authors:
- Chen, Hao
- Ye, Yu
- Xiao, Ming
- Skoglund, Mikael
- Poor, H. Vincent
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2021
doi: 10.1109/JIOT.2021.3058116
url: https://www.scopus.com/pages/publications/85101455750?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5360--5373
keywords:
- Alternating direction method of multipliers (ADMMs)
- coded edge computing
- consensus optimization
- decentralized learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0272 — Coded stochastic admm for decentralized consensus optimization with edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Big data, including applications with high security requirements, are often collected and stored on multiple heterogeneous devices, such as mobile devices, drones, and vehicles. Due to the limitations of communication costs and security requirements, it is of paramount importance to analyze information in a decentralized manner instead of aggregating data to a fusion center. To train large-scale machine learning models, edge/fog computing is often leveraged as an alternative to centralized learning. We consider the problem of learning model parameters in a multiagent system with data locally processed via distributed edge nodes. A class of minibatch stochastic alternating direction method of multipliers (ADMMs) algorithms is explored to develop the distributed learning model. To address two main critical challenges in distributed learning systems, i.e., communication bottleneck and straggler nodes (nodes with slow responses), error-control-coding-based stochastic incremental ADMM is investigated. Given an appropriate minibatch size, we show that the minibatch stochastic ADMM-based method converges in a rate of O(1/\sqrt {k}) , where k denotes the number of iterations. Through numerical experiments, it is revealed that the proposed algorithm is communication efficient, rapidly responding, and robust in the presence of straggler nodes compared with state-of-the-art algorithms. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0272.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
