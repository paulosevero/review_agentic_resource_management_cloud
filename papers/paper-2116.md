---
id: "paper-2116"
title: "Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments"
authors: ["Semerikov, Serhiy O.", "Vakaliuk, Tetiana A.", "Kanevska, Olga B.", "Ostroushko, Oksana A.", "Kolhatin, Andrii O."]
year: 2025
venue: "Journal of Edge Computing"
venue_type: "journal"
doi: "10.55056/jec.1000"
url: "https://www.scopus.com/pages/publications/105024324901?origin=resultslist"
publisher: "Academy of Cognitive and Natural Sciences"
pages: "179--233"
keywords: ["distributed inference", "edge computing", "edge intelligence", "knowledge distillation", "large language models", "model quantisation", "real-time inference"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "Review"

---

# paper-2116 — Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments

## Metadata

- **Authors:** Semerikov, Serhiy O. and Vakaliuk, Tetiana A. and Kanevska, Olga B. and Ostroushko, Oksana A. and Kolhatin, Andrii O.
- **Year:** 2025
- **Venue:** Journal of Edge Computing
- **DOI:** 10.55056/jec.1000
- **URL:** https://www.scopus.com/pages/publications/105024324901?origin=resultslist
- **Publisher:** Academy of Cognitive and Natural Sciences
- **Pages:** 179--233
- **Language:** English
- **Keywords:** distributed inference; edge computing; edge intelligence; knowledge distillation; large language models; model quantisation; real-time inference

### Abstract

Edge computing environments face unprecedented challenges in deploying large language models due to severe resource constraints, latency requirements, and privacy concerns that traditional cloud-based solutions cannot address. Current approaches struggle with the fundamental mismatch between LLMs’ computational demands-requiring gigabytes of memory and billions of operations-and edge devices’ limited capabilities, resulting in either degraded performance or infeasible deployments. This survey presents a systematic analysis of emerging techniques that enable efficient LLM deployment at the edge through four complementary strategies: model compression via quantisation and pruning that reduces memory footprint by up to 75% while maintaining accuracy, knowledge distillation frameworks achieving 4000× parameter reduction with comparable performance, edge-cloud collaborative architectures like EdgeShard delivering 50% latency reduction through intelligent workload distribution, and hardware-specific optimisations leveraging specialised accelerators. Extensive evaluation across multiple real-world testbeds demonstrates that hybrid edge-microservices architectures achieve 46% lower P99 latency and 67% higher throughput compared to monolithic approaches, while supporting 10,000 concurrent users with 100 ms latency constraints and reducing bandwidth consumption by 99.5% through selective cloud offloading. These advancements enable transformative applications in healthcare monitoring, autonomous systems, real-time IoT analytics, and personalised AI services, fundamentally reshaping how intelligence is delivered at the network edge while preserving privacy and ensuring responsiveness critical for next-generation computing paradigms.1 © Copyright for this article by its authors, published by the Academy of Cognitive and Natural Sciences.

## 04 — Title Screening

**Title:** Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge intelligence unleashed: a survey on deploying large language models in resource-constrained environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
