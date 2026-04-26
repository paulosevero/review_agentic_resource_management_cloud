---
id: "paper-1408"
title: "Intelligent Kubernetes Scheduling with Large Language Models"
authors: ["Bai, Xinyu", "Tang, Zhiqing", "Yao, Zhi", "Chen, Yao", "Guo, Jianxiong", "Wang, Tian", "Jia, Weijia"]
year: 2025
venue: "Proceedings - 2025 IEEE International Conference on Security, Privacy, Anonymity in Computation and Communication and Storage, SpaCCS 2025"
venue_type: "conference"
doi: "10.1109/SpaCCS67922.2025.00012"
url: "https://www.scopus.com/pages/publications/105033212483?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "16--23"
keywords: ["Edge computing", "Large Language Models", "Scheduling"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-1408 — Intelligent Kubernetes Scheduling with Large Language Models

## Metadata

- **Authors:** Bai, Xinyu and Tang, Zhiqing and Yao, Zhi and Chen, Yao and Guo, Jianxiong and Wang, Tian and Jia, Weijia
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE International Conference on Security, Privacy, Anonymity in Computation and Communication and Storage, SpaCCS 2025
- **DOI:** 10.1109/SpaCCS67922.2025.00012
- **URL:** https://www.scopus.com/pages/publications/105033212483?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 16--23
- **Language:** English
- **Keywords:** Edge computing; Large Language Models; Scheduling

### Abstract

The impressive natural language understanding and inference abilities of recent Large Language Models (LLMs) have enabled their use in scheduling tasks. Existing scheduling methods often neglect the integration of LLMs with schedulers. To fill in such gaps and address complex scheduling challenges in heterogeneous Kubernetes clusters, we propose two LLM-based approaches. Specifically: 1) LLMScheduler, an adaptive online scheduling framework in which the LLM actively participates in decision-making. It scores candidate nodes and selects the optimal one in real time for the clusters. 2) HybridScheduler, an offline intelligence injection framework that leverages LLMs to proactively generate strategic intents for the scoring function, informed by job profiles and node configurations. It then rapidly scores and selects nodes, similar to a traditional Kubernetes scheduler. 3) We validate our methods with large-scale simulations, demonstrating that LLMScheduler improves scheduling success rates by up to 7% on average compared to the best traditional scheduler, particularly under extreme cluster pressure. Moreover, HybridScheduler consistently outperforms all traditional heuristics in high-contention scenarios, while reliably maintaining millisecond-level decision latency. Our experimental results offer a quantitative foundation for designing future AI-driven systems that balance performance, latency, and cost. © 2025 IEEE.

## 04 — Title Screening

**Title:** Intelligent Kubernetes Scheduling with Large Language Models

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Intelligent Kubernetes Scheduling with Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Intelligent Kubernetes Scheduling with Large Language Models
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
