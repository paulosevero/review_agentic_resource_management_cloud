---
id: "paper-2663"
title: "Incremental DRL-Based Resource Management for Dynamic Network Slicing in an Urban-Wide Testbed"
authors: ["Li, Haiyuan", "Liu, Yuelin", "Madhukumar, Hari", "Emami, Amin", "Zhou, Xueqing", "Wu, Yulei", "Vasilakos, Xenofon", "Yan, Shuangyi", "Simeonidou, Dimitra"]
year: 2026
venue: "IEEE Transactions on Network and Service Management"
venue_type: "journal"
doi: "10.1109/TNSM.2025.3633927"
url: "https://www.scopus.com/pages/publications/105022256092?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "183--195"
keywords: ["incremental learning", "MADDPG", "Multi-access edge computing", "network slicing", "testbed deployment"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2663 — Incremental DRL-Based Resource Management for Dynamic Network Slicing in an Urban-Wide Testbed

## Metadata

- **Authors:** Li, Haiyuan and Liu, Yuelin and Madhukumar, Hari and Emami, Amin and Zhou, Xueqing and Wu, Yulei and Vasilakos, Xenofon and Yan, Shuangyi and Simeonidou, Dimitra
- **Year:** 2026
- **Venue:** IEEE Transactions on Network and Service Management
- **DOI:** 10.1109/TNSM.2025.3633927
- **URL:** https://www.scopus.com/pages/publications/105022256092?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 183--195
- **Language:** English
- **Keywords:** incremental learning; MADDPG; Multi-access edge computing; network slicing; testbed deployment

### Abstract

Multi-access edge computing provides localized resources within mobile networks to address the requirements of emerging latency-sensitive and computing-intensive applications. At the edge, dynamic requests necessitate sophisticated resource management for adaptive network slicing. This involves optimizing resource allocations, scaling functions, and load balancing to utilize only essential resources under constrained network scenarios. However, existing solutions largely assume static slice counts, ignoring the re-optimization overhead associated with management algorithms when slices fluctuate. Moreover, many approaches rely on simplified energy models that overlook intertemporal resource scheduling and are predominantly evaluated through simulations, neglecting critical practical considerations. This paper presents an incremental cooperative Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm for resource management in dynamic edge slicing. The proposed approach optimizes long-term slicing benefits by reducing delay and energy consumption while minimizing retraining overhead in response to slice variations. Furthermore, we implement an urban-wide edge computing testbed based on OpenStack and Kubernetes to validate the algorithm’s performance. Experimental results demonstrate that our incremental MADDPG method outperforms benchmark strategies in aggregated slicing utility and reduces training energy consumption by up to 50% compared to the re-optimization approach. © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** Incremental DRL-Based Resource Management for Dynamic Network Slicing in an Urban-Wide Testbed

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Incremental DRL-Based Resource Management for Dynamic Network Slicing in an Urban-Wide Testbed
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Incremental DRL-Based Resource Management for Dynamic Network Slicing in an Urban-Wide Testbed
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
