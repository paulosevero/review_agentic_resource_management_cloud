---
id: paper-1467
title: Distributed RAN Slicing Based on MATD3 Joint With Evolutionary Game Assisted User Association for MEC-Enabled HetNets
authors:
- Chen, Geng
- Mu, Xinzheng
- Liang, Hongjia
- Zeng, Qingtian
- Zhang, Yu-Dong
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2025
doi: 10.1109/TWC.2024.3491359
url: https://www.scopus.com/pages/publications/85209565901?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 260--276
keywords:
- distributed successive convex approximation
- evolutionary game
- MATD3
- network slicing
- User association
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1467 — Distributed RAN Slicing Based on MATD3 Joint With Evolutionary Game Assisted User Association for MEC-Enabled HetNets

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To cope with the dramatic growth of future network traffic and the diversity of services, beyond fifth-generation (B5G) and sixth-generation (6G) wireless communication need to balance the network load while being service-oriented. In this paper, we consider a multi-access edge computing (MEC) driven radio access network (RAN) slicing scenario in a heterogeneous cellular network (HetNet) with local traffic overload. First, since users are generally non absolutely rational when selecting base stations (BSs), an evolutionary game (EG) based user association (UA) scheme is proposed to solve the problem of overload. Specifically, we innovatively define the load function of the base stations (BSs) and combine resource capacity of BSs to form the payoff function to dynamically adjust the load. Second, we model the network slicing (NS) problem using the transmission rate, average latency and quality of service (QoS). The problem is further relaxed and an NS algorithm based on distributed successive convex approximation (DSCA) is presented to derive a theoretical upper bound reference value as a static offline criterion. Finally, considering the high randomness of user task arrival in the real scenario, we formulate the multi-base station slicing problem as a stochastic game (SG) and a multi-agent twin delayed deep deterministic policy gradient (MATD3)-based distributed network slicing algorithm is proposed to obtain excellent slicing strategies. Simulation results show that our proposed UA algorithm has a unique evolutionary equilibrium (EE) solution and is highly scalable. The proposed MATD3-based NS algorithm has better performance compared to other baseline algorithms and converges to a utility value that best approximates the theoretical upper bound. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1467.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
