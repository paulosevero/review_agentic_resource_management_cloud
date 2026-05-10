---
id: "paper-1986"
title: "A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach"
authors: ["Naydenov, Nikolas", "Ruseva, Stela", "Chemungor, Naomy Jerono", "Adewole, Kayode Sakariyah"]
year: 2025
venue: "ISMSIT 2025 - 9th International Symposium on Multidisciplinary Studies and Innovative Technologies, Proceedings"
venue_type: "conference"
doi: "10.1109/ISMSIT67332.2025.11268074"
url: "https://www.scopus.com/pages/publications/105031084139?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Anomaly Detection", "Cloud-Native", "Containerization", "eBPF", "Intrusion Detection", "Kubernetes", "Machine Learning", "Microservices", "Network Forensics", "Train-Serve Skew"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1986 — A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach

## Metadata

- **Authors:** Naydenov, Nikolas and Ruseva, Stela and Chemungor, Naomy Jerono and Adewole, Kayode Sakariyah
- **Year:** 2025
- **Venue:** ISMSIT 2025 - 9th International Symposium on Multidisciplinary Studies and Innovative Technologies, Proceedings
- **DOI:** 10.1109/ISMSIT67332.2025.11268074
- **URL:** https://www.scopus.com/pages/publications/105031084139?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Anomaly Detection; Cloud-Native; Containerization; eBPF; Intrusion Detection; Kubernetes; Machine Learning; Microservices; Network Forensics; Train-Serve Skew

### Abstract

The operational deployment of machine learning (ML) based security systems in production cloud environments remains a significant challenge, often hindered by a disconnect between offline training and real-time inference known as train-serve skew. This paper presents a novel, dual-workflow, cloud-native architecture for an Intrusion Detection and Prevention System (IDPS) that bridges this gap. Our architecture builds upon a flexible ML framework from foundational research, which was validated in an offline-only proof-of-concept. The primary contributions of this paper are twofold: first, we provide a complete blueprint for orchestrating the framework as a containerized, microservice-based cluster using platforms like Kubernetes. Second, we introduce a minimal-overhead online workflow that uses high-performance, kernel-level probes and a real-time agent to replicate the feature-rich vectors required for accurate detection, thus solving the train-serve skew problem. This dual-workflow design separates low-latency real-time detection from deep offline analysis, which leverages the foundational two-stage ML pipeline and context-aware capture tools. This work provides a validated blueprint for an effective IDPS that achieves the scalability, resilience, and maintainability required for a modern cloud security service.  © 2025 IEEE.

## 04 — Title Screening

**Title:** A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach
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
