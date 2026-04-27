---
id: "paper-1383"
title: "GAIKube: Generative AI-Based Proactive Kubernetes Container Orchestration Framework for Heterogeneous Edge Computing"
authors: ["Ali, Babar", "Golec, Muhammed", "Subramanian Murugesan, Subramaniam", "Wu, Huaming", "Singh Gill, Sukhpal", "Cuadrado, Felix", "Uhlig, Steve"]
year: 2025
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2024.3508771"
url: "https://www.scopus.com/pages/publications/105002560890?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "933--945"
keywords: ["container migration", "Edge computing", "generative AI", "Kubernetes", "service level agreement", "vertical scaling"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1383 — GAIKube: Generative AI-Based Proactive Kubernetes Container Orchestration Framework for Heterogeneous Edge Computing

## Metadata

- **Authors:** Ali, Babar and Golec, Muhammed and Subramanian Murugesan, Subramaniam and Wu, Huaming and Singh Gill, Sukhpal and Cuadrado, Felix and Uhlig, Steve
- **Year:** 2025
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2024.3508771
- **URL:** https://www.scopus.com/pages/publications/105002560890?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 933--945
- **Language:** English
- **Keywords:** container migration; Edge computing; generative AI; Kubernetes; service level agreement; vertical scaling

### Abstract

Containerized edge computing emerged as a preferred platform for latency-sensitive applications requiring informed and efficient decision-making accounting for the end user and edge service providers’ interests simultaneously. Edge decision engines exploit pipelined knowledge streams to enhance performance and often fall short by employing inferior resource predictors subjected to limited available training data. These shortcomings flow through the pipelines and adversely impact other modules, including schedulers leading to such decisions costing delays, user-experienced accuracy, Service Level Agreements (SLA) violations, and server faults. To address limited data, substandard CPU usage predictions, and container orchestration considering delay accuracy and SLA violations, we propose a threefold GAIKube framework offering Generative AI (GAI)-enabled proactive container orchestration for a heterogeneous edge computing paradigm. Addressing data limitation, GAIKube employs DoppelGANger (DGAN) to augment time series CPU usage data for a computationally heterogeneous edge cluster. In the second place, GAIKube leverages Google TimesFM for its long horizon predictions, 4.84 Root Mean Squared Error (RMSE) and 3.10 Mean Absolute Error (MAE) against veterans Long Short-Term Memory (LSTM) and Bidirectional LSTM (Bi-LSTM) on concatenated DGAN and original dataset. Considering TimesFM quality predictions utilizing the DGAN extended dataset, GAIKube pipelines CPU usage predictions of edge servers to a proposed dynamic container orchestrator. GAIKube orchestrator produces container scheduling, migration, dynamic vertical scaling, and hosted application model-switching to balance contrasting SLA violations, cost, and accuracy objectives avoiding server faults. Google Kubernetes Engine (GKE) based real testbed experiments show that the GAIKube orchestrator offers 3.43% SLA violations and 3.80% user-experienced accuracy loss with zero server faults at 1.46 CPU cores expense in comparison to industry-standard model-switching, GKE pod scaling, and GKE optimized scheduler. © 2015 IEEE.

## 04 — Title Screening

**Title:** GAIKube: Generative AI-Based Proactive Kubernetes Container Orchestration Framework for Heterogeneous Edge Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** GAIKube: Generative AI-Based Proactive Kubernetes Container Orchestration Framework for Heterogeneous Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** GAIKube: Generative AI-Based Proactive Kubernetes Container Orchestration Framework for Heterogeneous Edge Computing
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
