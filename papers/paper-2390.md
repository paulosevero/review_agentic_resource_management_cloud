---
id: "paper-2390"
title: "Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL"
authors: ["Younesi, Abolfazl", "Shabrang Maryan, Abbas", "Oustad, Elyas", "Najafabadi Samani, Zahra", "Ansari, Mohsen", "Fahringer, Thomas"]
year: 2025
venue: "Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025"
venue_type: "conference"
doi: "10.1145/3773274.3774267"
url: "https://www.scopus.com/pages/publications/105027166632?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: ""
keywords: ["Deep Reinforcement Learning", "Edge-Cloud Inference", "Large Language Model", "Lyapunov Optimization"]
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

# paper-2390 — Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL

## Metadata

- **Authors:** Younesi, Abolfazl and Shabrang Maryan, Abbas and Oustad, Elyas and Najafabadi Samani, Zahra and Ansari, Mohsen and Fahringer, Thomas
- **Year:** 2025
- **Venue:** Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025
- **DOI:** 10.1145/3773274.3774267
- **URL:** https://www.scopus.com/pages/publications/105027166632?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 
- **Language:** English
- **Keywords:** Deep Reinforcement Learning; Edge-Cloud Inference; Large Language Model; Lyapunov Optimization

### Abstract

Deploying large language models (LLMs) on edge devices is challenging due to their limited memory and power resources. Cloud-only inference reduces device burden but introduces high latency and cost. Static edge-cloud partitions optimize a single metric and struggle when bandwidth fluctuates. We propose Splitwise, a novel Lyapunov-assisted deep reinforcement learning (DRL) framework for fine-grained, adaptive partitioning of LLMs across edge and cloud environments. Splitwise decomposes transformer layers into attention heads and feed-forward sub-blocks, exposing exponentially more partition choices than layer-wise schemes. A hierarchical DRL policy, guided by Lyapunov optimization, jointly minimizes latency, energy consumption, and accuracy degradation while guaranteeing queue stability under stochastic workloads and variable network bandwidth. Splitwise also guarantees robustness via partition checkpoints with exponential backoff recovery in case of communication failures. Experiments on Jetson Orin NX, Galaxy S23, and Raspberry Pi 5 with GPTĝ€'2 (1.5B), LLaMAĝ€'7B, and LLaMAĝ€'13B show that Splitwise reduces endĝ€'toĝ€'end latency by 1.4 × -2.8 × and cuts energy consumption by up to 41% compared with existing partitioners. It lowers the 95th-percentile latency by 53-61% relative to cloud-only execution, while maintaining accuracy and modest memory requirements. © 2025 Copyright held by the owner/author(s).

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
