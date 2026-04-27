---
id: "paper-2595"
title: "Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration"
authors: ["He, Xinxin", "Yang, Yang", "Yang, Zhiyong", "Gao, Yifei", "Yin, Changchuan", "Chen, Shanzhi"]
year: 2026
venue: "IEEE Communications Magazine"
venue_type: "journal"
doi: "10.1109/MCOM.001.2500421"
url: "https://www.scopus.com/pages/publications/105031504551?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "34--41"
keywords: ["Agents", "Autonomous agents", "Behavioral research", "Cloud computing architecture", "Decision making", "Dynamics", "Highway administration", "Highway planning", "Intelligent agents", "Life cycle", "Natural resources management", "Network architecture", "Resource allocation", "Road vehicles", "Roads and streets", "Agent based", "Architecture management", "Cloud agents", "Collaborative systems", "Dynamic resources", "Intelligence models", "Management method", "Multi tasks", "Resource management", "Resources allocation", "Global optimization"]
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

# paper-2595 — Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration

## Metadata

- **Authors:** He, Xinxin and Yang, Yang and Yang, Zhiyong and Gao, Yifei and Yin, Changchuan and Chen, Shanzhi
- **Year:** 2026
- **Venue:** IEEE Communications Magazine
- **DOI:** 10.1109/MCOM.001.2500421
- **URL:** https://www.scopus.com/pages/publications/105031504551?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 34--41
- **Language:** English
- **Keywords:** Agents; Autonomous agents; Behavioral research; Cloud computing architecture; Decision making; Dynamics; Highway administration; Highway planning; Intelligent agents; Life cycle; Natural resources management; Network architecture; Resource allocation; Road vehicles; Roads and streets; Agent based; Architecture management; Cloud agents; Collaborative systems; Dynamic resources; Intelligence models; Management method; Multi tasks; Resource management; Resources allocation; Global optimization

### Abstract

Large artificial intelligence models (LAMs) have introduced new opportunities to 6G networks, whereas their integration into vehicle-road-cloud collaborative systems remains challenging due to insufficient model coordination and difficulties in dynamic resource adaptation. To address these issues, this article proposes an agent-based network architecture and a resource management method for vehicle-road-cloud collaboration. In this architecture, the cloud agent conducts largescale pretraining to characterize global resource allocation dynamics, while lightweight models are deployed at the road-side unit (RSU) agent and vehicle agent to enable real-time inference and decision-making. To balance model performance and resource consumption, we introduce a lifecycle management strategy for the agent network. By analyzing the relationship between performance gain and the consumption of communication and computation resources, we jointly optimize training data sampling rates, model pruning ratio, and resource allocation strategies. This enables dynamic adjustment of the update frequency for cloud-based large models and the fine-tuning frequency for edge-side models, thereby ensuring continuous and high-efficiency model inference in resource-constrained dynamic scenarios. Additionally, we design a decision LAM (D-LAM) for single-task scenarios, which employs sequence modeling and temporal embedding to achieve dynamic coordination of multidimensional resources. We further develop a decision multitask LAM (DM-LAM) to address complex multitask scenarios, which integrates a mixture-of-experts (MoE) mechanism with a gating network to support both personalized resource allocation for individual tasks and global optimization across heterogeneous tasks. Experimental results demonstrate that the proposed method significantly improves resource utilization efficiency and achieves 10±$1.2% higher task completion rates compared to decision transformer model.  © 2026 IEEE.

## 04 — Title Screening

**Title:** Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration
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
