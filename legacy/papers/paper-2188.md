---
id: "paper-2188"
title: "CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory"
authors: ["Suo, Jiashun", "Liao, Xiaojian", "Xiao, Limin", "Ruan, Li", "Wang, Jinquan", "Su, Xiao", "Huo, Zhisheng"]
year: 2025
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3676641.3715986"
url: "https://www.scopus.com/pages/publications/105002589582?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "178--191"
keywords: ["collaboration-of-experts (coe)", "edge computing", "ml inference"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2188 — CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory

## Metadata

- **Authors:** Suo, Jiashun and Liao, Xiaojian and Xiao, Limin and Ruan, Li and Wang, Jinquan and Su, Xiao and Huo, Zhisheng
- **Year:** 2025
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3676641.3715986
- **URL:** https://www.scopus.com/pages/publications/105002589582?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 178--191
- **Language:** English
- **Keywords:** collaboration-of-experts (coe); edge computing; ml inference

### Abstract

Large language models like GPT-4 are resource-intensive, but recent advancements suggest that smaller, specialized experts can outperform the monolithic models on specific tasks. The Collaboration-of-Experts (CoE) approach integrates multiple expert models, improving the accuracy of generated results and offering great potential for precision-critical applications, such as automatic circuit board quality inspection. However, deploying CoE serving systems presents challenges to memory capacity due to the large number of experts required, which can lead to significant performance overhead from frequent expert switching across different memory and storage tiers. We propose CoServe, an efficient CoE model serving system on heterogeneous CPU and GPU with limited memory. CoServe reduces unnecessary expert switching by leveraging expert dependency, a key property of CoE inference. CoServe introduces a dependency-aware request scheduler and dependency-aware expert management for efficient inference. It also introduces an offline profiler to automatically find optimal resource allocation on various processors and devices. In real-world intelligent manufacturing workloads, CoServe achieves 4.5× to 12× higher throughput compared to state-of-the-art systems. © 2025 ACM.

## 04 — Title Screening

**Title:** CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
