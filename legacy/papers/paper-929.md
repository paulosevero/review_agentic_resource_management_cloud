---
id: "paper-929"
title: "EdgeCloudAI: Edge-Cloud Distributed Video Analytics"
authors: ["Ghasemi, Mahshid", "Kostic, Zoran", "Ghaderi, Javad", "Zussman, Gil"]
year: 2024
venue: "ACM MobiCom 2024 - Proceedings of the 30th International Conference on Mobile Computing and Networking"
venue_type: "conference"
doi: "10.1145/3636534.3698857"
url: "https://www.scopus.com/pages/publications/105002588712?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "1778--1780"
keywords: ["edge-cloud computing", "real-time anomaly detection", "vision language models"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-929 — EdgeCloudAI: Edge-Cloud Distributed Video Analytics

## Metadata

- **Authors:** Ghasemi, Mahshid and Kostic, Zoran and Ghaderi, Javad and Zussman, Gil
- **Year:** 2024
- **Venue:** ACM MobiCom 2024 - Proceedings of the 30th International Conference on Mobile Computing and Networking
- **DOI:** 10.1145/3636534.3698857
- **URL:** https://www.scopus.com/pages/publications/105002588712?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 1778--1780
- **Language:** English
- **Keywords:** edge-cloud computing; real-time anomaly detection; vision language models

### Abstract

Recent advances in Visual Language Models (VLMs) have significantly enhanced video analytics. VLMs capture complex visual and textual connections. While Convolutional Neural Networks (CNNs) excel in spatial pattern recognition, VLMs provide a global context, making them ideal for tasks like complex incidents and anomaly detection. However, VLMs are much more computationally intensive, posing challenges for large-scale and real-time applications. This paper introduces EdgeCloudAI, a scalable system integrating VLMs and CNNs through edge-cloud computing. Edge-CloudAI performs initial video processing (e.g., CNN) on edge devices and offloads deeper analysis (e.g., VLM) to the cloud, optimizing resource use and reducing latency. We have deployed EdgeCloudAI on the NSF COSMOS testbed in NYC. In this demo, we will demonstrate EdgeCloudAI's performance in detecting user-defined incidents in real-time. © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** EdgeCloudAI: Edge-Cloud Distributed Video Analytics

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeCloudAI: Edge-Cloud Distributed Video Analytics
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeCloudAI: Edge-Cloud Distributed Video Analytics
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
