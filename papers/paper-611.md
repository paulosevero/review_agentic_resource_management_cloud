---
id: "paper-611"
title: "CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network"
authors: ["Hu, Shi-Hong", "Luo, Qu-Yuan", "Li, Guang-Hui", "Shi, Weisong", "Ye, Bao-Liu"]
year: 2023
venue: "Journal of Computer Science and Technology"
venue_type: "journal"
doi: "10.1007/s11390-023-2839-0"
url: "https://www.scopus.com/pages/publications/85178659413?origin=resultslist"
publisher: "Springer"
pages: "1113--1131"
keywords: ["deep reinforcement learning", "edge computing", "task scheduling", "vehicular edge computing"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-611 — CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network

## Metadata

- **Authors:** Hu, Shi-Hong and Luo, Qu-Yuan and Li, Guang-Hui and Shi, Weisong and Ye, Bao-Liu
- **Year:** 2023
- **Venue:** Journal of Computer Science and Technology
- **DOI:** 10.1007/s11390-023-2839-0
- **URL:** https://www.scopus.com/pages/publications/85178659413?origin=resultslist
- **Publisher:** Springer
- **Pages:** 1113--1131
- **Language:** English
- **Keywords:** deep reinforcement learning; edge computing; task scheduling; vehicular edge computing

### Abstract

Edge computing enabled Intelligent Road Network (EC-IRN) provides powerful and convenient computing services for vehicles and roadside sensing devices. The continuous emergence of transportation applications has caused a huge burden on roadside units (RSUs) equipped with edge servers in the Intelligent Road Network (IRN). Collaborative task scheduling among RSUs is an effective way to solve this problem. However, it is challenging to achieve collaborative scheduling among different RSUs in a completely decentralized environment. In this paper, we first model the interactions involved in task scheduling among distributed RSUs as a Markov game. Given that multi-agent deep reinforcement learning (MADRL) is a promising approach for the Markov game in decision optimization, we propose a collaborative task scheduling algorithm based on MADRL for EC-IRN, named CA-DTS, aiming to minimize the long-term average delay of tasks. To reduce the training costs caused by trial-and-error, CA-DTS specially designs a reward function and utilizes the distributed deployment and collective training architecture of counterfactual multi-agent policy gradient (COMA). To improve the stability of performance in large-scale environments, CA-DTS takes advantage of the action semantics network (ASN) to facilitate cooperation among multiple RSUs. The evaluation results of both the testbed and simulation demonstrate the effectiveness of our proposed algorithm. Compared with the baselines, CA-DTS can achieve convergence about 35% faster, and obtain average task delay that is lower by approximately 9.4%, 9.8%, and 6.7%, in different scenarios with varying numbers of RSUs, service types, and task arrival rates, respectively. © 2023, Institute of Computing Technology, Chinese Academy of Sciences.

## 04 — Title Screening

**Title:** CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network
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
