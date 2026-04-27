---
id: "paper-1433"
title: "Performance evaluation of selected ML algorithms in GC and AWS cloud environments"
authors: ["Blinowski, Grzegorz", "Bogucki, Marcin"]
year: 2025
venue: "International Journal of Electronics and Telecommunications"
venue_type: "journal"
doi: "10.24425/ijet.2025.155471"
url: "https://www.scopus.com/pages/publications/105020757926?origin=resultslist"
publisher: "Polska Akademia Nauk"
pages: ""
keywords: ["ML/AI algorithms", "performance evaluation", "Public Cloud"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1433 — Performance evaluation of selected ML algorithms in GC and AWS cloud environments

## Metadata

- **Authors:** Blinowski, Grzegorz and Bogucki, Marcin
- **Year:** 2025
- **Venue:** International Journal of Electronics and Telecommunications
- **DOI:** 10.24425/ijet.2025.155471
- **URL:** https://www.scopus.com/pages/publications/105020757926?origin=resultslist
- **Publisher:** Polska Akademia Nauk
- **Pages:** 
- **Language:** English
- **Keywords:** ML/AI algorithms; performance evaluation; Public Cloud

### Abstract

In this paper, we analyze the performance of common machine learning (ML) algorithms executed in Google Cloud and Amazon Web Services environments. The primary metric is training and prediction time as a function of the number of virtual machine cores. For comparison, benchmarks also include a "bare metal" (i.e.-non-cloud) environment, with results adjusted using the "Multi-thread Score" to account for architectural differences among the tested platforms. Our focus is on CPU-intensive algorithms. The test suite includes Support Vector Machines, Decision Trees, K-Nearest Neighbors, Linear Models, and Ensemble Methods. The evaluated classifiers, sourced from the scikit-learn and ThunderSVM libraries, include: Extra Trees, Support Vector Machines, KNearest Neighbors, Random Forest, Gradient Boosting Classifier, and Stochastic Gradient Descent. GPU-accelerated deep learning models, such as large language models, are excluded due to the difficulty of establishing a common baseline across platforms. The dataset used is the widely known "Higgs dataset," which describes kinematic properties measured by particle detectors in the search for the Higgs boson. Benchmark results are best described as varied—there is no clear trend, as training and prediction times scale differently depending on both the cloud platform and the algorithm type. This paper provides practical insights and guidance for deploying and optimizing CPU-based ML workloads in cloud environments. © 2025, Polska Akademia Nauk. All rights reserved.

## 04 — Title Screening

**Title:** Performance evaluation of selected ML algorithms in GC and AWS cloud environments

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Performance evaluation of selected ML algorithms in GC and AWS cloud environments
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Performance evaluation of selected ML algorithms in GC and AWS cloud environments
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
