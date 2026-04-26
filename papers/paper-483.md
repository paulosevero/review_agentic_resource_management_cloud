---
id: "paper-483"
title: "Reinforcement learning for resource management in multi-Tenant serverless platforms"
authors: ["Qiu, Haoran", "Mao, Weichao", "Patke, Archit", "Wang, Chen", "Franke, Hubertus", "Kalbarczyk, Zbigniew T.", "Ba\u015far, Tamer", "Iyer, Ravishankar K."]
year: 2022
venue: "EuroMLSys 2022 - Proceedings of the 2nd European Workshop on Machine Learning and Systems"
venue_type: "conference"
doi: "10.1145/3517207.3526971"
url: "https://www.scopus.com/pages/publications/85128360409?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "20--28"
keywords: ["function-As-A-service", "multi-Agent", "reinforcement learning", "resource allocation", "serverless computing"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-483 — Reinforcement learning for resource management in multi-Tenant serverless platforms

## Metadata

- **Authors:** Qiu, Haoran and Mao, Weichao and Patke, Archit and Wang, Chen and Franke, Hubertus and Kalbarczyk, Zbigniew T. and Başar, Tamer and Iyer, Ravishankar K.
- **Year:** 2022
- **Venue:** EuroMLSys 2022 - Proceedings of the 2nd European Workshop on Machine Learning and Systems
- **DOI:** 10.1145/3517207.3526971
- **URL:** https://www.scopus.com/pages/publications/85128360409?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 20--28
- **Language:** English
- **Keywords:** function-As-A-service; multi-Agent; reinforcement learning; resource allocation; serverless computing

### Abstract

Serverless Function-As-A-Service (FaaS) is an emerging cloud computing paradigm that frees application developers from infrastructure management tasks such as resource provisioning and scaling. To reduce the tail latency of functions and improve resource utilization, recent research has been focused on applying online learning algorithms such as reinforcement learning (RL) to manage resources. Compared to existing heuristics-based resource management approaches, RL-based approaches eliminate humans in the loop and avoid the painstaking generation of heuristics. In this paper, we show that the state-of-The-Art single-Agent RL algorithm (S-RL) suffers up to 4.6x higher function tail latency degradation on multi-Tenant serverless FaaS platforms and is unable to converge during training. We then propose and implement a customized multi-Agent RL algorithm based on Proximal Policy Optimization, i.e., multi-Agent PPO (MA-PPO). We show that in multi-Tenant environments, MA-PPO enables each agent to be trained until convergence and provides online performance comparable to S-RL in single-Tenant cases with less than 10% degradation. Besides, MA-PPO provides a 4.4x improvement in S-RL performance (in terms of function tail latency) in multi-Tenant cases.  © 2022 ACM.

## 04 — Title Screening

**Title:** Reinforcement learning for resource management in multi-Tenant serverless platforms

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Reinforcement learning for resource management in multi-Tenant serverless platforms
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Reinforcement learning for resource management in multi-Tenant serverless platforms
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
