---
id: "paper-1157"
title: "ECO-LLM: LLM-based Edge Cloud Optimization"
authors: ["Rao, Kunal", "Coviello, Giuseppe", "Benedetti, Priscilla", "De Vita, Ciro Giuseppe", "Mellone, Gennaro", "Chakradhar, Srimat"]
year: 2024
venue: "AI4Sys 2024 - Proceedings of the 2024 Workshop on AI For Systems, Part of:  HPDC 2024 - 33rd International Symposium on High-Performance Parallel and Distributed Computing"
venue_type: "conference"
doi: "10.1145/3660605.3660941"
url: "https://www.scopus.com/pages/publications/85204973236?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "7--12"
keywords: ["cloud computing", "customization", "edge computing", "generative artificial intelligence (GenAI)", "large language models (LLM)", "machine learning (ML)", "optimization", "video analytics"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-1157 — ECO-LLM: LLM-based Edge Cloud Optimization

## Metadata

- **Authors:** Rao, Kunal and Coviello, Giuseppe and Benedetti, Priscilla and De Vita, Ciro Giuseppe and Mellone, Gennaro and Chakradhar, Srimat
- **Year:** 2024
- **Venue:** AI4Sys 2024 - Proceedings of the 2024 Workshop on AI For Systems, Part of:  HPDC 2024 - 33rd International Symposium on High-Performance Parallel and Distributed Computing
- **DOI:** 10.1145/3660605.3660941
- **URL:** https://www.scopus.com/pages/publications/85204973236?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 7--12
- **Language:** English
- **Keywords:** cloud computing; customization; edge computing; generative artificial intelligence (GenAI); large language models (LLM); machine learning (ML); optimization; video analytics

### Abstract

AI/ML techniques have been used to solve systems problems, but their applicability to customize solutions on-the-fly has been limited. Traditionally, any customization required manually changing the AI/ML model or modifying the code, configuration parameters, application settings, etc. This incurs too much time and effort, and is very painful. In this paper, we propose a novel technique using Generative Artificial Intelligence (GenAI) technology, wherein instructions can be provided in natural language and actual code to handle any customization is automatically generated, integrated and applied on-the-fly. Such capability is extremely powerful since it makes customization of application settings or solution techniques super easy. Specifically, we propose ECO-LLM (LLM-based Edge Cloud Optimization), which leverages Large Language Models (LLM) to dynamically adjust placement of application tasks across edge and cloud computing tiers, in response to changes in application workload, such that insights are delivered quickly with low cost of operation (systems problem). Our experiments with real-world video analytics applications i.e. face recognition, human attributes detection and license plate recognition show that ECO-LLM is able to automatically generate code on-the-fly and adapt placement of application tasks across edge and cloud computing tiers. We note that the trigger workload (to switch between edge and cloud) for ECO-LLM is exactly the same as the baseline (manual) and actual placement performed by ECO-LLM is only slightly different i.e. on average (across 2 days) only 1.45% difference in human attributes detection and face recognition, and 1.11% difference in license plate recognition. Although we tackle this specific systems problem in this paper, our proposed GenAI-based technique is applicable to solve other systems problems too. © 2024 is held by the owner/author(s).

## 04 — Title Screening

**Title:** ECO-LLM: LLM-based Edge Cloud Optimization

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** ECO-LLM: LLM-based Edge Cloud Optimization
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** ECO-LLM: LLM-based Edge Cloud Optimization
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
