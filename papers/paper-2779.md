---
id: "paper-2779"
title: "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
authors: ["Sliwko, Leszek", "Mizeria-Pietraszko, Jolanta"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3665989"
url: "https://www.scopus.com/pages/publications/105030579766?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "28054--28074"
keywords: ["Artificial intelligence", "Kubernetes", "load balancing", "semantic parsing", "soft-affinity", "task assignment"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-2779 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing

## Metadata

- **Authors:** Sliwko, Leszek and Mizeria-Pietraszko, Jolanta
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3665989
- **URL:** https://www.scopus.com/pages/publications/105030579766?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 28054--28074
- **Language:** English
- **Keywords:** Artificial intelligence; Kubernetes; load balancing; semantic parsing; soft-affinity; task assignment

### Abstract

Cluster workload allocation often requires complex configurations, creating a usability gap. This paper introduces a semantic, intent-driven scheduling paradigm for cluster systems using Natural Language Processing. The system employs a Large Language Model (LLM) integrated via a Kubernetes scheduler extender to interpret natural language allocation hint annotations for soft affinity preferences. A prototype featuring a cluster state cache and an intent analyzer (using AWS Bedrock) was developed. Empirical evaluation demonstrated high LLM parsing accuracy (>95% Subset Accuracy on an evaluation ground-truth dataset) for top-tier models like Amazon Nova Pro/Premier and Mistral Pixtral Large, significantly outperforming a baseline engine. Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations, particularly excelling in complex and quantitative scenarios and handling conflicting soft preferences. The results validate using LLMs for accessible scheduling but highlight limitations like synchronous LLM latency, suggesting asynchronous processing for production readiness. This work confirms the viability of semantic soft affinity for simplifying workload orchestration and presents a proof-of-concept design. © 2013 IEEE.

## 04 — Title Screening

**Title:** Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing
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
