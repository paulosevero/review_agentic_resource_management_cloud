---
id: "paper-2139"
title: "Automated High-Level Code Optimization for Warehouse Performance"
authors: ["Shypula, Alexander", "Madaan, Aman", "Zeng, Yimeng", "Alon, Uri", "Gardner, Jacob", "Hashemi, Milad", "Neubig, Graham", "Ranganathan, Parthasarathy", "Bastani, Osbert", "Yazdanbakhsh, Amir"]
year: 2025
venue: "IEEE Micro"
venue_type: "journal"
doi: "10.1109/MM.2025.3590033"
url: "https://www.scopus.com/pages/publications/105011157266?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "60--71"
keywords: ["Artificial intelligence", "C++ (programming language)", "Computer architecture", "Optimization", "Semantics", "Statistical tests", "Warehouses", "Architecture research", "Code optimization", "Code semantics", "Moore Law", "Optimisations", "Optimizing programs", "Performance", "Program performance", "Source optimization", "Warehouse performance", "Codes (symbols)"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2139 — Automated High-Level Code Optimization for Warehouse Performance

## Metadata

- **Authors:** Shypula, Alexander and Madaan, Aman and Zeng, Yimeng and Alon, Uri and Gardner, Jacob and Hashemi, Milad and Neubig, Graham and Ranganathan, Parthasarathy and Bastani, Osbert and Yazdanbakhsh, Amir
- **Year:** 2025
- **Venue:** IEEE Micro
- **DOI:** 10.1109/MM.2025.3590033
- **URL:** https://www.scopus.com/pages/publications/105011157266?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 60--71
- **Language:** English
- **Keywords:** Artificial intelligence; C++ (programming language); Computer architecture; Optimization; Semantics; Statistical tests; Warehouses; Architecture research; Code optimization; Code semantics; Moore Law; Optimisations; Optimizing programs; Performance; Program performance; Source optimization; Warehouse performance; Codes (symbols)

### Abstract

In the twilight of Moore’s law, optimizing program performance has emerged as a central focus in computer architecture research. Yet, high-level source optimization remains challenging due to the intricate nature of understanding code semantics. Our approach unifies machine learning techniques with established insights and tools from computer architecture to tackle the inherent challenges of high-level optimization. In this work, we introduce a framework that harnesses large language models (LLMs) for high-level program optimization. We curate a dataset of competitive C++ submissions, each accompanied by extensive unit tests to capture performance-improving patterns. To mitigate the variability of performance measurements, we develop an evaluation harness using the gem5 full-system simulator. Our results show a mean speedup of 6.86, outperforming the average human optimization of 3.66×. We also give an overview of subsequent work in this space, describing how LLM-driven optimization enables autonomously applying performance-improving edits across billions of lines of code in Google data centers. © 1981-2012 IEEE.

## 04 — Title Screening

**Title:** Automated High-Level Code Optimization for Warehouse Performance

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Automated High-Level Code Optimization for Warehouse Performance
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Automated High-Level Code Optimization for Warehouse Performance
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
