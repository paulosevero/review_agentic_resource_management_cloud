---
id: "paper-2556"
title: "LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees"
authors: ["Ding, Guanyu", "Yang, Shiyu", "Lin, Han", "Chen, Zifan", "Yang, Jie Si"]
year: 2026
venue: "IEEE Open Journal of the Computer Society"
venue_type: "journal"
doi: "10.1109/OJCS.2026.3667549"
url: "https://www.scopus.com/pages/publications/105031664073?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "560--573"
keywords: ["adaptive optimization", "Cloud computing", "large language models (LLMs)", "resource scheduling", "SLA management", "task orchestration"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2556 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees

## Metadata

- **Authors:** Ding, Guanyu and Yang, Shiyu and Lin, Han and Chen, Zifan and Yang, Jie Si
- **Year:** 2026
- **Venue:** IEEE Open Journal of the Computer Society
- **DOI:** 10.1109/OJCS.2026.3667549
- **URL:** https://www.scopus.com/pages/publications/105031664073?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 560--573
- **Language:** English
- **Keywords:** adaptive optimization; Cloud computing; large language models (LLMs); resource scheduling; SLA management; task orchestration

### Abstract

Cloud resource scheduling presents a fundamental challenge in modern distributed computing, where heterogeneous workloads, complex task dependencies, and multi-objective optimization requirements exceed the capabilities of traditional rule-based and small-scale machine learning approaches. Existing schedulers struggle to dynamically adapt to evolving workload patterns while simultaneously satisfying Service Level Agreement (SLA) constraints, resource efficiency targets, and fairness policies. This article introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework that synergistically combines the contextual reasoning capabilities of foundation models with the execution guarantees of classical optimization techniques. Our approach transforms heterogeneous cluster states—including task dependency graphs, real-time resource utilization metrics, and SLA specifications—into a unified structured-textual representation that leverages LLMs' few-shot learning and causal reasoning abilities to generate intelligent scheduling candidates. These candidates are subsequently refined through a lightweight Integer Linear Programming (ILP) module that ensures feasibility and optimality under resource constraints. We evaluate LLMSched on Google's production cluster trace dataset, demonstrating significant improvements over state-of-the-art baselines: 23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations across diverse workload scenarios. Extensive ablation studies validate the contributions of each architectural component, while robustness analysis under workload perturbations confirms the framework's practical viability. Our work establishes a new paradigm for intelligent resource management that bridges the gap between neural reasoning and algorithmic precision, opening avenues for LLM applications in systems optimization domains. © 2020 IEEE.

## 04 — Title Screening

**Title:** LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees
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
