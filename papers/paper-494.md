---
id: "paper-494"
title: "Learning Mean-Field Control for Delayed Information Load Balancing in Large Queuing Systems"
authors: ["Tahir, Anam", "Cui, Kai", "Koeppl, Heinz"]
year: 2022
venue: "ACM International Conference Proceeding Series"
venue_type: "conference"
doi: "10.1145/3545008.3545025"
url: "https://www.scopus.com/pages/publications/85138543215?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: ""
keywords: ["load balancing", "mean-field control", "parallel systems", "reinforcement learning"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-494 — Learning Mean-Field Control for Delayed Information Load Balancing in Large Queuing Systems

## Metadata

- **Authors:** Tahir, Anam and Cui, Kai and Koeppl, Heinz
- **Year:** 2022
- **Venue:** ACM International Conference Proceeding Series
- **DOI:** 10.1145/3545008.3545025
- **URL:** https://www.scopus.com/pages/publications/85138543215?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 
- **Language:** English
- **Keywords:** load balancing; mean-field control; parallel systems; reinforcement learning

### Abstract

Recent years have seen a great increase in the capacity and parallel processing power of data centers and cloud services. To fully utilize the said distributed systems, optimal load balancing for parallel queuing architectures must be realized. Existing state-of-the-art solutions fail to consider the effect of communication delays on the behaviour of very large systems with many clients. In this work, we consider a multi-agent load balancing system, with delayed information, consisting of many clients (load balancers) and many parallel queues. In order to obtain a tractable solution, we model this system as a mean-field control problem with enlarged state-action space in discrete time through exact discretization. Subsequently, we apply policy gradient reinforcement learning algorithms to find an optimal load balancing solution. Here, the discrete-time system model incorporates a synchronization delay under which the queue state information is synchronously broadcasted and updated at all clients. We then provide theoretical performance guarantees for our methodology in large systems. Finally, using experiments, we prove that our approach is not only scalable but also shows good performance when compared to the state-of-the-art power-of-d variant of the Join-the-Shortest-Queue (JSQ) and other policies in the presence of synchronization delays.  © 2022 Owner/Author.

## 04 — Title Screening

**Title:** Learning Mean-Field Control for Delayed Information Load Balancing in Large Queuing Systems

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Learning Mean-Field Control for Delayed Information Load Balancing in Large Queuing Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Learning Mean-Field Control for Delayed Information Load Balancing in Large Queuing Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
