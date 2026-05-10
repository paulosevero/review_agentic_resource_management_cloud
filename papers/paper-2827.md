---
id: paper-2827
title: 'iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation'
authors:
- Wang, Puwei
- Liu, Ruiheng
- Huang, Keman
- Du, Xiaoyong
venue: IEEE Transactions on Software Engineering
venue_type: journal
year: 2026
doi: 10.1109/TSE.2026.3656819
url: https://www.scopus.com/pages/publications/105028438290?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- GraphQL+
- Inter-Service Data Communication
- LLM-based Multi-Agent System
- Unified Computation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2827 — iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In data-intensive microservice-based systems, frequent and large-scale inter-service communication poses a critical performance bottleneck, degrading throughput and escalating latency. Existing solutions exhibit notable limitations: microservice merging sacrifices loose coupling and system evolvability; resource-aware scheduling enhances communication efficiency but fails to reduce data volume; dynamic deployment reduces network distances while introducing compute-resource contention; and unnecessary data transfer elimination remains ineffective under massive data loads. Hence, to overcome these challenges, we propose iRUC, an approach for inter-service data communication Reduction via Unified Computation. In particular, we first design GraphQL+, an executable declarative language that extends GraphQL with service-interaction semantics to achieve unified, cross-language modeling of data processing and transmission across microservices. Second, we develop an LLM-based multi-agent system leveraging Claude 4.5 Sonnet and Gemini 2.5 Pro to automatically parse microservice code and synthesize corresponding GraphQL+ models. Third, we implement the unified execution engine for GraphQL+ models, including the database gateway that preserves microservice database autonomy while enabling cross-database queries. This design enables iRUC to perform the unified modeling and execution of data processing and transmission across microservices, thereby significantly reducing inter-service data transfer while maintaining microservice independence. Experimental evaluation on nine GitHub open-source microservice projects deployed on Huawei Cloud demonstrates iRUC’s effectiveness: compared with the unnecessary transfer elimination, dynamic deployment, and serverless computing approaches, iRUC improves throughput by 5.57×, 1.52×, and 1.87×, respectively, while reducing latency to 7.7%, 40.7%, and 37.4% of those approaches. These results show that iRUC achieves significant performance improvements in large-scale data processing scenarios. © 1976-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2827.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
