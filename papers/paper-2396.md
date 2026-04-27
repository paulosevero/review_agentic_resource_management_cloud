---
id: "paper-2396"
title: "IC-Cache: Efficient Large Language Model Serving via In-context Caching"
authors: ["Yu, Yifan", "Gan, Yu", "Sarda, Nikhil", "Tsai, Lillian", "Shen, Jiaming", "Zhou, Yanqi", "Krishnamurthy, Arvind", "Lai, Fan", "Levy, Hank", "Culler, David"]
year: 2025
venue: "SOSP 2025 - Proceedings of the 2025 ACM SIGOPS 31st Symposium on Operating Systems Principles"
venue_type: "conference"
doi: "10.1145/3731569.3764829"
url: "https://www.scopus.com/pages/publications/105020848529?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "375--398"
keywords: ["cloud computing", "large language models (LLMs)", "LLM serving", "load balancing", "quality-efficiency tradeoff", "request routing", "semantic caching"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2396 — IC-Cache: Efficient Large Language Model Serving via In-context Caching

## Metadata

- **Authors:** Yu, Yifan and Gan, Yu and Sarda, Nikhil and Tsai, Lillian and Shen, Jiaming and Zhou, Yanqi and Krishnamurthy, Arvind and Lai, Fan and Levy, Hank and Culler, David
- **Year:** 2025
- **Venue:** SOSP 2025 - Proceedings of the 2025 ACM SIGOPS 31st Symposium on Operating Systems Principles
- **DOI:** 10.1145/3731569.3764829
- **URL:** https://www.scopus.com/pages/publications/105020848529?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 375--398
- **Language:** English
- **Keywords:** cloud computing; large language models (LLMs); LLM serving; load balancing; quality-efficiency tradeoff; request routing; semantic caching

### Abstract

Large language models (LLMs) have excelled in various applications, yet serving them at scale is challenging due to their substantial resource demands and high latency. Our real-world studies reveal that over 70% of user requests to LLMs have semantically similar counterparts, suggesting the potential for knowledge transfer among requests. However, naively caching and reusing past responses leads to a big quality drop.In this paper, we introduce IC-Cache, a caching system that enables live LLM capability augmentation to improve serving efficiency: by leveraging historical request-response pairs from larger models as in-context examples, IC-Cache empowers small LLMs to imitate and even exceed the compositional abilities (e.g., reasoning) of their larger counterparts, enabling selective offloading of requests to reduce cost and latency. Achieving this live augmentation at scale introduces intricate trade-offs between response quality, latency, and system throughput. For a new request, IC-Cache efficiently selects similar, high-utility examples to prepend them to the new request's input. At scale, it adaptively routes requests across LLMs of varying capabilities, accounting for response quality and serving loads. IC-Cache employs a cost-aware cache replay mechanism that refines example quality offline to maximize online cache utility and efficiency. Evaluations on millions of realistic requests demonstrate that IC-Cache improves LLM serving throughput by 1.4-5.9x and reduces latency by 28-71% without hurting response quality. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** IC-Cache: Efficient Large Language Model Serving via In-context Caching

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** IC-Cache: Efficient Large Language Model Serving via In-context Caching
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** IC-Cache: Efficient Large Language Model Serving via In-context Caching
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
