---
id: "paper-1061"
title: "Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing"
authors: ["Liu, Guoqiang", "Xu, Xiaolong", "Xu, Xiyuan", "Ji, Xinyue", "Qi, Lianyong", "Zhang, Xuyun"]
year: 2024
venue: "Proceedings of the IEEE International Conference on Web Services, ICWS"
venue_type: "conference"
doi: "10.1109/ICWS62655.2024.00127"
url: "https://www.scopus.com/pages/publications/85210226564?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1089--1096"
keywords: ["Collaborative Service Placement", "Edge Computing", "Latency-Sensitive", "Leader-Follower Architecture", "MARL"]
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

# paper-1061 — Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing

## Metadata

- **Authors:** Liu, Guoqiang and Xu, Xiaolong and Xu, Xiyuan and Ji, Xinyue and Qi, Lianyong and Zhang, Xuyun
- **Year:** 2024
- **Venue:** Proceedings of the IEEE International Conference on Web Services, ICWS
- **DOI:** 10.1109/ICWS62655.2024.00127
- **URL:** https://www.scopus.com/pages/publications/85210226564?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1089--1096
- **Language:** English
- **Keywords:** Collaborative Service Placement; Edge Computing; Latency-Sensitive; Leader-Follower Architecture; MARL

### Abstract

By distributing computing and storage resources to edge servers (ESs), edge computing enables service execution closer to requests, alleviating high latency caused by long-distance data transmission. The communication between ESs facilitates collaborative service placement (CSP) on multiple ESs, leading to latency reduction and thereby improving the quality of service. However, the discrepancies in service request distributions among ESs pose challenge to effective CSP, while limited prior knowledge further increases the difficulty in policy formation. Additionally, the delayed awareness of placement strategies among other ESs exacerbates the influence of non-Markovian nature. To overcome above challenges, a leader-follower based multi-agent reinforcement learning for CSP scheme, named LFMCSP, is proposed in this paper. Specifically, a CSP model is formulated, with ESs abstracted as intelligent agents within it. Then, the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm is utilized to explore potential patterns in complex requests by experience sharing. To achieve transparency of global states for all agents, the leader-follower architecture is integrated into MADDPG. Through rigorous experiments and comparisons with various baseline schemes, LFMCSP demonstrates effectiveness in reducing service execution delays.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing
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
