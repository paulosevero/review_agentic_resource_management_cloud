---
id: "paper-114"
title: "Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach"
authors: ["Chen, Xianfu", "Zhao, Zhifeng", "Wu, Celimuge", "Bennis, Mehdi", "Liu, Hang", "Ji, Yusheng", "Zhang, Honggang"]
year: 2019
venue: "IEEE Journal on Selected Areas in Communications"
venue_type: "journal"
doi: "10.1109/JSAC.2019.2933893"
url: "https://www.scopus.com/pages/publications/85070673256?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2377--2392"
keywords: ["deep reinforcement learning", "Markov decision process", "mobile-edge computing", "Network slicing", "packet scheduling", "radio access networks"]
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

# paper-114 — Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Chen, Xianfu and Zhao, Zhifeng and Wu, Celimuge and Bennis, Mehdi and Liu, Hang and Ji, Yusheng and Zhang, Honggang
- **Year:** 2019
- **Venue:** IEEE Journal on Selected Areas in Communications
- **DOI:** 10.1109/JSAC.2019.2933893
- **URL:** https://www.scopus.com/pages/publications/85070673256?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2377--2392
- **Language:** English
- **Keywords:** deep reinforcement learning; Markov decision process; mobile-edge computing; Network slicing; packet scheduling; radio access networks

### Abstract

With the cellular networks becoming increasingly agile, a major challenge lies in how to support diverse services for mobile users (MUs) over a common physical network infrastructure. Network slicing is a promising solution to tailor the network to match such service requests. This paper considers a system with radio access network (RAN)-only slicing, where the physical infrastructure is split into slices providing computation and communication functionalities. A limited number of channels are auctioned across scheduling slots to MUs of multiple service providers (SPs) (i.e., the tenants). Each SP behaves selfishly to maximize the expected long-term payoff from the competition with other SPs for the orchestration of channels, which provides its MUs with the opportunities to access the computation and communication slices. This problem is modelled as a stochastic game, in which the decision makings of a SP depend on the global network dynamics as well as the joint control policy of all SPs. To approximate the Nash equilibrium solutions, we first construct an abstract stochastic game with the local conjectures of channel auction among the SPs. We then linearly decompose the per-SP Markov decision process to simplify the decision makings at a SP and derive an online scheme based on deep reinforcement learning to approach the optimal abstract control policies. Numerical experiments show significant performance gains from our scheme. © 1983-2012 IEEE.

## 04 — Title Screening

**Title:** Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach
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
