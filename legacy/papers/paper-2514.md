---
id: "paper-2514"
title: "Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA"
authors: ["Babu, Anju", "Josemin Bala, G."]
year: 2026
venue: "Frontiers in Computer Science"
venue_type: "journal"
doi: "10.3389/fcomp.2026.1739223"
url: "https://www.scopus.com/pages/publications/105031123085?origin=resultslist"
publisher: "Frontiers Media SA"
pages: ""
keywords: ["Bidirectional Successive Halving and Attention Gated Recurrent Unit (BiSHAGRU)", "Exponentially Half-life Weighted Moving Average (EHWMA)", "fog computing", "healthcare platforms", "latency", "Recurrent Tuned Kernel Density Estimation (RTKDE)", "Secretary Halton Sequenced Bird Optimization Algorithm (SHSBOA)"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2514 — Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA

## Metadata

- **Authors:** Babu, Anju and Josemin Bala, G.
- **Year:** 2026
- **Venue:** Frontiers in Computer Science
- **DOI:** 10.3389/fcomp.2026.1739223
- **URL:** https://www.scopus.com/pages/publications/105031123085?origin=resultslist
- **Publisher:** Frontiers Media SA
- **Pages:** 
- **Language:** English
- **Keywords:** Bidirectional Successive Halving and Attention Gated Recurrent Unit (BiSHAGRU); Exponentially Half-life Weighted Moving Average (EHWMA); fog computing; healthcare platforms; latency; Recurrent Tuned Kernel Density Estimation (RTKDE); Secretary Halton Sequenced Bird Optimization Algorithm (SHSBOA)

### Abstract

Fog computing integrated with healthcare Internet of Things (IoT) systems enables low-latency processing for time-critical medical applications. However, dynamic request variations, limited fog resources, and node failures can significantly increase latency and reduce system reliability. This paper proposes a dynamic request-aware fog-node deployment framework to mitigate latency in healthcare fog-computing platforms. Recurrent Tuned Kernel Density Estimation (RTKDE) is used to detect dynamic request changes, and Exponentially Half-life Weighted Moving Average (EHWMA) assesses request growth trends. Based on the estimated workload, fog nodes are adaptively scaled and optimally deployed using the Secretary Halton Sequenced Bird Optimization Algorithm (SHSBOA). System reliability is enhanced through faulty fog-node detection using a Bidirectional Successive Halving and Attention Gated Recurrent Unit (BiSHAGRU) model, while redundant fog-to-cloud transmissions are reduced using a Multi-Agent Weighted Reward Reinforcement Learning (MAWRRL) approach. Simulation results using iFogSim demonstrate the effectiveness of the proposed framework. RTKDE achieves a Mean Integrated Square Error (MISE) of 0.042, EHWMA attains a Mean Square Error (MSE) of 0.006, and SHSBOA records a latency of 3,122 ms for 100 requests. BiSHAGRU achieves 99.23% fault detection accuracy, and MAWRRL attains a 93.02% success rate in redundant data handling, confirming improved latency reduction and reliability. Copyright © 2026 Babu and Josemin Bala.

## 04 — Title Screening

**Title:** Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA
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
