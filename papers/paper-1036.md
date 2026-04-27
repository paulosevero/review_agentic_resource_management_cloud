---
id: "paper-1036"
title: "POSTER: Adaptive Load Balancing with Flow Block for LLM"
authors: ["Li, Xingyi", "Zhang, Yiran", "Zhang, Hu", "Wang, Shangguang"]
year: 2024
venue: "SIGCOMM Posters and Demos 2024 - Proceedings of the 2024 SIGCOMM Poster and Demo Sessions, Part of SIGCOMM 2024"
venue_type: "conference"
doi: "10.1145/3672202.3673747"
url: "https://www.scopus.com/pages/publications/85202451693?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "69--71"
keywords: ["collective communication", "data center network", "load balancing"]
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

# paper-1036 — POSTER: Adaptive Load Balancing with Flow Block for LLM

## Metadata

- **Authors:** Li, Xingyi and Zhang, Yiran and Zhang, Hu and Wang, Shangguang
- **Year:** 2024
- **Venue:** SIGCOMM Posters and Demos 2024 - Proceedings of the 2024 SIGCOMM Poster and Demo Sessions, Part of SIGCOMM 2024
- **DOI:** 10.1145/3672202.3673747
- **URL:** https://www.scopus.com/pages/publications/85202451693?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 69--71
- **Language:** English
- **Keywords:** collective communication; data center network; load balancing

### Abstract

We design ABLB (Adaptive Block Load Balancing), a switch-based adaptive routing load balancing mechanism based on the granularity of the flow block and aware of PFC pauses in RDMA networks. We evaluate ABLB with the NS-3 simulator under the collective communication traffic of LLMs. The simulation results show that ABLB is superior to previous switch-based load balancing schemes. For example, ABLB achieves up to 51.50% lower 99th FCT slowdown than LetFLow.  © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** POSTER: Adaptive Load Balancing with Flow Block for LLM

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** POSTER: Adaptive Load Balancing with Flow Block for LLM
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** POSTER: Adaptive Load Balancing with Flow Block for LLM
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
