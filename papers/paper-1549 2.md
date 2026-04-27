---
id: "paper-1549"
title: "Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems"
authors: ["Dubrovskiy, Sergey", "Yassine, Abdulsalam"]
year: 2025
venue: "2025 7th Computing, Communications and IoT Applications Conference, ComComAp 2025"
venue_type: "conference"
doi: "10.1109/ComComAp68359.2025.11353170"
url: "https://www.scopus.com/pages/publications/105033484126?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "279--284"
keywords: ["decentralized learning", "edge computing", "federated learning", "gossip protocols", "Internet of Things", "multi-agent system", "partial-model sharing"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1549 — Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems

## Metadata

- **Authors:** Dubrovskiy, Sergey and Yassine, Abdulsalam
- **Year:** 2025
- **Venue:** 2025 7th Computing, Communications and IoT Applications Conference, ComComAp 2025
- **DOI:** 10.1109/ComComAp68359.2025.11353170
- **URL:** https://www.scopus.com/pages/publications/105033484126?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 279--284
- **Language:** English
- **Keywords:** decentralized learning; edge computing; federated learning; gossip protocols; Internet of Things; multi-agent system; partial-model sharing

### Abstract

We present a decentralized, gossip-based federated learning protocol for heterogeneous Internet of Things multi-agent systems where agents exchange only mutually relevant model components. Each agent partitions its local model into a shared subvector (a subset of parameters) and a private subvector, performs local optimization on the full model. During gossip rounds, agents exchange only the overlapping shared parameters from the shared part of the model with contacted peers using configurable mixing weights, staleness-aware weighting, and optional compression. The protocol supports asynchronous operation, opportunistic connectivity, and open membership with frequent joins and departures. We provide a compact matrix formulation of shared-parameter mixing, derive convergence intuition separating optimization and consensus errors, and identify sufficient connectivity and spectral-gap conditions for mixing on shared subspaces. The approach enables scalable, bandwidth-efficient collaboration for drone swarms, vehicular fleets, and other resource-constrained Internet of Things systems.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
