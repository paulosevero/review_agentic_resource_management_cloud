---
id: paper-2878
title: Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing
authors:
- Yang, Lei
- Gan, Shuying
- Wang, Xijun
- Liu, Jing
- Chen, Xiang
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-14681-6_4
url: https://www.scopus.com/pages/publications/105030651417?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 41--52
keywords:
- edge computing
- large language models
- reinforcement learning
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

# paper-2878 — Adaptive Batch Processing and Resource Allocation for LLM Inference in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) have revolutionized artificial intelligence, showcasing unprecedented capabilities across a wide range of tasks and significantly enhancing edge computing. However, deploying LLMs on edge devices presents challenges due to the distributed nature of users across edge nodes and the complexity of request types. To address these challenges, this paper first establishes an LLM inference model within an edge computing system and formulates an optimization problem aimed at maximizing the number of requests processed per unit time while satisfying user demands. To solve this problem, we model the system as a Semi-Markov Decision Process (SMDP) and employ reinforcement learning methods to propose the Dynamic Inference Separable Proximal Policy Optimization (DISPPO) algorithm. This algorithm dynamically adjusts the order of the prefill and decode stages. We evaluate the performance of DISPPO in edge-based LLM inference by comparing it with traditional inference methods. Simulation results demonstrate that DISPPO outperforms traditional methods in LLM inference scenarios. Additionally, we explore the algorithm’s performance across different batch sizes. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2878.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
