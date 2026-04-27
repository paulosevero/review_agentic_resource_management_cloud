---
id: "paper-2031"
title: "Automated Lifting for Cloud Infrastructure-as-Code Programs"
authors: ["Peng, Jingjia", "Qiu, Yiming", "Kon, Patrick Tser Jern", "Zhao, Pinhan", "Huang, Yibo", "Guo, Zheng", "Wang, Xinyu", "Chen, Ang"]
year: 2025
venue: "Proceedings - 2025 IEEE/ACM International Workshop on Cloud Intelligence and AIOps, AIOps 2025"
venue_type: "conference"
doi: "10.1109/AIOps66738.2025.00007"
url: "https://www.scopus.com/pages/publications/105009460224?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4--9"
keywords: ["AIOps", "Cloud Management", "Infrastructure-as-Code", "Program Lifting", "Reverse Engineering"]
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

# paper-2031 — Automated Lifting for Cloud Infrastructure-as-Code Programs

## Metadata

- **Authors:** Peng, Jingjia and Qiu, Yiming and Kon, Patrick Tser Jern and Zhao, Pinhan and Huang, Yibo and Guo, Zheng and Wang, Xinyu and Chen, Ang
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE/ACM International Workshop on Cloud Intelligence and AIOps, AIOps 2025
- **DOI:** 10.1109/AIOps66738.2025.00007
- **URL:** https://www.scopus.com/pages/publications/105009460224?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4--9
- **Language:** English
- **Keywords:** AIOps; Cloud Management; Infrastructure-as-Code; Program Lifting; Reverse Engineering

### Abstract

Infrastructure-as-code (IaC) is reshaping how cloud resources are managed. IaC users write high-level programs to define their desired infrastructure, and the underlying IaC platforms automatically deploy the constituent resources into the cloud. While proven powerful at creating greenfield deployments (i.e., deployments from scratch), existing IaC platforms provide limited support for managing brownfield infrastructure (i.e., existing, non-IaC deployments). This hampers migration from legacy management approaches to an IaC workflow and hinders wider IaC adoption. Managing brownfield deployments requires techniques to lift low-level cloud states and translate them into corresponding IaC programs - the reversal of the regular deployment process. Existing tools rely heavily on rule-based reverse engineering, which suffers from the lack of automation, limited resource coverage, and prevalence of errors. In this work, we lay out the vision for Lilac, an approach that frees IaC lifting from extensive manual engineering. Lilac brings the best of both worlds: leveraging LLMs to automate lifting rule extraction, coupled with symbolic methods to provide correctness assurance. We envision that Lilac would enable the construction of an automated and provider-agnostic lifting tool with high coverage and accuracy. A prototype of LILAC is available here.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Automated Lifting for Cloud Infrastructure-as-Code Programs

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Automated Lifting for Cloud Infrastructure-as-Code Programs
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Automated Lifting for Cloud Infrastructure-as-Code Programs
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
