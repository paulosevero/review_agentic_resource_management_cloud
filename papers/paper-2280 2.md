---
id: "paper-2280"
title: "SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration"
authors: ["Wang, Huiyu", "Liu, Zhicheng", "Wang, Xiaofei", "Qiu, Chao", "Zhang, Cheng", "Wang, Wenyu", "Ye, Qianwen"]
year: 2025
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-96-2864-3_7"
url: "https://www.scopus.com/pages/publications/105002576903?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "75--87"
keywords: ["Cloud-Edge Collaboration", "Diffusion Models", "Edge Intelligence", "Generative AI", "Model Inference"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2280 — SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration

## Metadata

- **Authors:** Wang, Huiyu and Liu, Zhicheng and Wang, Xiaofei and Qiu, Chao and Zhang, Cheng and Wang, Wenyu and Ye, Qianwen
- **Year:** 2025
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-96-2864-3_7
- **URL:** https://www.scopus.com/pages/publications/105002576903?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 75--87
- **Language:** English
- **Keywords:** Cloud-Edge Collaboration; Diffusion Models; Edge Intelligence; Generative AI; Model Inference

### Abstract

In recent years, the rapid rise of Artificial Intelligence Generated Content (AIGC) has been accompanied by a surge in demand for generative AI application services. This trend has not only driven the diversified deployment of large-scale models but also posed more significant challenges to the efficient inference of these models. Current computing solutions have struggled to solely keep pace with growing user demands, which results in insufferable latency and inefficient performance. Integrating cloud computing and edge computing for the inference process of large models is deemed a promising solution, while related resource scheduling issues are still pending. To address this challenge, we focus our research on diffusion models, a representative model in the field of generative artificial intelligence, and propose a cloud-edge collaborative framework to accelerate the inference pipeline of text-to-image diffusion models. Our optimization goal is to minimize the average completion time of inference tasks while maintaining image quality. Considering that the inference for each image is an iterative process, we propose a step clipping strategy to save and reuse intermediate results to reduce iterations, compressing the calculation amount of inference tasks. Above this, we design a task scheduling strategy using proximal policy optimization, which can make efficient resource decisions. Experiments demonstrate the superiority of our strategy over local execution, greedy task scheduling strategy, and learning-based task scheduling strategies. Compared with the three baselines, the average task completion time under different system configurations is reduced by 1.093 s, 1.024 s, and 0.481 s, respectively. © IFIP International Federation for Information Processing 2025.

## 04 — Title Screening

**Title:** SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** SC-TSDRL: A Cloud-Edge Collaboration Framework for Diffusion Model Inference Acceleration
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
