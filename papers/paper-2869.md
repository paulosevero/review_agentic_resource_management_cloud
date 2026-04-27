---
id: "paper-2869"
title: "Towards Resource-Efficient Serverless LLM Inference with SLINFER"
authors: ["Xu, Chuhao", "Li, Zijun", "Chen, Quan", "Zhao, Han", "Tang, Xueyan", "Guo, Minyi"]
year: 2026
venue: "Proceedings - International Symposium on High-Performance Computer Architecture"
venue_type: "conference"
doi: "10.1109/HPCA68181.2026.11408548"
url: "https://www.scopus.com/pages/publications/105035386893?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["Computer hardware", "Graphics processing unit", "Computational demands", "Compute resources", "CPU architecture", "Elastic demand", "Fine grained", "Forward looking", "Heterogeneous hardware", "On demands", "Resource-efficient", "Resources allocation", "Program processors"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2869 — Towards Resource-Efficient Serverless LLM Inference with SLINFER

## Metadata

- **Authors:** Xu, Chuhao and Li, Zijun and Chen, Quan and Zhao, Han and Tang, Xueyan and Guo, Minyi
- **Year:** 2026
- **Venue:** Proceedings - International Symposium on High-Performance Computer Architecture
- **DOI:** 10.1109/HPCA68181.2026.11408548
- **URL:** https://www.scopus.com/pages/publications/105035386893?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** Computer hardware; Graphics processing unit; Computational demands; Compute resources; CPU architecture; Elastic demand; Fine grained; Forward looking; Heterogeneous hardware; On demands; Resource-efficient; Resources allocation; Program processors

### Abstract

The rise of LLMs has driven demand for private serverless deployments, characterized by moderate-sized models and infrequent requests. While existing serverless solutions follow exclusive GPU allocation, we take a step back to explore modern platforms and find that: Emerging CPU architectures with built-in accelerators are capable of serving LLMs but remain underutilized, and both CPUs and GPUs can accommodate multiple LLMs simultaneously. We propose SLINFER, a resource-efficient serverless inference scheme tailored for small- to mid-sized LLMs that enables elastic and on-demand sharing across heterogeneous hardware. SLINFER tackles three fundamental challenges: (1) precise, fine-grained compute resource allocation at token-level to handle fluctuating computational demands; (2) a coordinated and forward-looking memory scaling mechanism to detect out-ofmemory hazards and reduce operational overhead; and (3) a dual approach that consolidates fragmented instances through proactive preemption and reactive bin-packing. Experimental results on 4 32-core CPUs and 4 A100 GPUs show that SLINFER improves serving capacity by 47% - 62% through sharing, while further leveraging CPUs boosts this to 86% - 154%.  © 2026 IEEE.

## 04 — Title Screening

**Title:** Towards Resource-Efficient Serverless LLM Inference with SLINFER

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Towards Resource-Efficient Serverless LLM Inference with SLINFER
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Towards Resource-Efficient Serverless LLM Inference with SLINFER
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
