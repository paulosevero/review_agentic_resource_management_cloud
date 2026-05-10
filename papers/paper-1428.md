---
id: paper-1428
title: Swarm Intelligence for AI/ML Workload in Distributed Cloud Infrastructure
authors:
- Bhat, Kiran
venue: Proceedings of 8th International Conference on Computing Methodologies and Communication, ICCMC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCMC65190.2025.11139928
url: https://www.scopus.com/pages/publications/105016901953?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AI inference
- ant colony optimization
- cloud computing
- load balancing
- swarm intelligence
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1428 — Swarm Intelligence for AI/ML Workload in Distributed Cloud Infrastructure

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a novel swarm intelligence approach for load balancing AI/ML inference workloads in distributed cloud environments. The proliferation of AI/ML applications across industries has created an unprecedented demand for efficient model serving infrastructure in cloud environments. As organizations deploy diverse models ranging from computer vision to large language models, the challenge of optimally distributing inference workloads across heterogeneous GPU resources becomes critical. Traditional load balancing approaches fail to adapt to the dynamic nature of AI workloads, leading to suboptimal resource utilization and increased latency. This paper presents a novel swarm intelligence approach using Ant Colony Optimization (ACO) for intelligent load balancing of AI/ML inference requests. Unlike traditional web requests, AI inference workloads exhibit unique patterns: variable execution times, memory-intensive resource requirements, hardware-specific dependencies, and dynamic batch processing needs. These characteristics create heterogeneous demands that traditional load balancers cannot optimize for effectively, necessitating specialized approaches for efficient resource allocation and scheduling. Inspired by the foraging behavior of ants, our system employs digital agents that deposit pheromone trails to mark efficient paths to available GPU resources, enabling self-organizing and adaptive workload distribution. Experimental results demonstrate that our approach achieves X% reduction in average inference latency and Y © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1428.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
