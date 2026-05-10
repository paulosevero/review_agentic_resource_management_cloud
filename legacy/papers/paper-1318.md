---
id: "paper-1318"
title: "Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics"
authors: ["Yue, Xiaofei", "Yang, Song", "Zhu, Liehuang", "Trajanovski, Stojan", "Fu, Xiaoming"]
year: 2024
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM52122.2024.10621303"
url: "https://www.scopus.com/pages/publications/85201815032?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2498--2507"
keywords: ["Graph neural networks", "Reinforcement learning", "Current performance", "Decisions makings", "Demeter", "Distributed data", "Fine grained", "Global services", "Large volumes", "Low latency", "Multi-agent reinforcement learning", "Service level objective", "Resource allocation"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1318 — Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics

## Metadata

- **Authors:** Yue, Xiaofei and Yang, Song and Zhu, Liehuang and Trajanovski, Stojan and Fu, Xiaoming
- **Year:** 2024
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM52122.2024.10621303
- **URL:** https://www.scopus.com/pages/publications/85201815032?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2498--2507
- **Language:** English
- **Keywords:** Graph neural networks; Reinforcement learning; Current performance; Decisions makings; Demeter; Distributed data; Fine grained; Global services; Large volumes; Low latency; Multi-agent reinforcement learning; Service level objective; Resource allocation

### Abstract

In the era of global services, low-latency analytics on large-volume geo-distributed data has been a regular demand for application decision-making. Serverless computing facilitates fast function start-up and deployment, making it an attractive way for geo-distributed analytics. We argue that the serverless paradigm holds the potential to breach current performance bottlenecks via fine-grained function orchestration. However, how to configure it for geo-distributed analytics remains ambiguous. To fill this gap, we present Demeter, a scalable fine-grained function orchestrator for geo-distributed serverless analytics systems. Demeter aims to minimize the composite cost of co-existing jobs while meeting the user-specific Service Level Objectives (SLO). To handle the volatile environments and learn the diverse function demands, a Multi-Agent Reinforcement Learning (MARL) solution is used to co-optimize the per-function placement and resource allocation. The MARL extracts holistic and compact states via hierarchical graph neural networks, and then designs a novel actor network to shrink the huge decision space and model complexity. Finally, we implement Demeter and evaluate it using realistic workloads. The experimental results reveal that Demeter significantly saves costs by 23.3%∼32.7%, while reducing SLO violations by over 27.4%, surpassing state-of-the-art solutions. © 2024 IEEE.

## 04 — Title Screening

**Title:** Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics
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
