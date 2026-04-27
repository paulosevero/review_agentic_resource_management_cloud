---
id: "paper-1595"
title: "Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes"
authors: ["Godhani, Payal", "Bhat, Ajay"]
year: 2025
venue: "Proceedings of IEEE International Conference for Women in Innovation, Technology and Entrepreneurship, ICWITE 2025"
venue_type: "conference"
doi: "10.1109/ICWITE64848.2025.11306960"
url: "https://www.scopus.com/pages/publications/105032389556?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Inferencing on AMD", "Machine Learning Inferencing", "Sustainability On Kubernetes", "XGBoost ML Model"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1595 — Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes

## Metadata

- **Authors:** Godhani, Payal and Bhat, Ajay
- **Year:** 2025
- **Venue:** Proceedings of IEEE International Conference for Women in Innovation, Technology and Entrepreneurship, ICWITE 2025
- **DOI:** 10.1109/ICWITE64848.2025.11306960
- **URL:** https://www.scopus.com/pages/publications/105032389556?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Inferencing on AMD; Machine Learning Inferencing; Sustainability On Kubernetes; XGBoost ML Model

### Abstract

Kubernetes has proven to be one of the most powerful platforms for containerization, offering unique features such as flexibility, scalability, and fault tolerance. The orchestration platform's ease of use and impressive orchestration capabilities have driven its widespread adoption in the machine learning domain for inferencing and training. However, Kubernetes has its own set of challenges with respect to its default resource configuration. Its inefficient CPU resource utilization has led to high power consumption during AI inferencing [1]. This paper conducts research on the energy efficiency of Kubernetes in the context of machine learning and also proposes a dynamic framework that aims at reducing the power consumption of the inferencing workload by adjusting the CPU allocation in real-time on an AMD cluster. The framework configures the containers to their most optimal CPU allocation settings on the Kubernetes cluster while maintaining the workloads latency thresholds defined by the service level agreement. We describe a holistic solution that can be leveraged by all the inferencing workloads using Kubernetes, taking into account the inferencing performance and its power consumption. We discuss the results of a tree-based XGBoost (Extreme Gradient Boost) inferencing workload where the power consumption was reduced by 75% as compared to the default settings for the SLA used in this research. We show that by introducing a dynamic CPU-allocation framework, we can see significant improvements in the power consumption for machine learning inferencing workloads on Kubernetes clusters without substantially compromising inferencing performance. This research also highlights that Kubernetes potential is not just limited to container orchestration but is capable of dynamically optimizing energy usage in cloud-native AI applications. This research contributes to the growing need for more sustainable and greener AI deployments, especially in the age of generative AI.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
