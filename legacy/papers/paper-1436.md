---
id: "paper-1436"
title: "Temporal Fusion Transformer Based Vertical Scaling Management for Kubernetes"
authors: ["Bora, Kemalcan", "Kartsakli, Elli", "Quinones Moreno, Eduardo"]
year: 2025
venue: "IEEE International Conference on Cloud Computing, CLOUD"
venue_type: "conference"
doi: "10.1109/CLOUD67622.2025.00058"
url: "https://www.scopus.com/pages/publications/105015954855?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "468--473"
keywords: ["Kubernetes", "Language Models", "Memory Resource Optimization", "Temporal Fusion Transformer", "Vertical Scaling"]
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1436 — Temporal Fusion Transformer Based Vertical Scaling Management for Kubernetes

## Metadata

- **Authors:** Bora, Kemalcan and Kartsakli, Elli and Quinones Moreno, Eduardo
- **Year:** 2025
- **Venue:** IEEE International Conference on Cloud Computing, CLOUD
- **DOI:** 10.1109/CLOUD67622.2025.00058
- **URL:** https://www.scopus.com/pages/publications/105015954855?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 468--473
- **Language:** English
- **Keywords:** Kubernetes; Language Models; Memory Resource Optimization; Temporal Fusion Transformer; Vertical Scaling

### Abstract

Language Models (LMs) deployed in Kubernetes face resource management challenges due to their variable computational demands. Traditional scaling methods, like the default Vertical Pod Autoscaler (VPA), struggle to adapt, often causing inefficient resource use and performance issues. We propose the Temporal Fusion Transformer Based Dynamic Vertical Pod Autoscaler (TFT-DVPA), which employs advanced time series forecasting to predict and adjust memory allocation. Tested with three Small Language Models (under 100 million parameters) under simulated fluctuating workloads, TFT-DVPA outperforms the default VPA, achieving lower prediction errors and improved resource efficiency.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Temporal Fusion Transformer Based Vertical Scaling Management for Kubernetes

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Temporal Fusion Transformer Based Vertical Scaling Management for Kubernetes
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Temporal Fusion Transformer Based Vertical Scaling Management for Kubernetes
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
