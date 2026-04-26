---
id: "paper-2234"
title: "Cost-Effective, Low Latency Vector Search with Azure Cosmos DB"
authors: ["Upreti, Nitish", "Simhadri, Harsha Vardhan", "Sundar, Hari Sudan", "Sundaram, Krishnan", "Boshra, Samer", "Perumalswamy, Balachandar", "Atri, Shivam", "Chisholm, Martin", "Singh, Revti Raman", "Yang, Greg", "Hass, Tamara", "Dudhey, Nitesh", "Pattipaka, Subramanyam", "Hildebrand, Mark", "Manohar, Magdalen", "Moffitt, Jack", "Xu, Haiyang", "Datha, Naren", "Gupta, Suryansh", "Krishnaswamy, Ravishankar", "Gupta, Prashant", "Sahu, Abhishek", "Varada, Hemeswari", "Barthwal, Sudhanshu", "Mor, Ritika", "Codella, James", "Cooper, Shaun", "Pilch, Kevin", "Moreno, Simon", "Kataria, Aayush", "Kulkarni, Santosh", "Deshpande, Neil", "Sagare, Amar", "Billa, Dinesh", "Fu, Zishan", "Vishal, Vipul"]
year: 2025
venue: "Proceedings of the VLDB Endowment"
venue_type: "conference"
doi: "10.14778/3750601.3750635"
url: "https://www.scopus.com/pages/publications/105016646248?origin=resultslist"
publisher: "VLDB Endowment"
pages: "5166--5183"
keywords: ["Automatic indexing", "Distributed database systems", "Query processing", "Search engines", "Semantic Web", "Semantics", "Vectors", "Cost effective", "High costs", "Low latency", "Operational database", "Optimisations", "Performance", "Search costs", "Search quality", "Semantic search", "Vector index", "Cost effectiveness"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2234 — Cost-Effective, Low Latency Vector Search with Azure Cosmos DB

## Metadata

- **Authors:** Upreti, Nitish and Simhadri, Harsha Vardhan and Sundar, Hari Sudan and Sundaram, Krishnan and Boshra, Samer and Perumalswamy, Balachandar and Atri, Shivam and Chisholm, Martin and Singh, Revti Raman and Yang, Greg and Hass, Tamara and Dudhey, Nitesh and Pattipaka, Subramanyam and Hildebrand, Mark and Manohar, Magdalen and Moffitt, Jack and Xu, Haiyang and Datha, Naren and Gupta, Suryansh and Krishnaswamy, Ravishankar and Gupta, Prashant and Sahu, Abhishek and Varada, Hemeswari and Barthwal, Sudhanshu and Mor, Ritika and Codella, James and Cooper, Shaun and Pilch, Kevin and Moreno, Simon and Kataria, Aayush and Kulkarni, Santosh and Deshpande, Neil and Sagare, Amar and Billa, Dinesh and Fu, Zishan and Vishal, Vipul
- **Year:** 2025
- **Venue:** Proceedings of the VLDB Endowment
- **DOI:** 10.14778/3750601.3750635
- **URL:** https://www.scopus.com/pages/publications/105016646248?origin=resultslist
- **Publisher:** VLDB Endowment
- **Pages:** 5166--5183
- **Language:** English
- **Keywords:** Automatic indexing; Distributed database systems; Query processing; Search engines; Semantic Web; Semantics; Vectors; Cost effective; High costs; Low latency; Operational database; Optimisations; Performance; Search costs; Search quality; Semantic search; Vector index; Cost effectiveness

### Abstract

Vector indexing enables semantic search over diverse corpora and has become an important interface to databases for both users and AI agents. Efficient vector search requires deep optimizations in database systems. This has motivated a new class of specialized vector databases that optimize for vector search quality and cost. Instead, we argue that a scalable, high-performance, and cost-efficient vector search system can be built inside a cloud-native operational database like Azure Cosmos DB while leveraging the benefits of a distributed database such as high availability, durability, and scale. We do this by deeply integrating DiskANN, a state-of-the-art vector indexing library, inside Azure Cosmos DB NoSQL. This system uses a single vector index per partition stored in existing index trees, and kept in sync with underlying data. It supports <20ms query latency over an index spanning 10 million vectors, has stable recall over updates, and offers approximately 43× and 12× lower query cost compared to Pinecone and Zilliz serverless enterprise products. It also scales out to billions of vectors via automatic partitioning. This convergent design presents a point in favor of integrating vector indices into operational databases in the context of recent debates on specialized vector databases, and offers a template for vector indexing in other databases. © 2025, VLDB Endowment. All rights reserved.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
