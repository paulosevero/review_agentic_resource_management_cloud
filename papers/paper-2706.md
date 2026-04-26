---
id: "paper-2706"
title: "AsynDBT: asynchronous distributed bilevel tuning for efficient in-context learning with large language models"
authors: ["Ma, Hui", "Dou, Shaoyu", "Liu, Ya", "Xing, Fei", "Feng, Li", "Pi, Feng"]
year: 2026
venue: "Scientific Reports"
venue_type: "journal"
doi: "10.1038/s41598-026-39582-5"
url: "https://www.scopus.com/pages/publications/105033711588?origin=resultslist"
publisher: "Nature Research"
pages: ""
keywords: ["Bilevel optimization", "Federated learning", "In-context learning", "Large language models"]
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

# paper-2706 — AsynDBT: asynchronous distributed bilevel tuning for efficient in-context learning with large language models

## Metadata

- **Authors:** Ma, Hui and Dou, Shaoyu and Liu, Ya and Xing, Fei and Feng, Li and Pi, Feng
- **Year:** 2026
- **Venue:** Scientific Reports
- **DOI:** 10.1038/s41598-026-39582-5
- **URL:** https://www.scopus.com/pages/publications/105033711588?origin=resultslist
- **Publisher:** Nature Research
- **Pages:** 
- **Language:** English
- **Keywords:** Bilevel optimization; Federated learning; In-context learning; Large language models

### Abstract

With the rapid development of large language models (LLMs), an increasing number of applications leverage cloud-based LLM APIs to reduce usage costs. However, since cloud-based models’ parameters and gradients are agnostic, users have to manually or use heuristic algorithms to adjust prompts for intervening LLM outputs, which requiring costly optimization procedures. In-context learning (ICL) has recently emerged as a promising paradigm that enables LLMs to adapt to new tasks using examples provided within the input, eliminating the need for parameter updates. Nevertheless, the advancement of ICL is often hindered by the lack of high-quality data, which is often sensitive and different to share. Federated learning (FL) offers a potential solution by enabling collaborative training of distributed LLMs while preserving data privacy. Despite this issues, previous FL approaches that incorporate ICL have struggled with severe straggler problems and challenges associated with heterogeneous non-identically data. To address these problems, we propose an asynchronous distributed bilevel tuning (AsynDBT) algorithm that optimizes both in-context learning samples and prompt fragments based on the feedback from the LLM, thereby enhancing downstream task performance. Benefiting from its distributed architecture, AsynDBT provides privacy protection and adaptability to heterogeneous computing environments. Furthermore, we present a theoretical analysis establishing the convergence guarantees of the proposed algorithm. Extensive experiments conducted on multiple benchmark datasets demonstrate the effectiveness and efficiency of AsynDBT. © The Author(s) 2026.

## 04 — Title Screening

**Title:** AsynDBT: asynchronous distributed bilevel tuning for efficient in-context learning with large language models

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** AsynDBT: asynchronous distributed bilevel tuning for efficient in-context learning with large language models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** AsynDBT: asynchronous distributed bilevel tuning for efficient in-context learning with large language models
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
