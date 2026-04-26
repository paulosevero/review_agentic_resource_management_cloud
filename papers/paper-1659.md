---
id: "paper-1659"
title: "DEEPSERVE: Serverless Large Language Model Serving at Scale"
authors: ["Hu, Junhao", "Xu, Jiang", "Liu, Zhixia", "He, Yulong", "Chen, Yuetao", "Xu, Hao", "Liu, Jiang", "Meng, Jie", "Zhang, Baoquan", "Wan, Shining", "Dan, Gengyuan", "Dong, Zhiyu", "Ren, Zhihao", "Liu, Changhong", "Xie, Tao", "Lin, Dayun", "Zhang, Qin", "Yu, Yue", "Feng, Hao", "Chen, Xusheng", "Shan, Yizhou"]
year: 2025
venue: "Proceedings of the 2025 USENIX Annual Technical Conference, ATC 2025"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/105011589711?origin=resultslist"
publisher: "USENIX Association"
pages: "57--72"
keywords: ["Cloud environments", "Co-located", "Cold-start", "Design Component", "Language model", "Micro kernel", "Resources allocation", "Scheduling policies", "Simple++", "Task modelling", "Agents"]
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

# paper-1659 — DEEPSERVE: Serverless Large Language Model Serving at Scale

## Metadata

- **Authors:** Hu, Junhao and Xu, Jiang and Liu, Zhixia and He, Yulong and Chen, Yuetao and Xu, Hao and Liu, Jiang and Meng, Jie and Zhang, Baoquan and Wan, Shining and Dan, Gengyuan and Dong, Zhiyu and Ren, Zhihao and Liu, Changhong and Xie, Tao and Lin, Dayun and Zhang, Qin and Yu, Yue and Feng, Hao and Chen, Xusheng and Shan, Yizhou
- **Year:** 2025
- **Venue:** Proceedings of the 2025 USENIX Annual Technical Conference, ATC 2025
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/105011589711?origin=resultslist
- **Publisher:** USENIX Association
- **Pages:** 57--72
- **Language:** English
- **Keywords:** Cloud environments; Co-located; Cold-start; Design Component; Language model; Micro kernel; Resources allocation; Scheduling policies; Simple++; Task modelling; Agents

### Abstract

>In this paper, we propose DEEPSERVE, a scalable and serverless AI platform designed to efficiently serve large language models (LLMs) at scale in cloud environments. DEEPSERVE addresses key challenges such as resource allocation, serving efficiency, and cold start latencies through four main design components. First, DEEPSERVE uses a simple serverless abstraction called the request-job-task model, which helps manage diverse AI workloads across post-training and model-serving tasks. Second, DEEPSERVE integrates an in-house serving engine named FLOWSERVE using a microkernel-inspired design, NPU-centric execution, and SPMD-based parallelism to optimize LLM serving. Third, DEEPSERVE includes novel scheduling policies tailored for a configuration with both PD-disaggregated and PD-colocated instances. Fourth, DEEPSERVE includes optimizations such as pre-warmed pods, DRAM pre-loading, and NPU-fork, which allow DEEPSERVE to scale up to 64 instances in seconds. DEEPSERVE has been in production for over a year, operating on a large Ascend NPU cluster and providing industry-standard APIs for fine-tuning, agent serving, and model serving to our customers. © 2025 by The USENIX Association. All rights reserved.

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
