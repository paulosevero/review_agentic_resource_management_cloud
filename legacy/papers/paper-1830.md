---
id: "paper-1830"
title: "The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities"
authors: ["Li, Ning", "Guo, Song", "Zhang, Tuo", "Li, Muqing", "Hong, Zicong", "Zhou, Qihua", "Yuan, Xin", "Zhang, Haijun"]
year: 2025
venue: "IEEE Communications Magazine"
venue_type: "journal"
doi: "10.1109/MCOM.001.2400717"
url: "https://www.scopus.com/pages/publications/105014471164?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "164--171"
keywords: ["Architecture", "Dynamics", "Memory architecture", "Mobile edge computing", "Network architecture", "Servers", "Topology", "Communication resources", "Computational resources", "Deployment architecture", "Deployment strategy", "Dynamic allocations", "Edge server", "Heterogeneous hardware", "Mixture of experts", "Property", "Ubiquitous intelligence", "Digital storage"]
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
    human_justification: "Review"

---

# paper-1830 — The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities

## Metadata

- **Authors:** Li, Ning and Guo, Song and Zhang, Tuo and Li, Muqing and Hong, Zicong and Zhou, Qihua and Yuan, Xin and Zhang, Haijun
- **Year:** 2025
- **Venue:** IEEE Communications Magazine
- **DOI:** 10.1109/MCOM.001.2400717
- **URL:** https://www.scopus.com/pages/publications/105014471164?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 164--171
- **Language:** English
- **Keywords:** Architecture; Dynamics; Memory architecture; Mobile edge computing; Network architecture; Servers; Topology; Communication resources; Computational resources; Deployment architecture; Deployment strategy; Dynamic allocations; Edge server; Heterogeneous hardware; Mixture of experts; Property; Ubiquitous intelligence; Digital storage

### Abstract

The powerfulness of LLMS indicates that deploying various LLMS with different scales and architectures on end, edge, and cloud to satisfy different requirements and adaptive heterogeneous hardware is the critical way to achieve ubiquitous intel-ligence for 6G. However, the massive parameters of LLMS poses significant challenges in deploying them on edge servers due to high computational and storage demands. Considering that the sparse activation in Mixture of Experts (MoE) is effective on scalable and dynamic allocation of computational and communications resources at the edge, this article proposes a novel MoE-empowered col-laborative deployment framework for edge LLMS, denoted as CoEL. This framework fully leverages the properties of MoE architecture and encom-passes three key aspects: model quantization, intra-server and inter-server cooperation, and token pruning and fusion. The CoEL begins with quantizing experts based on their importance and popularity, assigning different bit widths to different experts. Then, considering the heterogeneous resources of edge servers and model deployment requirements, a multi-dimensional collaborative deployment strat-egy is proposed. This strategy employs intra-server cooperation if the compressed model can be deployed on a single edge server; otherwise, it trig-gers inter-server cooperation and deploys experts across multiple edge servers distributed. Additionally, to minimize data transmission delays between servers, a token compression approach is applied. Finally, given the dynamic of network topology, resource status, and user requirements, the deployment strategies are regularly updated to maintain its relevance and effectiveness. This article also delineates the challenges and potential research directions for the deployment of edge LLMS. © 1979-2012 IEEE.

## 04 — Title Screening

**Title:** The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities
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
