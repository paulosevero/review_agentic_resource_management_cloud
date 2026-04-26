---
id: "paper-303"
title: "Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications"
authors: ["Khaleq, Abeer Abdel", "Ra, Ilkyeun"]
year: 2021
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2021.3061890"
url: "https://www.scopus.com/pages/publications/85101769830?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "35464--35476"
keywords: ["Autonomous autoscaling", "Kubernetes", "microservices autoscaling", "real-time cloud applications", "reinforcement learning"]
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

# paper-303 — Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications

## Metadata

- **Authors:** Khaleq, Abeer Abdel and Ra, Ilkyeun
- **Year:** 2021
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2021.3061890
- **URL:** https://www.scopus.com/pages/publications/85101769830?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 35464--35476
- **Language:** English
- **Keywords:** Autonomous autoscaling; Kubernetes; microservices autoscaling; real-time cloud applications; reinforcement learning

### Abstract

Cloud applications are becoming more containerized in nature. Developing a cloud application based on a microservice architecture imposes different challenges including scalability at the container level. What adds to the challenge is that cloud applications impose quality of service (QoS) requirements and have various resource demands requiring a customized scaling approach. For example, real-time applications require near real time response time as a QoS. Existing autoscaling technologies such as Kubernetes offer some customization to a set of threshold values for autoscaling. The challenge is identifying the right values for the different autoscaling parameters that will guarantee QoS in a changing dynamic environment. Advancements in machine learning and reinforcement learning (RL) provides a means for autoscaling in cloud applications with no domain knowledge. In this article, we introduce an intelligent autonomous autoscaling system for microservices autoscaling in the cloud with QoS constraints. The system consists of two modules. The first module identifies the microservice resource demand via a generic autoscaling algorithm deployed on the Google Kubernetes Engine (GKE). Our algorithm adapts the Kubernetes autoscaling paradigm based on the application resource requirements. The second module uses reinforcement learning agents to learn and identify the autoscaling threshold values based on the resource demand and QoS. Experimental results show an enhancement in the microservice response time up to 20% compared to the default autoscaling paradigm. In addition, the RL agents can identify the autoscaling threshold values while maintaining a response time below the QoS constraint. Our proposed work provides a customized autoscaling solution for microservices in cloud applications while adhering to QoS constraints with minimum user interaction.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications
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
