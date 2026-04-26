---
id: "paper-2174"
title: "EVALUATION OF THE PERFORMANCE OF LLMs DEPLOYMENTS IN SELECTED CLOUD-BASED CONTAINER SERVICES; [OCENA WYDAJNOŚCI WDROŻEŃ LLM W WYBRANYCH USŁUGACH KONTENEROWYCH OPARTYCH NA CHMURZE]"
authors: ["St\u0119gierski, Mateusz", "Szpak, Piotr", "Przy\u0142ucki, S\u0142awomir"]
year: 2025
venue: "Informatyka, Automatyka, Pomiary w Gospodarce i Ochronie Srodowiska"
venue_type: "journal"
doi: "10.35784/iapgos.8206"
url: "https://www.scopus.com/pages/publications/105026487493?origin=resultslist"
publisher: "Politechnika Lubelska"
pages: "142--150"
keywords: ["auto-scaling", "language models", "load testing", "performance comparison", "serverless containers"]
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

# paper-2174 — EVALUATION OF THE PERFORMANCE OF LLMs DEPLOYMENTS IN SELECTED CLOUD-BASED CONTAINER SERVICES; [OCENA WYDAJNOŚCI WDROŻEŃ LLM W WYBRANYCH USŁUGACH KONTENEROWYCH OPARTYCH NA CHMURZE]

## Metadata

- **Authors:** Stęgierski, Mateusz and Szpak, Piotr and Przyłucki, Sławomir
- **Year:** 2025
- **Venue:** Informatyka, Automatyka, Pomiary w Gospodarce i Ochronie Srodowiska
- **DOI:** 10.35784/iapgos.8206
- **URL:** https://www.scopus.com/pages/publications/105026487493?origin=resultslist
- **Publisher:** Politechnika Lubelska
- **Pages:** 142--150
- **Language:** English
- **Keywords:** auto-scaling; language models; load testing; performance comparison; serverless containers

### Abstract

The growing adoption of serverless container services has created challenges in selecting optimal cloud platforms for production LLM deployments, yet comparative performance evaluations remain limited. This study evaluates AWS Fargate and Azure Container Apps for LLM deployments, investigating whether architectural differences cause substantial performance variations under diverse load patterns. We conducted systematic experiments using containerized Llama 3.2:1b across multiple scenarios: baseline measurements, inference tests with varying prompt lengths, streaming API performance, and concurrent load testing with progressive scaling. Each scenario was executed on both standard and auto-scaled infrastructure with 10 runs per configuration to ensure statistical reliability. Key findings reveal distinct platform characteristics: AWS Fargate demonstrates superior baseline API response times and time-to-first-token performance, while Azure Container Apps consistently outperforms AWS in inference processing for short and medium prompts with better consistency across test runs. Streaming performance shows platform-specific trade-offs, with AWS achieving lower initial latency but Azure providing superior token generation consistency. Under concurrent loads, both platforms maintain full capacity at lower concurrency levels, but AWS exhibits exponential response time degradation at higher loads while Azure shows more linear, predictable scaling behavior. Statistical analysis confirms significant performance differences across all metrics, validating that platform architecture fundamentally impacts LLM deployment performance. These findings indicate platform selection should align with specific workload requirements: AWS Fargate for latency-critical applications with steady loads, and Azure Container Apps for inference-intensive workloads requiring robust scaling and consistency. This study offers crucial benchmarking data for businesses deploying production-grade AI services on serverless container platforms. © 2025, Politechnika Lubelska. All rights reserved.

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
