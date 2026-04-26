---
id: "paper-2000"
title: "Performance Evaluation of SLMs on Edge Devices"
authors: ["Oguchi, Masato"]
year: 2025
venue: "2025 IEEE 12th International Conference on Communications and Networking, ComNet 2025"
venue_type: "conference"
doi: "10.1109/ComNet68251.2025.11325519"
url: "https://www.scopus.com/pages/publications/105033143961?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["edge computing", "edge device", "LLM", "performance evaluation", "privacy protection", "SLM"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2000 — Performance Evaluation of SLMs on Edge Devices

## Metadata

- **Authors:** Oguchi, Masato
- **Year:** 2025
- **Venue:** 2025 IEEE 12th International Conference on Communications and Networking, ComNet 2025
- **DOI:** 10.1109/ComNet68251.2025.11325519
- **URL:** https://www.scopus.com/pages/publications/105033143961?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; edge device; LLM; performance evaluation; privacy protection; SLM

### Abstract

As large language models (LLMs) become increasingly integrated into practical applications, concerns about data privacy have intensified, particularly regarding the handling of sensitive personal data on edge devices. This study investigates the feasibility of executing small language models (SLMs) directly on edge devices to preserve privacy without offloading data to cloud servers. Three recent SLMs - Llama 3.2 (Meta), Phi-4-mini (Microsoft), and Gemma 3n (Google) - were evaluated on two NVIDIA Jetson devices: the resource-limited Jetson Nano and the more powerful Jetson AGX Orin. Their performance was compared against a GPU-equipped server. Experimental results show that while low-end devices struggle to meet computational demands, high-end edge devices can execute SLMs with acceptable performance for non-real-time tasks. All three SLMs also supported multilingual input/output, including Japanese. These findings suggest that privacy-aware AI applications using on-device SLMs are feasible under certain conditions. The results highlight the need for further optimization of both models and hardware to enable broader deployment.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Performance Evaluation of SLMs on Edge Devices

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Performance Evaluation of SLMs on Edge Devices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Performance Evaluation of SLMs on Edge Devices
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
