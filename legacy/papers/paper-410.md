---
id: "paper-410"
title: "Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach"
authors: ["Gao, Lynn", "Chen, Yutian", "Tang, Bin"]
year: 2022
venue: "Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST"
venue_type: "conference"
doi: "10.1007/978-3-031-23141-4_22"
url: "https://www.scopus.com/pages/publications/85148698291?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "291--309"
keywords: ["Data centers", "k-stroll Problem", "Reinforcement learning", "Service function chaining"]
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

# paper-410 — Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach

## Metadata

- **Authors:** Gao, Lynn and Chen, Yutian and Tang, Bin
- **Year:** 2022
- **Venue:** Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
- **DOI:** 10.1007/978-3-031-23141-4_22
- **URL:** https://www.scopus.com/pages/publications/85148698291?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 291--309
- **Language:** English
- **Keywords:** Data centers; k-stroll Problem; Reinforcement learning; Service function chaining

### Abstract

Service function chaining (SFC), consisting of a sequence of virtual network functions (VNFs) (i.e., firewalls and load balancers), is an effective service provision technique in modern data center networks. By requiring cloud user traffic to traverse the VNFs in order, SFC improves the security and performance of the cloud user applications. In this paper, we study how to place an SFC inside a data center to minimize the network traffic of the virtual machine (VM) communication. We take a cooperative multi-agent reinforcement learning approach, wherein multiple agents collaboratively figure out the traffic-efficient route for the VM communication. Underlying the SFC placement is a fundamental graph-theoretical problem called the k-stroll problem. Given a weighted graph G(V, E), two nodes s, and an integer k, the k-stroll problem is to find the shortest path from s to t that visits at least k other nodes in the graph. Our work is the first to take a multi-agent learning approach to solve k-stroll problem. We compare our learning algorithm with an optimal and exhaustive algorithm and an existing dynamic programming(DP)-based heuristic algorithm. We show that our learning algorithm, although lacking the complete knowledge of the network assumed by existing research, delivers comparable or even better VM communication time while taking two orders of magnitude of less execution time. © 2022, ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering.

## 04 — Title Screening

**Title:** Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach
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
