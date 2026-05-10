---
id: paper-2234
title: Cost-Effective, Low Latency Vector Search with Azure Cosmos DB
authors:
- Upreti, Nitish
- Simhadri, Harsha Vardhan
- Sundar, Hari Sudan
- Sundaram, Krishnan
- Boshra, Samer
- Perumalswamy, Balachandar
- Atri, Shivam
- Chisholm, Martin
- Singh, Revti Raman
- Yang, Greg
- Hass, Tamara
- Dudhey, Nitesh
- Pattipaka, Subramanyam
- Hildebrand, Mark
- Manohar, Magdalen
- Moffitt, Jack
- Xu, Haiyang
- Datha, Naren
- Gupta, Suryansh
- Krishnaswamy, Ravishankar
- Gupta, Prashant
- Sahu, Abhishek
- Varada, Hemeswari
- Barthwal, Sudhanshu
- Mor, Ritika
- Codella, James
- Cooper, Shaun
- Pilch, Kevin
- Moreno, Simon
- Kataria, Aayush
- Kulkarni, Santosh
- Deshpande, Neil
- Sagare, Amar
- Billa, Dinesh
- Fu, Zishan
- Vishal, Vipul
venue: Proceedings of the VLDB Endowment
venue_type: conference
year: 2025
doi: 10.14778/3750601.3750635
url: https://www.scopus.com/pages/publications/105016646248?origin=resultslist
publisher: VLDB Endowment
pages: 5166--5183
keywords:
- Automatic indexing
- Distributed database systems
- Query processing
- Search engines
- Semantic Web
- Semantics
- Vectors
- Cost effective
- High costs
- Low latency
- Operational database
- Optimisations
- Performance
- Search costs
- Search quality
- Semantic search
- Vector index
- Cost effectiveness
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2234 — Cost-Effective, Low Latency Vector Search with Azure Cosmos DB

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vector indexing enables semantic search over diverse corpora and has become an important interface to databases for both users and AI agents. Efficient vector search requires deep optimizations in database systems. This has motivated a new class of specialized vector databases that optimize for vector search quality and cost. Instead, we argue that a scalable, high-performance, and cost-efficient vector search system can be built inside a cloud-native operational database like Azure Cosmos DB while leveraging the benefits of a distributed database such as high availability, durability, and scale. We do this by deeply integrating DiskANN, a state-of-the-art vector indexing library, inside Azure Cosmos DB NoSQL. This system uses a single vector index per partition stored in existing index trees, and kept in sync with underlying data. It supports <20ms query latency over an index spanning 10 million vectors, has stable recall over updates, and offers approximately 43× and 12× lower query cost compared to Pinecone and Zilliz serverless enterprise products. It also scales out to billions of vectors via automatic partitioning. This convergent design presents a point in favor of integrating vector indices into operational databases in the context of recent debates on specialized vector databases, and offers a template for vector indexing in other databases. © 2025, VLDB Endowment. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2234.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
