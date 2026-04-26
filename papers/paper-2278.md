---
id: "paper-2278"
title: "Providing load flexibility by reshaping power profiles of large language model workloads"
authors: ["Wang, Yi", "Guo, Qinglai", "Chen, Min"]
year: 2025
venue: "Advances in Applied Energy"
venue_type: "journal"
doi: "10.1016/j.adapen.2025.100232"
url: "https://www.scopus.com/pages/publications/105010873248?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Energy efficiency", "Frequency scaling", "Large language model", "Load flexibility", "Renewable energy"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2278 — Providing load flexibility by reshaping power profiles of large language model workloads

## Metadata

- **Authors:** Wang, Yi and Guo, Qinglai and Chen, Min
- **Year:** 2025
- **Venue:** Advances in Applied Energy
- **DOI:** 10.1016/j.adapen.2025.100232
- **URL:** https://www.scopus.com/pages/publications/105010873248?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Energy efficiency; Frequency scaling; Large language model; Load flexibility; Renewable energy

### Abstract

The emergence of large language models (LLM) has driven a significant increase of AI workload in data center power demand. Renewable-powered solutions to decarbonizing LLM workload and reducing electricity costs are faced with the combined volatility of stochastic user requests and renewable energy. The key to removing the barriers in sustainable AI development lies in the adjustable capability of LLM power profiles. Therefore, this paper focuses on exploring the potential load flexibility of LLM workload and proposes a coordinated scheduling framework, notably, without computing performance degradation. Driven by the existence of the energy-optimal core frequency for graphics processing units (GPU), the energy-performance decoupling phenomenon is discovered and proved, where collaborative scaling in GPU quantity and frequency can change power but not computing performance. Motivated by this, the framework slows down the fine-tuning cluster and utilizes idle GPU resources from the inference cluster to maintain the computing performance of fine-tuning tasks. Consequently, the power consumption of the total cluster is reduced, which provides a fresh source of load flexibility. Furthermore, the framework employs dynamic frequency scaling to more flexibly modify the power profile of the expanded fine-tuning cluster. The computing performance is particularly guaranteed through temporal coupling constraints. In a simulated study supported by real-world data, the results prove a 6.8% power-saving ability and 11.3% cost-saving gains on average. © 2025 The Authors

## 04 — Title Screening

**Title:** Providing load flexibility by reshaping power profiles of large language model workloads

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Providing load flexibility by reshaping power profiles of large language model workloads
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Providing load flexibility by reshaping power profiles of large language model workloads
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
