---
id: "paper-1008"
title: "Automating Cloud Deployment for Real-Time Online Foundation Model Inference"
authors: ["Li, Yang", "Li, Zhenhua", "Han, Zhenhua", "Zhang, Quanlu", "Ma, Xiaobo"]
year: 2024
venue: "IEEE/ACM Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TNET.2023.3321967"
url: "https://www.scopus.com/pages/publications/85174846491?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1509--1523"
keywords: ["Automating", "cloud configuration", "deep learning inference", "real-time services"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1008 — Automating Cloud Deployment for Real-Time Online Foundation Model Inference

## Metadata

- **Authors:** Li, Yang and Li, Zhenhua and Han, Zhenhua and Zhang, Quanlu and Ma, Xiaobo
- **Year:** 2024
- **Venue:** IEEE/ACM Transactions on Networking
- **DOI:** 10.1109/TNET.2023.3321967
- **URL:** https://www.scopus.com/pages/publications/85174846491?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1509--1523
- **Language:** English
- **Keywords:** Automating; cloud configuration; deep learning inference; real-time services

### Abstract

Deep neural network (DNN) foundation models are currently exhibiting high prediction accuracy and strong adaptability to broad tasks with remarkably large model scales. They are increasingly becoming the backend support of DNN-driven real-time online services, e.g., Siri and Instagram. Such services require low-latency and cost-efficiency for quality-of-service and commercial competitiveness. When deployed in a cloud environment, these services call for an appropriate selection of cloud configurations (i.e., specific types of VM instances), as well as a considerate device placement plan that places the operations of the model to multiple GPUs via model parallelism for cost-efficiency. Currently, the deployment mainly relies on service providers' manual efforts, which is not only onerous but also far from satisfactory oftentimes due to the huge joint search space of cloud configurations and device placement plans (for a same service, a poor deployment can incur significantly more costs by tens of times). In this paper, we attempt to efficiently automate the cloud deployment for real-time foundation model inference with minimum costs under the constraint of acceptably low latency. This attempt is enabled by 1) jointly leveraging the Bayesian Optimization and Deep Reinforcement Learning to adaptively unearth the (nearly) optimal cloud configuration and device placement with limited search time, and 2) enhancing the cost-efficiency of the deployment based on the probing-informed block multiplexing mechanism and Tensor Algebra SuperOptimizer. We implement a prototype system based on TensorFlow, conduct extensive experiments on top of Microsoft Azure, and demonstrate the generality and scalability of our solution. Results show that for lightweight DNN models and foundation models, our solution essentially saves inference costs by up to 15% and 47% with 57% and 38% lower search overheads respectively, compared with non-trivial baselines.  © 1993-2012 IEEE.

## 04 — Title Screening

**Title:** Automating Cloud Deployment for Real-Time Online Foundation Model Inference

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Automating Cloud Deployment for Real-Time Online Foundation Model Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Automating Cloud Deployment for Real-Time Online Foundation Model Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
