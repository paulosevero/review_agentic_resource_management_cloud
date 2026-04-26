---
id: "paper-1768"
title: "Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters"
authors: ["Lehmann, Noah", "Groth, Christian"]
year: 2025
venue: "2025 3rd International Conference on Federated Learning Technologies and Applications, FLTA 2025"
venue_type: "conference"
doi: "10.1109/FLTA67013.2025.11336462"
url: "https://www.scopus.com/pages/publications/105033519665?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "463--470"
keywords: ["availability", "eviction", "kubernetes", "maintenance", "migration", "scheduling", "singleton"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1768 — Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters

## Metadata

- **Authors:** Lehmann, Noah and Groth, Christian
- **Year:** 2025
- **Venue:** 2025 3rd International Conference on Federated Learning Technologies and Applications, FLTA 2025
- **DOI:** 10.1109/FLTA67013.2025.11336462
- **URL:** https://www.scopus.com/pages/publications/105033519665?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 463--470
- **Language:** English
- **Keywords:** availability; eviction; kubernetes; maintenance; migration; scheduling; singleton

### Abstract

Maintaining service availability in heterogeneous, resource-constrained edge clusters remains a significant challenge, particularly when workloads depend on specialized hardware or cannot be interrupted without user impact. Existing Kubernetes scheduling and maintenance solutions often assume workload replication or statelessness, leaving a gap in handling singleton, hardware-bound, and user-interactive pods typical of many edge AI deployments. This paper identifies these gaps by surveying current approaches to node maintenance scheduling, pod eviction, and rescheduling, highlighting their limitations in heterogeneous and low-redundancy environments. To address these challenges, we propose a system that integrates a custom Kubernetes operator for defining maintenance windows with a controller responsible for patient, eviction-aware restarts and workload rescheduling. Our design introduces soft time constraints, respects hardware affinity, and minimizes disruption to critical workloads such as long-running ML training or interactive LLM services. By building on standard Kubernetes mechanisms with custom logic, the approach improves resilience and operational predictability. A prototype implementation accompanies this paper, and we conclude by outlining future directions including automation, adaptive scheduling, and maintenance strategies tailored to edge AI clusters. © 2025 IEEE.

## 04 — Title Screening

**Title:** Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Patient Rescheduling for Non-Disruptive Maintenance in Edge-Aware Kubernetes Clusters
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
