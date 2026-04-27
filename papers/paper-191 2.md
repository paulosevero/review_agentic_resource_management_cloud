---
id: "paper-191"
title: "Resource Management for Power-Constrained HEVC Transcoding Using Reinforcement Learning"
authors: ["Costero, Luis", "Iranfar, Arman", "Zapater, Marina", "Igual, Francisco D.", "Olcoz, Katzalin", "Atienza, David"]
year: 2020
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2020.3004735"
url: "https://www.scopus.com/pages/publications/85089679578?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "2834--2850"
keywords: ["DVFS", "HEVC", "power capping", "Q-learning", "reinforcement learning", "Resource management", "self-adaptation"]
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

# paper-191 — Resource Management for Power-Constrained HEVC Transcoding Using Reinforcement Learning

## Metadata

- **Authors:** Costero, Luis and Iranfar, Arman and Zapater, Marina and Igual, Francisco D. and Olcoz, Katzalin and Atienza, David
- **Year:** 2020
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2020.3004735
- **URL:** https://www.scopus.com/pages/publications/85089679578?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 2834--2850
- **Language:** English
- **Keywords:** DVFS; HEVC; power capping; Q-learning; reinforcement learning; Resource management; self-adaptation

### Abstract

The advent of online video streaming applications and services along with the users' demand for high-quality contents require High Efficiency Video Coding (HEVC), which provides higher video quality and more compression at the cost of increased complexity. On one hand, HEVC exposes a set of dynamically tunable parameters to provide trade-offs among Quality-of-Service (QoS), performance, and power consumption of multi-core servers on the video providers' data center. On the other hand, resource management of modern multi-core servers is in charge of adapting system-level parameters, such as operating frequency and multithreading, to deal with concurrent applications and their requirements. Therefore, efficient multi-user HEVC streaming necessitates joint adaptation of application- and system-level parameters. Nonetheless, dealing with such a large and dynamic design space is challenging and difficult to address through conventional resource management strategies. Thus, in this work, we develop a multi-agent Reinforcement Learning framework to jointly adjust application- and system-level parameters at runtime to satisfy the QoS of multi-user HEVC streaming in power-constrained servers. In particular, the design space, composed of all design parameters, is split into smaller independent sub-spaces. Each design sub-space is assigned to a particular agent so that it can explore it faster, yet accurately. The benefits of our approach are revealed in terms of adaptability and quality (with up to to $4times$4× improvements in terms of QoS when compared to a static resource management scheme), and learning time ($6 times$6× faster than an equivalent mono-agent implementation). Finally, we show that the power-capping techniques formulated outperform the hardware-based power capping with respect to quality. © 1990-2012 IEEE.

## 04 — Title Screening

**Title:** Resource Management for Power-Constrained HEVC Transcoding Using Reinforcement Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Resource Management for Power-Constrained HEVC Transcoding Using Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Resource Management for Power-Constrained HEVC Transcoding Using Reinforcement Learning
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
