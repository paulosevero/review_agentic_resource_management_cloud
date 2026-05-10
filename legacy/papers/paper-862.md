---
id: "paper-862"
title: "Joint Task and Computing Resource Allocation in Distributed Edge Computing Systems via Multi-Agent Deep Reinforcement Learning"
authors: ["Chen, Yan", "Sun, Yanjing", "Yu, Hao", "Taleb, Tarik"]
year: 2024
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2024.3375374"
url: "https://www.scopus.com/pages/publications/85187975110?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "3479--3494"
keywords: ["distributed task allocation", "Edge computing", "multi-agent deep reinforcement learning", "quality of experience", "resource allocation"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-862 — Joint Task and Computing Resource Allocation in Distributed Edge Computing Systems via Multi-Agent Deep Reinforcement Learning

## Metadata

- **Authors:** Chen, Yan and Sun, Yanjing and Yu, Hao and Taleb, Tarik
- **Year:** 2024
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2024.3375374
- **URL:** https://www.scopus.com/pages/publications/85187975110?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 3479--3494
- **Language:** English
- **Keywords:** distributed task allocation; Edge computing; multi-agent deep reinforcement learning; quality of experience; resource allocation

### Abstract

Edge servers can collaborate to enhance service capability. However, cloud servers may be unable to execute centralized management due to unpredictable communications. In such systems, distributed task and resource management are vital but challenging due to heterogeneity and various restrictions. Therefore, this paper studies such edge systems and formulates the distributed joint task and computing resource allocation problem for maximizing the quality of experience (QoE). Given the restrictions on real-time state observations and resource management involving other facilities, we decompose it into sub-problems of distributed task allocation and computing resource allocation. After formulating the problem as a partially observed Markov decision process, we propose a two-step approach that depends on multi-agent (MA) deep reinforcement learning. First, each edge server performs a policy to allocate tasks for its associated users according to a partial observation. We employ the MA deep deterministic policy gradient to tackle vast spaces of discrete actions. Besides, we incorporate the action entropy of massive users' task allocation to enhance exploration. Then, we prove that the QoE-maximized computing resource allocation is a problem of maxing a sum of sigmoids, and we address it by sigmoidal programming. Simulation results reveal that the proposed approach dramatically improves the system QoE and reduces the average service latency. Besides, the proposed solution outperforms benchmarks in training and convergence.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Joint Task and Computing Resource Allocation in Distributed Edge Computing Systems via Multi-Agent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Joint Task and Computing Resource Allocation in Distributed Edge Computing Systems via Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Joint Task and Computing Resource Allocation in Distributed Edge Computing Systems via Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
