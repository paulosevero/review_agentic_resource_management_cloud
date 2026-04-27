---
id: "paper-1668"
title: "Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach"
authors: ["Huang, Hualong", "Du, Yongkang", "Zhan, Wenhan", "Duan, Hancong", "Peng, Kai", "Cheng, Yamin", "Ye, Yalan", "Zhao, Zitian"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3611003"
url: "https://www.scopus.com/pages/publications/105016601032?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["batch processing", "computation offloading", "deep reinforcement learning", "Edge-Cloud collaboration", "MLLM inference", "resource allocation"]
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
    human_justification: "RL"

---

# paper-1668 — Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach

## Metadata

- **Authors:** Huang, Hualong and Du, Yongkang and Zhan, Wenhan and Duan, Hancong and Peng, Kai and Cheng, Yamin and Ye, Yalan and Zhao, Zitian
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3611003
- **URL:** https://www.scopus.com/pages/publications/105016601032?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** batch processing; computation offloading; deep reinforcement learning; Edge-Cloud collaboration; MLLM inference; resource allocation

### Abstract

The deployment of multimodal large language models (MLLMs) on resource-constrained mobile devices poses significant challenges due to their high computational demands. This paper introduces a novel two-timescale optimization framework for efficient MLLM inference in Edge-Cloud networks, addressing the problem of multi-timescale resource management by jointly optimizing slow-timescale MLLMs deployment decisions and fast-timescale batch scheduling, GPU resource allocation, and bandwidth allocation under dynamic network conditions and spatiotemporal request heterogeneity. Our key innovation is a hierarchical twin delayed deep deterministic policy gradient (HALTD3) algorithm that integrates attention mechanisms and long short-term memory networks to optimize slow-timescale MLLMs deployment and fast-timescale resource allocation, minimizing weighted system costs including deployment cost, end-to-end latency, and energy consumption, while meeting stringent quality-of-service requirements. Extensive experiments demonstrate that the HALTD3 algorithm substantially outperforms baseline methods in reducing system costs across diverse MLLM workloads and dynamic network scenarios, validating its effectiveness for practical edge-cloud collaborative inference. © 2014 IEEE.

## 04 — Title Screening

**Title:** Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach
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
