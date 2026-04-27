---
id: "paper-958"
title: "Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach"
authors: ["Huang, Victoria", "Chen, Gang", "Zuo, Xingquan", "Zomaya, Albert Y.", "Sohrabi, Nasrin", "Tari, Zahir", "Fu, Qiang"]
year: 2024
venue: "IEEE Transactions on Cybernetics"
venue_type: "journal"
doi: "10.1109/TCYB.2023.3266448"
url: "https://www.scopus.com/pages/publications/85159824039?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3211--3224"
keywords: ["Distributed software-defined networking (SDN)controllers", "multiagent deep reinforcement learning (MA-DRL)", "request dispatching", "resource scheduling", "SDN"]
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

# paper-958 — Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach

## Metadata

- **Authors:** Huang, Victoria and Chen, Gang and Zuo, Xingquan and Zomaya, Albert Y. and Sohrabi, Nasrin and Tari, Zahir and Fu, Qiang
- **Year:** 2024
- **Venue:** IEEE Transactions on Cybernetics
- **DOI:** 10.1109/TCYB.2023.3266448
- **URL:** https://www.scopus.com/pages/publications/85159824039?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3211--3224
- **Language:** English
- **Keywords:** Distributed software-defined networking (SDN)controllers; multiagent deep reinforcement learning (MA-DRL); request dispatching; resource scheduling; SDN

### Abstract

Software-defined networking (SDN) allows flexible and centralized control in cloud data centers. An elastic set of distributed SDN controllers is often required to provide sufficient yet cost-effective processing capacity. However, this introduces a new challenge: Request Dispatching among the controllers by SDN switches. It is essential to design a dispatching policy for each switch to guide the request distribution. Existing policies are designed under certain assumptions, including a single centralized agent, global network knowledge, and a fixed number of controllers, which often cannot be satisfied in practice. This article proposes MADRina, Multiagent Deep Reinforcement Learning for request dispatching, to design policies with high dispatching adaptability and performance. First, we design a multiagent system to address the limitation of using a centralized agent with global network knowledge. Second, we propose a Deep Neural Network-based adaptive policy to enable request dispatching over an elastic set of controllers. Third, we develop a new algorithm to train the adaptive policies in a multiagent context. We prototype MADRina and build a simulation tool to evaluate its performance using real-world network data and topology. The results show that MADRina can significantly reduce response time by up to 30% compared to existing approaches.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach
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
