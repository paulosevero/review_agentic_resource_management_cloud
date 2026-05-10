---
id: paper-1575
title: 'GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training'
authors:
- Gan, Xinbiao
- Li, Tiejun
- Wu, Liang
- Zhang, Qiang
- Song, Lingyun
- Yang, Bo
- Liu, Jie
- Lu, Kai
venue: WWW 2025 - Proceedings of the ACM Web Conference
venue_type: conference
year: 2025
doi: 10.1145/3696410.3714741
url: https://www.scopus.com/pages/publications/105005139119?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 786--795
keywords:
- graph model
- graph processing
- Graph500
- message aggregation
- supercomputers
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1575 — GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient processing of large-scale graphs with billions to trillions of edges is essential for training graph-based large language models (LLMs) in web-scale systems. The increasing complexity and size of these models create significant communication challenges due to the extensive message exchanges required across distributed nodes. Current graph engines struggle to effectively scale across hundreds of computing nodes because they often overlook variations in communication costs within the interconnection hierarchy. This paper presents GraphCom, a communication-efficient message graph engine for graph processing on supercomputers. Our key idea is to leverage the network topology information to perform communication hierarchy-aware message aggregation, where messages are (i) gathered to the responsible nodes (referred to as monitors) in the source domains, (ii) transferred between monitors, and (iii) scattered to the target nodes in the target domains. GraphCom’s aggregation is more aggressive in that each source domain (instead of the source node). We have implemented GraphCom on top of MPI. We demonstrate GraphCom’s effectiveness with synthetic benchmarks and real-world graphs, utilizing up to 79,024 nodes and over 1.2 million processor cores, demonstrating that GraphCom surpasses leading graph-parallel systems and state-of-the-art counterparts in both throughput and scalability. Moreover, we have deployed GraphCom on a production supercomputer, where it consistently outperforms the top solutions on the Graph500 list. These results highlight the potential GraphCom has to significantly improve the efficiency of distributed large-scale graph-based LLM training by optimizing communication between distributed systems, making it an invaluable graph engine for distributed training tasks on web-scale graphs. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1575.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
