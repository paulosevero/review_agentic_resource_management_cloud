---
id: paper-2604
title: Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks
authors:
- Hevesli, Muhammet
- Mohammed Seid, Abegaz
- Erbad, Aiman
- Abdallah, Mohamed
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2025.3555440
url: https://www.scopus.com/pages/publications/105001386163?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 217--236
keywords:
- air-ground network
- edge network
- metaverse
- Mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2604 — Multi-Agent DRL for Queue-Aware Task Offloading in Hierarchical MEC-Enabled Air-Ground Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC)-enabled air-ground networks advance 6G wireless networks by utilizing aerial base stations (ABSs) such as autonomous aerial vehicles (AAVs) and high altitude platform stations (HAPS) to provide dynamic services to ground IoT devices (IoTDs). These IoTDs support real-time applications like multimedia and Metaverse services, which demand high computational resources and strict quality of service (QoS) guarantees, specifically in terms of latency and efficient task queue management. However, IoTDs often face constraints in energy and computational power, requiring efficient queue management and task scheduling to maintain QoS. To address these challenges, AAVs and HAPS are deployed to supplement the computational limitations of IoTDs by offloading tasks for distributed processing. Due to AAVs’ resource limitations, particularly in terms of power and coverage area, HAPS are used to enhance their capabilities and extend coverage. Overloaded AAVs may relay tasks to HAPS, creating a multi-tier computing system. This paper addresses the overall energy minimization problem in the MEC-enabled air-ground integrated network (MAGIN) by optimizing AAV trajectories, computing resource allocation, and queue-aware task offloading decisions. The optimization problem is highly complex due to the nonconvex and nonlinear nature of this hierarchical system, which traditional methods cannot effectively solve. To tackle this, we reformulate the problem as a multi-agent Markov decision process (MDP) with continuous action spaces and heterogeneous agents. We propose a novel variant of multi-agent proximal policy optimization (MAPPO) with Beta distribution (MAPPO-BD) to solve this problem. Extensive simulations show that MAPPO-BD significantly outperforms other baselines, achieving superior energy savings and efficient resource management in MAGIN, while adhering to constraints related to queue delays and edge computing capabilities. © 2015 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2604.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
