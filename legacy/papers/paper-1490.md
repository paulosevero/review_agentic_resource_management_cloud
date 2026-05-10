---
id: "paper-1490"
title: "SCOOT: SLO-Oriented Performance Tuning for LLM Inference Engines"
authors: ["Cheng, Ke", "Wang, Zhi", "Hu, Wen", "Yang, Tiannuo", "Li, Jianguo", "Zhang, Sheng"]
year: 2025
venue: "WWW 2025 - Proceedings of the ACM Web Conference"
venue_type: "conference"
doi: "10.1145/3696410.3714930"
url: "https://www.scopus.com/pages/publications/105005162023?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "829--839"
keywords: ["Bayesian Optimization", "Cloud Computing", "LLM Inference Engine", "Performance Tuning", "Service-Level Objective"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "LLMs é o workload não o tomador de decisões"

---

# paper-1490 — SCOOT: SLO-Oriented Performance Tuning for LLM Inference Engines

## Metadata

- **Authors:** Cheng, Ke and Wang, Zhi and Hu, Wen and Yang, Tiannuo and Li, Jianguo and Zhang, Sheng
- **Year:** 2025
- **Venue:** WWW 2025 - Proceedings of the ACM Web Conference
- **DOI:** 10.1145/3696410.3714930
- **URL:** https://www.scopus.com/pages/publications/105005162023?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 829--839
- **Language:** English
- **Keywords:** Bayesian Optimization; Cloud Computing; LLM Inference Engine; Performance Tuning; Service-Level Objective

### Abstract

As large language models (LLMs) are gaining increasing popularity across a wide range of web applications, it is of great importance to optimize service-level objectives (SLOs) for LLM inference services to enhance user satisfaction and improve the competitiveness of cloud vendors. In this paper, we observe that adjusting the parameters of LLM inference engines can improve service performance, and the optimal parameter configurations of different services are different. Therefore, we propose SCOOT, an automatic performance tuning system to optimize SLOs for each LLM inference service by tuning the parameters of the inference engine. SCOOT jointly exploits single-objective and multiple-objective Bayesian optimization (BO) techniques to handle various optimization objectives via exploration and exploitation. Moreover, SCOOT prunes the search space with known constraints and adopts a random forest to learn hidden constraints during the tuning process to mitigate invalid exploration. To improve the tuning efficiency, SCOOT utilizes the parallel suggestion to accelerate the tuning process. Extensive experiments demonstrate that SCOOT considerably outperforms existing tuning techniques in SLO optimization while greatly improving the tuning efficiency. Moreover, SCOOT is universally applicable to various LLM inference engines including vLLM and TensorRT-LLM. Currently, SCOOT has already been implemented in the production environment at Ant Group. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** SCOOT: SLO-Oriented Performance Tuning for LLM Inference Engines

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** SCOOT: SLO-Oriented Performance Tuning for LLM Inference Engines
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** SCOOT: SLO-Oriented Performance Tuning for LLM Inference Engines
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
