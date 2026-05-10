---
id: "paper-2235"
title: "Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions"
authors: ["Vamja, Tirth", "Ray, Kaustabha", "George, Felix", "Devi, Umamaheswari"]
year: 2025
venue: "2025 5th International Conference on AI-ML-Systems, AIMLSystems 2025"
venue_type: "conference"
doi: "10.1109/AIMLSYSTEMS67835.2025.11330349"
url: "https://www.scopus.com/pages/publications/105034890127?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "135--143"
keywords: ["Computer hardware", "Electric power utilization", "Graphics processing unit", "Green computing", "Information management", "Partitions (building)", "Power management", "Program processors", "Cloud data centers", "Data driven", "Efficient power managements", "Machine-learning", "Model method", "Partition levels", "Power", "Power estimations", "Power modeling", "Reducing costs", "Aggregates"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2235 — Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions

## Metadata

- **Authors:** Vamja, Tirth and Ray, Kaustabha and George, Felix and Devi, Umamaheswari
- **Year:** 2025
- **Venue:** 2025 5th International Conference on AI-ML-Systems, AIMLSystems 2025
- **DOI:** 10.1109/AIMLSYSTEMS67835.2025.11330349
- **URL:** https://www.scopus.com/pages/publications/105034890127?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 135--143
- **Language:** English
- **Keywords:** Computer hardware; Electric power utilization; Graphics processing unit; Green computing; Information management; Partitions (building); Power management; Program processors; Cloud data centers; Data driven; Efficient power managements; Machine-learning; Model method; Partition levels; Power; Power estimations; Power modeling; Reducing costs; Aggregates

### Abstract

Efficient power management in cloud data centers is essential for reducing costs, enhancing performance, and minimizing environmental impact. GPUs, critical for tasks like machine learning (ML) and GenAI, are major contributors to power consumption. NVIDIA's Multi-Instance GPU (MIG) technology improves GPU utilization by enabling isolated partitions with per-partition resource tracking, facilitating GPU sharing by multiple tenants. However, accurately apportioning GPU power consumption among MIG instances, which is required for proper energy and carbon accounting and management, remains challenging due to lack of hardware support. This paper addresses this challenge by developing software methods to estimate power usage per MIG partition. We find that light-weight methods with good accuracy can be difficult to construct and hence explore the use of ML-based power models to enable accurate, partition-level power estimation. Our exploration reveals that a single generic offline power model or modeling method is not applicable across diverse workloads, especially with concurrent MIG usage, and that workload-specific models constructed using partition-level utilization metrics of workloads under execution can significantly improve accuracy. We also propose scaling the MIG power predicted by the models using total measured GPU power, when available, to eliminate aggregate error and reduce error in per-MIG estimations. Using NVIDIA A100 GPUs, we demonstrate and evaluate our approach for accurate partition-level power estimation for workloads including matrix multiplication and Large Language Model inference. © 2025 IEEE.

## 04 — Title Screening

**Title:** Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions
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
