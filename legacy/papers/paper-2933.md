---
id: "paper-2933"
title: "EdgeNetLLM: Cloud–Edge Collaborative Adaptation of Large Language Models for Mobile Networking"
authors: ["Zheng, Xixi", "Li, You", "Zheng, Baokun", "Zhang, Chuan", "Zhu, Liehuang"]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2025.3624100"
url: "https://www.scopus.com/pages/publications/105019925534?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "3928--3943"
keywords: ["cloud-edge collaboration", "deep learning", "Large language models", "mobile networking", "model adaptation"]
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
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2933 — EdgeNetLLM: Cloud–Edge Collaborative Adaptation of Large Language Models for Mobile Networking

## Metadata

- **Authors:** Zheng, Xixi and Li, You and Zheng, Baokun and Zhang, Chuan and Zhu, Liehuang
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2025.3624100
- **URL:** https://www.scopus.com/pages/publications/105019925534?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 3928--3943
- **Language:** English
- **Keywords:** cloud-edge collaboration; deep learning; Large language models; mobile networking; model adaptation

### Abstract

With the development of deep learning (DL), many applications in mobile networks increasingly rely on deep neural networks (DNNs) optimized for specific tasks. However, existing DNN-based methods require labor-intensive model design and computationally intensive centralized training, resulting in high costs, poor scalability, and limited generalization. Inspired by large language models (LLMs), some works have utilized the powerful pre-trained knowledge of LLMs as foundation models to adapt to a variety of mobile networking tasks. However, due to the inherent nature of LLMs, fine-tuning and deploying these architectures in real-world mobile network environments is a challenging task. To address this challenge, we propose EdgeNetLLM, a novel framework that enables efficient LLM adaptation in mobile network scenarios through cloud-edge collaboration. EdgeNetLLM offloads the heavy computation and fine-tuning tasks to the cloud via cloud-edge cooperation, and adapts to the corresponding mobile network tasks with minimal cost through one-time pruning, supporting lightweight inference. Additionally, on the edge side, multimodal input processing and task specialization can also be adapted to different tasks with minimal cost, reducing interaction latency between the cloud and the edge. We evaluate EdgeNetLLM on the representative mobile network tasks of adaptive bitrate streaming (ABR) and cluster job scheduling (CJS). The results demonstrate that it significantly reduces adaptation costs while maintaining task performance. Specifically, a model with approximately 40% sparsity achieves 89% and 96.8% of the task performance compared to state-of-the-art method. © 2013 IEEE.

## 04 — Title Screening

**Title:** EdgeNetLLM: Cloud–Edge Collaborative Adaptation of Large Language Models for Mobile Networking

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** EdgeNetLLM: Cloud–Edge Collaborative Adaptation of Large Language Models for Mobile Networking
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** EdgeNetLLM: Cloud–Edge Collaborative Adaptation of Large Language Models for Mobile Networking
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
