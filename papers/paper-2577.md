---
id: "paper-2577"
title: "CPID-MAAC: RL for Joint User Association and Trajectory Control in UAV-Assisted MEC Systems"
authors: ["Gao, Zhen", "Xie, Qipeng", "Yang, Lei", "Dai, Yu", "Wang, Weizheng"]
year: 2026
venue: "IEEE Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TON.2025.3644923"
url: "https://www.scopus.com/pages/publications/105025453831?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2316--2331"
keywords: ["Lagrangian algorithm", "reinforcement learning (RL)", "Unreewed aerial vehicle (UAV)-assisted multi-access edge computing (MEC)", "user association and trajectory control"]
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

# paper-2577 — CPID-MAAC: RL for Joint User Association and Trajectory Control in UAV-Assisted MEC Systems

## Metadata

- **Authors:** Gao, Zhen and Xie, Qipeng and Yang, Lei and Dai, Yu and Wang, Weizheng
- **Year:** 2026
- **Venue:** IEEE Transactions on Networking
- **DOI:** 10.1109/TON.2025.3644923
- **URL:** https://www.scopus.com/pages/publications/105025453831?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2316--2331
- **Language:** English
- **Keywords:** Lagrangian algorithm; reinforcement learning (RL); Unreewed aerial vehicle (UAV)-assisted multi-access edge computing (MEC); user association and trajectory control

### Abstract

Existing joint user association and trajectory control (JUATC) methods provide remarkably high data rates for mobile users (MUs) in unreewed aerial vehicle (UAV)-assisted multi-access edge computing systems. Nevertheless, current methods give more attention to the uplink and downlink of MU, which must be associated with the same UAV or base station (BS), ignoring the network’s heterogeneity and considerably reducing the MU’s communication efficiency. Furthermore, UAVs typically provide communication services to MUs under partial observation, leading to challenges in achieving optimal service performance due to information loss. Moreover, although existing solutions can readily reach optimal, restriction-fulfilling strategies, they frequently breach restrictions during intermediate iterations. To address these issues, we present a fully decentralized JUATC algorithm based on the Communication and Proportional-Integral-Derivative (PID) Lagrangian-based Multi-Agent Actor-Critic (CPID-MAAC). First, to improve communication efficiency, we consider that each MU can be associated with a different UAV or BS in the uplink and downlink. Second, we establish a messaging mechanism between UAVs based on autoencoding UAV’s observations to handle the information loss. Finally, to alleviate constraint-violating behavior, we incorporate the PID Lagrangian algorithm. The experiments show that CPID-MAAC improves data rate by 7.88%~16.03% and drastically reduces the number of constraint violations during UAV agent training. © 2025 IEEE.

## 04 — Title Screening

**Title:** CPID-MAAC: RL for Joint User Association and Trajectory Control in UAV-Assisted MEC Systems

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** CPID-MAAC: RL for Joint User Association and Trajectory Control in UAV-Assisted MEC Systems
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** CPID-MAAC: RL for Joint User Association and Trajectory Control in UAV-Assisted MEC Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
