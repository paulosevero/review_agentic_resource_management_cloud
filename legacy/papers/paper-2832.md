---
id: "paper-2832"
title: "Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method"
authors: ["Wang, Yingxin", "Feng, Binbin", "Ding, Zhijun"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-95-5012-8_20"
url: "https://www.scopus.com/pages/publications/105028325820?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "267--281"
keywords: ["ensemble inference", "function-as-a-service", "instance autoscaling", "serverless computing"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-2832 — Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method

## Metadata

- **Authors:** Wang, Yingxin and Feng, Binbin and Ding, Zhijun
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-95-5012-8_20
- **URL:** https://www.scopus.com/pages/publications/105028325820?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 267--281
- **Language:** English
- **Keywords:** ensemble inference; function-as-a-service; instance autoscaling; serverless computing

### Abstract

Ensemble learning achieves superior performance and generalization capabilities by leveraging multiple base models to collaboratively obtain prediction results, while the concurrent execution of multiple models also introduces significant latency and resource overhead challenges. Serverless computing frameworks have emerged as a popular choice for supporting ensemble inference services due to their on-demand dynamic allocation of computational resources. However, existing serverless scheduling methods suffer from prominent issues such as static request scheduling leading to high response latency and independent function scaling causing frequent bottlenecks. To address these challenges, this paper proposes a multi-agent-driven serverless dual-mode adaptive ensemble inference method to achieve end-to-end joint optimization of request distribution, model composition, and instance scaling. Specifically, 1) Heterogeneous feature-enhanced ensemble service dynamic route method, which realizes heuristic combination of user group portrait and base model through offline unsupervised log clustering, and considers the real-time resource status online to achieve rapid request distribution with O(1) time complexity; 2) Master-slave instance autoscaling algorithm based on multi-agent reinforcement learning, which realizes dynamic balance between local resource awareness and global bottleneck optimization through modeling collaboration and competition relationship between master-slave inference nodes. Finally, experimental validation on real-world clusters using public datasets has demonstrated the performance and overhead advantages of the proposed method. Our approach reduces latency by 13.4%, improves accuracy by 9.1%, and lowers CPU and memory occupancy by 19.4% and 3.9% compared to state-of-the-art inference serving systems. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

## 04 — Title Screening

**Title:** Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
