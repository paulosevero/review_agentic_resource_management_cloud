---
id: paper-1042
title: Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks
authors:
- Liang, Yuxin
- Yang, Peng
- He, Yuanyuan
- Lyu, Feng
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901571
url: https://www.scopus.com/pages/publications/105000832164?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2647--2652
keywords:
- Mobile edge computing
- Backhaul traffics
- Content creation
- Content production
- Content services
- Edge modeling
- EDGE Networks
- Edge server
- Resource-efficient
- Service delays
- Traffic loads
- Generative adversarial networks
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

# paper-1042 — Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The surging development of Artificial Intelligence-Generated Content (AIGC) marks a transformative era of the content creation and production. Edge servers promise attractive benefits, e.g., reduced service delay and backhaul traffic load, for hosting AIGC services compared to cloud-based solutions. However, the scarcity of available resources on the edge pose significant challenges in deploying generative AI models. In this paper, by characterizing the resource and delay demands of typical generative AI models, we find that the consumption of storage and GPU memory, as well as the model switching delay represented by I/O delay during the preloading phase, are significant and vary across models. These multidimensional coupling factors render it difficult to make efficient edge model deployment decisions. Hence, we present a collaborative edge-cloud framework aiming to properly manage generative AI model deployment on the edge. Specifically, we formulate edge model deployment problem considering heterogeneous features of models as an optimization problem, and propose a model-level decision selection algorithm to solve it. It enables pooled resource sharing and optimizes the trade-off between resource consumption and delay in edge generative AI model deployment. Simulation results validate the efficacy of the proposed algorithm compared with baselines, demonstrating its potential to reduce overall costs by providing feature-aware model deployment decisions. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1042.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
