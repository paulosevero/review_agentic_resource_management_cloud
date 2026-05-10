---
id: paper-1944
title: 'AtoNet: An Adaptive Distributed Algorithm for Dynamic Topology Management in Decentralized IoT Networks'
authors:
- Mastromauro, Luigi
- Ozmen, Muslum Ozgur
- Kinsy, Michel
venue: Proceedings - 2025 IEEE Conference on Cloud and Big Data Computing, CBDCom 2025
venue_type: conference
year: 2025
doi: 10.1109/CBDCOM68404.2025.00022
url: https://www.scopus.com/pages/publications/105033525085?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 104--111
keywords:
- Decentralized Coordination
- Distributed Algorithm
- Dynamic Topology
- Edge Computing
- IoT Networks
- Self-Adaptive Networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1944 — AtoNet: An Adaptive Distributed Algorithm for Dynamic Topology Management in Decentralized IoT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing complexity of decentralized IoT and edge environments requires systems capable of real-time topological self-organization, autonomous role assignment, and adaptive resilience under dynamic and unpredictable conditions. However, current approaches often rely on static structures, centralized orchestration, or periodic reevaluation, limiting their scalability and robustness. In this work, we propose AtoNet, a fully decentralized and adaptive algorithm for dynamic topology management in IoT networks. AtoNet leverages behavioral validation, trust-based role assignment, and inter-agent coordination to ensure resilient structure formation and secure, autonomous operation. The system includes real-time event detection, fault tolerance via heartbeat-based monitoring, and local topology reconfiguration triggered by trust decay or network stress. Experimental simulations demonstrate that AtoNet maintains low latency, high throughput, and fast adaptation rates, even in highly volatile or congested scenarios, highlighting its potential applicability in decentralized edge-IoT contexts. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1944.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
