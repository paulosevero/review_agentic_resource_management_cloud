---
id: "paper-1324"
title: "Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]"
authors: ["Zhai, Ennan", "Cao, Jiamin", "Qian, Kun", "Guan, Yu"]
year: 2024
venue: "Jisuanji Yanjiu yu Fazhan/Computer Research and Development"
venue_type: "journal"
doi: "10.7544/issn1000-1239.202440576"
url: "https://www.scopus.com/pages/publications/85210285646?origin=resultslist"
publisher: "Science Press"
pages: "2664--2677"
keywords: ["AI infrastructure", "collective communication", "communication scheduling", "data center networks", "large language model (LLMs)", "large models", "model training"]
language: "Chinese"
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1324 — Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]

## Metadata

- **Authors:** Zhai, Ennan and Cao, Jiamin and Qian, Kun and Guan, Yu
- **Year:** 2024
- **Venue:** Jisuanji Yanjiu yu Fazhan/Computer Research and Development
- **DOI:** 10.7544/issn1000-1239.202440576
- **URL:** https://www.scopus.com/pages/publications/85210285646?origin=resultslist
- **Publisher:** Science Press
- **Pages:** 2664--2677
- **Language:** Chinese
- **Keywords:** AI infrastructure; collective communication; communication scheduling; data center networks; large language model (LLMs); large models; model training

### Abstract

Large language models (LLMs) with hundreds of billions of parameters have brought significant technological and business transformations to today’s AI and cloud services. However, there exists a fundamental difference in network pattern between LLM training and general cloud computing (e.g., Amazon EC2 Elastic compute service), leading to a variety of new challenges. These challenges mainly include load balancing difficulties due to the traffic pattern difference (Challenge 1), the impact of multi-job communication contention on GPU utilization (Challenge 2), and high sensitivity to network failures (Challenge 3). Therefore, data center network technologies designed for general cloud computing (e.g., network architecture, routing, communication scheduling, and reliability) are no longer suitable for LLM training today. This necessitates the development of new data center networks and accompanying technical solutions specifically for LLM training. We introduce Alibaba Cloud’s high-performance network (HPN) and the multi-job communication scheduling approach Crux, designed to address the aforementioned challenges. HPN introduces a two-layer, dual-plane network architecture, which not only achieves high-speed interconnectivity for 15 000 GPUs within a Pod but also ensures precise routing suitable for LLM training (addressing Challenge 1). Furthermore, HPN proposes a novel dual-top-of-rack (ToR) design, replacing the traditional single ToR switch connection in data center networks and fundamentally avoiding single-point failure reliability risks (partially addressing Challenge 3). To tackle Challenge 2, Crux reduces the NP-complete problem of optimizing GPU utilization by modeling it as a communication scheduling issue related to GPU computational intensity. Crux then proposes an algorithm that prioritizes the flows of job with higher GPU computational intensity, significantly reducing multi-job communication contention and improving GPU utilization. Compared with the state-of-the-art efforts, Crux increases GPU utilization by up to 23%. Both HPN and Crux have been deployed and used in Alibaba Cloud production for over eight months and will continue to evolve and iterate. Building on this, we further envision possible research directions in the field of LLM training and inference, providing guidance for subsequent work. © 2024 Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
