---
id: "paper-2635"
title: "MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces"
authors: ["Khan, Zafar Iqbal", "Khan, Muzafar", "Shah, Syed Nasir Mehmood"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3676311"
url: "https://www.scopus.com/pages/publications/105033477084?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "44165--44184"
keywords: ["adaptive dynamic time quantum", "Cloud scheduling", "CloudSimPlus", "multi-agent systems", "multi-tier architecture"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2635 — MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces

## Metadata

- **Authors:** Khan, Zafar Iqbal and Khan, Muzafar and Shah, Syed Nasir Mehmood
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3676311
- **URL:** https://www.scopus.com/pages/publications/105033477084?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 44165--44184
- **Language:** English
- **Keywords:** adaptive dynamic time quantum; Cloud scheduling; CloudSimPlus; multi-agent systems; multi-tier architecture

### Abstract

Task scheduling is required to optimize the use of resources and minimize the waiting time in cloud computing systems. However, the traditional fixed scheduling techniques cannot address the variability, heterogeneity and dynamic behavior of cloud workloads. Current time-sharing schedulers use fixed CPU time quantum and do not have any dynamic mechanisms to adapt to the workload, and SLA-driven priorities, resulting in poor performance of cloud infrastructures. To overcome these drawbacks, this paper proposes a novel Multi-Agent Adaptive Dynamic Round Robin (MAADRR) scheduling model for dynamic and heterogeneous cloud systems. Compared with traditional single-layer schedulers, MAADRR has hierarchical agent-based coordination. This allows it to balance workloads across the infrastructure and have local flexibility simultaneously. The framework is implemented and evaluated on the CloudSim Plus simulator and enables realistic modelling of the multi-level cloud execution environment. The VM-level agents Adaptive Round Robin are dynamically changed by real-time quantum due to real-time workload feedback. A global coordination agent, which exists at the infrastructure layer, integrates the previously set scheduling strategies, such as Dynamic Max-Min, DRALBA, PSSLB, PSSELB, and DeRALBA, to coordinate the distribution of different tasks among the heterogeneous resources. This multi-agent design is cooperative and provides autonomous local optimization, stability, and fairness of the system. The experiments were conducted on workloads of varying sizes. The experimental results obtained from Google-Cluster-like Job (GoCJ) traces demonstrate that MAADRR is a more energy-efficient solution and outperforms the baseline methods in terms of Energy Consumption, Throughput, Average Waiting Time (AWT), Average Turnaround Time (ATAT), and Total Completion Time (TCT). The findings confirm that MAADRR is a scalable scheduling framework that is suitable for cloud environments. © 2026 The Authors.

## 04 — Title Screening

**Title:** MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces
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
