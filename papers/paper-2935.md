---
id: "paper-2935"
title: "Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach"
authors: ["Zhong, Liang", "Tian, Shen", "Zeng, Deze", "Qu, Zhihao", "Hu, Chengyu"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3658536"
url: "https://www.scopus.com/pages/publications/105028895133?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "15976--15988"
keywords: ["Deep reinforcement learning", "depth of discharge (DoD)", "Lyapunov optimization", "satellite edge computing", "task offloading"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2935 — Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach

## Metadata

- **Authors:** Zhong, Liang and Tian, Shen and Zeng, Deze and Qu, Zhihao and Hu, Chengyu
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3658536
- **URL:** https://www.scopus.com/pages/publications/105028895133?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 15976--15988
- **Language:** English
- **Keywords:** Deep reinforcement learning; depth of discharge (DoD); Lyapunov optimization; satellite edge computing; task offloading

### Abstract

Low Earth orbit (LEO) satellite mobile edge computing (SMEC) has emerged as a pivotal technology for delivering low-latency communication and computational services to underserved regions. However, ensuring sustainable operation of SMEC systems remains challenging due to limited onboard energy and battery degradation, which is critically influenced by the depth of discharge (DoD). This article investigates the collaborative DoD optimization problem in heterogeneous SMEC, formulating it as a long-term stochastic optimization aimed at minimizing DoD while maintaining system stability under dynamic energy supply and stochastic task arrivals. To address the computational intractability of this problem, we propose a Lyapunov-guided optimization framework that integrates Lyapunov optimization with a multiagent deep reinforcement learning algorithm. Specifically, due to the inability to predict the future state of the system, we employ Lyapunov optimization to transform the long-term objective into a sequence of per-time-slot subproblems. Subsequently, given the high complexity of minimizing the derived Lyapunov drift function directly, we utilize a multiagent deep deterministic policy gradient (MADDPG) algorithm to solve these subproblems. This approach leverages MADDPG's proven capability in handling complex sequential decision-making processes while enabling real-time adaptive optimization in dynamic environments. Extensive simulations demonstrate that the proposed framework achieves significant reduction in DoD, bounded delays, and stable queue dynamics in diverse scenarios, outperforming baseline methods to substantially extend the lifetime of the SMEC service while maintaining the required service quality.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach
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
