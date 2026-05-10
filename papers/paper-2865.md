---
id: paper-2865
title: Joint Task Offloading and Resource Allocation for Collaborative VEC Network
authors:
- Xu, Zhenyuan
- Li, Yanjun
- Chen, Yuzhe
- Cheng, Zhen
- Wang, Zhibo
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2026
doi: 10.1109/TITS.2025.3631306
url: https://www.scopus.com/pages/publications/105021658661?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1814--1828
keywords:
- convex optimization
- multi-agent deep reinforcement learning
- resource allocation
- task offloading
- Vehicular edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2865 — Joint Task Offloading and Resource Allocation for Collaborative VEC Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is a promising technique for handling computation-intensive and delay-sensitive tasks by offloading them to roadside units (RSUs) or base stations (BSs) equipped with edge computing servers. However, the uneven spatial-temporal distribution of vehicles causes load imbalances among edge servers. To address this challenge, we propose a two-layer collaborative VEC network paradigm that incorporates offloading modes such as vehicle-to-RSU (V2R), vehicle-to-BS (V2B), and RSU-to-RSU collaboration. Within this framework, task offloading and resource allocation are jointly optimized to maximize system utility, which integrates revenue, delay, and energy consumption, while ensuring that vehicular tasks meet their delay requirements. Given the problem's complexity and scalability concerns, we introduce a distributed framework and propose the joint task offloading and resource allocation (JTORA) algorithm. This algorithm decomposes the original problem into two sub-problems: task offloading and resource allocation. The task offloading sub-problem is modeled as a potential game and solved using the multi-agent twin delayed deep deterministic policy gradient (MATD3) framework. Based on the offloading decisions, the resource allocation sub-problem is further divided into multiple convex optimization problems. The system utility, derived from task offloading and resource allocation decisions, serves as a reward to iteratively evaluate, train the learning model, and refine the offloading strategy. Theoretical analysis confirms that the JTORA algorithm converges to the Nash equilibrium (NE). Simulations using real traffic data validate the proposed algorithm's effectiveness and superiority over existing methods. Specifically, the JTORA algorithm improves overall system utility by reducing task processing delays and energy consumption while increasing the task completion rate. © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2865.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
