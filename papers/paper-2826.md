---
id: "paper-2826"
title: "Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability"
authors: ["Wang, Peng", "Qi, Kaiyuan", "Zhen, Feng", "Yan, Bingheng", "Guo, Tao"]
year: 2026
venue: "Concurrency and Computation: Practice and Experience"
venue_type: "journal"
doi: "10.1002/cpe.70705"
url: "https://www.scopus.com/pages/publications/105035843575?origin=resultslist"
publisher: "John Wiley and Sons Ltd"
pages: ""
keywords: ["cross-architecture code migration", "explainable software transformation", "large language models", "multi-ISA optimization", "QA-driven interaction"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: ""
    human_justification: ""

---

# paper-2826 — Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability

## Metadata

- **Authors:** Wang, Peng and Qi, Kaiyuan and Zhen, Feng and Yan, Bingheng and Guo, Tao
- **Year:** 2026
- **Venue:** Concurrency and Computation: Practice and Experience
- **DOI:** 10.1002/cpe.70705
- **URL:** https://www.scopus.com/pages/publications/105035843575?origin=resultslist
- **Publisher:** John Wiley and Sons Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** cross-architecture code migration; explainable software transformation; large language models; multi-ISA optimization; QA-driven interaction

### Abstract

Cross-architecture code migration has become essential as data centers transition from homogeneous x86 systems to heterogeneous “one-cloud, multi-chip” infrastructures that include ARM64, RISC-V, and domestic processors. Traditional approaches, such as manual refactoring and rule-based rewriting, face challenges in maintaining semantic correctness, scalability, and explainability. This paper presents an interactive, question-answering (QA)-driven framework that uses a frozen large language model (LLM) as a semantic reasoning engine. The framework combines static analysis, AST-based semantic-distance modeling, and a self-evolving rule base for validated transformations, ensuring transparency, explainability, and architecture-aware migration. It supports multiple languages (C++, Python, Java) and ISAs (x86, ARM64, RISC-V) without the need for fine-tuning the LLM. Evaluation on 30 real-world codebases shows an average migration accuracy of 92.4%, approaching expert-level performance (95.1%), with a 4.2× reduction in migration errors and significant reduction in developer time (from 20–25 h to 8 h). These results demonstrate that the QA-driven, LLM-based migration framework significantly improves efficiency, accuracy, and scalability. © 2026 John Wiley & Sons Ltd.

## 04 — Title Screening

**Title:** Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
