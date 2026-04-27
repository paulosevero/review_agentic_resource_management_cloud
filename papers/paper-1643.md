---
id: "paper-1643"
title: "UELLM: A Unified and Efficient Approach for Large Language Model Inference Serving"
authors: ["He, Yiyuan", "Xu, Minxian", "Wu, Jingfeng", "Zheng, Wanyi", "Ye, Kejiang", "Xu, Chengzhong"]
year: 2025
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-981-96-0805-8_16"
url: "https://www.scopus.com/pages/publications/85212921991?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "218--235"
keywords: ["Cloud Computing", "Large Language Model Inference", "Resource Management", "Scheduling Algorithm"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1643 — UELLM: A Unified and Efficient Approach for Large Language Model Inference Serving

## Metadata

- **Authors:** He, Yiyuan and Xu, Minxian and Wu, Jingfeng and Zheng, Wanyi and Ye, Kejiang and Xu, Chengzhong
- **Year:** 2025
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-981-96-0805-8_16
- **URL:** https://www.scopus.com/pages/publications/85212921991?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 218--235
- **Language:** English
- **Keywords:** Cloud Computing; Large Language Model Inference; Resource Management; Scheduling Algorithm

### Abstract

In the context of Machine Learning as a Service (MLaaS) clouds, the extensive use of Large Language Models (LLMs) often requires efficient management of significant query loads. When providing real-time inference services, several challenges arise. Firstly, increasing the number of GPUs may lead to a decrease in inference speed due to a heightened communication overhead, while an inadequate number of GPUs can lead to out-of-memory errors. Secondly, different deployment strategies need to be evaluated to guarantee optimal utilization and minimal inference latency. Lastly, inefficient orchestration of inference queries can easily lead to significant Service Level Objective (SLO) violations. To address these challenges, we propose a Unified and Efficient approach for Large Language Model inference serving (UELLM), which consists of three main components: 1)resourceprofiler, 2)batchscheduler, and 3)LLMdeployer. The resourceprofiler characterizes resource usage of inference queries by predicting resource demands based on a fine-tuned LLM. The batchscheduler effectively batches the queries profiled by the resourceprofiler based on batching algorithms, aiming to decrease inference delays while meeting SLO and efficient batch processing of inference queries. The LLMdeployer can efficiently deploy LLMs by considering the current cluster hardware topology and LLM characteristics, enhancing resource utilization and reducing resource overhead. UELLM minimizes resource overhead, reduces inference latency, and lowers SLO violation rates. Compared with state-of-the-art (SOTA) techniques, UELLM reduces the inference latency by 72.3% to 90.3%, enhances GPU utilization by 1.2× to 4.1×, and increases throughput by 1.92× to 4.98×, it can also serve without violating the inference latency SLO. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

## 04 — Title Screening

**Title:** UELLM: A Unified and Efficient Approach for Large Language Model Inference Serving

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** UELLM: A Unified and Efficient Approach for Large Language Model Inference Serving
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** UELLM: A Unified and Efficient Approach for Large Language Model Inference Serving
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
