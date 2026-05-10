---
id: paper-2237
title: A distributed UAV analytics framework for DAO-based swarm systems
authors:
- Vasalos, Averkios
- Economopoulos, Achileas
- Oikonomakis, Andreas
- Chakraborty, Abhinaba
- Kourtis, Michail-Alexandros
- Alexandridis, Georgios
- Tavernier, Wouter
- Xilouris, George
- Chochliouros, Ioannis
- Vasalos, Ioannis
- Trakadas, Panagiotis
venue: Proceedings of the IEEE Symposium on Reliable Distributed Systems
venue_type: conference
year: 2025
doi: 10.1109/SRDS69199.2025.00057
url: https://www.scopus.com/pages/publications/105033366253?origin=resultslist
publisher: IEEE Computer Society
pages: 458--464
keywords:
- Decentralized Data Processing
- Drone Swarm
- Edge Computing
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2237 — A distributed UAV analytics framework for DAO-based swarm systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) are increasingly deployed in inspection and monitoring missions, yet onboard computation and communication impose significant energy burdens that limit flight time and operational scope. In this work, we introduce a novel, blockchain-enabled framework—grounded in the Distributed Autonomous Organization (DAO) paradigm—for orchestrating distributed analytics across a swarm of UAVs. Leveraging the OASEES project’s smart-contract architecture, each drone embeds a Metrics Module for real-time power monitoring, a Behavioral Module for adaptive control, and a Blockchain Agent that autonomously proposes, votes on, and executes collective decisions. Three concurrent threads—Proposal Trigger, Voting, and Action Execution—enable fully decentralized governance of swarm behavior: from detecting critical energy thresholds and formulating swarm-wide conservation maneuvers, to executing approved strategies across all members. We validate our framework in a UAV-based infrastructure inspection scenario, employing a YOLOv5 object-detection pipeline to classify four corrosion classes on a telecommunications mast under three video-capture modalities (short-distance, long-distance, and horizontally concatenated streams). Across all configurations, our system achieves near-perfect precision, recall, and mean Average Precision (mAP50–95 ≈ 0.995), demonstrating both the efficacy of distributed workload inference and the feasibility of treating a single drone as a multi-feed processor. These results underscore the potential of DAO-driven UAV swarms for energy-aware, resilient aerial analytics, and pave the way for fully decentralized 5G/6G-enabled airborne networks. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2237.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
