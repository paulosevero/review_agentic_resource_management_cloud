---
id: "paper-923"
title: "Ymir: A Scheduler for Foundation Model Fine-tuning Workloads in Datacenters"
authors: ["Gao, Wei", "Zhuang, Weiming", "Li, Minghao", "Sun, Peng", "Wen, Yonggang", "Zhang, Tianwei"]
year: 2024
venue: "Proceedings of the International Conference on Supercomputing"
venue_type: "conference"
doi: "10.1145/3650200.3656599"
url: "https://www.scopus.com/pages/publications/85196256698?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "259--271"
keywords: ["Cluster Management System", "Foundation Model Fine-tuning"]
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
    human_justification: "LLM as workload"

---

# paper-923 — Ymir: A Scheduler for Foundation Model Fine-tuning Workloads in Datacenters

## Metadata

- **Authors:** Gao, Wei and Zhuang, Weiming and Li, Minghao and Sun, Peng and Wen, Yonggang and Zhang, Tianwei
- **Year:** 2024
- **Venue:** Proceedings of the International Conference on Supercomputing
- **DOI:** 10.1145/3650200.3656599
- **URL:** https://www.scopus.com/pages/publications/85196256698?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 259--271
- **Language:** English
- **Keywords:** Cluster Management System; Foundation Model Fine-tuning

### Abstract

The breakthrough of foundation models makes foundation model fine-tuning (FMF) workloads prevalent in modern GPU datacenters. However, existing schedulers tailored for model training do not consider the unique characteristics of FMs, making them inefficient in handling FMF workloads. To bridge the gap, we propose Ymir, a scheduler to improve the efficiency of FMF workloads in GPU datacenters. Ymir leverages the shared FM backbone architecture to expedite FMF workloads from two aspects: (1) Ymir investigates the task transferability among different FMF workloads and automatically merges FMF workloads with the same FM into one to improve the cluster-wide efficiency via transfer learning. (2) Ymir reuses the fine-tuning runtime of FMF workloads to reduce the significant context switch overhead. We conduct 32-GPU physical experiments and 240-GPU trace-driven simulations to validate the effectiveness of Ymir. Ymir can reduce the average job completion time by up to 4.3 × compared with existing state-of-the-art schedulers. It also promotes scheduling fairness by fully exploiting the task transferability. More supplementary materials can be found on our project website https://sites.google.com/view/ymir-project.  © 2024 Owner/Author.

## 04 — Title Screening

**Title:** Ymir: A Scheduler for Foundation Model Fine-tuning Workloads in Datacenters

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Ymir: A Scheduler for Foundation Model Fine-tuning Workloads in Datacenters
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Ymir: A Scheduler for Foundation Model Fine-tuning Workloads in Datacenters
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
