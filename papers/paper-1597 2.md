---
id: "paper-1597"
title: "Bringing GenAI awareness to Workload Management (Industry Track)"
authors: ["Govindarajan, Kavya", "Naik, Priyanka", "Goel, Seep", "Kumar, Ashok Pon", "Jayachandran, Praveen"]
year: 2025
venue: "Middleware Industrial Track 2025 - Proceedings of the Middleware Industrial Track 2025"
venue_type: "conference"
doi: "10.1145/3721463.3772058"
url: "https://www.scopus.com/pages/publications/105029838428?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "8--14"
keywords: ["Cluster Scheduling", "LLM Tuning", "Resource Allocation"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1597 — Bringing GenAI awareness to Workload Management (Industry Track)

## Metadata

- **Authors:** Govindarajan, Kavya and Naik, Priyanka and Goel, Seep and Kumar, Ashok Pon and Jayachandran, Praveen
- **Year:** 2025
- **Venue:** Middleware Industrial Track 2025 - Proceedings of the Middleware Industrial Track 2025
- **DOI:** 10.1145/3721463.3772058
- **URL:** https://www.scopus.com/pages/publications/105029838428?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 8--14
- **Language:** English
- **Keywords:** Cluster Scheduling; LLM Tuning; Resource Allocation

### Abstract

With the rise of Large Language Models, enterprises today, use fine-tuning to adopt models for their specific usecases. Fine tuning jobs are compute intensive, and hence, while deploying such jobs, a scheduler must efficiently allocate the resources of accelerators such as GPUs. However, cluster orchestrators such as Kubernetes do not consider accelerators as first class citizens, and hence, are not equipped to ensure optimized resource allocations for fine tuning jobs. To address this issue, in this paper, we propose KAM, a Generative AI (GenAI)-aware workload manager. KAM provides users with the flexibility to choose and scale the amount of GPU allocations for a job with the aim of reducing its makespan and improve GPU utilization. It is light weight and works alongside existing schedulers. Experimental results show that KAM reduces job wait time by 3.5× and improves makespan by 1.6× on real workload traces, thereby making it a valuable addition to enterprise GenAI deployments. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Bringing GenAI awareness to Workload Management (Industry Track)

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Bringing GenAI awareness to Workload Management (Industry Track)
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Bringing GenAI awareness to Workload Management (Industry Track)
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
