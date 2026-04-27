---
id: "paper-2192"
title: "TurboBatch - Rate-Safe Asynchronous Batch Processing for Cloud LLM APIs"
authors: ["Syed, Rayan", "Robitshek, Noah"]
year: 2025
venue: "Proceedings - 2025 IEEE International Conference on Cloud Engineering, IC2E 2025"
venue_type: "conference"
doi: "10.1109/IC2E65552.2025.00014"
url: "https://www.scopus.com/pages/publications/105022161129?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "65--66"
keywords: ["cloud computing", "large language models", "llm inference", "rate limiting"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2192 — TurboBatch - Rate-Safe Asynchronous Batch Processing for Cloud LLM APIs

## Metadata

- **Authors:** Syed, Rayan and Robitshek, Noah
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE International Conference on Cloud Engineering, IC2E 2025
- **DOI:** 10.1109/IC2E65552.2025.00014
- **URL:** https://www.scopus.com/pages/publications/105022161129?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 65--66
- **Language:** English
- **Keywords:** cloud computing; large language models; llm inference; rate limiting

### Abstract

We present TURBOBATCH, an asynchronous batch processing system enabling large-scale LLM inference under strict API rate limits. Existing approaches to LLM workloads require manual tuning and operator oversight to avoid quota violations, limiting scalability and increasing cost. TurboBatch combines accurate token usage prediction with adaptive rate control to fully automate batch processing of millions of LLM requests - a previously unaddressed gap in client-side orchestration for quota-constrained LLM APIs. In production tests, the system achieves sustained high throughput, demonstrating its practical viability for real-world LLM applications beyond OpenAI APIs. © 2025 IEEE.

## 04 — Title Screening

**Title:** TurboBatch - Rate-Safe Asynchronous Batch Processing for Cloud LLM APIs

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** TurboBatch - Rate-Safe Asynchronous Batch Processing for Cloud LLM APIs
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** TurboBatch - Rate-Safe Asynchronous Batch Processing for Cloud LLM APIs
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
