---
id: "paper-2689"
title: "Supply Framework of Physical Machine Demand in Elastic Computing Service"
authors: ["Liu, Zhanyu", "Zhang, Xudong", "Hu, Zhidong", "Li, Xiejing", "Peng, Fei", "Zhou, Jian", "Deng, Siyu", "Zheng, Guanjie"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-3-662-72243-5_27"
url: "https://www.scopus.com/pages/publications/105020015201?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "474--491"
keywords: ["cloud computing", "elastic computing service", "time series forecasting"]
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

# paper-2689 — Supply Framework of Physical Machine Demand in Elastic Computing Service

## Metadata

- **Authors:** Liu, Zhanyu and Zhang, Xudong and Hu, Zhidong and Li, Xiejing and Peng, Fei and Zhou, Jian and Deng, Siyu and Zheng, Guanjie
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-3-662-72243-5_27
- **URL:** https://www.scopus.com/pages/publications/105020015201?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 474--491
- **Language:** English
- **Keywords:** cloud computing; elastic computing service; time series forecasting

### Abstract

In the context of Elastic Computing Service (ECS), ensuring an adequate supply of physical machines to meet the varying computing demands is crucial for sustaining high performance and low cost. In industrial practices, different from the typical resource allocation problem that allocates the computing demand into servers, provision of physical servers is a supply chain problem that predicts the future demand for physical machines based on forecasts derived from historical vCPU usage and potential future customer needs, particularly for those customers with high demand. This provision process encompasses three main stages: customer text demand analysis, future demand forecasting, and the allocation of physical servers. However, each stage presents specific challenges. Firstly, large demands from customers are often ambiguously expressed. Secondly, the forecasting process is complicated to model due to the scarce, spiky, and ambiguous nature of the data. Thirdly, the conversion of forecasted vCPU demand into actual physical server quantities is inefficient and ineffective. To address these issues, we propose a novel framework for physical server provisioning. Initially, client requests are aggregated and processed using Large Language Model to extract Potential Future Demand (PFD). Subsequently, future vCPU demand is predicted based on PFD data through a specialized forecasting model tailored with PFD-specific optimizations. Finally, physical machine allocation is executed employing a hierarchical bin-packing algorithm enhanced by heuristic selection and integer programming. Extensive experiments demonstrate the effectiveness and efficiency of the proposed framework with over 60% accuracy improvement and 90% fragment reduction on average compared with the baselines. This framework has been applied to the real industrial scenario of Alibaba Cloud. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

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
