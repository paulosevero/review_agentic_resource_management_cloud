---
id: "paper-1310"
title: "Asteroid: Resource-Efficient Hybrid Pipeline Parallelism for Collaborative DNN Training on Heterogeneous Edge Devices"
authors: ["Ye, Shengyuan", "Zeng, Liekang", "Chu, Xiaowen", "Xing, Guoliang", "Chen, Xu"]
year: 2024
venue: "ACM MobiCom 2024 - Proceedings of the 30th International Conference on Mobile Computing and Networking"
venue_type: "conference"
doi: "10.1145/3636534.3649363"
url: "https://www.scopus.com/pages/publications/85206391599?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "312--326"
keywords: ["data parallelism", "distributed machine learning", "Edge intelligence", "hybrid parallelism", "pipeline parallelism"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1310 — Asteroid: Resource-Efficient Hybrid Pipeline Parallelism for Collaborative DNN Training on Heterogeneous Edge Devices

## Metadata

- **Authors:** Ye, Shengyuan and Zeng, Liekang and Chu, Xiaowen and Xing, Guoliang and Chen, Xu
- **Year:** 2024
- **Venue:** ACM MobiCom 2024 - Proceedings of the 30th International Conference on Mobile Computing and Networking
- **DOI:** 10.1145/3636534.3649363
- **URL:** https://www.scopus.com/pages/publications/85206391599?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 312--326
- **Language:** English
- **Keywords:** data parallelism; distributed machine learning; Edge intelligence; hybrid parallelism; pipeline parallelism

### Abstract

On-device Deep Neural Network (DNN) training has been recognized as crucial for privacy-preserving machine learning at the edge. However, the intensive training workload and limited onboard computing resources pose significant challenges to the availability and efficiency of model training. While existing works address these challenges through native resource management optimization, we instead leverage our observation that edge environments usually comprise a rich set of accompanying trusted edge devices with idle resources beyond a single terminal. We propose Asteroid, a distributed edge training system that breaks the resource walls across heterogeneous edge devices for efficient model training acceleration. Asteroid adopts a hybrid pipeline parallelism to orchestrate distributed training, along with a judicious parallelism planning for maximizing throughput under certain resource constraints. Furthermore, a fault-tolerant yet lightweight pipeline replay mechanism is developed to tame the device-level dynamics for training robustness and performance stability. We implement Asteroid on heterogeneous edge devices with both vision and language models, demonstrating up to 12.2× faster training than conventional parallelism methods and 2.1× faster than state-of-the-art hybrid parallelism methods through evaluations. Furthermore, Asteroid can recover training pipeline 14× faster than baseline methods while preserving comparable throughput despite unexpected device exiting and failure. © 2024 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Asteroid: Resource-Efficient Hybrid Pipeline Parallelism for Collaborative DNN Training on Heterogeneous Edge Devices

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Asteroid: Resource-Efficient Hybrid Pipeline Parallelism for Collaborative DNN Training on Heterogeneous Edge Devices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Asteroid: Resource-Efficient Hybrid Pipeline Parallelism for Collaborative DNN Training on Heterogeneous Edge Devices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
