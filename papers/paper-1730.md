---
id: "paper-1730"
title: "Cloud Based Architecture for Robotic Fleet Management Using AWS Services"
authors: ["Khanday, Sai Krishna"]
year: 2025
venue: "2025 International Conference on Next Generation Computing Systems: Intelligent System for Sustainable Development, ICNGCS 2025 - Conference Proceedings"
venue_type: "conference"
doi: "10.1109/ICNGCS64900.2025.11183314"
url: "https://www.scopus.com/pages/publications/105021924143?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AWS", "Cloud", "Docker", "DynamoDB", "Kubernetes", "RoboMaker", "Robotics", "ROS"]
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

# paper-1730 — Cloud Based Architecture for Robotic Fleet Management Using AWS Services

## Metadata

- **Authors:** Khanday, Sai Krishna
- **Year:** 2025
- **Venue:** 2025 International Conference on Next Generation Computing Systems: Intelligent System for Sustainable Development, ICNGCS 2025 - Conference Proceedings
- **DOI:** 10.1109/ICNGCS64900.2025.11183314
- **URL:** https://www.scopus.com/pages/publications/105021924143?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AWS; Cloud; Docker; DynamoDB; Kubernetes; RoboMaker; Robotics; ROS

### Abstract

The integration of cloud computing with robotics has transformed how robotic systems are designed, managed, and deployed. As robots increasingly rely on large-scale data and compute-intensive processes, offloading tasks to the cloud enables enhanced autonomy and operational efficiency, particularly in environments utilizing extensive sensor networks. Traditional standalone robotic systems face limitations in scalability, resource management, and coordination across multiple agents. To address these challenges, this study proposes a cloud-based architecture tailored for robotic fleet management using Amazon Web Services (AWS). The architecture is divided into three core components: single robot development, multi-robot coordination, and a REST API for real-time monitoring. Single robot simulations are developed and executed using AWS RoboMaker integrated with ROS and Gazebo, while multi-robot applications are written in AWS Cloud9, containerized using Amazon ECR, and orchestrated via Amazon EKS in Kubernetes Pods. Robot states are synchronized using Amazon DynamoDB, and a serverless REST API - built with AWS Lambda and API Gateway - visualizes the operational status of the fleet. The architecture ensures high availability, scalability, and secure coordination, offering a robust framework for managing both simulated and physical robotic deployments in distributed environments. © 2025 IEEE.

## 04 — Title Screening

**Title:** Cloud Based Architecture for Robotic Fleet Management Using AWS Services

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cloud Based Architecture for Robotic Fleet Management Using AWS Services
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cloud Based Architecture for Robotic Fleet Management Using AWS Services
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
