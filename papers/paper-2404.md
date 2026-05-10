---
id: paper-2404
title: LLM-Driven Offloading Decisions for Edge Object Detection in Smart City Deployments
authors:
- Yuan, Xingyu
- Li, He
venue: Smart Cities
venue_type: journal
year: 2025
doi: 10.3390/smartcities8050169
url: https://www.scopus.com/pages/publications/105019923085?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning
- edge computing
- large language model
- object detection
- offloading
- smart city
- YOLO
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
    my_justification: Out of scope
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

# paper-2404 — LLM-Driven Offloading Decisions for Edge Object Detection in Smart City Deployments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Highlights: What are the main findings? We introduce an LLM-driven framework that auto-generates and refines DRL reward functions from natural language objectives for edge offloading in object detection. On a real-world dataset, policies trained with LLM-generated rewards achieve higher throughput and lower process latency than expert-designed rewards. DRL policies can be retargeted across objectives (e.g., latency, energy, and accuracy) using prompts only, eliminating manual reward redesign. What is the implication of the main finding? Engineering overhead is reduced while accelerating the adaptation of edge AI services when goals or conditions change. The robustness of offloading and scheduling improves under heterogeneous workloads, fluctuating bandwidths, and dynamic device capabilities. Object detection is a critical technology for smart city development. As request volumes surge, inference is increasingly offloaded from centralized clouds to user-proximal edge sites to reduce latency and backhaul traffic. However, heterogeneous workloads, fluctuating bandwidth, and dynamic device capabilities make offloading and scheduling difficult to optimize in edge environments. Deep reinforcement learning (DRL) has proved effective for this problem, but in practice, it relies on manually engineered reward functions that must be redesigned whenever service objectives change. To address this limitation, we introduce an LLM-driven framework that retargets DRL policies for edge object detection directly through natural language instructions. By leveraging understanding of the text and encoding capabilities of large language models (LLMs), our system (i) interprets the current optimization objective; (ii) generates an executable, environment-compatible reward function code; and (iii) iteratively refines the reward via closed-loop simulation feedback. In simulations for a real-world dataset, policies trained with LLM-generated rewards adapt from prompts alone and outperform counterparts trained with expert-designed rewards, while eliminating manual reward engineering. © 2025 by the authors.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2404.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
