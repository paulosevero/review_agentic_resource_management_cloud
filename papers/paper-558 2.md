---
id: "paper-558"
title: "AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices"
authors: ["Cai, Binlei", "Wang, Bin", "Yang, Meihong", "Guo, Qin"]
year: 2023
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2023.01.014"
url: "https://www.scopus.com/pages/publications/85147192698?origin=resultslist"
publisher: "Elsevier B.V."
pages: "61--75"
keywords: ["Cloud computing", "Microservices", "Quality of service", "Reinforcement learning", "Resource management", "Tail latency"]
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
    human_decision: ""
    human_justification: ""

---

# paper-558 — AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices

## Metadata

- **Authors:** Cai, Binlei and Wang, Bin and Yang, Meihong and Guo, Qin
- **Year:** 2023
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2023.01.014
- **URL:** https://www.scopus.com/pages/publications/85147192698?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 61--75
- **Language:** English
- **Keywords:** Cloud computing; Microservices; Quality of service; Reinforcement learning; Resource management; Tail latency

### Abstract

Modern user-facing services are progressively evolving from large monolithic applications to complex graphs of loosely-coupled microservices. While microservice architecture greatly improves the efficiency of development and operation, it also complicates resource allocation and performance guarantee due to complex dependencies across different microservices. To prevent resource wastage and ensure user satisfaction, we present AutoMan, a learning-driven resource manager for microservices that enables much more efficient resource provisioning while guaranteeing the end-to-end tail latency Service Level Objective (SLO). AutoMan leverages a multi-agent deep deterministic policy gradient (MADDPG)-based method to capture the dependencies across different microservices and to allocate a proper amount of resources to each microservice subject to the target end-to-end tail latency SLO. During runtime, it further proactively identifies the critical microservices responsible for performance anomaly by deriving partial SLOs mathematically, and performs dynamic reprovisioning to mitigate the potential SLO violations. Testbed experiments show that AutoMan can save CPU and memory resources by up to 49.6% and 29.1% on average, while guaranteeing the same end-to-end tail latency objective. © 2023 Elsevier B.V.

## 04 — Title Screening

**Title:** AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AutoMan: Resource-efficient provisioning with tail latency guarantees for microservices
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
