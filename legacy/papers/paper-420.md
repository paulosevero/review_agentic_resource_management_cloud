---
id: "paper-420"
title: "Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning"
authors: ["Guo, Yingya", "Ma, Yulong", "Luo, Huan", "Wu, Jianping"]
year: 2022
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2022.3172283"
url: "https://www.scopus.com/pages/publications/85129633172?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "2870--2881"
keywords: ["deep reinforcement learning", "egress selection", "Inter-DC WAN", "routing optimization", "traffic engineering"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-420 — Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning

## Metadata

- **Authors:** Guo, Yingya and Ma, Yulong and Luo, Huan and Wu, Jianping
- **Year:** 2022
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2022.3172283
- **URL:** https://www.scopus.com/pages/publications/85129633172?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 2870--2881
- **Language:** English
- **Keywords:** deep reinforcement learning; egress selection; Inter-DC WAN; routing optimization; traffic engineering

### Abstract

To reduce the investment on network infrastructure, many online service providers have begun to adopt the shared inter-DataCenter Wide Area Network (inter-DC WAN) that connects different datacenters and Internet Service Providers (ISPs). The shared inter-DC WAN accommodates two kinds of traffic, i.e. delay-sensitive ISP-facing traffic and high-throughput inter-DC traffic. Traffic Engineering (TE) in the shared inter-DC WAN should determine the routing paths for all traffic to achieve link load balancing, while select lower-latency egress routers for ISP-facing traffic to guarantee the Quality of Service (QoS). Therefore, this paper mainly focuses on jointly optimizing routing paths selection and egress router selection to strike a balance between QoS and link load balancing. Specifically, we first formulate the TE problem in the shared inter-DC WAN as a mixed integer nonlinear programming problem. Then, a TED method is proposed to jointly optimize the egress router selection and routing path selection by learning an intelligent agent with Deep Reinforcement Learning (DRL). The learnt agent can self-adaptively and rapidly select the optimal egress routers by considering the utilization-latency balance when traffic demand changes. Finally, we conduct extensive evaluations on Alibaba WAN with real traffic traces to demonstrate the effectiveness and superiority of the proposed method.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
