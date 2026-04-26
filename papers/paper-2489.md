---
id: "paper-2489"
title: "QoS-Driven Hybrid Inference Scheme for Generative Diffusion Models in MEC-Enabled AI-Generated Content Networks"
authors: ["Zhuang, Xinyi", "Wu, Jiaqi", "Wu, Hongjia", "Tang, Ming", "Gao, Lin"]
year: 2025
venue: "IEEE International Conference on Communications"
venue_type: "conference"
doi: "10.1109/ICC52391.2025.11161497"
url: "https://www.scopus.com/pages/publications/105018453800?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1151--1156"
keywords: ["Energy utilization", "Mobile edge computing", "Quality of service", "Robotics", "Content creation", "Content network", "Content-based", "Diffusion model", "Edge computing", "Edge server", "Hybrid inference", "Phase based", "Quality-of-service", "User equipments", "Benchmarking"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-2489 — QoS-Driven Hybrid Inference Scheme for Generative Diffusion Models in MEC-Enabled AI-Generated Content Networks

## Metadata

- **Authors:** Zhuang, Xinyi and Wu, Jiaqi and Wu, Hongjia and Tang, Ming and Gao, Lin
- **Year:** 2025
- **Venue:** IEEE International Conference on Communications
- **DOI:** 10.1109/ICC52391.2025.11161497
- **URL:** https://www.scopus.com/pages/publications/105018453800?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1151--1156
- **Language:** English
- **Keywords:** Energy utilization; Mobile edge computing; Quality of service; Robotics; Content creation; Content network; Content-based; Diffusion model; Edge computing; Edge server; Hybrid inference; Phase based; Quality-of-service; User equipments; Benchmarking

### Abstract

AI-Generated Content (AIGC) based on Generative Diffusion Models (GDMs) is revolutionizing content creation and promoting substantial advancements in domains like autonomous driving and robotics. Leveraging progress in Mobile Edge Computing (MEC) and model compression techniques, GDMs are increasingly being deployed on Edge Servers (ESs) and User Equipments (UEs), which typically face resource limitations. In such MEC-enabled scenarios, designing an efficient inference scheme for GDMs still remains a significant challenge, due to the resource constraints on ESs and UEs as well as the personalized demands of AIGC users. In this work, we propose a novel hybrid inference scheme, which consists of two stages: public prompt generation and common-to-personalized inference. In the first stage, a Large Language Model (LLM) is adopted to generate public prompts derived from the common features of users' personal prompts. In the second stage, a common inference phase based on public prompts is first executed for all users (to produce common intermediate results), and then a personalized inference phase based on each user's personal prompts is performed for each individual user (to generate final contents). Clearly, by introducing the common inference phase, the total inference steps can be significantly reduced. In such a scheme, we further study a hybrid inference optimization problem to optimize both common and personalized inference steps, aiming to maximize the total Quality of Service (QoS), while minimizing delay and energy consumption. Simulation results show that our proposed scheme significantly outperforms existing benchmarks, with the performance gains ranging from 12.6% to 102.2%.  © 2025 IEEE.

## 04 — Title Screening

**Title:** QoS-Driven Hybrid Inference Scheme for Generative Diffusion Models in MEC-Enabled AI-Generated Content Networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** QoS-Driven Hybrid Inference Scheme for Generative Diffusion Models in MEC-Enabled AI-Generated Content Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** QoS-Driven Hybrid Inference Scheme for Generative Diffusion Models in MEC-Enabled AI-Generated Content Networks
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
