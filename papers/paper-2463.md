---
id: "paper-2463"
title: "Responsive DNN Adaptation for Video Analytics against Environment Shift via Hierarchical Mobile-Cloud Collaborations"
authors: ["Zhao, Maozhe", "Liu, Shengzhong", "Wu, Fan", "Chen, Guihai"]
year: 2025
venue: "ACM SenSys 2025 - 23rd ACM Conference on Embedded Networked Sensor Systems, In Transactions to Conference Embedded Artificial Intelligence and Sensing Systems"
venue_type: "conference"
doi: "10.1145/3715014.3722044"
url: "https://www.scopus.com/pages/publications/105035739021?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "317--331"
keywords: ["continuous learning", "mobile computing", "video analytics"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2463 — Responsive DNN Adaptation for Video Analytics against Environment Shift via Hierarchical Mobile-Cloud Collaborations

## Metadata

- **Authors:** Zhao, Maozhe and Liu, Shengzhong and Wu, Fan and Chen, Guihai
- **Year:** 2025
- **Venue:** ACM SenSys 2025 - 23rd ACM Conference on Embedded Networked Sensor Systems, In Transactions to Conference Embedded Artificial Intelligence and Sensing Systems
- **DOI:** 10.1145/3715014.3722044
- **URL:** https://www.scopus.com/pages/publications/105035739021?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 317--331
- **Language:** English
- **Keywords:** continuous learning; mobile computing; video analytics

### Abstract

Mobile video analysis systems often encounter various deploying environments, where environment shifts present greater demands for responsiveness in adaptations of deployed "expert DNN models". Existing model adaptation frameworks primarily operate in a cloud-centric way, exhibiting degraded performance during adaptation and delayed reactions to environment shifts. Instead, this paper proposes MOCHA, a novel framework optimizing the responsiveness of continuous model adaptation through hierarchical collaborations between mobile and cloud resources. Specifically, MOCHA (1) reduces adaptation response delays by performing on-device model reuse and fast fine-tuning before requesting cloud model retrieval and end-to-end retraining; (2) accelerates history expert model retrieval by organizing them into a structured taxonomy utilizing domain semantics analyzed by a cloud foundation model as indices; (3) enables efficient local model reuse by maintaining onboard expert model caches for frequent scenes, which proactively prefetch model weights from the cloud model database. Extensive evaluations with real-world videos on three DNN tasks show MOCHA improves the model accuracy during adaptation by up to 6.8% while saving the response delay and retraining time by up to 35.5× and 3.0× respectively.  © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** Responsive DNN Adaptation for Video Analytics against Environment Shift via Hierarchical Mobile-Cloud Collaborations

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Responsive DNN Adaptation for Video Analytics against Environment Shift via Hierarchical Mobile-Cloud Collaborations
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Responsive DNN Adaptation for Video Analytics against Environment Shift via Hierarchical Mobile-Cloud Collaborations
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
