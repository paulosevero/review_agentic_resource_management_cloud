---
id: paper-1730
title: Cloud Based Architecture for Robotic Fleet Management Using AWS Services
authors:
- Khanday, Sai Krishna
venue: '2025 International Conference on Next Generation Computing Systems: Intelligent System for Sustainable Development, ICNGCS 2025 - Conference Proceedings'
venue_type: conference
year: 2025
doi: 10.1109/ICNGCS64900.2025.11183314
url: https://www.scopus.com/pages/publications/105021924143?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AWS
- Cloud
- Docker
- DynamoDB
- Kubernetes
- RoboMaker
- Robotics
- ROS
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1730 — Cloud Based Architecture for Robotic Fleet Management Using AWS Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of cloud computing with robotics has transformed how robotic systems are designed, managed, and deployed. As robots increasingly rely on large-scale data and compute-intensive processes, offloading tasks to the cloud enables enhanced autonomy and operational efficiency, particularly in environments utilizing extensive sensor networks. Traditional standalone robotic systems face limitations in scalability, resource management, and coordination across multiple agents. To address these challenges, this study proposes a cloud-based architecture tailored for robotic fleet management using Amazon Web Services (AWS). The architecture is divided into three core components: single robot development, multi-robot coordination, and a REST API for real-time monitoring. Single robot simulations are developed and executed using AWS RoboMaker integrated with ROS and Gazebo, while multi-robot applications are written in AWS Cloud9, containerized using Amazon ECR, and orchestrated via Amazon EKS in Kubernetes Pods. Robot states are synchronized using Amazon DynamoDB, and a serverless REST API - built with AWS Lambda and API Gateway - visualizes the operational status of the fleet. The architecture ensures high availability, scalability, and secure coordination, offering a robust framework for managing both simulated and physical robotic deployments in distributed environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1730.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
