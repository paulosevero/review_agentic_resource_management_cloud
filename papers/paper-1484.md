---
id: "paper-1484"
title: "Task-Level Energy Profiling of Large Language Model Inference"
authors: ["Chen, Haichun", "Duan, Xinyu", "Sun, Yimeng", "Wang, Yehan", "Chen, Shijie", "Ding, Zhaohao", "Dehghanian, Payman"]
year: 2025
venue: "2025 IEEE 9th Conference on Energy Internet and Energy System Integration, EI2 2025"
venue_type: "conference"
doi: "10.1109/EI268505.2025.11425055"
url: "https://www.scopus.com/pages/publications/105035782813?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2657--2661"
keywords: ["Data Center", "Energy Profiling", "Inference", "Large Language Model", "Load Modeling"]
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
    human_justification: "LLM as workload"

---

# paper-1484 — Task-Level Energy Profiling of Large Language Model Inference

## Metadata

- **Authors:** Chen, Haichun and Duan, Xinyu and Sun, Yimeng and Wang, Yehan and Chen, Shijie and Ding, Zhaohao and Dehghanian, Payman
- **Year:** 2025
- **Venue:** 2025 IEEE 9th Conference on Energy Internet and Energy System Integration, EI2 2025
- **DOI:** 10.1109/EI268505.2025.11425055
- **URL:** https://www.scopus.com/pages/publications/105035782813?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2657--2661
- **Language:** English
- **Keywords:** Data Center; Energy Profiling; Inference; Large Language Model; Load Modeling

### Abstract

With the rise of Large Language Models (LLMs), the frequency and scale of inference requests continue to grow. To support LLM inference workloads, the energy consumption of AI-centric data center has increased. Therefore, inference energy consumption modeling is critical as the foundation for understanding and optimizing energy usage. However, existing models overlook inference-related factors such as model parameters, hardware configuration, and prompt features, resulting in inaccurate modeling of inference energy consumption. To address this issue, we propose a two-stage augmented energy profiling model for LLM inference. In the first stage, we apply Kmeans to predict response token length, which serves as an enhanced feature for subsequent energy modeling. In the second stage, we use the predicted token length together with other original features as inputs, and apply XGBoost to model the inference energy consumption. To validate the model, we conduct case studies on a public dataset, where our method reduce the Mean Absolute Error from 0.39 to 0.043, achieving an 89% error reduction over the baseline. © 2025 IEEE.

## 04 — Title Screening

**Title:** Task-Level Energy Profiling of Large Language Model Inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Task-Level Energy Profiling of Large Language Model Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Task-Level Energy Profiling of Large Language Model Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
