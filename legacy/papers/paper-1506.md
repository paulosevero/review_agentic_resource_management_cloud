---
id: "paper-1506"
title: "Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs"
authors: ["Darzi, Erfan", "Balija, Sree Bhargavi", "Demir, Buse"]
year: 2025
venue: "WoSC11 2025 - Proceedings of the 11th International Workshop on Serverless Computing, Part of Middleware Conference"
venue_type: "conference"
doi: "10.1145/3774899.3775014"
url: "https://www.scopus.com/pages/publications/105029344902?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "20--25"
keywords: ["elastic resource allocation", "GPU multi-tenancy", "LLM inference", "pay-as-you-go GPUs", "serverless computing", "SLO compliance", "TTFT", "vLLM"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1506 — Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs

## Metadata

- **Authors:** Darzi, Erfan and Balija, Sree Bhargavi and Demir, Buse
- **Year:** 2025
- **Venue:** WoSC11 2025 - Proceedings of the 11th International Workshop on Serverless Computing, Part of Middleware Conference
- **DOI:** 10.1145/3774899.3775014
- **URL:** https://www.scopus.com/pages/publications/105029344902?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 20--25
- **Language:** English
- **Keywords:** elastic resource allocation; GPU multi-tenancy; LLM inference; pay-as-you-go GPUs; serverless computing; SLO compliance; TTFT; vLLM

### Abstract

Multi-tenant LLM inference platforms face unpredictable tail latency from noisy-neighbor interference, violating service-level objectives (SLOs) critical for serverless and elastic cloud workloads. We present a VM-deployable controller that enables fine-grained, dynamic resource allocation by combining Multi-Instance GPU (MIG) reconfiguration, PCIe-aware placement, and lightweight isolation guardrails. The controller samples per-tenant tail latency (including time-to-first-token for autoregressive serving), correlates system signals to detect interference, and adaptively adjusts isolation using host-only controls deployable in cloud environments without fabric privileges. Evaluated on vLLM serving OLMo 2 7B Instruct across a 16-GPU cluster, our approach reduces SLO miss-rate by ≈32% and improves TTFT p99 by ≈10-15% with ≤5% throughput cost, demonstrating practical elastic GPU allocation for serverless LLM inference.  © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
