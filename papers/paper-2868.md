---
id: "paper-2868"
title: "Serving Long-Context LLMs at the Mobile Edge: Test-Time Reinforcement Learning-Based Model Caching and Inference Offloading"
authors: ["Xu, Minrui", "Niyato, Dusit", "Brinton, Christopher G."]
year: 2026
venue: "IEEE Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TON.2026.3669011"
url: "https://www.scopus.com/pages/publications/105031713871?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3808--3823"
keywords: ["auction theory", "deep reinforcement learning (DRL)", "large language models (LLMs)", "Mobile edge networks"]
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
    human_justification: "LLM as workload"

---

# paper-2868 — Serving Long-Context LLMs at the Mobile Edge: Test-Time Reinforcement Learning-Based Model Caching and Inference Offloading

## Metadata

- **Authors:** Xu, Minrui and Niyato, Dusit and Brinton, Christopher G.
- **Year:** 2026
- **Venue:** IEEE Transactions on Networking
- **DOI:** 10.1109/TON.2026.3669011
- **URL:** https://www.scopus.com/pages/publications/105031713871?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3808--3823
- **Language:** English
- **Keywords:** auction theory; deep reinforcement learning (DRL); large language models (LLMs); Mobile edge networks

### Abstract

Large Language Models (LLMs) can perform zero-shot learning on unseen tasks and few-shot learning on complex reasoning tasks. However, resource-limited mobile edge networks struggle to support long-context LLM serving for LLM agents during multi-round interactions with users. Unlike stateless computation offloading and static service offloading in edge computing, optimizing LLM serving at edge servers is challenging because LLMs continuously learn from context which raises accuracy, latency, and resource consumption dynamics. In this paper, we propose a joint model caching and inference offloading framework that utilizes test-time deep reinforcement learning (T2DRL) to optimize deployment and execution strategies for long-context LLM serving. In this framework, we analyze the performance convergence and design an optimization problem considering the utilization of context windows in LLMs. Furthermore, the T2DRL algorithm can learn in both the training phase and the testing phase to proactively manage cached models and service requests and adapt to context changes and usage patterns during execution. To further enhance resource allocation efficiency, we propose a double Dutch auction (DDA) mechanism, which dynamically aligns the marginal value of an additional reasoning path with the marginal cost of reasoning services. Finally, experimental results demonstrate that the T2DRL algorithm can reduce system costs by at least 30% compared to baselines while guaranteeing the performance of LLM agents in real-world perception and reasoning tasks. © 2025 IEEE.

## 04 — Title Screening

**Title:** Serving Long-Context LLMs at the Mobile Edge: Test-Time Reinforcement Learning-Based Model Caching and Inference Offloading

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Serving Long-Context LLMs at the Mobile Edge: Test-Time Reinforcement Learning-Based Model Caching and Inference Offloading
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Serving Long-Context LLMs at the Mobile Edge: Test-Time Reinforcement Learning-Based Model Caching and Inference Offloading
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
