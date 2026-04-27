---
id: "paper-866"
title: "Scaling Container Caching to Larger Networks with Multi-Agent Reinforcement Learning"
authors: ["Chen, Austin", "Ishigaki, Genya"]
year: 2024
venue: "Proceedings - International Conference on Computer Communications and Networks, ICCCN"
venue_type: "conference"
doi: "10.1109/ICCCN61486.2024.10637588"
url: "https://www.scopus.com/pages/publications/85203264619?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Container Caching", "Multi-Agent Reinforcement Learning", "Serverless Edge Computing (SEC)"]
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

# paper-866 — Scaling Container Caching to Larger Networks with Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Chen, Austin and Ishigaki, Genya
- **Year:** 2024
- **Venue:** Proceedings - International Conference on Computer Communications and Networks, ICCCN
- **DOI:** 10.1109/ICCCN61486.2024.10637588
- **URL:** https://www.scopus.com/pages/publications/85203264619?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Container Caching; Multi-Agent Reinforcement Learning; Serverless Edge Computing (SEC)

### Abstract

The development of containers as a tool for scalable computing has led to the increased use of the serverless edge computing paradigm. In particular, containers enable fast deployment of services to edge networks, allowing users to access spatially closer servers and resulting in lower latency. As instantiating containers can cause extra delay called a cold start delay, container caching, which keeps used containers alive in memory for reuse by the next user, has been proposed to mitigate the delay. However, such edge servers are constrained in their memory capacity, and there is a need for an efficient caching strategy. In this paper, we demonstrate that Multi-Agent Reinforcement Learning (MARL) can effectively learn a cache replacement policy and outperform traditional heuristic and centralized Deep Reinforcement Learning (DRL) algorithms. Our results also show that the proposed MARL's smaller action space has a significant advantage over DRL, which requires full information about the network. In particular, our research demonstrates that MARL is able to scale to larger networks without significant sacrifices to performance.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Scaling Container Caching to Larger Networks with Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Scaling Container Caching to Larger Networks with Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Scaling Container Caching to Larger Networks with Multi-Agent Reinforcement Learning
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
