---
id: "paper-2873"
title: "Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits"
authors: ["Yahya, Mariam", "Sezgin, Aydin", "Maghsudi, Setareh"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3670034"
url: "https://www.scopus.com/pages/publications/105032419744?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Best arm identification (BAI)", "collaborative learning", "linear bandits", "multi -access edge computing (MEC)", "service placement"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2873 — Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits

## Metadata

- **Authors:** Yahya, Mariam and Sezgin, Aydin and Maghsudi, Setareh
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3670034
- **URL:** https://www.scopus.com/pages/publications/105032419744?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Best arm identification (BAI); collaborative learning; linear bandits; multi -access edge computing (MEC); service placement

### Abstract

As users in small cell networks increasingly rely on computation-intensive services, cloud-based access often results in high latency. Multi-access edge computing (MEC) mitigates this by bringing computational resources closer to end users, with small base stations (SBSs) serving as edge servers to enable low-latency service delivery. However, limited edge capacity makes it challenging to decide which services to deploy locally versus in the cloud, especially under unknown service demand and dynamic network conditions. To tackle this problem, we model service demand as a linear function of service attributes and formulate the service placement task as a linear bandit problem, where SBSs act as agents and services as arms. The goal is to identify the service that, when placed at the edge, offers the greatest reduction in total user delay compared to cloud deployment. We propose a distributed and adaptive multi-agent best-arm identification (BAI) algorithm under a fixed-confidence setting, where SBSs collaborate to accelerate learning. Simulations show that our algorithm identifies the optimal service with the desired confidence and achieves near-optimal speedup, as the number of learning rounds decreases proportionally with the number of SBSs. We also provide theoretical analysis of the algorithm's sample complexity and communication overhead. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits
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
