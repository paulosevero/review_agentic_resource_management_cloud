---
id: "paper-1491"
title: "Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL"
authors: ["Chinta, Pratima", "Naidu, Gokul", "Manjunatha, B.", "Ponnath, Anand"]
year: 2025
venue: "2025 IEEE International Conference on Omni-Layer Intelligent Systems, COINS 2025"
venue_type: "conference"
doi: "10.1109/COINS65080.2025.11125795"
url: "https://www.scopus.com/pages/publications/105016145843?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Cloud Cost Data insights", "Generative AI", "Large Language Models", "Natural language processing", "Text-to-SQL"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "Out of scope"

---

# paper-1491 — Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL

## Metadata

- **Authors:** Chinta, Pratima and Naidu, Gokul and Manjunatha, B. and Ponnath, Anand
- **Year:** 2025
- **Venue:** 2025 IEEE International Conference on Omni-Layer Intelligent Systems, COINS 2025
- **DOI:** 10.1109/COINS65080.2025.11125795
- **URL:** https://www.scopus.com/pages/publications/105016145843?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud Cost Data insights; Generative AI; Large Language Models; Natural language processing; Text-to-SQL

### Abstract

Modern enterprises increasingly leverage public cloud services to host application workloads with underlying cloud components, service tiers, and associated costs. These usage-based charging models introduce complexity. This necessitates the analysis of substantial data volumes to derive valuable insights. In this paper, we aim to address the challenge of enabling business and financial stakeholders to efficiently interpret cloud cost data and its trends without SQL expertise. We present an AI-powered system built on the DSPy framework that translates natural language questions into SQL queries using an enterprise-grade Large Language Model (LLM), delivering context-aware and desired responses. Existing dashboards and NLP approaches rely on rule-based parsing, requiring predefined data schemas and manual configuration. DSPy also uses these schemas but enhances flexibility by adapting them through structured pipelines and multi-step reasoning to improve accuracy. To train and evaluate our model, we augment a small dataset of question-SQL pairs through LLM-based generation and manual refinement. Additionally, we develop a custom recommendation engine using search-based techniques in Python to identify and disambiguate field names and values for both users and the LLM. Our system achieves 90% execution accuracy on our dataset, which indicates that the generated SQL queries return correct results when executed on the target database. These results demonstrate the effectiveness of prompt-tuned LLMs and in-context learning in providing a scalable, accessible solution for enterprise data analysis, ultimately enhancing decision-making in financial management.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
