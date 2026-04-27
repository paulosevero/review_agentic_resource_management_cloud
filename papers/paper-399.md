---
id: "paper-399"
title: "Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing"
authors: ["Ding, Shiyao", "Lin, Donghui"]
year: 2022
venue: "IEICE Transactions on Information and Systems"
venue_type: "journal"
doi: "10.1587/transinf.2021KBP0007"
url: "https://www.scopus.com/pages/publications/85131224051?origin=resultslist"
publisher: "Institute of Electronics Information Communication Engineers"
pages: "864--872"
keywords: ["coalition structure generation", "deep Q-network", "edge computing", "internet of things", "MDP", "multi-agent systems", "reinforcement learning"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-399 — Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing

## Metadata

- **Authors:** Ding, Shiyao and Lin, Donghui
- **Year:** 2022
- **Venue:** IEICE Transactions on Information and Systems
- **DOI:** 10.1587/transinf.2021KBP0007
- **URL:** https://www.scopus.com/pages/publications/85131224051?origin=resultslist
- **Publisher:** Institute of Electronics Information Communication Engineers
- **Pages:** 864--872
- **Language:** English
- **Keywords:** coalition structure generation; deep Q-network; edge computing; internet of things; MDP; multi-agent systems; reinforcement learning

### Abstract

With the high development of computation requirements in Internet of Things, resource-limited edge servers usually require to cooperate to perform the tasks. Most related studies usually assume a static cooperation approach which might not suit the dynamic environment of edge computing. In this paper, we consider a dynamic cooperation approach by guiding edge servers to form coalitions dynamically. It raises two issues: 1) how to guide them to optimally form coalitions and 2) how to cope with the dynamic feature where server statuses dynamically change as the tasks are performed. The coalitional Markov decision process (CMDP) model proposed in our previous work can handle these issues well. However, its basic solution, coalitional Q-learning, cannot handle the large scale problem when the task number is large in edge computing. Our response is to propose a novel algorithm called deep coalitional Q-learning (DCQL) to solve it. To sum up, we first formulate the dynamic cooperation problem of edge servers as a CMDP: each edge server is regarded as an agent and the dynamic process is modeled as a MDP where the agents observe the current state to formulate several coalitions. Each coalition takes an action to impact the environment which correspondingly transfers to the next state to repeat the above process. Then, we propose DCQL which includes a deep neural network and so can well cope with large scale problem. DCQL can guide the edge servers to form coalitions dynamically with the target of optimizing some goal. Furthermore, we run experiments to verify our proposed algorithm’s effectiveness in different settings. Copyright © 2022 The Institute of Electronics, Information and Communication Engineers

## 04 — Title Screening

**Title:** Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing
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
