---
id: "paper-2142"
title: "Priority-Aware Preemptive Scheduling for Mixed-Priority Workloads in MoE Inference"
authors: ["Siavashi, Mohammad", "Keshmiri Dindarloo, Faezeh", "Kostic, Dejan", "Chiesa, Marco"]
year: 2025
venue: "EuroMLSys 2025 - Proceedings of the 2025 5th Workshop on Machine Learning and Systems"
venue_type: "conference"
doi: "10.1145/3721146.3721956"
url: "https://www.scopus.com/pages/publications/105003631563?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "132--138"
keywords: ["GPU acceleration", "large language models", "latency-sensitive inference", "mixture-of-experts", "preemptive scheduling", "priority-Aware scheduling"]
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

# paper-2142 — Priority-Aware Preemptive Scheduling for Mixed-Priority Workloads in MoE Inference

## Metadata

- **Authors:** Siavashi, Mohammad and Keshmiri Dindarloo, Faezeh and Kostic, Dejan and Chiesa, Marco
- **Year:** 2025
- **Venue:** EuroMLSys 2025 - Proceedings of the 2025 5th Workshop on Machine Learning and Systems
- **DOI:** 10.1145/3721146.3721956
- **URL:** https://www.scopus.com/pages/publications/105003631563?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 132--138
- **Language:** English
- **Keywords:** GPU acceleration; large language models; latency-sensitive inference; mixture-of-experts; preemptive scheduling; priority-Aware scheduling

### Abstract

Large Language Models have revolutionized natural language processing, yet serving them efficiently in data centers remains challenging due to mixed workloads comprising latency-sensitive (LS) and best-effort (BE) jobs. Existing inference systems employ iteration-level first-come-first-served scheduling, causing head-of-line blocking when BE jobs delay LS jobs. We introduce QLLM, a novel inference system designed for Mixture of Experts (MoE) models, featuring a fine-grained, priority-Aware preemptive scheduler. QLLM enables expert-level preemption, deferring BE job execution while minimizing LS time-To-first-Token (TTFT). Our approach removes iteration-level scheduling constraints, enabling the scheduler to preempt jobs at any layer based on priority. Evaluations on an Nvidia A100 GPU show that QLLM significantly improves performance. It reduces LS TTFT by an average of 65.5× and meets the SLO at up to 7 requests/sec, whereas the baseline fails to do so under the tested workload. Additionally, it cuts LS turnaround time by up to 12.8× without impacting throughput. QLLM is modular, extensible, and seamlessly integrates with Hugging Face MoE models. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Priority-Aware Preemptive Scheduling for Mixed-Priority Workloads in MoE Inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Priority-Aware Preemptive Scheduling for Mixed-Priority Workloads in MoE Inference
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Priority-Aware Preemptive Scheduling for Mixed-Priority Workloads in MoE Inference
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
