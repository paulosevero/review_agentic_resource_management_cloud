---
id: "paper-2655"
title: "A Learning-Based Incentive Mechanism for Mobile AIGC Service in Vehicular Edge Computing"
authors: ["Li, Xiangyu", "Chen, Honglong", "Ni, Zhichen", "Sun, Haiyang", "Yang, Yubin", "Wu, Liantao", "Xia, Feng"]
year: 2026
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2026.3663491"
url: "https://www.scopus.com/pages/publications/105030051980?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AIGC", "deep reinforcement learning", "incentive mechanism", "vehicular edge computing"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2655 — A Learning-Based Incentive Mechanism for Mobile AIGC Service in Vehicular Edge Computing

## Metadata

- **Authors:** Li, Xiangyu and Chen, Honglong and Ni, Zhichen and Sun, Haiyang and Yang, Yubin and Wu, Liantao and Xia, Feng
- **Year:** 2026
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2026.3663491
- **URL:** https://www.scopus.com/pages/publications/105030051980?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AIGC; deep reinforcement learning; incentive mechanism; vehicular edge computing

### Abstract

In the field of Internet of Vehicles (IoV), the emergence of artificial intelligence generated content (AIGC) has provided a new approach for synthesizing, manipulating, and modifying driving data. The physical remoteness of cloud servers makes it challenging to ensure timely and secure data transmission. Therefore, it is essential to fully utilize edge servers and vehicular terminals equipped with small-scale generative AI servers to form a vehicular network. However, the allocation and transmission of tasks to vehicles face many challenging issues, such as underutilization of idle vehicle resources. In this paper, we establish an incentive mechanism driven by rewards based on different resource costs and design a multi-stage Stackelberg game under conditions of information asymmetry to address the issue of resource wastage in vehicular terminals. Specifically, self-interested vehicles are not forced to share resources or reveal their private information, such as vehicle dwell time and resource quantity. We first prove the existence and uniqueness of a Stackelberg equilibrium under complete information sharing. To handle information asymmetry without requiring vehicles to reveal private parameters, we then propose a proximal policy optimization (PPO)-based Vehicular terminal Resource Pricing mechanism (PVRP) that learns pricing strategies from interaction histories; this approach both preserves vehicular privacy and enables efficient convergence toward the Stackelberg equilibrium in dynamic settings. Extensive simulation results demonstrate that the proposed mechanism greatly outperforms existing methods in both static and dynamic vehicular networks. © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** A Learning-Based Incentive Mechanism for Mobile AIGC Service in Vehicular Edge Computing

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A Learning-Based Incentive Mechanism for Mobile AIGC Service in Vehicular Edge Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Learning-Based Incentive Mechanism for Mobile AIGC Service in Vehicular Edge Computing
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
