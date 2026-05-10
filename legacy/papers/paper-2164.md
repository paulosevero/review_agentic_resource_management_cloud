---
id: "paper-2164"
title: "Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework"
authors: ["Soule, Julien", "Jamont, Jean-Paul", "Occello, Michel", "Traonouez, Louis-Marie", "Theron, Paul"]
year: 2025
venue: "IEEE International Conference on Cloud Computing, CLOUD"
venue_type: "conference"
doi: "10.1109/CLOUD67622.2025.00015"
url: "https://www.scopus.com/pages/publications/105015982237?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "43--53"
keywords: ["Adversarial", "formatting", "Horizontal Pod Autoscaling", "insert", "Multi-Agent Reinforcement Learning", "Multi-Agent System Design component", "style", "styling"]
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
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-2164 — Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework

## Metadata

- **Authors:** Soule, Julien and Jamont, Jean-Paul and Occello, Michel and Traonouez, Louis-Marie and Theron, Paul
- **Year:** 2025
- **Venue:** IEEE International Conference on Cloud Computing, CLOUD
- **DOI:** 10.1109/CLOUD67622.2025.00015
- **URL:** https://www.scopus.com/pages/publications/105015982237?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 43--53
- **Language:** English
- **Keywords:** Adversarial; formatting; Horizontal Pod Autoscaling; insert; Multi-Agent Reinforcement Learning; Multi-Agent System Design component; style; styling

### Abstract

In cloud-native systems, Kubernetes clusters with interdependent services often face challenges to their operational resilience due to poor workload management issues such as resource blocking, bottlenecks, or continuous pod crashes. These vulnerabilities are further amplified in adversarial scenarios, such as Distributed Denial-of-Service attacks (DDoS). Conventional Horizontal Pod Autoscaling (HPA) approaches struggle to address such dynamic conditions, while reinforcement learning-based methods, though more adaptable, typically optimize single goals like latency or resource usage, neglecting broader failure scenarios. We propose decomposing the overarching goal of maintaining operational resilience into failure-specific sub-goals delegated to collaborative agents, collectively forming an HPA Multi-Agent System (MAS). We introduce an automated, four-phase online framework for HPA MAS design: 1) modeling a digital twin built from cluster traces; 2) training agents in simulation using roles and missions tailored to failure contexts; 3) analyzing agent behaviors for explainability; and 4) transferring learned policies to the real cluster. Experimental results demonstrate that the generated HPA MASs outperform three state-of-the-art HPA systems in sustaining operational resilience under various adversarial conditions in a proposed complex cluster.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework
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
