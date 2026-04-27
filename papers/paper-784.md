---
id: "paper-784"
title: "IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning"
authors: ["Yu, Jiadong", "Li, Yang", "Liu, Xiaolan", "Sun, Bo", "Wu, Yuan", "Hin-Kwok Tsang, Danny"]
year: 2023
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2022.3224291"
url: "https://www.scopus.com/pages/publications/85144061172?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4296--4312"
keywords: ["deep deterministic policy gradient", "IRS", "mobile edge computing", "NOMA", "reinforcement learning"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-784 — IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Yu, Jiadong and Li, Yang and Liu, Xiaolan and Sun, Bo and Wu, Yuan and Hin-Kwok Tsang, Danny
- **Year:** 2023
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2022.3224291
- **URL:** https://www.scopus.com/pages/publications/85144061172?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4296--4312
- **Language:** English
- **Keywords:** deep deterministic policy gradient; IRS; mobile edge computing; NOMA; reinforcement learning

### Abstract

By employing powerful edge servers for data processing, mobile edge computing (MEC) has been recognized as a promising technology to support emerging computation-intensive applications. Besides, non-orthogonal multiple access (NOMA)-aided MEC system can further enhance the spectral efficiency with massive tasks offloading. However, with more dynamic devices brought online and the uncontrollable stochastic channel environment, it is even desirable to deploy appealing technique, i.e., intelligent reflecting surfaces (IRS), in the MEC system to flexibly tune the communication environment and improve the system energy efficiency. In this paper, we investigate the joint offloading, communication and computation resource allocation for the IRS-assisted NOMA MEC system. We first formulate a mixed integer energy efficiency maximization problem with system queue stability constraint. We then propose the Lyapunov-function-based Mixed Integer Deep Deterministic Policy Gradient (LMIDDPG) algorithm which is based on the centralized reinforcement learning (RL) framework. To be specific, we design the mixed integer action space mapping which contains both continuous mapping and integer mapping. Moreover, the award function is defined as the upper-bound of the Lyapunov drift-plus-penalty function. To enable end devices (EDs) to choose actions independently at the execution stage, we further propose the Heterogeneous Multi-agent LMIDDPG (HMA-LMIDDPG) algorithm based on distributed RL framework with homogeneous EDs and heterogeneous base station (BS) as heterogeneous multi-agent. Numerical results show that our proposed algorithms can achieve superior energy efficiency performance to the benchmark algorithms while maintaining the queue stability. Specially, the distributed structure HMA-LMIDDPG can acquire more energy efficiency gain than the centralized structure LMIDDPG.  © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
