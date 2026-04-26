---
id: "paper-1232"
title: "Migrating Existing Container Workload to Kubernetes - LLM Based Approach and Evaluation"
authors: ["Ueno, Masaru", "Uchiumi, Tetsuya"]
year: 2024
venue: "Proceedings - 2024 IEEE International Conference on Software Maintenance and Evolution, ICSME 2024"
venue_type: "conference"
doi: "10.1109/ICSME58944.2024.00074"
url: "https://www.scopus.com/pages/publications/85215505532?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "701--706"
keywords: ["Configuration management", "Kubernetes", "LLM", "program synthesis"]
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

# paper-1232 — Migrating Existing Container Workload to Kubernetes - LLM Based Approach and Evaluation

## Metadata

- **Authors:** Ueno, Masaru and Uchiumi, Tetsuya
- **Year:** 2024
- **Venue:** Proceedings - 2024 IEEE International Conference on Software Maintenance and Evolution, ICSME 2024
- **DOI:** 10.1109/ICSME58944.2024.00074
- **URL:** https://www.scopus.com/pages/publications/85215505532?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 701--706
- **Language:** English
- **Keywords:** Configuration management; Kubernetes; LLM; program synthesis

### Abstract

Although Kubernetes has become a widespread open-source system that automates the management of containerized applications, its complexity can be a significant barrier, particularly for application developers unfamiliar with it. One approach employs large language models (LLMs) to assist developers in generating Kubernetes manifests; however it is currently impossible to determine whether the output satisfies given specifications and is comprehensible. In this study, we proposed a benchmarking method for evaluating the effectiveness of LLMs in synthesizing manifests, using the Compose specification - a standard widely adopted by application developers - as input. The proposed benchmarking method revealed that LLMs generally produce accurate results that compensate for simple specification gaps. However, we also observed that inline comments for readability were often omitted, and completion accuracy was low for atypical inputs with unclear intentions.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Migrating Existing Container Workload to Kubernetes - LLM Based Approach and Evaluation

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Migrating Existing Container Workload to Kubernetes - LLM Based Approach and Evaluation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Migrating Existing Container Workload to Kubernetes - LLM Based Approach and Evaluation
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
