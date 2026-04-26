---
id: "paper-2775"
title: "Prediction-based GPU sharing for distributed training"
authors: ["Shin, Changyong", "Go, Younghun", "Yoo, Yeonho", "Jeong, Jinwoo", "Hwang, Jaehyun", "Yang, Gyeongsik", "Yoo, Chuck"]
year: 2026
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2026.108413"
url: "https://www.scopus.com/pages/publications/105034268374?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Cloud computing", "GPU Scheduling", "GPU Sharing", "Performance prediction", "Service level agreement"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2775 — Prediction-based GPU sharing for distributed training

## Metadata

- **Authors:** Shin, Changyong and Go, Younghun and Yoo, Yeonho and Jeong, Jinwoo and Hwang, Jaehyun and Yang, Gyeongsik and Yoo, Chuck
- **Year:** 2026
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2026.108413
- **URL:** https://www.scopus.com/pages/publications/105034268374?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud computing; GPU Scheduling; GPU Sharing; Performance prediction; Service level agreement

### Abstract

AbstractGPU sharing aims to enhance the efficiency of GPU utilization by running distributed deep learning training jobs concurrently. However, GPU sharing poses a significant challenge: the increase in job completion time (JCT) caused by interference between jobs is inconsistent, complicating job scheduling. Our experiments reveal that the degree of JCT increase varies by as much as  ∼ 3.7 × . While previous studies have analyzed this JCT inconsistency problem, none of them have been able to minimize the inconsistency. We propose TensorShare, a proactive GPU sharing technique that leverages a deep learning model to predict the extent of JCT increase. This study defines a new metric, called GPU SLA, which represents the upper threshold of JCT increase. TensorShare then introduces a novel scheduler that proactively identifies which jobs meet GPU SLA while minimizing the JCT increase. Our evaluation shows that TensorShare improves GPU SLA satisfaction rates by 26.1 × –47.3 ×  and reduces the JCT increase by 37%–60%. Furthermore, we evaluate TensorShare with large language models that are not included in training TensorShare’s prediction model, achieving  ∼ 7 ×  and  ∼ 10.3 ×  improvements in GPU SLA satisfaction and JCT inconsistency, respectively. © 2026 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC license. http://creativecommons.org/licenses/by-nc/4.0/

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
