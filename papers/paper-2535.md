---
id: "paper-2535"
title: "LightLoader: Accelerate Python FaaS Cold-Start via Multi-level Source Code Optimization"
authors: ["Chen, Pengyu", "Chen, Wei", "Wu, Guoquan", "Wei, Jun"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-95-5015-9_7"
url: "https://www.scopus.com/pages/publications/105028365267?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "92--106"
keywords: ["cold-start", "FaaS", "Python", "serverless computing"]
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

# paper-2535 — LightLoader: Accelerate Python FaaS Cold-Start via Multi-level Source Code Optimization

## Metadata

- **Authors:** Chen, Pengyu and Chen, Wei and Wu, Guoquan and Wei, Jun
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-95-5015-9_7
- **URL:** https://www.scopus.com/pages/publications/105028365267?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 92--106
- **Language:** English
- **Keywords:** cold-start; FaaS; Python; serverless computing

### Abstract

Cold starts are a big challenge in Function-as-a-Service (FaaS). While most solutions focus on optimizing the runtime environment and FaaS scheduling, they often overlook the impact of FaaS implementation on cold-start latency. Dynamic languages like Python, with their extensive dependency imports and dynamic building processes, can particularly suffer from longer startup times. We propose LightLoader, an approach to accelerating Python-based FaaS (i.e., PyFaaS) cold start by debloating them and optimizing their dynamic build. LightLoader rewrites PyFaaS by converting potentially unused functions to on-demand dynamic loading, thereby reducing loading time. It also delays third-party package loading until its first use instead of importing these all at the beginning. Notably, to ensure that these rewrites do not compromise the original PyFaaS’s functionalities, we utilize a large language model (LLM) to test and repair the optimized PyFaaS iteratively. We implemented a prototype on the popular open-source serverless platform OpenFaaS and conducted an extensive evaluation with PyFaaS of various sizes and functionalities. The experimental results show that LightLoader effectively accelerates PyFaaS cold starts, reducing end-to-end latency by 11.44% on average, a 9.32% improvement over the state-of-the-art solution. It also decreases the runtime memory utilization by an average of 9.28% and up to 43.27%. LightLoader is platform-independent and can be a supplement to the optimizations of other layers. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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
