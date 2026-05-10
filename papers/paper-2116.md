---
id: paper-2116
title: 'Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments'
authors:
- Semerikov, Serhiy O.
- Vakaliuk, Tetiana A.
- Kanevska, Olga B.
- Ostroushko, Oksana A.
- Kolhatin, Andrii O.
venue: Journal of Edge Computing
venue_type: journal
year: 2025
doi: 10.55056/jec.1000
url: https://www.scopus.com/pages/publications/105024324901?origin=resultslist
publisher: Academy of Cognitive and Natural Sciences
pages: 179--233
keywords:
- distributed inference
- edge computing
- edge intelligence
- knowledge distillation
- large language models
- model quantisation
- real-time inference
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
    my_justification: Review
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

# paper-2116 — Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing environments face unprecedented challenges in deploying large language models due to severe resource constraints, latency requirements, and privacy concerns that traditional cloud-based solutions cannot address. Current approaches struggle with the fundamental mismatch between LLMs’ computational demands-requiring gigabytes of memory and billions of operations-and edge devices’ limited capabilities, resulting in either degraded performance or infeasible deployments. This survey presents a systematic analysis of emerging techniques that enable efficient LLM deployment at the edge through four complementary strategies: model compression via quantisation and pruning that reduces memory footprint by up to 75% while maintaining accuracy, knowledge distillation frameworks achieving 4000× parameter reduction with comparable performance, edge-cloud collaborative architectures like EdgeShard delivering 50% latency reduction through intelligent workload distribution, and hardware-specific optimisations leveraging specialised accelerators. Extensive evaluation across multiple real-world testbeds demonstrates that hybrid edge-microservices architectures achieve 46% lower P99 latency and 67% higher throughput compared to monolithic approaches, while supporting 10,000 concurrent users with 100 ms latency constraints and reducing bandwidth consumption by 99.5% through selective cloud offloading. These advancements enable transformative applications in healthcare monitoring, autonomous systems, real-time IoT analytics, and personalised AI services, fundamentally reshaping how intelligence is delivered at the network edge while preserving privacy and ensuring responsiveness critical for next-generation computing paradigms.1 © Copyright for this article by its authors, published by the Academy of Cognitive and Natural Sciences.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2116.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
