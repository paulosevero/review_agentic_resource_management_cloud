---
id: "paper-1452"
title: "MAPPO for Edge Server Monitoring"
authors: ["Chamoun, Samuel", "McDowell, Christian", "Buchanan, Robin", "Chan, Kevin", "Graves, Eric", "Sun, Yin"]
year: 2025
venue: "Proceedings - IEEE Military Communications Conference MILCOM"
venue_type: "conference"
doi: "10.1109/MILCOM64451.2025.11310582"
url: "https://www.scopus.com/pages/publications/105031776050?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Cooperative communication", "Costs", "Decision making", "Edge computing", "Electric load dispatching", "Observability", "Optimization", "Problem solving", "Query processing", "Throughput", "Centralised", "Communication problems", "Edge server", "Finite queue", "Finite-time", "Goal-oriented communication", "Multi agent", "Policy optimization", "Server monitoring", "Time-varying availability", "Multi agent systems"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1452 — MAPPO for Edge Server Monitoring

## Metadata

- **Authors:** Chamoun, Samuel and McDowell, Christian and Buchanan, Robin and Chan, Kevin and Graves, Eric and Sun, Yin
- **Year:** 2025
- **Venue:** Proceedings - IEEE Military Communications Conference MILCOM
- **DOI:** 10.1109/MILCOM64451.2025.11310582
- **URL:** https://www.scopus.com/pages/publications/105031776050?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Cooperative communication; Costs; Decision making; Edge computing; Electric load dispatching; Observability; Optimization; Problem solving; Query processing; Throughput; Centralised; Communication problems; Edge server; Finite queue; Finite-time; Goal-oriented communication; Multi agent; Policy optimization; Server monitoring; Time-varying availability; Multi agent systems

### Abstract

In this paper, we consider a goal-oriented communication problem for edge server monitoring, where jobs arrive intermittently at multiple dispatchers and must be assigned to shared edge servers with finite queues and time-varying availability. Accurate knowledge of server status is critical for sustaining high throughput, yet remains challenging under dynamic workloads and partial observability. To address this challenge, each dispatcher maintains server knowledge through two complementary mechanisms: (i) active status queries that provide instantaneous updates at a communication cost, and (ii) job execution feedback that reveals server conditions upon successful or failed job completion. We formulate a cooperative multi-agent distributed decision-making problem in which dispatchers jointly optimize query scheduling to balance throughput against communication overhead. To solve this problem, we propose a Multi-Agent Proximal Policy Optimization (MAPPO)-based algorithm that leverages centralized training with de-centralized execution (CTDE) to learn distributed query-and-dispatch policies under partial and stale observations. Experiments show that MAPPO achieves superior throughput-cost tradeoffs and significantly outperforms baseline strategies across varying query costs, job arrival rates, and dispatchers.  © 2025 IEEE.

## 04 — Title Screening

**Title:** MAPPO for Edge Server Monitoring

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** MAPPO for Edge Server Monitoring
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** MAPPO for Edge Server Monitoring
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
