---
id: "paper-2628"
title: "Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents"
authors: ["Kapoor, Rahul", "Kas, Miray"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3675074"
url: "https://www.scopus.com/pages/publications/105033247089?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "43552--43568"
keywords: ["Active learning", "AIOps", "anomaly detection", "data center observability", "dynamic resolution", "large language models"]
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

# paper-2628 — Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents

## Metadata

- **Authors:** Kapoor, Rahul and Kas, Miray
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3675074
- **URL:** https://www.scopus.com/pages/publications/105033247089?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 43552--43568
- **Language:** English
- **Keywords:** Active learning; AIOps; anomaly detection; data center observability; dynamic resolution; large language models

### Abstract

The 'observability tax' - the escalating cost of telemetry in hyperscale data centers - forces a trade-off between expensive full-fidelity monitoring and low-cost sampling that misses critical 'gray failures.' While traditional AIOps models act as passive post-hoc analyzers, the novelty of this work lies in reformulating observability as an active, hypothesis-driven process. To achieve this, we propose a Dynamic Resolution Architecture where a Topology-Aware LLM Agent dynamically controls the telemetry resolution of the underlying infrastructure. Our Topology-Aware Active LLM Agent employs 'Sentinel Sampling,' monitoring 100% of nodes with low-cost essential metrics and only upgrading to high-resolution extended telemetry when semantically justified. Unlike rigid heuristics, the agent uses semantic reasoning to distinguish legitimate heavy workloads from pathological failures, even when root causes are hidden by layers of indirection in our physics-based simulation. Experimental results show the Active Agent achieves an F1 score of 0.95, significantly outperforming a cost-matched heuristic baseline (F1 0.65). Using a 'Skeptical Site Reliability Engineer (SRE)' protocol, the agent achieves 0.99 precision in distinguishing genuine failures from high-load noise. Our 'Wake-on-Anomaly' cost model shows an 84% reduction in telemetry bandwidth and a 12.5% reduction in Total Cost of Ownership compared to standard ingestion. This work demonstrates that observability is primarily a data selection, not data volume, problem, solvable via semantic active reasoning.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Breaking the Observability Tax: Dynamic Resolution Anomaly Detection via Topology-Aware Active LLM Agents
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
