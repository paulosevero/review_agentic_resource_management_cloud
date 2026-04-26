---
id: "paper-2225"
title: "Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM"
authors: ["Trappen, Tim", "Ke\u00dfler, Robert", "Pabel, Roland", "Achter, Viktor", "Wesner, Stefan"]
year: 2025
venue: "MIND 2025 - Proceedings of the 1st International Workshop on Next-Gen Middleware for MLOps in Distributed Systems"
venue_type: "conference"
doi: "10.1145/3774902.3776632"
url: "https://www.scopus.com/pages/publications/105026748894?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "13--18"
keywords: ["high-performance computing", "inference", "large language model"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2225 — Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM

## Metadata

- **Authors:** Trappen, Tim and Keßler, Robert and Pabel, Roland and Achter, Viktor and Wesner, Stefan
- **Year:** 2025
- **Venue:** MIND 2025 - Proceedings of the 1st International Workshop on Next-Gen Middleware for MLOps in Distributed Systems
- **DOI:** 10.1145/3774902.3776632
- **URL:** https://www.scopus.com/pages/publications/105026748894?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 13--18
- **Language:** English
- **Keywords:** high-performance computing; inference; large language model

### Abstract

Due to rising demands for Artificial Inteligence (AI) inference, especially in higher education, novel solutions utilising existing infrastructure are emerging. The utilisation of High-Performance Computing (HPC) has become a prevalent approach for the implementation of such solutions. However, the classical operating model of HPC does not adapt well to the requirements of synchronous, user-facing dynamic AI application workloads. In this paper, we propose our solution that serves LLMs by integrating vLLM, Slurm and Kubernetes on the supercomputer RAMSES. The initial benchmark indicates that the proposed architecture scales efficiently for 100, 500 and 1000 concurrent requests, incurring only an overhead of approximately 500 ms in terms of end-to-end latency.  © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM
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
