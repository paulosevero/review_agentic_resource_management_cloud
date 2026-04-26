---
id: "paper-2900"
title: "Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs"
authors: ["Yun, Sanggeon", "Masukawa, Ryozo", "Hassan, Raheeb", "Na, Minhyoung", "Imani, Mohsen"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3653660"
url: "https://www.scopus.com/pages/publications/105027974073?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "13702--13711"
keywords: ["edge computing", "graph neural networks", "knowledge graph", "multimodal fusion", "Multimodal video anomaly detection"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2900 — Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs

## Metadata

- **Authors:** Yun, Sanggeon and Masukawa, Ryozo and Hassan, Raheeb and Na, Minhyoung and Imani, Mohsen
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3653660
- **URL:** https://www.scopus.com/pages/publications/105027974073?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 13702--13711
- **Language:** English
- **Keywords:** edge computing; graph neural networks; knowledge graph; multimodal fusion; Multimodal video anomaly detection

### Abstract

The integration of multimodal data is critical for mission-specific tasks that require holistic reasoning over heterogeneous information sources, particularly in resource-constrained environments. MissionGNN, a hierarchical Graph Neural Network (GNN) framework, has demonstrated the feasibility of deploying complex task models on edge devices by leveraging knowledge graphs (KGs). However, effectively fusing multiple modalities remains a fundamental challenge, as fusion design directly affects the trade-off between computational efficiency and inference accuracy. In this paper, we introduce three novel KG-centric multimodal fusion strategies for video anomaly detection within a hierarchical GNN-based reasoning framework: KG-based early fusion, late fusion, and reasoning fusion. We further propose modality-aware knowledge graph generation to enable more targeted, modality-specific reasoning. We conduct extensive experiments on the XD-Violence dataset to evaluate these approaches in terms of detection performance, computational overhead, energy consumption, and the cost of large language model (LLM)-based KG generation. Our results reveal distinct trade-offs among the fusion strategies. Early KG-based fusion provides a well-balanced solution, achieving notable accuracy gains while reducing per-frame energy consumption by over 70%. Late fusion, which employs half-sized modality-aware KGs, yields additional accuracy improvements with only a modest increase in computational cost. Reasoning fusion delivers the highest performance, achieving 72.93% mAP and establishing state-of-the-art results, albeit at the expense of increased resource usage. These findings offer actionable insights for the design of efficient multimodal GNN-based reasoning systems. By systematically characterizing the trade-offs among fusion strategies, this work provides a practical framework to guide the selection of energy-efficient and accuracy-aware solutions for mission-critical applications operating under diverse resource constraints. © 2013 IEEE.

## 04 — Title Screening

**Title:** Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs
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
