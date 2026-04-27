---
id: "paper-2791"
title: "A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning"
authors: ["Sundara Krishnan, K.", "Michael Priya, E."]
year: 2026
venue: "International Journal of Software Engineering and Knowledge Engineering"
venue_type: "journal"
doi: "10.1142/S0218194025501001"
url: "https://www.scopus.com/pages/publications/105026804366?origin=resultslist"
publisher: "World Scientific"
pages: "1003--1037"
keywords: ["artificial intelligence", "automated analysis", "cloud computing", "deep learning", "Heart prediction"]
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
    final_score: 0.1666
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2791 — A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning

## Metadata

- **Authors:** Sundara Krishnan, K. and Michael Priya, E.
- **Year:** 2026
- **Venue:** International Journal of Software Engineering and Knowledge Engineering
- **DOI:** 10.1142/S0218194025501001
- **URL:** https://www.scopus.com/pages/publications/105026804366?origin=resultslist
- **Publisher:** World Scientific
- **Pages:** 1003--1037
- **Language:** English
- **Keywords:** artificial intelligence; automated analysis; cloud computing; deep learning; Heart prediction

### Abstract

Heart Disease (HD) diagnosis can be imperative by amalgamating IoT and AI, as IoT devices permit continuous, real-time patient data monitoring, when AI algorithms afford precise, personalized risk assessments and extrapolative analysis. This approach is practical because it enables early detection and involvement, thereby enhancing patient outcomes by addressing potential problems before they escalate. Earlier research has frequently been constrained by data collection in static, inadequate personalization and a lack of real-time analysis. To address the challenges in heart disease diagnosis within smart healthcare environments, we propose a novel Double Level Risk-based Personalized Heart Disease Detection Model (DLR-PHDM). Similar to our previous work, this model begins with data acquisition using IoT devices and pre-processing at the Distributed Edge Server (DES). The pre-processed data is then fed into an Attention-based Long Short-Term Memory-Capsule Network (ALSTM-CapsNet) for classifying patient risk into three levels: low, moderate and high, based on Electronic Health Records (EHRs) and current sensor data. The risk classification results are managed by a Distributed Reinforced Scheduler (DRS) for Heart Disease Crisis Planning (HDCP), where patient data is scheduled according to their risk level using Multi-Agent Deep Reinforcement Learning (MA-DRL). This scheduling takes into account factors such as patient risk score, resource availability, wait time and appointment slot utilization. Subsequently, the scheduled reports are sent to the Multi-Cloud Server (MCS) for heart disease detection, utilizing tailored AI models: Support Vector Machine (SVM) for low-risk, Convolutional Neural Network (CNN) for moderate risk and Transformer-based CNN (T-CNN) for high-risk patients. The detected results are then used to provide personalized recommendations to the corresponding patients. During implementation, the proposed DLR-PHDM model demonstrated superior performance, achieving an accuracy of 99.79%, precision of 99.10%, specificity of 98.62%, sensitivity of 99.95% and an F-score of 99.12%. It outperformed the state-of-the-art heart disease prediction models. © 2026 World Scientific Publishing Company.

## 04 — Title Screening

**Title:** A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning

### Machine Screening

- **Final Score:** 0.1666 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.5
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
