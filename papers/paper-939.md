---
id: "paper-939"
title: "RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering"
authors: ["Gui, Fei", "Wang, Songtao", "Li, Dan", "Chen, Li", "Gao, Kaihui", "Min, Congcong", "Wang, Yi"]
year: 2024
venue: "ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference"
venue_type: "conference"
doi: "10.1145/3651890.3672231"
url: "https://www.scopus.com/pages/publications/85202299053?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "71--85"
keywords: ["machine learning", "network optimization", "traffic engineering"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-939 — RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering

## Metadata

- **Authors:** Gui, Fei and Wang, Songtao and Li, Dan and Chen, Li and Gao, Kaihui and Min, Congcong and Wang, Yi
- **Year:** 2024
- **Venue:** ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference
- **DOI:** 10.1145/3651890.3672231
- **URL:** https://www.scopus.com/pages/publications/85202299053?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 71--85
- **Language:** English
- **Keywords:** machine learning; network optimization; traffic engineering

### Abstract

Internet traffic bursts usually happen within a second, thus conventional burst mitigation methods ignore the potential of Traffic Engineering (TE). However, our experiments indicate that a TE system, with a sub-second control loop latency, can effectively alleviate burst-induced congestion. TE-based methods can leverage network-wide tunnel-level information to make globally informed decisions (e.g., balancing traffic bursts among multiple paths). Our insight in reducing control loop latency is to let each router make local TE decisions, but this introduces the key challenge of minimizing performance loss compared to centralized TE systems.In this paper, we present RedTE, a novel distributed TE system with a control loop latency of < 100ms, while achieving performance comparable to centralized TE systems. RedTE's innovation is the modeling of TE as a distributed cooperative multi-agent problem, and we design a novel multi-agent deep reinforcement learning algorithm to solve it, which enables each agent to make globally informed decisions solely based on local information. We implement real RedTE routers and deploy them on a WAN spanning six city datacenters. Evaluation reveals notable improvements compared to existing solutions: < 100ms of control loop latency, a 37.4% reduction in maximum link utilization, and a 78.9% reduction in average queue length.  © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering
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
