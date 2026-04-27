---
id: "paper-2921"
title: "Service reliability of intelligent computing cluster systems for large language models"
authors: ["Zhang, Hanxiao", "Zhang, Chen", "Wang, Yingdong", "Li, Yan-Fu"]
year: 2026
venue: "Reliability Engineering and System Safety"
venue_type: "journal"
doi: "10.1016/j.ress.2026.112484"
url: "https://www.scopus.com/pages/publications/105032108262?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Data parallelism", "Distributed computing systems", "Parallel training", "Pipeline parallelism", "System reliability"]
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

# paper-2921 — Service reliability of intelligent computing cluster systems for large language models

## Metadata

- **Authors:** Zhang, Hanxiao and Zhang, Chen and Wang, Yingdong and Li, Yan-Fu
- **Year:** 2026
- **Venue:** Reliability Engineering and System Safety
- **DOI:** 10.1016/j.ress.2026.112484
- **URL:** https://www.scopus.com/pages/publications/105032108262?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Data parallelism; Distributed computing systems; Parallel training; Pipeline parallelism; System reliability

### Abstract

Intelligent computing cluster system (ICCS) is a distributed computing infrastructure designed for training large language models (LLMs). Most of the existing reliability works on computing systems has predominantly focued on conventional architectures, such as generic data center networks and conventional cloud infrastructures. To our knowledge, the service reliability of new computing infrastructure, ICCS, has not been studied in literature. This paper bridges the gaps between academic research and industrial practice by developing a comprehensive service reliability framework for ICCS on LLM. The service reliability is defined from the perspective of the execution of parallelized training, taking into account the hybrid parallelism strategy of pipeline and data parallelism. The reliability assessment approach is developed concerning the inherent uncertainies on GPU performance. Meanwhile, to improve the service reliability metric, a reliability optimization problem is constructed to derive an optimal parallelism strategy, called RDpipe. The computational experiments are conducted to analyze the service reliability facing the different environmental settings. The results show that the derived RDpipe strategy has higher reliability and more stable performance than other classical parallelism strategies. © 2026 Elsevier Ltd.

## 04 — Title Screening

**Title:** Service reliability of intelligent computing cluster systems for large language models

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Service reliability of intelligent computing cluster systems for large language models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Service reliability of intelligent computing cluster systems for large language models
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
