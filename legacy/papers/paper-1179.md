---
id: "paper-1179"
title: "Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming"
authors: ["Shao, Ziling", "Yang, Helin", "Xiao, Liang", "Su, Wei", "Chen, Yifan", "Xiong, Zehui"]
year: 2024
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2024.3432491"
url: "https://www.scopus.com/pages/publications/85200241000?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "13358--13374"
keywords: ["Anti-jamming", "deep reinforcement learning", "energy and latency minimization", "mobile edge computing", "resource management", "unmanned aerial vehicle"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1179 — Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming

## Metadata

- **Authors:** Shao, Ziling and Yang, Helin and Xiao, Liang and Su, Wei and Chen, Yifan and Xiong, Zehui
- **Year:** 2024
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2024.3432491
- **URL:** https://www.scopus.com/pages/publications/85200241000?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 13358--13374
- **Language:** English
- **Keywords:** Anti-jamming; deep reinforcement learning; energy and latency minimization; mobile edge computing; resource management; unmanned aerial vehicle

### Abstract

In mobile edge computing (MEC) systems, multiple unmanned aerial vehicles (UAVs) can be utilized as aerial servers to provide computing, communication, and storage services for edge users, called UAV-assisted MEC, which has emerged as a promising technology to improve both the computing and communication performances. Unlike existing works without considering jamming attacks, we investigate a multi-UAV-assisted-MEC scenario under multiple malicious jammers and then propose a resource management approach with the objective of minimizing both the system energy consumption and latency. Due to the time-varying nature of communication environments, we design a multi-agent deep reinforcement learning (MADRL)-based resource management approach to dynamically adjust the CPU frequency, communication bandwidth, and channel access selection of UAVs to enhance the system performance against jamming attacks. On this basis, in order to enhance the algorithm learning efficiency, we propose a multi-agent twin-delayed deep deterministic policy algorithm in combination with the prioritized experience replay mechanism (PER-MATD3) to effectively search for the joint resource management strategy under high-dimensional state and action spaces, where the time-varying channel state information and imperfect attack behavior information are also effectively trained to improve the learning capacity and convergence speed. Simulation and experimental results verify that the proposed approach can significantly decrease the overall system latency (i.e., computing and communication latency) and energy consumption compared to other benchmark algorithms under different real-world settings.  © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
