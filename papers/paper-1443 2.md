---
id: "paper-1443"
title: "Interruption-Aware Computation Offloading in the Industrial Internet of Things"
authors: ["Bui, Khoi Anh", "Yoo, Myungsik"]
year: 2025
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s25092904"
url: "https://www.scopus.com/pages/publications/105004895922?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["edge computing", "IIoT", "multi-agent deep reinforcement learning", "task offloading"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1443 — Interruption-Aware Computation Offloading in the Industrial Internet of Things

## Metadata

- **Authors:** Bui, Khoi Anh and Yoo, Myungsik
- **Year:** 2025
- **Venue:** Sensors
- **DOI:** 10.3390/s25092904
- **URL:** https://www.scopus.com/pages/publications/105004895922?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; IIoT; multi-agent deep reinforcement learning; task offloading

### Abstract

Designing an efficient task offloading system is essential in the Industrial Internet of Things (IIoT). Owing to the limited computational capability of IIoT devices, offloading tasks to edge servers enhances computational efficiency. When an edge server is overloaded, it may experience interruptions, preventing it from serving local devices. Existing studies mainly address interruptions by rerouting, rescheduling, or implementing reactive strategies to mitigate their impact. In this study, we introduce an interruption-aware proactive task offloading framework for IIoT. We develop a load-based interruption model in which the probability of server interruption is formulated as an exponential function of the total computational load, which provides a more realistic estimation of service availability. This framework employs Multi-Agent Advantage Actor–Critic (MAA2C)—a simple yet efficient approach that enables decentralized decision-making while handling large action spaces and maintaining coordination through the centralized critic to make adaptive offloading decisions, taking into account edge availability, resource limitations, device cooperation, and interruptions. Experimental results show that our approach effectively reduces the average total service delay by optimizing the tradeoff between system delay and availability in IIoT networks. Additionally, we investigate the impact of various system parameters on performance under an interruptible edge task offloading scenario, providing valuable insights into how these parameters influence the overall system behavior and efficiency. © 2025 by the authors.

## 04 — Title Screening

**Title:** Interruption-Aware Computation Offloading in the Industrial Internet of Things

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Interruption-Aware Computation Offloading in the Industrial Internet of Things
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Interruption-Aware Computation Offloading in the Industrial Internet of Things
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
