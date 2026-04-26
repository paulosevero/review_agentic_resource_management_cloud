---
id: "paper-1527"
title: "LLM-Aided In-Field Workload Generation for Detecting Silent Data Corruptions at Scale"
authors: ["Domanski, Peter", "Sahoo, Deepesh", "Ortega, Eduardo", "Firouzi, Farshad", "Chakrabarty, Krishnendu"]
year: 2025
venue: "Proceedings - International Test Conference"
venue_type: "conference"
doi: "10.1109/ITC58126.2025.00018"
url: "https://www.scopus.com/pages/publications/105024530250?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "121--130"
keywords: ["Data reliability", "Datacenter", "Error-detection mechanism", "Field testing", "In-field", "Large scale data", "Manufacturing fields", "Silent data corruptions", "Test case", "Voltage droop", "Workload generation", "Chemical detection"]
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

# paper-1527 — LLM-Aided In-Field Workload Generation for Detecting Silent Data Corruptions at Scale

## Metadata

- **Authors:** Domanski, Peter and Sahoo, Deepesh and Ortega, Eduardo and Firouzi, Farshad and Chakrabarty, Krishnendu
- **Year:** 2025
- **Venue:** Proceedings - International Test Conference
- **DOI:** 10.1109/ITC58126.2025.00018
- **URL:** https://www.scopus.com/pages/publications/105024530250?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 121--130
- **Language:** English
- **Keywords:** Data reliability; Datacenter; Error-detection mechanism; Field testing; In-field; Large scale data; Manufacturing fields; Silent data corruptions; Test case; Voltage droop; Workload generation; Chemical detection

### Abstract

Computational integrity is crucial in large-scale data centers where Silent Data Corruptions (SDCs) pose a growing reliability challenge. SDCs can lead to incorrect computation results not captured by traditional error detection mechanisms, making their detection and mitigation essential. However, existing post-manufacturing and in-field testing methods, such as opportunistic and ripple testing, face significant scalability challenges due to high computational costs and test times. We propose an LLM-aided approach for generating targeted test cases to detect SDCs. As a case study, we focus on the functional blocks of a RISC-V CV32E40P processor core. Our method generates targeted test cases that maximize voltage droops in given hardware modules, such as functional units, increasing the likelihood of triggering SDCs in-field. Additionally, our approach is architecture-aware and layout-aware, enhancing fault activation and enabling automated optimization of generated test cases. Experimental evaluations demonstrate that the proposed method significantly improves SDC detection efficiency by reducing the number of required test cases while preserving high test coverage. Compared to commonly used test cases, the proposed approach increases average voltage droops by up to 38%. By integrating LLM-aided test case generation, the proposed approach achieves voltage droops of up to 9% relative to the supply voltage, improving the effectiveness of in-field SDC detection and mitigation strategies.  © 2025 IEEE.

## 04 — Title Screening

**Title:** LLM-Aided In-Field Workload Generation for Detecting Silent Data Corruptions at Scale

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LLM-Aided In-Field Workload Generation for Detecting Silent Data Corruptions at Scale
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LLM-Aided In-Field Workload Generation for Detecting Silent Data Corruptions at Scale
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
