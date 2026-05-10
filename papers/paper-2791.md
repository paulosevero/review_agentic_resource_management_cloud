---
id: paper-2791
title: A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning
authors:
- Sundara Krishnan, K.
- Michael Priya, E.
venue: International Journal of Software Engineering and Knowledge Engineering
venue_type: journal
year: 2026
doi: 10.1142/S0218194025501001
url: https://www.scopus.com/pages/publications/105026804366?origin=resultslist
publisher: World Scientific
pages: 1003--1037
keywords:
- artificial intelligence
- automated analysis
- cloud computing
- deep learning
- Heart prediction
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2791 — A Double-Level Risk-Based Personalized Heart Disease Detection Model for Smart Health Environment Using IoT and Deep Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Heart Disease (HD) diagnosis can be imperative by amalgamating IoT and AI, as IoT devices permit continuous, real-time patient data monitoring, when AI algorithms afford precise, personalized risk assessments and extrapolative analysis. This approach is practical because it enables early detection and involvement, thereby enhancing patient outcomes by addressing potential problems before they escalate. Earlier research has frequently been constrained by data collection in static, inadequate personalization and a lack of real-time analysis. To address the challenges in heart disease diagnosis within smart healthcare environments, we propose a novel Double Level Risk-based Personalized Heart Disease Detection Model (DLR-PHDM). Similar to our previous work, this model begins with data acquisition using IoT devices and pre-processing at the Distributed Edge Server (DES). The pre-processed data is then fed into an Attention-based Long Short-Term Memory-Capsule Network (ALSTM-CapsNet) for classifying patient risk into three levels: low, moderate and high, based on Electronic Health Records (EHRs) and current sensor data. The risk classification results are managed by a Distributed Reinforced Scheduler (DRS) for Heart Disease Crisis Planning (HDCP), where patient data is scheduled according to their risk level using Multi-Agent Deep Reinforcement Learning (MA-DRL). This scheduling takes into account factors such as patient risk score, resource availability, wait time and appointment slot utilization. Subsequently, the scheduled reports are sent to the Multi-Cloud Server (MCS) for heart disease detection, utilizing tailored AI models: Support Vector Machine (SVM) for low-risk, Convolutional Neural Network (CNN) for moderate risk and Transformer-based CNN (T-CNN) for high-risk patients. The detected results are then used to provide personalized recommendations to the corresponding patients. During implementation, the proposed DLR-PHDM model demonstrated superior performance, achieving an accuracy of 99.79%, precision of 99.10%, specificity of 98.62%, sensitivity of 99.95% and an F-score of 99.12%. It outperformed the state-of-the-art heart disease prediction models. © 2026 World Scientific Publishing Company.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2791.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
