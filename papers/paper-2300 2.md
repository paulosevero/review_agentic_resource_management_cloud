---
id: "paper-2300"
title: "Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge"
authors: ["Wu, Hai", "Chen, Xu", "Huang, Kaibin"]
year: 2025
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2025.3544333"
url: "https://www.scopus.com/pages/publications/85219583356?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4839--4852"
keywords: ["edge computing", "fine-tuning", "Foundation models (FoMo's)"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-2300 — Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge

## Metadata

- **Authors:** Wu, Hai and Chen, Xu and Huang, Kaibin
- **Year:** 2025
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2025.3544333
- **URL:** https://www.scopus.com/pages/publications/85219583356?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4839--4852
- **Language:** English
- **Keywords:** edge computing; fine-tuning; Foundation models (FoMo's)

### Abstract

The emergence of large-scale foundation models (FoMo's) that can perform human-like intelligence motivates their deployment at the network edge for devices to access state-of-the-art artificial intelligence (AI). For better user experiences, the pre-trained FoMo's need to be adapted to specialized downstream tasks through fine-tuning techniques. To transcend a single device's memory and computation limitations, we advocate multi-device cooperation within the device-edge cooperative fine-tuning (DEFT) paradigm, where edge devices cooperate to simultaneously optimize different parts of fine-tuning parameters within a FoMo. The edge server is responsible for coordination and gradient aggregation. However, the parameter blocks reside at different depths within a FoMo architecture, leading to varied computation latency-and-memory cost due to gradient backpropagation-based calculations. The heterogeneous on-device computation and memory capacities and channel conditions necessitate an integrated communication-and-computation (C2) allocation of local computation loads and uplink communication resources to achieve low-latency (LoLa) DEFT. To this end, we consider the depth-ware DEFT block allocation problem. The involved optimal block-device matching is tackled by the proposed low-complexity Cutting-RecoUNting-CHecking (CRUNCH) algorithm, which is designed by exploiting the monotone-increasing property between block depth and computation latency-and-memory cost. Next, the joint bandwidth-and-block allocation (JBBA) makes the problem more sophisticated, i.e., mathematically NP-hard. We observe a splittable Lagrangian expression through the transformation and analysis of the original problem, where the variables indicating device involvement are introduced to decouple the block and bandwidth allocation. Then, the dual ascent method is employed to tackle the JBBA problem iteratively. Within each iteration, block allocation and bandwidth allocation are optimized concurrently. The optimal block allocation sub-problem is solved efficiently by applying the Hungarian method facilitated by the proposed CRUNCH algorithm. On the other hand, the bandwidth allocation sub-problem is solved in closed form, shedding light on favorable allocations to resource-limited devices. Through extensive experiments conducted on the GLUE benchmark, our results demonstrate significant latency reduction achievable by LoLa DEFT for fine-tuning a RoBERTa model.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge
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
