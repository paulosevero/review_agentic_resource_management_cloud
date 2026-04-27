---
id: "paper-2744"
title: "ServLessSense: Serverless Smell Detection Tool"
authors: ["Perera, Hasini Sumalee", "Codabux, Zadia", "Palomba, Fabio"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-3-032-04403-7_3"
url: "https://www.scopus.com/pages/publications/105016155413?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "21--28"
keywords: ["Code Smell Detection", "Refactoring", "Serverless Computing"]
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

# paper-2744 — ServLessSense: Serverless Smell Detection Tool

## Metadata

- **Authors:** Perera, Hasini Sumalee and Codabux, Zadia and Palomba, Fabio
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-3-032-04403-7_3
- **URL:** https://www.scopus.com/pages/publications/105016155413?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 21--28
- **Language:** English
- **Keywords:** Code Smell Detection; Refactoring; Serverless Computing

### Abstract

Serverless computing has gained widespread adoption due to its scalability, cost-efficiency, and abstraction of infrastructure management. However, the shift toward event-driven, function-based architectures introduces new code quality challenges and development practices that differ from traditional paradigms. While recent research has identified serverless-specific bad practices commonly referred to as “smells,” there remains a lack of automated tools to support their detection and remediation. This paper presents ServLessSense, a tool designed to detect code smells automatically in serverless applications written in JavaScript and TypeScript. Built using a custom ESLint plugin, ServLessSense identifies five serverless-specific smells, provides visualizations through an interactive dashboard, and integrates Large Language Models to offer automated refactoring suggestions. We evaluated the precision and recall of the tool using five open-source serverless applications and conducted a pilot survey study to assess its potential usefulness from the practitioners’ perspective. The results indicate that ServLessSense is helpful in detecting serverless-specific smells and generating refactoring suggestions. The survey participants showed an overall favorable perspective towards ServLessSense. Tool & Data: https://doi.org/10.5281/zenodo.15477162 Demo Video: https://youtu.be/3WDCiqBpQ9c © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

## 04 — Title Screening

**Title:** ServLessSense: Serverless Smell Detection Tool

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ServLessSense: Serverless Smell Detection Tool
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ServLessSense: Serverless Smell Detection Tool
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
