---
id: paper-2289
title: 'EdgeAIGC: Model caching and resource allocation for edge artificial intelligence generated content'
authors:
- Wen, Wu
- Huang, Yibin
- Zhao, Xinxin
- Zhang, Peiying
- Liu, Kai
- Shi, Guowei
venue: Digital Communications and Networks
venue_type: journal
year: 2025
doi: 10.1016/j.dcan.2025.07.003
url: https://www.scopus.com/pages/publications/105025355851?origin=resultslist
publisher: KeAi Communications Co.
pages: 1941--1950
keywords:
- Edge intelligence
- Edge model caching
- Generative AI
- Resource allocation
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2289 — EdgeAIGC: Model caching and resource allocation for edge artificial intelligence generated content

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of generative artificial intelligence technology, the traditional cloud-based centralized model training and inference face significant limitations due to high transmission latency and costs, which restrict user-side in-situ Artificial Intelligence Generated Content (AIGC) service requests. To this end, we propose the Edge Artificial Intelligence Generated Content (EdgeAIGC) framework, which can effectively address the challenges of cloud computing by implementing in-situ processing of services close to the data source through edge computing. However, AIGC models usually have a large parameter scale and complex computing requirements, which poses a huge challenge to the storage and computing resources of edge devices. This paper focuses on the edge intelligence model caching and resource allocation problems in the EdgeAIGC framework, aiming to improve the cache hit rate and resource utilization of edge devices for models by optimizing the model caching strategy and resource allocation scheme, and realize in-situ AIGC service processing. With the optimization objectives of minimizing service request response time and execution cost in resource-constrained environments, we employ the Twin Delayed Deep Deterministic Policy Gradient algorithm for optimization. Experimental results show that, compared with other methods, our model caching and resource allocation strategies can effectively improve the cache hit rate by at least 41.06% and reduce the response cost as well. © 2025 Chongqing University of Posts and Telecommunications.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2289.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
