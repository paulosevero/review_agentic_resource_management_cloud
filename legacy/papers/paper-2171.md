---
id: "paper-2171"
title: "TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms"
authors: ["Stojkovic, Jovan", "Zhang, Chaojie", "Goiri, \u00cd\u00f1igo", "Choukse, Esha", "Qiu, Haoran", "Fonseca, Rodrigo", "Torrellas, Josep", "Bianchini, Ricardo"]
year: 2025
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3676641.3716025"
url: "https://www.scopus.com/pages/publications/105002564863?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "1266--1281"
keywords: ["cloud datacenters", "gpus", "large language models", "power management", "thermal management"]
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
    human_justification: "LLM as workload"

---

# paper-2171 — TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms

## Metadata

- **Authors:** Stojkovic, Jovan and Zhang, Chaojie and Goiri, Íñigo and Choukse, Esha and Qiu, Haoran and Fonseca, Rodrigo and Torrellas, Josep and Bianchini, Ricardo
- **Year:** 2025
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3676641.3716025
- **URL:** https://www.scopus.com/pages/publications/105002564863?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 1266--1281
- **Language:** English
- **Keywords:** cloud datacenters; gpus; large language models; power management; thermal management

### Abstract

The rising demand for generative large language models (LLMs) poses challenges for thermal and power management in cloud datacenters. Traditional techniques are often inadequate for LLM inference due to the fine-grained, millisecond-scale execution phases, each with distinct performance, thermal, and power profiles. Additionally, LLM inference workloads are sensitive to various configuration parameters (e.g., model parallelism, size, and quantization) that involve trade-offs between performance, temperature, power, and output quality. Moreover, clouds often co-locate SaaS and IaaS workloads, each with different levels of visibility and flexibility. To address these challenges, we propose TAPAS, a thermal- and power-aware framework designed for LLM inference clusters in the cloud. TAPAS enhances cooling and power oversubscription capabilities, reducing the total cost of ownership (TCO) while effectively handling emergencies (e.g., cooling and power failures). TAPAS leverages historical temperature and power data, along with the adaptability of SaaS workloads, to: (1) efficiently place new GPU workload VMs within cooling and power constraints, (2) route LLM inference requests across SaaS VMs, and (3) reconfigure SaaS VMs to manage load spikes and emergency situations. Our evaluation on a large GPU cluster demonstrates significant reductions in thermal and power throttling events, boosting system efficiency. © 2025 ACM.

## 04 — Title Screening

**Title:** TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms
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
