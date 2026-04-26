---
id: "paper-2422"
title: "Cache-Aware Transformer-Based Scheduling for LLM-Driven IoT Workflows in Multi-Clouds"
authors: ["Zhang, Jianbo", "Mashayekhy, Lena"]
year: 2025
venue: "Proceedings - 2025 IEEE Cloud Summit, Cloud-Summit 2025"
venue_type: "conference"
doi: "10.1109/Cloud-Summit64795.2025.00028"
url: "https://www.scopus.com/pages/publications/105015438289?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "137--142"
keywords: ["Internet of Things", "Model Context Protocol", "Online Scheduling", "Reinforcement Learning", "Serverless"]
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

# paper-2422 — Cache-Aware Transformer-Based Scheduling for LLM-Driven IoT Workflows in Multi-Clouds

## Metadata

- **Authors:** Zhang, Jianbo and Mashayekhy, Lena
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE Cloud Summit, Cloud-Summit 2025
- **DOI:** 10.1109/Cloud-Summit64795.2025.00028
- **URL:** https://www.scopus.com/pages/publications/105015438289?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 137--142
- **Language:** English
- **Keywords:** Internet of Things; Model Context Protocol; Online Scheduling; Reinforcement Learning; Serverless

### Abstract

The integration of Large Language Models (LLMs) into Internet-of-Things (IoT) ecosystems has enabled users to issue high-level natural-language intents that are automatically translated into fine-grained, serverless workflows using protocols such as the Model Context Protocol (MCP). These workflows span heterogeneous multi-cloud platforms, where effective scheduling must account for latency, cost, platform failures, and opportunities for cache reuse. Traditional scheduling heuristics and existing reinforcement learning methods fall short in these highly dynamic environments, especially when decisions must be made online. We propose CATS, a Cache-Aware Transformer Scheduler, trained using Proximal Policy Optimization (PPO) for adaptive placement and deferral of serverless function executions. CATS models dynamic system conditions, including per-platform failure probabilities, critical-path dependencies, and cache-hit likelihoods, within a Transformer-based policy architecture that learns when to defer execution to exploit cache reuse without incurring excessive delay. We evaluate CATS using a custom event-driven simulator under realistic workload traces. Compared to benchmarks, CATS reduces makespan by up to 30%, computational cost by 40%, and retries by over 50%, while maintaining low scheduling latency suitable for real-time deployment. This work establishes a new direction for reinforcement learning–based orchestration of LLM-driven IoT workflows across dynamic, failure-prone multi-cloud environments. ©2025 IEEE.

## 04 — Title Screening

**Title:** Cache-Aware Transformer-Based Scheduling for LLM-Driven IoT Workflows in Multi-Clouds

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Cache-Aware Transformer-Based Scheduling for LLM-Driven IoT Workflows in Multi-Clouds
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Cache-Aware Transformer-Based Scheduling for LLM-Driven IoT Workflows in Multi-Clouds
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
