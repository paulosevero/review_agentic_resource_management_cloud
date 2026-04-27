---
id: "paper-2627"
title: "Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads"
authors: ["Kaarat, Arjun", "Reddy Batthula, Venkata Jaipal", "Segall, Richard"]
year: 2026
venue: "Proceedings - 5th International Conference on Informatics and Software Engineering, IISEC 2026"
venue_type: "conference"
doi: "10.1109/IISEC69317.2026.11418430"
url: "https://www.scopus.com/pages/publications/105036000174?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "555--560"
keywords: ["Cosine Similarity", "Generative AI", "Geometric Scheduling", "GPU Clusters", "Kubernetes", "Resource Fragmentation", "Vector Bin Packing"]
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

# paper-2627 — Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads

## Metadata

- **Authors:** Kaarat, Arjun and Reddy Batthula, Venkata Jaipal and Segall, Richard
- **Year:** 2026
- **Venue:** Proceedings - 5th International Conference on Informatics and Software Engineering, IISEC 2026
- **DOI:** 10.1109/IISEC69317.2026.11418430
- **URL:** https://www.scopus.com/pages/publications/105036000174?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 555--560
- **Language:** English
- **Keywords:** Cosine Similarity; Generative AI; Geometric Scheduling; GPU Clusters; Kubernetes; Resource Fragmentation; Vector Bin Packing

### Abstract

Generative AI workloads demand heterogeneous resources (GPUs, CPU cores, and high-bandwidth memory) in highly variable combinations. Current cluster schedulers, including Kubernetes, largely treat placement as scalar capacity packing (e.g., average utilization), which can mask infeasible nodes-servers may appear partially utilized while having no free GPUs, leaving CPUs or memory stranded. We propose Residual-Aware Geometric Packing (RAGP), a scheduling approach that matches each workload to a node's residual multi-resource capacity. RAGP represents workload demand and server residual capacity as multi-dimensional vectors and uses cosine similarity to quantify alignment between a workload's resource profile and a node's remaining capacity.This geometric matching preferentially places CPU-intensive workloads on CPU-rich nodes, memory-intensive workloads on memory-rich nodes, and complementary workloads together, reducing fragmentation and improving effective utilization. To address bursty inference behavior, RAGP incorporates a predictive buffer: it forecasts short-horizon resource demand (including memory growth with longer conversations) and reserves headroom proactively rather than relying on instantaneous measurements. © 2026 IEEE.

## 04 — Title Screening

**Title:** Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads
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
