---
id: paper-1582
title: Research on Computation Offloading and Resource Allocation Strategy Based on MADDPG for Integrated Space–Air–Marine Network
authors:
- Gao, Haixiang
venue: Entropy
venue_type: journal
year: 2025
doi: 10.3390/e27080803
url: https://www.scopus.com/pages/publications/105014520532?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- computation offloading
- integrated space–air–marine network
- MADDPG
- mobile edge computing
- resource allocation
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

# paper-1582 — Research on Computation Offloading and Resource Allocation Strategy Based on MADDPG for Integrated Space–Air–Marine Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates the problem of computation offloading and resource allocation in an integrated space–air–sea network based on unmanned aerial vehicle (UAV) and low Earth orbit (LEO) satellites supporting Maritime Internet of Things (M-IoT) devices. Considering the complex, dynamic environment comprising M-IoT devices, UAVs and LEO satellites, traditional optimization methods encounter significant limitations due to non-convexity and the combinatorial explosion in possible solutions. A multi-agent deep deterministic policy gradient (MADDPG)-based optimization algorithm is proposed to address these challenges. This algorithm is designed to minimize the total system costs, balancing energy consumption and latency through partial task offloading within a cloud–edge-device collaborative mobile edge computing (MEC) system. A comprehensive system model is proposed, with the problem formulated as a partially observable Markov decision process (POMDP) that integrates association control, power control, computing resource allocation, and task distribution. Each M-IoT device and UAV acts as an intelligent agent, collaboratively learning the optimal offloading strategies through a centralized training and decentralized execution framework inherent in the MADDPG. The numerical simulations validate the effectiveness of the proposed MADDPG-based approach, which demonstrates rapid convergence and significantly outperforms baseline methods, and indicate that the proposed MADDPG-based algorithm reduces the total system cost by 15–60% specifically. © 2025 by the author.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1582.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
