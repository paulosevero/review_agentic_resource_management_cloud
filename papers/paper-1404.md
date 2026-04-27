---
id: "paper-1404"
title: "ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control"
authors: ["Avgerinos, Vasilis", "Ramantas, Kostas", "Alonso, Luis", "Verikoukis, Christos"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3648858"
url: "https://www.scopus.com/pages/publications/105025885742?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Agentic Systems", "AIOps", "Autonomous Infrastructure Management", "Closed-Loop Control", "Edge Computing", "Intent-Based Networking", "IoT Orchestration", "Kubernetes", "Large Language Models (LLMs)", "SLA Monitoring"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1404 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control

## Metadata

- **Authors:** Avgerinos, Vasilis and Ramantas, Kostas and Alonso, Luis and Verikoukis, Christos
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3648858
- **URL:** https://www.scopus.com/pages/publications/105025885742?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Agentic Systems; AIOps; Autonomous Infrastructure Management; Closed-Loop Control; Edge Computing; Intent-Based Networking; IoT Orchestration; Kubernetes; Large Language Models (LLMs); SLA Monitoring

### Abstract

The growing complexity of cloud-native, edge, and IoT infrastructures has made manual configuration, fault remediation, and lifecycle management increasingly unsustainable. Traditional automation techniques—such as rule-based logic or bespoke machine learning pipelines—struggle with adaptability and explainability in dynamic environments. Recent advances in Large Language Models (LLMs), however, have introduced new opportunities for autonomous, intent-driven infrastructure control. In this work, we present a closed-loop framework that integrates LLM agents for automated Root Cause Analysis (RCA) and mitigation of faults within cloud-edge and IoT systems. When SLA violations are detected, the agent identifies likely root causes and selects corrective actions—such as pod rescheduling, scaling, or configuration updates—executed via a Model Context Protocol (MCP) server exposing management tool functionalities through an API. This RCA-plus-mitigation loop enables fault handling that is both explainable and adaptive. We evaluate our system on a cluster running synthetic IoT workloads under emulated stressors using a reproducible benchmarking setup. Results show that the agent identifies SLA violations with 52.9% accuracy and mitigates 70.7% of them successfully. Notably, the agent incorporates validation steps to ensure system stability after interventions. These findings highlight the feasibility of LLMs for real-time infrastructure healing and their potential role in future AIOps workflows. © 2014 IEEE.

## 04 — Title Screening

**Title:** ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
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
