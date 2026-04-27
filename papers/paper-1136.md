---
id: "paper-1136"
title: "Alibaba HPN: A Data Center Network for Large Language Model Training"
authors: ["Qian, Kun", "Xi, Yongqing", "Cao, Jiamin", "Gao, Jiaqi", "Xu, Yichi", "Guan, Yu", "Fu, Binzhang", "Shi, Xuemei", "Zhu, Fangbo", "Miao, Rui", "Wang, Chao", "Wang, Peng", "Zhang, Pengcheng", "Zeng, Xianlong", "Ruan, Eddie", "Yao, Zhiping", "Zhai, Ennan", "Cai, Dennis"]
year: 2024
venue: "ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference"
venue_type: "conference"
doi: "10.1145/3651890.3672265"
url: "https://www.scopus.com/pages/publications/85201172886?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "691--706"
keywords: ["AI infrastructure", "data center networks", "large language model", "model training", "network architecture"]
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

# paper-1136 — Alibaba HPN: A Data Center Network for Large Language Model Training

## Metadata

- **Authors:** Qian, Kun and Xi, Yongqing and Cao, Jiamin and Gao, Jiaqi and Xu, Yichi and Guan, Yu and Fu, Binzhang and Shi, Xuemei and Zhu, Fangbo and Miao, Rui and Wang, Chao and Wang, Peng and Zhang, Pengcheng and Zeng, Xianlong and Ruan, Eddie and Yao, Zhiping and Zhai, Ennan and Cai, Dennis
- **Year:** 2024
- **Venue:** ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference
- **DOI:** 10.1145/3651890.3672265
- **URL:** https://www.scopus.com/pages/publications/85201172886?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 691--706
- **Language:** English
- **Keywords:** AI infrastructure; data center networks; large language model; model training; network architecture

### Abstract

This paper presents HPN, Alibaba Cloud's data center network for large language model (LLM) training. Due to the differences between LLMs and general cloud computing (e.g., in terms of traffic patterns and fault tolerance), traditional data center networks are not well-suited for LLM training. LLM training produces a small number of periodic, bursty flows (e.g., 400Gbps) on each host. This characteristic of LLM training predisposes Equal-Cost Multi-Path (ECMP) to hash polarization, causing issues such as uneven traffic distribution. HPN introduces a 2-tier, dual-plane architecture capable of interconnecting 15K GPUs within one Pod, typically accommodated by the traditional 3-tier Clos architecture. Such a new architecture design not only avoids hash polarization but also greatly reduces the search space for path selection. Another challenge in LLM training is that its requirement for GPUs to complete iterations in synchronization makes it more sensitive to singlepoint failure (typically occurring on ToR). HPN proposes a new dual-ToR design to replace the single-ToR in traditional data center networks. HPN has been deployed in our production for more than eight months. We share our experience in designing, and building HPN, as well as the operational lessons of HPN in production.  © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** Alibaba HPN: A Data Center Network for Large Language Model Training

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Alibaba HPN: A Data Center Network for Large Language Model Training
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Alibaba HPN: A Data Center Network for Large Language Model Training
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
