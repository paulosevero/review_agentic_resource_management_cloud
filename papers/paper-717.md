---
id: "paper-717"
title: "Learning Cooperative Oversubscription for Cloud by Chance-Constrained Multi-Agent Reinforcement Learning"
authors: ["Sheng, Junjie", "Wang, Lu", "Yang, Fangkai", "Qiao, Bo", "Dong, Hang", "Wang, Xiangfeng", "Jin, Bo", "Wang, Jun", "Qin, Si", "Rajmohan, Saravan", "Lin, Qingwei", "Zhang, Dongmei"]
year: 2023
venue: "ACM Web Conference 2023 - Proceedings of the World Wide Web Conference, WWW 2023"
venue_type: "conference"
doi: "10.1145/3543507.3583298"
url: "https://www.scopus.com/pages/publications/85159296912?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "2927--2936"
keywords: ["Cloud Computing", "Multi-Agent System", "Over Subscription", "Reinforcement Learning"]
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

# paper-717 — Learning Cooperative Oversubscription for Cloud by Chance-Constrained Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Sheng, Junjie and Wang, Lu and Yang, Fangkai and Qiao, Bo and Dong, Hang and Wang, Xiangfeng and Jin, Bo and Wang, Jun and Qin, Si and Rajmohan, Saravan and Lin, Qingwei and Zhang, Dongmei
- **Year:** 2023
- **Venue:** ACM Web Conference 2023 - Proceedings of the World Wide Web Conference, WWW 2023
- **DOI:** 10.1145/3543507.3583298
- **URL:** https://www.scopus.com/pages/publications/85159296912?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 2927--2936
- **Language:** English
- **Keywords:** Cloud Computing; Multi-Agent System; Over Subscription; Reinforcement Learning

### Abstract

Oversubscription is a common practice for improving cloud resource utilization. It allows the cloud service provider to sell more resources than the physical limit, assuming not all users would fully utilize the resources simultaneously. However, how to design an oversubscription policy that improves utilization while satisfying some safety constraints remains an open problem. Existing methods and industrial practices are over-conservative, ignoring the coordination of diverse resource usage patterns and probabilistic constraints. To address these two limitations, this paper formulates the oversubscription for cloud as a chance-constrained optimization problem and proposes an effective Chance-Constrained Multi-Agent Reinforcement Learning (C2MARL) method to solve this problem. Specifically, C2MARL reduces the number of constraints by considering their upper bounds and leverages a multi-agent reinforcement learning paradigm to learn a safe and optimal coordination policy. We evaluate our C2MARL on an internal cloud platform and public cloud datasets. Experiments show that our C2MARL outperforms existing methods in improving utilization () under different levels of safety constraints. © 2023 ACM.

## 04 — Title Screening

**Title:** Learning Cooperative Oversubscription for Cloud by Chance-Constrained Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Learning Cooperative Oversubscription for Cloud by Chance-Constrained Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Learning Cooperative Oversubscription for Cloud by Chance-Constrained Multi-Agent Reinforcement Learning
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
