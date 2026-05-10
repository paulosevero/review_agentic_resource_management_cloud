---
id: "paper-953"
title: "Characterization of Large Language Model Development in the Datacenter"
authors: ["Hu, Qinghao", "Ye, Zhisheng", "Wang, Zerui", "Wang, Guoteng", "Zhang, Meng", "Chen, Qiaoling", "Sun, Peng", "Lin, Dahua", "Wang, Xiaolin", "Luo, Yingwei", "Wen, Yonggang", "Zhang, Tianwei"]
year: 2024
venue: "Proceedings of the 21st USENIX Symposium on Networked Systems Design and Implementation, NSDI 2024"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/85188821548?origin=resultslist"
publisher: "USENIX Association"
pages: "709--729"
keywords: ["Computational linguistics", "Deep learning", "Systems analysis", "Characterization studies", "Datacenter", "Hardware failures", "Language model", "Large-scale clusters", "Model development", "Non-trivial", "Parallelization strategies", "Performance", "Resources utilizations", "Fault tolerance"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Out of scope"

---

# paper-953 — Characterization of Large Language Model Development in the Datacenter

## Metadata

- **Authors:** Hu, Qinghao and Ye, Zhisheng and Wang, Zerui and Wang, Guoteng and Zhang, Meng and Chen, Qiaoling and Sun, Peng and Lin, Dahua and Wang, Xiaolin and Luo, Yingwei and Wen, Yonggang and Zhang, Tianwei
- **Year:** 2024
- **Venue:** Proceedings of the 21st USENIX Symposium on Networked Systems Design and Implementation, NSDI 2024
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/85188821548?origin=resultslist
- **Publisher:** USENIX Association
- **Pages:** 709--729
- **Language:** English
- **Keywords:** Computational linguistics; Deep learning; Systems analysis; Characterization studies; Datacenter; Hardware failures; Language model; Large-scale clusters; Model development; Non-trivial; Parallelization strategies; Performance; Resources utilizations; Fault tolerance

### Abstract

Large Language Models (LLMs) have presented impressive performance across several transformative tasks. However, it is non-trivial to efficiently utilize large-scale cluster resources to develop LLMs, often riddled with numerous challenges such as frequent hardware failures, intricate parallelization strategies, and imbalanced resource utilization. In this paper, we present an in-depth characterization study of a six-month LLM development workload trace collected from our GPU datacenter Acme. Specifically, we investigate discrepancies between LLMs and prior task-specific Deep Learning (DL) workloads, explore resource utilization patterns, and identify the impact of various job failures. Our analysis summarizes hurdles we encountered and uncovers potential opportunities to optimize systems tailored for LLMs. Furthermore, we introduce our system efforts: (1) fault-tolerant pretraining, which enhances fault tolerance through LLM-involved failure diagnosis and automatic recovery. (2) decoupled scheduling for evaluation, which achieves timely performance feedback via trial decomposition and scheduling optimization. © 2024 Proceedings of the 21st USENIX Symposium on Networked Systems Design and Implementation, NSDI 2024. All rights reserved.

## 04 — Title Screening

**Title:** Characterization of Large Language Model Development in the Datacenter

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Characterization of Large Language Model Development in the Datacenter
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Characterization of Large Language Model Development in the Datacenter
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
