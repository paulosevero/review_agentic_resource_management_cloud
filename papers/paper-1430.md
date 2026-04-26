---
id: "paper-1430"
title: "In-Context Example Ordering for LLM-Based API Sequence Generation"
authors: ["Bhope, Rahul Atul", "Venkateswaran, Praveen", "Jayaram, K.R.", "Isahagian, Vatche", "Muthusamy, Vinod", "Venkatasubramanian, Nalini"]
year: 2025
venue: "Middleware Demos Posters and Doctoral Symposium 2025 - Proceedings of the 2025 International Middleware Conference Demos Posters and Doctoral Symposium Track, Part of Middleware 2025"
venue_type: "conference"
doi: "10.1145/3721464.3777432"
url: "https://www.scopus.com/pages/publications/105027159054?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "7--9"
keywords: ["distributed systems", "edge computing", "example ordering", "in-context learning", "large language models", "natural language to API", "prompt engineering"]
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

# paper-1430 — In-Context Example Ordering for LLM-Based API Sequence Generation

## Metadata

- **Authors:** Bhope, Rahul Atul and Venkateswaran, Praveen and Jayaram, K.R. and Isahagian, Vatche and Muthusamy, Vinod and Venkatasubramanian, Nalini
- **Year:** 2025
- **Venue:** Middleware Demos Posters and Doctoral Symposium 2025 - Proceedings of the 2025 International Middleware Conference Demos Posters and Doctoral Symposium Track, Part of Middleware 2025
- **DOI:** 10.1145/3721464.3777432
- **URL:** https://www.scopus.com/pages/publications/105027159054?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 7--9
- **Language:** English
- **Keywords:** distributed systems; edge computing; example ordering; in-context learning; large language models; natural language to API; prompt engineering

### Abstract

We demonstrate OptiSeq [1], an edge-cloud middleware system that converts natural language queries into executable API sequences with high reliability in distributed environments. A central challenge in such systems is that large language models (LLMs) can generate incorrect API sequences, causing costly retries that consume edge bandwidth and add cloud latency. Our demonstration shows how OptiSeq, a lightweight inference-time example-ordering optimization engine, reduces these failures by intelligently arranging in-context examples before prompting the LLM. In our distributed architecture, (1) natural language queries originate at the edge, (2) relevant examples are retrieved from an edge-hosted vector store, (3) OptiSeq runs within the middleware pipeline to optimize prompt construction, (4) a cloud-hosted LLM generates API sequences, and (5) a distributed API execution layer carries out the calls. Through live demonstrations on real-world API sequencing tasks, we show that OptiSeq-guided prompting reduces retry attempts by 35-45 % while maintaining high accuracy. This work presents the first demonstration of ordering-aware middleware for natural-language-to-API sequence generation deployed across edge-cloud systems.  © 2025 Copyright held by the owner/author(s).

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
