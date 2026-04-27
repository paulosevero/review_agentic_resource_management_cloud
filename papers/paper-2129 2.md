---
id: "paper-2129"
title: "Characteristics and Link Congestion Awareness"
authors: ["Shen, Zhipeng", "Li, Lei", "Zhang, Lihong", "Liu, Bing", "Cai, Anning", "Huang, Shan"]
year: 2025
venue: "Proceedings - 2025 IEEE Cyber Science and Technology Congress, CyberSciTech 2025"
venue_type: "conference"
doi: "10.1109/CyberSciTech68397.2025.00012"
url: "https://www.scopus.com/pages/publications/105032631668?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "45--54"
keywords: ["AI", "Dynamic Traffic Regulation", "GPU Communication Path", "Load Balance", "Network Topology", "RoCE"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2129 — Characteristics and Link Congestion Awareness

## Metadata

- **Authors:** Shen, Zhipeng and Li, Lei and Zhang, Lihong and Liu, Bing and Cai, Anning and Huang, Shan
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE Cyber Science and Technology Congress, CyberSciTech 2025
- **DOI:** 10.1109/CyberSciTech68397.2025.00012
- **URL:** https://www.scopus.com/pages/publications/105032631668?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 45--54
- **Language:** English
- **Keywords:** AI; Dynamic Traffic Regulation; GPU Communication Path; Load Balance; Network Topology; RoCE

### Abstract

In the context of AI computing RoCE networks, the low-entropy traffic characteristics of training and inference services lead to load imbalance in RoCE networks, reducing GPU communication efficiency and affecting AI service operations. To address this issue, this paper proposes RNL (RoCE Network Load-balance), a framework specifically designed for load balancing in AI RoCE networks. RNL conducts real-time modeling of AI task communication relationships and paths, as well as network link loads. It uses a multi-dimensional link congestion assessment algorithm to accurately calculate the congestion score of all network paths and based on in-depth analysis of the communication primitives of AI business GPU, identifies communication bandwidth and delay requirements. It achieves precise scheduling and orchestration of AI business communication paths, ensuring balanced load distribution of RoCE network for AI business.The RNL design leverages existing commercial high-performance network interface cards and RoCE switches, eliminating dependence on special hardware and ensuring good compatibility with existing AI computing data center networks. Experimental results show that the proposed scheme significantly enhances RoCE network performance, GPU communication primitives, and inference performance of large AI language models. Specifically, it improves network link bandwidth utilization by 85%, link balance dispersion by 90%, bandwidth of AllReduce/AllGather communication primitives by over 50%, and throughput/TTFT/TPOT of large AI model inference by over 30%, providing an effective solution for constructing high-performance AI RoCE networks.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Characteristics and Link Congestion Awareness

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Characteristics and Link Congestion Awareness
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Characteristics and Link Congestion Awareness
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
