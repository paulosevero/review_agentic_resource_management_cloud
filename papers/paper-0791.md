---
id: paper-0791
title: MATD3-Based Joint User Association and Resource Allocation in UAV Networks
authors:
- Zhang, Hualei
- Du, Jun
- Jiang, Chunxiao
- Fakhreddine, Aymen
- Alhammadi, Ahmed
- Wang, Jintao
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2023
doi: 10.1109/GLOBECOM54140.2023.10436877
url: https://www.scopus.com/pages/publications/85186225680?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6892--6897
keywords:
- Antennas
- Convex optimization
- Markov processes
- Mobile edge computing
- Multi agent systems
- Unmanned aerial vehicles (UAV)
- Aerial vehicle
- Computation intensives
- Computation service
- Coverage area
- Mountainous area
- Multi agent
- Remote areas
- Resources allocation
- User associations
- Vehicle network
- Resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0791 — MATD3-Based Joint User Association and Resource Allocation in UAV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, mobile edge computing (MEC) has been proposed as a promising technique to alleviate the challenges faced by delay and computation-intensive applications. However, users in remote and mountainous areas continue to face difficulties obtaining reliable computation services. To overcome this obstacle, unmanned aerial vehicles (UAVs) equipped with MEC servers have emerged as a popular solution. In such a multi-UAV network, the coverage areas of the UAVs might overlap, which would result in resource wastage and interference. To address this issue, we investigate a collaborative UAV-assisted MEC system for both aerial users (AUs) and ground users (GUs) in this work. Specifically, each user is covered by multiple UAV servers, and the resources of UAVs are dynamic over time. The main objective of this work is to reduce the average delay and improve the service success rate by jointly designing the UAV server-user association, bandwidth, and computing resource allocation strategy. To address the non-convex optimization problem mentioned above, we formulate a multi-agent extension of Markov decision processes (MDPs) for the system and design a cooperative Multi-Agent Twin Delayed Deep Deterministic Policy Gradient (MATD3) approach for each UAV server to make decisions using a centralized training approach with distributed execution. Simulation results validate that the proposed approach can achieve a superior success service rate with a lower delay compared with baselines. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0791.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
