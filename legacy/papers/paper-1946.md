---
id: "paper-1946"
title: "Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow"
authors: ["Mei, Yixuan", "Zhuang, Yonghao", "Miao, Xupeng", "Yang, Juncheng", "Jia, Zhihao", "Vinayak, Rashmi"]
year: 2025
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3669940.3707215"
url: "https://www.scopus.com/pages/publications/105002391614?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "586--602"
keywords: ["cloud computing", "distributed systems", "large language model serving", "system for ml"]
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
    human_justification: "LLM as workload"

---

# paper-1946 — Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow

## Metadata

- **Authors:** Mei, Yixuan and Zhuang, Yonghao and Miao, Xupeng and Yang, Juncheng and Jia, Zhihao and Vinayak, Rashmi
- **Year:** 2025
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3669940.3707215
- **URL:** https://www.scopus.com/pages/publications/105002391614?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 586--602
- **Language:** English
- **Keywords:** cloud computing; distributed systems; large language model serving; system for ml

### Abstract

This paper introduces Helix, a distributed system for high-throughput, low-latency large language model (LLM) serving in heterogeneous GPU clusters. The key idea behind Helix is to formulate inference computation of LLMs over heterogeneous GPUs and network connections as a max-flow problem on directed, weighted graphs, whose nodes represent GPU instances and edges capture both GPU and network heterogeneity through their capacities. Helix then uses a mixed integer linear programming (MILP) algorithm to discover highly optimized strategies to serve LLMs on heterogeneous GPUs. This approach allows Helix to jointly optimize model placement and request scheduling, two highly entangled tasks in heterogeneous LLM serving. Our evaluation on several heterogeneous clusters ranging from 24 to 42 GPU nodes shows that Helix improves serving throughput by up to 3.3x and reduces prompting and decoding latency by up to 66% and 24%, respectively, compared to existing approaches. Helix is available at https://github.com/Thesys-lab/Helix-ASPLOS25.  © 2025 ACM.

## 04 — Title Screening

**Title:** Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow
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
