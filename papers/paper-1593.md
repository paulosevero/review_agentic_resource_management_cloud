---
id: "paper-1593"
title: "Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions"
authors: ["Ginarsa, Nyoman Agus Nugraha", "Santoso, Bagus Jati"]
year: 2025
venue: "Proceedings - 2025 4th International Conference on Electronics Representation and Algorithm: Artificial Intelligence: Creating Tomorrow's World Today, ICERA 2025"
venue_type: "conference"
doi: "10.1109/ICERA66156.2025.11087276"
url: "https://www.scopus.com/pages/publications/105013473906?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "400--404"
keywords: ["Amazon Bedrock", "autoscaling", "generative AI", "Kubernetes"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1593 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions

## Metadata

- **Authors:** Ginarsa, Nyoman Agus Nugraha and Santoso, Bagus Jati
- **Year:** 2025
- **Venue:** Proceedings - 2025 4th International Conference on Electronics Representation and Algorithm: Artificial Intelligence: Creating Tomorrow's World Today, ICERA 2025
- **DOI:** 10.1109/ICERA66156.2025.11087276
- **URL:** https://www.scopus.com/pages/publications/105013473906?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 400--404
- **Language:** English
- **Keywords:** Amazon Bedrock; autoscaling; generative AI; Kubernetes

### Abstract

In the context of cloud-native architecture, the need for an efficient autoscaling mechanism is crucial to ensure service availability while avoiding resource waste. The Horizontal Pod Autoscaler (HPA) in Kubernetes has limitations in responding to real-time load spikes. This research aims to develop a prediction-based autoscaling approach using the Claude 3.7 Sonnet generative AI model via Amazon Bedrock. Historical CPU and memory data were collected by Prometheus at certain intervals, then converted to CSV format and sent to Claude 3.7 to generate a prediction of the number of pods needed in the next five minutes. The prediction results are then automatically applied to the Amazon EKS cluster via the Kubernetes API. The test results show that this approach can improve resource utilization efficiency and maintain service stability during traffic fluctuations, when compared to conventional HPA. This research also reveals that the accuracy of the prediction is highly dependent on the quality of the historical data, prompt, and AI model used. In the future, this research will expand the scope by adding other metrics such as latency, request rate, and I/O, and comparing the performance between generative AI models on Amazon Bedrock. © 2025 IEEE.

## 04 — Title Screening

**Title:** Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
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
